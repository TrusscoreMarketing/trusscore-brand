# Trusscore PowerPoint Visual Spec (Section 14b)

> On-demand reference for the `trusscore-brand-guidelines` skill. **Load when building, editing, or reviewing any .pptx.** The `trusscore-pptx` skill is the build layer and mirrors these values; this file is canon if they ever differ. Content relocated verbatim from SKILL.md Section 14b and the Section 0 pptx color-pop rule.

## 14b. PowerPoint Visual Spec

This spec is reverse-engineered from the production master template and confirmed against two example decks (`Trusscore Powerpoint Design Examples.pptx`, `Trusscore_Powerpoint_Template.pptx`), read from live slide XML, July 2026. Values below are exact and current. This is the only authoritative version; verify after any future edit that it persisted.

**Canonical color correction:** the theme's `accent1`/`dk2` swatch is stored as `#3A4B5B` (one digit off from `#3A4B5C`). This is a typo in the theme XML, not a second valid value. Title text bypasses the theme swatch and hardcodes `#3A4B5C` directly; that hardcoded value is canon. When building new Trusscore pptx files use `#3A4B5C` and do not rely on the theme's `accent1`/`dk2` token for slate.

**Confirmed accent values:** TC Blue `#009BD6`, TC Green `#6BA543`, TC Yellow `#FEB100`.

**Neutral grey ramp (documented).** Trusscore decks use a full slate-tinted neutral scale, not the single TC Grey `#DFDBDA`. All of the following are approved neutrals (light → dark): `#F5F6F7`, `#EEF1F3`, `#E8EAEC` (1pt hairline dividers), `#E1E5E8` (0.75pt card borders), `#DDE3E8`, `#CFD6DC`, `#8A9BAC` (muted labels), `#6A7A88` (muted supporting/caption text). TC Grey `#DFDBDA` remains valid alongside these. Use greys from this ramp for borders, panel fills, and muted text; never an off-palette neutral. Snap imprecise re-entries to canon: `#3A4B5B`→`#3A4B5C`, `#6BA542`→`#6BA543`, `#009BD7`/`#0099D5`→`#009BD6`, `#FDB116`→`#FEB100`.

**Two darks.** TC Text `#111A22` for body copy and captions; `#222B33` for a slightly lighter heading dark (headings only, never body).

**Warm accent is TC Yellow `#FEB100` only.** The gold `#F4A700` seen in older decks is off-brand; do not use it, normalize to `#FEB100`.

### Slide dimensions
12,192,000 × 6,858,000 EMU (13.33" × 7.5", standard 16:9 widescreen).

### Slide layouts — build every new slide from a template layout
The master defines a complete set of named layouts. When adding slides, instantiate one of these (or duplicate an existing slide that uses it) so the new slide inherits the theme, the footer lockup, and correct positioning. Do not invent layouts or hand-place chrome.

- **Covers / title:** Title Slide, Title1 (2_Title1), Title3 (1_Title3), Title - Agriculture
- **Section dividers:** Section - General, Section - Choose your own picture, Section - Residential, Section - Residential/SlatWall
- **Agenda:** Agenda — include one (right after the cover) when the deck has ~6+ content slides, 3+ distinct sections, or is external/formal; skip it for short (≤5-slide) or single-topic decks. 3–6 sentence-case items mirroring the section titles.
- **Content:** Title and Content, Title Only, Two Columns, Two Columns with Headings, Blank, DEFAULT
- **Picture:** Picture Left, Picture Right, 1 (full-picture)
- **Quote:** Quote, 1_Quote
- **Closing:** Ending, Ending1 (1_Ending, 1_Ending1)

Use the segment-specific divider where one exists (Residential, Agriculture, SlatWall) rather than recoloring a generic one. If a needed slide type is not listed, compose it inside Title and Content or Blank rather than creating a new master layout.

### Cover / section-divider slides
- Background: solid fill, TC Slate `#3A4B5B` (theme `accent1`).
- Logo lockup (white wordmark + yellow truss mark + "material + science" tagline): top-left, offset 537,460 / 473,468 EMU (≈0.59" / 0.52"), sized 3,898,508 × 861,773 EMU (≈4.26" × 0.94").
- Title text: white, bold, Aptos, below the logo lockup. One keyword within the title may be set in TC Yellow (`accent2`) for emphasis; the rest stays white. Do not yellow more than one phrase per title.
- Solo truss mark (solid TC Yellow `#FEB100`, no wordmark): bottom-right corner, offset ≈11.56" / 6.18", sized ≈1.18" × 0.93".
- The three light-grey outlined parallelograms sometimes on the cover are an optional flourish, not required. Omit unless deliberately reintroducing.

