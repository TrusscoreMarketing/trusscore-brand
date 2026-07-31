#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint.py - deterministic, zero-token lint for de-slop's mechanical checks.

Runs the regex-decidable subset of the mechanical standards (ai-writing.md
style patterns + Trusscore editorial rules) so LLM graders only judge what
a regex cannot. Company precedence is built in: the Trusscore standard
(brand-guidelines Sections 11-13) wins over ai-writing.md's absolute bans
(em dashes are allowed, max two, unspaced; H1/H2 take Title Case).

Usage:
    python lint.py <file.md|file.txt> [--json]

Input is plain text / markdown. For docx or pptx, run against the
extracted text. Exit code: 0 = clean, 1 = findings, 2 = usage error.
"""
import io
import json
import re
import sys

EM = "—"

# Section 9 / voice.md banned words. (word/phrase, regex, note)
BANNED_WORDS = [
    ("synergy", r"\bsynerg(?:y|ies|istic)\b", "banned word (Section 9)"),
    ("guru", r"\bgurus?\b", "banned word (Section 9)"),
    ("disruptor", r"\bdisrupt(?:or|ors)\b", "banned word (Section 9)"),
    ("game-changer", r"\bgame[- ]chang(?:er|ers|ing)\b", "banned word (Section 9)"),
    ("innovative solution", r"\binnovative solutions?\b", "banned phrase (Section 9)"),
    ("best-in-class", r"\bbest[- ]in[- ]class\b", "banned phrase (Section 9) - prove it with specifics"),
    ("industry-leading", r"\bindustry[- ]leading\b", "banned phrase (voice.md 7)"),
    ("leverage (verb)", r"\bleverag(?:e[sd]?|ing)\b", "banned as a verb (Section 9) - use 'use'; verify it is a verb"),
    ("plastic", r"\bplastics?\b", "banned (Section 9) - use 'material' or the product name"),
]

# Section 13 banned abbreviations / product-name forms.
BANNED_ABBREV = [
    ("WCB", r"\bWCB\b", "banned abbreviation (Section 13)"),
    ("W&C", r"\bW&C\b", "banned abbreviation (Section 13)"),
    ("SW", r"\bSW\b", "banned abbreviation (Section 13) - verify not a compass/other use"),
    ("TC panels", r"\bTC panels\b", "banned form (Section 13)"),
    ("TC boards", r"\bTC boards\b", "banned form (Section 13)"),
    ("Trusscore boards", r"\bTrusscore boards\b", "banned form (Section 13)"),
    ("plastic panels", r"\bplastic panels\b", "banned form (Section 13)"),
    ("PVC panels", r"\bPVC panels\b", "banned form (Section 13)"),
]

SMALL_WORDS = {
    "a", "an", "the", "and", "but", "for", "nor", "or", "so", "yet",
    "at", "by", "in", "of", "on", "to", "up", "with", "as", "if", "vs",
    "via", "per", "from", "into", "onto", "over", "down", "off", "out",
}


def lint_text(text):
    findings = []
    lines = text.splitlines()

    def add(line_no, rule, severity, quote, note):
        findings.append({
            "line": line_no, "rule": rule, "severity": severity,
            "quote": quote.strip()[:120], "note": note,
        })

    # --- em dashes ---
    em_total = 0
    for i, line in enumerate(lines, 1):
        for m in re.finditer(EM, line):
            em_total += 1
        for m in re.finditer(r"[ \t]" + EM + r"|" + EM + r"[ \t]", line):
            add(i, "em-dash-spaced", "should-fix", line,
                "spaced em dash - company standard is unspaced word" + EM + "word (Section 12)")
    if em_total > 2:
        add(0, "em-dash-count", "should-fix", "{} em dashes in piece".format(em_total),
            "maximum two em dashes per content piece (Section 12)")

    # --- possessive Trusscore's ---
    for i, line in enumerate(lines, 1):
        if re.search(r"\bTrusscore[’']s\b", line):
            add(i, "possessive-brand", "blocker", line,
                "brand name never takes the possessive (Section 13)")

    # --- banned words / abbreviations ---
    for i, line in enumerate(lines, 1):
        for name, pat, note in BANNED_WORDS:
            if re.search(pat, line, re.IGNORECASE):
                add(i, "banned-word:" + name, "should-fix", line, note)
        for name, pat, note in BANNED_ABBREV:
            if re.search(pat, line):
                add(i, "banned-abbrev:" + name, "blocker", line, note)

    # --- terminal period on bullets ---
    for i, line in enumerate(lines, 1):
        if re.match(r"^\s*[-*•]\s+.*[^.]\.\s*$", line) and not line.rstrip().endswith(("...", "….")):
            add(i, "bullet-terminal-period", "should-fix", line,
                "bullets are fragments - no terminal period (Section 12)")

    # --- Title Case on H1/H2 (best-effort heuristic; warnings only) ---
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,2})\s+(.*)$", line)
        if not m:
            continue
        heading = re.sub(r"[`*_\[\]()]", "", m.group(2)).strip()
        words = [w for w in re.split(r"[\s/]+", heading) if w]
        bad = []
        for j, w in enumerate(words):
            core = w.strip(".,:;!?\"'()")
            if not core or not core[0].isalpha():
                continue
            if core.isupper() or any(c.isdigit() for c in core):
                continue
            first_or_last = j == 0 or j == len(words) - 1
            if core[0].islower() and (first_or_last or core.lower() not in SMALL_WORDS):
                bad.append(core)
        if bad:
            add(i, "title-case", "warning", line,
                "H1/H2 take Title Case (Section 11); lowercase major word(s): "
                + ", ".join(bad) + " (heuristic - verify)")

    return findings


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    as_json = "--json" in argv
    if len(args) != 1:
        print(__doc__)
        return 2
    try:
        text = io.open(args[0], encoding="utf-8").read()
    except OSError as e:
        print("cannot read {}: {}".format(args[0], e))
        return 2
    findings = lint_text(text)
    real = [f for f in findings if f["severity"] != "warning"]
    if as_json:
        print(json.dumps(findings, indent=2))
    else:
        for f in findings:
            print("{severity:9s} L{line:<4d} {rule}: {note}\n          > {quote}".format(**f))
        print("\n{} finding(s), {} warning(s)".format(len(real), len(findings) - len(real)))
    return 1 if real else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
