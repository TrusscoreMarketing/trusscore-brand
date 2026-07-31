#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync-check.py - standards-sync drift detector (skeleton).

Problem (feedback journal, Jul 10-31): de-slop's generated check files
(visual.md, voice.md, company-fit.md, contexts/*) are static snapshots of
the trusscore-brand-guidelines skill. Nothing triggers a re-sync when the
brand skill changes, so value drift recurs (yellow-tint lists, font-surface
maps, em-dash rules). This script makes the drift visible; wiring it into
CI (run on any PR touching the brand skill) is the follow-up.

Current scope (v0): compares the hex-color vocabulary of the brand skill
(SKILL.md + references/) against de-slop's visual.md, and reports values
present in the brand standard but missing from the generated check file.
Extend with font-surface maps and punctuation-rule extraction as needed.

Usage: python tools/sync-check.py   (exit 1 on drift)
"""
import io
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = os.path.join(ROOT, "skills", "trusscore-brand-guidelines")
VISUAL = os.path.join(ROOT, "skills", "de-slop", "references", "checks", "visual.md")

HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")


def hexes(path):
    return {h.upper() for h in HEX.findall(io.open(path, encoding="utf-8").read())}


def main():
    brand_files = [os.path.join(BRAND, "SKILL.md")] + \
        sorted(glob.glob(os.path.join(BRAND, "references", "*.md")))
    brand_hex = set()
    for f in brand_files:
        brand_hex |= hexes(f)
    if not os.path.exists(VISUAL):
        print("visual.md not found; nothing to compare")
        return 0
    visual_hex = hexes(VISUAL)
    missing = sorted(brand_hex - visual_hex)
    stale = sorted(visual_hex - brand_hex)
    if missing:
        print("DRIFT: brand-standard colors missing from de-slop visual.md:")
        for h in missing:
            print("  ", h)
    if stale:
        print("NOTE: colors in visual.md not present in the brand skill (verify):")
        for h in stale:
            print("  ", h)
    if missing:
        print("\nRe-run the de-slop adapter against the brand skill to refresh.")
        return 1
    print("in sync: %d brand colors all present in visual.md" % len(brand_hex))
    return 0


if __name__ == "__main__":
    sys.exit(main())
