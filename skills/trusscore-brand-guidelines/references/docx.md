# Trusscore Word / Print Document Spec (docx)

> On-demand reference for the `trusscore-brand-guidelines` skill. **Load when building or reviewing any Word/print document (.docx).** New in July 2026 — codifies the docx layer that was previously re-derived per build (Freestanding Display brief, SlatWall delegation brief, DH Docks memo, Banding R&D brief). The bundled builder `scripts/trusscore_docx.py` implements this spec in code — prefer it over hand-rolling python-docx.

## Fonts and styles — set explicitly, every time

- **Aptos for everything** — headings, body, tables, lists, captions. The docx format skill's Arial default is overridden per Section 0 of the core skill.
- Patch the `Normal` style AND every heading style explicitly. Do not rely on inheritance from the document default.
- **List styles do not inherit the Normal override.** `List Bullet`, `List Number`, and `List Number 2` each need the Aptos font patch applied directly — this gap shipped twice before being codified.

## Type scale

| Role | Size | Weight | Color | Notes |
|---|---|---|---|---|
| Document title | 20pt | Bold | TC Slate `#3A4B5C` | Once, first page |
| H1 | 16pt | Bold | TC Slate `#3A4B5C` | Major sections |
| H2 | 13pt | Bold | TC Slate `#3A4B5C` | Subsections |
| H3 | 11.5pt | Bold | TC Slate `#3A4B5C` | Minor headings |
| Body | 11pt | Regular | TC Text `#111A22` | |
| Caption / meta | 9pt | Regular | grey `#6A7A88` | Secondary lines only |

- **Line spacing: 1.25–1.28 for body.** The web 1.7 body rule does not apply to Word documents — 1.7 reads as double-spaced in print.
- **Margins: 0.8" top/bottom, 0.9" left/right.**
- Headings get space before (~12pt H1, ~10pt H2) rather than empty paragraphs.
- Title Case on H1/H2 per core Section 11; sentence case on H3+ and body.

## Logo treatment

- **Title page:** full logo (slate wordmark + yellow truss + tagline), ~2.05" wide, top of page.
- **Running header (pages 2+):** wordmark-only version, ~0.95" wide — at this size the tagline falls below its 8pt print minimum (core Section 8), so the tagline lock-up must not be used.
- Always the real logo asset file — never "Trusscore" set in styled text.

## Tables

- Header row: Aptos Bold, TC Slate text on white, with a **2pt TC Slate `#3A4B5C` bottom border** (the "slate header underline").
- Body rows: **1pt TC Grey `#DFDBDA` horizontal dividers** between rows. No vertical borders, no outer box unless the table is a callout card, no zebra striping.
- Numbers right-aligned; body cells 10–11pt Aptos, TC Text.
- Stat cards / KPI callouts are rebuilt as bordered Word tables: `0.5–1pt #DFDBDA` four-sided border, white fill, label small + muted, number large + bold TC Slate. No shadows, no fills-for-decoration.

## Dividers and callouts

- Horizontal section divider: **1pt `#DFDBDA`** rule (the docx equivalent of the deck's `#E1E5E8` 0.75pt and web's 1px `#DFDBDA`).
- Callout box: table-cell with **TC Yellow 20% `#FFF0C2` fill and TC Slate text**, or a four-sided `0.5pt #DFDBDA` border — never a single-edge accent bar (universal ban, core Section 2).

## Internal classification labels

For internal memos and briefs, a classification label ("INTERNAL | CONFIDENTIAL") is set in **TC Slate, all caps, letter-spaced, small (9–10pt)** — not the TC Yellow eyebrow. The yellow eyebrow is scoped to marketing content; editorial/internal documents take no decorative accent above headings, and the classification label is a label, not an eyebrow.

## Explicitly out of scope in Word

Do not attempt: truss-mark parallelograms, 38° angled section transitions, icon systems, or any decorative geometry. Word is a typographic medium here — typography, whitespace, and the table/divider treatments above carry the whole design. Skipping these elements is correct, not a gap.

## Build path

Use `scripts/trusscore_docx.py` (bundled with this skill): pre-set styles (Aptos incl. list-style patches, slate headings, TC Text body, margins), helpers (`title_block`, `para`, `bullet`, `numbered`, `table`, `callout`), and `qa_verify(path)` for post-build verification. Fall back to raw python-docx only for elements the builder doesn't cover, still following this spec.

## Pre-publication checklist — Word documents

- [ ] Aptos on every style actually used — including `List Bullet` / `List Number` / `List Number 2` patched explicitly
- [ ] Headings TC Slate `#3A4B5C` (verify the hex, not "dark blue-ish")
- [ ] Body TC Text `#111A22`, 1.25–1.28 line spacing
- [ ] Tables: slate header underline + grey row dividers, no vertical borders, no zebra
- [ ] Logo is the real asset: ~2.05" title page, ~0.95" wordmark-only running header
- [ ] Classification label (if internal) in TC Slate, not yellow
- [ ] Em dashes: unspaced, maximum two in the document
- [ ] Bullets: no terminal periods
- [ ] `qa_verify()` from `trusscore_docx.py` passes (fonts, heading color, em-dash count, table borders)