### Content slides
- Background: solid white (`bg1` / `lt1`).
- Title: top-left, offset 537,460 / 456,432 EMU (≈0.59" / 0.50"), width ≈11,117,083 EMU (≈12.16").
- Title type: **Aptos Light** (confirmed from the master `titleStyle`), **48pt to start**, TC Slate `#3A4B5C` (hardcoded, not theme-referenced), -20 letter-spacing, 100% line spacing. Not bold.
- **Title sizing rule:** 48pt is the starting size. If a title is too long for one comfortable line, it may be reduced to fit, **down to a hard floor of 32pt**. If it still will not fit at 32pt, **shorten or tighten the title** — never go below 32pt. Titles should not dominate the top of the slide; a title that needs sub-32pt type is a signal to cut words, not shrink further.
- Footer logo lockup (slate wordmark + yellow truss mark + tagline): bottom-right, offset ≈11.10" / 6.86", sized ≈1.66" × 0.37". Placed once on the slide master and inherited by every content layout. Do not duplicate it on individual slides.
- Body text font: Aptos throughout, set explicitly per text run (the theme default is Calibri Light and applies silently if Aptos is not set per run).
- **No all-caps kicker / eyebrow line above or below slide headings.** Use the heading alone with whitespace. (The one permitted exception is the small letter-spaced category label above a stat-card row, below.)
- **Bullet levels:** top-level bullets use the solid yellow truss glyph; sub-bullets use the outline (hollow) truss glyph — both are built into the master body style (levels 1 and 2). For a label plus supporting copy, put the label on the top bullet and the copy on an outline sub-bullet. No terminal period on any bullet (Section 12).
- **Body type scale — auto-tier ladder.** Content-slide body steps down a fixed ladder to fit the slide. Pick the **largest step where all content fits without crowding** (top-level / sub-bullet):
  - **28 / 24** — default (up to ~3 short items)
  - **24 / 20** — standard (3–4 items, or a line that wraps)
  - **20 / 16** — dense (only when needed; **16pt is the hard floor**)
  - If it will not fit at 20/16, **split the slide or cut copy** — never shrink below 16.

  Change the step by content density, and **reduce words before reducing size** (a 6-bullet slide should become two slides, not 16pt type). Card labels, captions, callouts, and flow-node text: 16–22pt. PowerPoint auto-fit stays on only as a backstop, never as the sizing mechanism. Industry reference for projected slides: title 36–44pt, body 24–28pt, captions 18–20pt; Trusscore titles are 48pt (title rule above).
- **Bullet spacing:** keep the glyph close to its text. Top-level bullets hang the text ~0.28" (256,032 EMU) from the glyph; sub-bullets indent ~0.28" further with the same tight gap. Override the master's wider default indent — do not leave a large gap between the truss glyph and the text.

### Stat / data cards
Used for executive summaries, KPI rows, and metric call-outs.

- Shape: rounded rectangle, corner radius 6% (`adj val 6000`) — a subtle rounding, not a pill.
- Fill: solid white `#FFFFFF`.
- Border: 0.75pt (9525 EMU), `#E1E5E8`.
- No shadow, no gradient (`effectLst` empty), consistent with Section 6.
- **No colored top-border accent stripe, and no left-side or any-side color-line border, on cards or boxes.** A colored edge line on a card, box, quote, or callout reads as generic AI-template filler (same reason as the icon-circle ban in Section 4). Carry category distinction through a section header label above the card row (e.g. "DIVISION 1 | SAMPLES" in TC Text, small caps or letter-spaced), not through per-card color or an edge stripe.
- Card label (e.g. "TOTAL SAMPLE UNITS"): small caps or uppercase, TC Text `#111A22`, muted weight.
- Big number: TC Slate or TC Text, bold, large — the focal point of the card.
- Supporting line: muted grey from the ramp (`#8A9BAC` or `#6A7A88`), not an off-palette grey.

**Card-row emphasis variant (approved).** A single stat/data card on its own stays white. But in a *row* of cards, fills may vary to create rhythm: white, a grey from the ramp (`#F5F6F7`, `#EEF1F3`), a light yellow tint (`#FFF8EC`), or full TC Slate `#3A4B5C`. The rule is that **exactly one card is the dark-slate stand-out** — the emphasis card carrying the row's most important number (number in TC Yellow `#FEB100`, label white, supporting line in a light grey such as `#DDE3E8`). Constraints: only one dark-slate card per row; never make every card a different color (that reads as the rejected AI dashboard); do not pair yellow-tint and blue fills in the same row; keep the hairline border, 6% radius, and no-shadow rules. This is fill-for-emphasis, not the banned per-card *edge stripe*.

### Trend / delta indicators — approved functional exception
Up/down change indicators (e.g. "▲ 193.2% MoM", "▼ 54.5% MoM") use red for decline and green for growth. This is a functional convention parallel to the red/green rules for financial spreadsheets; it is not decorative color-coding and is not subject to the 60-30-10 yellow ceiling or the card-accent ban, because it is a data signal attached to a specific number, not a category indicator.
- Decline: red `#DC3545`.
- Growth: TC Green `#6BA543`.
- This red is reserved exclusively for this functional purpose and is used nowhere else in Trusscore visual identity. (Older decks used `#E05C5C` / `#C0392B` here; those are off-spec — standardize on `#DC3545`.)

### Callout / highlight boxes
- Fill: light yellow tint `#FFF8EC`.
- Border: TC Yellow `#FEB100`.
- Used sparingly — one per slide maximum, reserved for a genuinely important takeaway, not a repeating per-slide device.

### Visual and text balance (mix, do not max)
Two failure modes are both off-brand: a deck of nothing but headings and bullets (boring), and a deck where every slide is a card grid or stat block (busy, and it reads as a template). Trusscore decks deliberately mix the two.

- **Roughly half and half.** Across the content slides, about half carry a built visual treatment (card row, stat callouts, flow diagram, two-column, or a real photo) and about half are text-forward (a heading with concise prose or one short, clean list). A well-set text slide is on-brand, not a failure — whitespace is a feature.
- **One treatment per slide.** Choose a single dominant device per slide. Never stack a card row, stat callouts, and a callout box on one slide.
- **Rotate for rhythm.** No more than two visually-heavy slides in a row; alternate text-forward and visual slides so the deck breathes.
- **Earn the visual.** Use a graphic only when the content fits it: numbers → stat callouts; parallel items → a card row; a sequence → a flow diagram; a comparison → two columns; a real space → a photo. If the point is explanatory, keep it a clean text slide.
- **Density cap.** At most about 60% of content slides should carry a built graphic. The cover, the closing slate slide, and any full-photo slide count on the visual side. Tune the ratio to the audience — a data readout leans more visual, a narrative deck leans more text — but never let the whole deck collapse to one mode.

---

## pptx color-pop rule (avoiding flat-deck fatigue without sliding back to generic)

Bare Slate icons are the default and must not be replaced with colored circles (Section 4 of the core skill). But an all-Slate deck across 20+ slides can read as flat. One controlled yellow accent per slide is permitted — never more than one, and never stacked with another pop technique on the same slide. Pick based on what the slide is actually doing:

| Slide content | Pop technique |
|---|---|
| Feature/benefit list where one item is genuinely the most important — not just the first or most convenient to pick | Recolor that one icon's stroke to TC Yellow `#FEB100`; every sibling icon on the slide stays TC Slate |
| A metric, stat, or number worth remembering | The number itself renders in TC Yellow, bold; all icons on the slide stay TC Slate |
| One dominant idea anchoring the whole slide | A single icon at hero size (32px, Section 4) in TC Yellow as the focal point; all other icons on the slide stay small and TC Slate |

**Before using technique 1:** confirm the content actually has a hierarchy — one item the audience should walk away remembering over the others. If all items on the list carry equal weight, do not force a winner by recoloring one icon arbitrarily; that reads as random rather than intentional. Default to all-Slate instead, or use technique 2/3 if the slide has a genuine standout stat or single idea.

**Hard limits, regardless of technique chosen:**
- Maximum one pop per slide — never two yellow elements (e.g., a yellow stat AND a yellow icon) on the same slide
- This still counts against the 60-30-10 yellow ceiling (Section 2) — don't treat "one pop per slide" as license to ignore the overall ratio across the deck
- If a slide has no clear standout item, stat, or dominant idea, default to all-Slate — don't force a pop where the content doesn't earn one

---

## Pre-publication checklist — PowerPoint

- [ ] Aptos set explicitly on every text run — not left to inherit the theme's Calibri Light default
- [ ] Title color is hardcoded `#3A4B5C` — not pulled from the theme's `accent1`/`dk2` swatch (which contains a one-digit typo, `#3A4B5B`)
- [ ] Stat/data cards are white with a thin neutral border — no colored top-border accent stripe
- [ ] Card category distinction comes from a section header label, not per-card color-coding
- [ ] Red/green trend indicators used only for actual up/down deltas attached to a number — never as decorative or category color
- [ ] No icon-in-colored-circle treatment (see Section 4 and pptx color-pop rule)
- [ ] Footer logo lockup inherited from the slide master — not duplicated manually on individual slides
