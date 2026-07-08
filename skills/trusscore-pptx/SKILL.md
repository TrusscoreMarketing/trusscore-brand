---
name: trusscore-pptx
description: "Build any Trusscore PowerPoint deck, slide, or presentation. Use whenever a .pptx is created, edited, or read for Trusscore — monthly reports, executive summaries, sales decks, internal reviews, section dividers, KPI/stat slides — or whenever the user says deck, slides, presentation, or names a Trusscore .pptx file. This skill is the brand layer: it does NOT replace the public `pptx` skill's build mechanics, it sits on top of them and enforces the Trusscore visual spec (Section 14b of the trusscore-brand-guidelines skill) on every slide. Always prefer this skill over the generic `pptx` skill for Trusscore work."
license: Internal — Trusscore
---

# Trusscore PowerPoint Skill (brand layer)

You are building a Trusscore-branded deck. Two skills work together and neither is optional:

1. **Public `pptx` skill = HOW to build.** All file mechanics come from it — creating from scratch (`pptxgenjs.md`), editing from a template (`editing.md`), extracting text, thumbnails, packing/unpacking, and the required QA render step. Read those files for the build method. Do not reimplement mechanics here.
2. **This skill = HOW it must look and read.** It applies the Trusscore visual spec and overrides every public-skill default that conflicts with the brand. **When the two disagree, this skill wins.**

The authoritative visual source is **Section 14b (PowerPoint Visual Spec)** in the `trusscore-brand-guidelines` skill, reverse-engineered from the production master template. The values are mirrored below for convenience, but if this file and Section 14b ever differ, **Section 14b is canon** — re-read it and follow it.

---

## Order of operations (do not skip)

1. **Load the brand.** Read the `trusscore-brand-guidelines` skill (Section 14b for visuals; the voice/identity/mechanics sections for copy). Apply account-level Trusscore preferences that are already always in effect.
2. **Pick the build path** from the public `pptx` skill:
   - Editing or extending an existing Trusscore deck, or the master template is available → **template/editing path** (`editing.md`). This is preferred for Trusscore because it inherits the master slide's footer logo lockup and theme.
   - No template available → **from-scratch path** (`pptxgenjs.md`), then apply every value in "The 14b spec" below by hand.
3. **Build the slides** using public-skill mechanics, but obeying the Overrides and the 14b spec.
4. **Run the Trusscore review** (copy + visual) before delivery — see "Review" below.
5. **Run the public skill's required QA render** and fix real issues (overlap, overflow, misalignment) — with the font caveat noted below.

---

## Master template

The production master is **`Trusscore_Amazon_Monthly_Report_May_2026.pptx`** (the file Section 14b was reverse-engineered from). Bundle this template with the skill (e.g. an `assets/` folder) and default to the editing path against it, because the master already carries: the 16:9 slide size, the theme, the slate cover fill, and the footer logo lockup placed once on the slide master. Building on it is faster and more correct than recreating chrome from scratch.

> If the template file is not present in the session, say so and either ask for it or fall back to the from-scratch path and reconstruct the chrome from the 14b values below.

---

## Slide types — build every new slide from a template layout

The master template defines a full set of **named slide layouts**. When adding slides to a Trusscore deck, **choose one of these layouts and instantiate it** — do not invent a new layout or hand-place chrome. Building on a template layout is what inherits the theme, the footer logo lockup, and correct positioning automatically. In the editing path this means: add the new slide against the desired layout by name (or duplicate an existing slide that already uses it), then replace only the content.

The 26 layouts, grouped by purpose:

- **Covers / title:** `Title Slide`, `Title1` (`2_Title1`), `Title3` (`1_Title3`), `Title - Agriculture`
- **Section dividers:** `Section - General`, `Section - Choose your own picture`, `Section - Residential`, `Section - Residential/SlatWall`
- **Agenda:** `Agenda`
- **Content:** `Title and Content`, `Title Only`, `Two Columns`, `Two Columns with Headings`, `Blank`, `DEFAULT`
- **Picture layouts:** `Picture Left`, `Picture Right`, `1` (full-picture)
- **Quote:** `Quote`, `1_Quote`
- **Closing:** `Ending`, `Ending1` (`1_Ending`, `1_Ending1`)

Rules:
- Match the layout to the segment where one exists (e.g. `Section - Residential`, `Title - Agriculture`) — the template already provides segment-specific dividers, so use them rather than recoloring a generic one.
- If the deck needs a slide type not in this list, prefer composing it inside `Title and Content` or `Blank` over creating a new master layout.
- Never duplicate the footer lockup onto a slide — it's inherited from the layout/master.

---

## Overrides — where the public pptx skill is WRONG for Trusscore

The public skill gives generic "make it pop" advice. Several of its defaults directly conflict with Trusscore. Override them every time:

| Public pptx skill says | Trusscore rule (override) |
|---|---|
| "Pick a bold, content-informed color palette"; "don't default to blue"; dark "premium" backgrounds | **No.** The palette is locked: TC Slate `#3A4B5C`, TC Yellow `#FEB100`, TC Blue `#009BD6`, TC Green `#6BA543`, White `#FFFFFF`. Covers/dividers are solid slate; content slides are solid white. Never invent a palette, never use an off-palette background, never use the public skill's sample palettes. Hold the 60-30-10 balance (≈60% white/light, ≈30% slate, ≤10% yellow). |
| "Never default to Aptos" (a QA-rendering caveat) | **Trusscore IS Aptos.** Aptos is the brand font for Office output and must be set explicitly per text run (the theme's silent default is Calibri Light and must not win). The public warning is about QA-preview fidelity, not a brand rule — handle it via the Font/QA note below, do not swap the font. |
| "Commit to a motif — icons in colored circles" | **Banned.** No circle containers on icons. Use Lucide outline icons only, uncontained. The Trusscore motif is the yellow truss mark, used per 14b (solo mark bottom-right on covers). |
| "Every slide needs a visual element / avoid text-only slides" — pushes decorative maximalism | Favor **restraint**. Clean, whitespace-forward slides are on-brand. Add a visual when it carries meaning (a chart, a real install photo, a KPI card), not to fill space. Real installs / AI-cleaned real photos only — never stock or AI-generated-as-real imagery. |
| "Don't repeat the same layout — vary aggressively" | Favor a **consistent, repeatable Trusscore layout system** over per-slide novelty. Category distinction comes from section header labels, not from reinventing the grid each slide. |
| Small **ALL-CAPS title / kicker line above or below a heading** | **Do not use.** No all-caps eyebrow/kicker text set above or below headings — the user has explicitly rejected this pattern. Use the heading alone with whitespace. *(Note: 14b's stat-card guidance still allows a small letter-spaced category label ABOVE a row of cards, e.g. "DIVISION 1 | SAMPLES", as the alternative to per-card color-coding. Keep that specific card-row label if used, but do not add all-caps kickers to ordinary slide headings. If you want these unified, tell me and I'll reconcile 14b too.)** |

**No left-side (or any-side) color line accent / border on boxes or cards.** A colored vertical rule down the left edge of a box, quote, callout, or content block is banned — same reasoning as the rejected card top-stripe: it reads as generic AI-template filler. This covers left-border accents, sidebar stripes, and any single-side colored border on any shape, not just cards. Set a box apart with a subtle background tint or a section label above it, never with an edge line. (This extends the brand skill's existing "no left-border accents on headings on white backgrounds" rule to all boxes and cards.)

Rules where the public skill already **agrees** with Trusscore — keep enforcing them: no accent lines under titles; no decorative color bars / edge stripes / single-side borders; don't center body text; no low-contrast text; don't ship overflowing text.

---

## Visual and text balance (mix, do not max)

Two failure modes are both off-brand: a deck of nothing but headings and bullets (boring), and a deck where every slide is a card grid or stat block (busy, and it reads as a template). Trusscore decks deliberately mix the two.

- **Roughly half and half.** Across the content slides, about half carry a built visual treatment (card row, stat callouts, flow diagram, two-column, or a real photo) and about half are text-forward (a heading with concise prose or one short, clean list). A well-set text slide is on-brand, not a failure — whitespace is a feature.
- **One treatment per slide.** Choose a single dominant device per slide. Never stack a card row and stat callouts and a callout box on the same slide.
- **Rotate for rhythm.** No more than two visually-heavy slides in a row. Alternate text-forward and visual slides so the deck breathes.
- **Earn the visual.** Use a graphic only when the content fits it: numbers → stat callouts; parallel items → a card row; a sequence → a flow diagram; a comparison → two columns; a real space → a photo. If the point is explanatory, keep it a clean text slide.
- **Density cap.** At most about 60% of content slides should carry a built graphic. The cover, the closing slate slide, and any full-photo slide count on the visual side.

This is the middle path between the public skill's "every slide needs a visual" (too much) and a plain bulleted deck (too little): restraint plus rhythm. Tune the ratio to the audience — a data readout leans more visual, a narrative deck leans more text — but never let the whole deck collapse to one mode.

---

## The 14b spec (mirror of Section 14b — Section 14b is canon)

**Canonical colors.** Use `#3A4B5C` for slate in new work (title text hardcodes it; the theme swatch `#3A4B5B` is a one-digit typo — do not rely on it). Confirmed accents: TC Blue `#009BD6`, TC Green `#6BA543`, TC Yellow `#FEB100`.

**Neutral grey ramp** (extracted from the example decks, approved as documented neutrals — all slate-tinted, light → dark): `#F5F6F7`, `#EEF1F3`, `#E8EAEC` (1pt hairline dividers), `#E1E5E8` (0.75pt card borders), `#DDE3E8`, `#CFD6DC`, `#8A9BAC` (muted labels), `#6A7A88` (muted supporting/caption text). The single documented TC Grey `#DFDBDA` remains valid alongside these. Use greys from this ramp for borders, panel fills, and muted text — never an off-palette neutral.

**Two darks.** TC Text `#111A22` for body copy and captions; `#222B33` for a slightly lighter heading dark (headings only). Do not use `#222B33` for body.

**Warm accent.** TC Yellow `#FEB100` only. The gold `#F4A700` seen in the example decks is off-brand — do not use it; normalize to `#FEB100`.

**Decline red.** `#DC3545` is canon (functional up/down data signal only). The `#E05C5C` / `#C0392B` reds in the example decks are off-spec — do not copy them; use `#DC3545`.

**Slide size.** 12,192,000 × 6,858,000 EMU (13.33" × 7.5", 16:9 widescreen).

**Cover / section-divider slides**
- Background: solid TC Slate `#3A4B5B` (theme `accent1`).
- Logo lockup (white wordmark + yellow truss mark + "material + science" tagline): top-left, offset 537,460 / 473,468 EMU (≈0.59" / 0.52"), sized 3,898,508 × 861,773 EMU (≈4.26" × 0.94").
- Title: white, bold, Aptos, below the lockup. **One** keyword may be set in TC Yellow for emphasis; the rest stays white. Never yellow more than one phrase.
- Solo truss mark (solid TC Yellow `#FEB100`, no wordmark): bottom-right, offset ≈11.56" / 6.18", sized ≈1.18" × 0.93".
- The three light-grey outlined parallelograms sometimes seen on the cover are an optional flourish, **not** required. Omit unless deliberately reintroducing.

**Content slides**
- Background: solid white.
- Title: top-left, offset 537,460 / 456,432 EMU (≈0.59" / 0.50"), width ≈11,117,083 EMU (≈12.16").
- Title type: **Aptos Light** (confirmed from the master `titleStyle`), **48pt to start**, TC Slate `#3A4B5C` (hardcoded), -20 letter-spacing, 100% line spacing. Not bold.
- **Title sizing:** start at 48pt. If a title is too long for one comfortable line, reduce to fit down to a **hard floor of 32pt**; if it still will not fit at 32pt, **shorten the title** rather than going smaller. A title must not dominate the top of the slide.
- Footer logo lockup (slate wordmark + yellow truss mark + tagline): bottom-right, ≈11.10" / 6.86", ≈1.66" × 0.37". It lives on the slide master and is inherited — **do not duplicate it on individual slides.**
- Body font: Aptos throughout, set explicitly per run.

**Stat / data cards** (executive summaries, KPI rows, metric call-outs)
- Rounded rectangle, corner radius 6% (`adj val 6000`) — subtle, not a pill.
- Fill solid white `#FFFFFF`; border 0.75pt (9525 EMU) in `#E1E5E8` (the confirmed deck value; supersedes the earlier `#E3E7EB`).
- **No shadow, no gradient** (`effectLst` empty).
- **No colored top-border accent stripe** on cards (tested and rejected — reads as generic AI dashboard). Carry category distinction through a section header label above the card row, not per-card color.
- Card label (e.g. "TOTAL SAMPLE UNITS"): small caps / uppercase, TC Text `#111A22`, muted weight.
- Big number: TC Slate or TC Text, bold, large — the focal point.
- Supporting line: muted grey / TC Text at reduced opacity — a documented grey, not an off-palette grey.
- **Card-row emphasis variant:** a lone card stays white, but in a *row* of cards fills may vary across white, ramp grey (`#F5F6F7`/`#EEF1F3`), light-yellow tint (`#FFF8EC`), or full TC Slate `#3A4B5C` for rhythm. Exactly one dark-slate card is the stand-out (number in TC Yellow, label white). One slate card per row max; never every card a different color; no yellow-tint plus blue fills in one row. Fill-for-emphasis, not an edge stripe.

**Trend / delta indicators — approved functional exception**
- Up/down change signals (e.g. "▲ 193.2% MoM", "▼ 54.5% MoM") use red for decline, green for growth. This is a data signal, not decoration — exempt from the yellow ceiling and the card-accent ban.
- Decline: red `#DC3545` (reserved **only** for this — never a general accent). Growth: TC Green `#6BA543`.

**Callout / highlight boxes**
- Fill light yellow tint `#FFF8EC`; border TC Yellow `#FEB100`.
- One per slide maximum, for a genuinely important takeaway — not a per-slide device.

---

## Font / QA reconciliation (Aptos)

Aptos is mandatory brand output, but the public skill's LibreOffice-based QA render may substitute it and report false text-fit results. So:
- **Ship Aptos.** Set it explicitly on every run; never substitute a "safe" font to satisfy QA.
- When QA flags overflow on an Aptos container, treat the flag as **approximate** — verify the real fit by eye/thumbnail and give text containers ~10% slack rather than changing the font.
- Do all layout QA (overlap, alignment, off-slide elements) as normal; only the Aptos text-fit signal is the unreliable one.

---

## Voice & identity (defer to the brand skill, but never violate on a slide)

Slide copy follows the same Trusscore rules as all content: never the possessive "Trusscore's"; full trademarked names on first reference (Trusscore® Wall&CeilingBoard™, Trusscore® SlatWall™, etc.); never "plastic," never the internal abbreviations (WCB/SW) in visible copy; "PVC" only in technical body copy, never headlines. Headlines / H1–H2 in Title Case, everything else sentence case. Oxford comma always; em dashes no spaces; fractions not decimals; imperial first; U.S. spelling. Approved messaging lines by segment (see brand skill) — never use drywall as the comparison in commercial or agricultural decks.

---

## Review (required before delivery)

The Trusscore review gate is the **`de-slop` skill**. Run it on the finished deck before delivery — it is the single quality gate for both copy and visuals, and it replaces the older "copy review prompt / visual review prompt" step.

1. **Run de-slop on the deck** (e.g. "de-slop this deck", or point it at the .pptx path). It classifies the output as visual + copy, marketing context, and grades it against the Trusscore standard files, returning one scorecard: what's off, the governing rule, and a suggestion.
2. **de-slop detects and suggests — it never edits.** You (this skill) own the fixes. Apply the fixes it flags, then re-run if any blockers fired.
3. Its **Visual check** is what enforces this spec at review time (palette + 60-30-10, Aptos everywhere, no icon circles, no accent stripes, no left/any-side box borders, no all-caps kickers on headings, footer lockup not duplicated, one yellow keyword max on covers, one callout max per slide). For that to work, de-slop's `references/checks/visual.md` and `references/contexts/marketing.md` must be populated with the Trusscore design system — see note below.
4. Then run the public `pptx` skill's required **QA render** and fix real layout issues (with the Aptos font caveat above).

> **Setup dependency:** de-slop ships with placeholder `visual.md` / `voice.md` / `marketing.md` files. Until they're filled with the Trusscore system (from Section 14b + the brand skill's voice rules), the Visual and Voice checks grade against generic examples, not Trusscore. Populate them once (via de-slop's companion adapter skill, or by hand) so the gate is real. A silent pass on an unpopulated check is meaningless.

---

## Draft notes / to confirm with the skill owner
- Master template `Trusscore_Amazon_Monthly_Report_May_2026.pptx` should be bundled in this skill's `assets/` so the editing path always has it.
- Decide whether to reconcile the all-caps ban with 14b's "small-caps label above a card row" allowance (currently kept as the one permitted exception).
- Confirm the exact grey used for card supporting lines (14b says "a documented grey" — pin the hex).
