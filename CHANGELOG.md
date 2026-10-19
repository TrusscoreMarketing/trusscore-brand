# Changelog

All notable changes to the Trusscore brand system are recorded here. Format follows [Keep a Changelog](https://keepachangelog.com); versions follow [Semantic Versioning](https://semver.org).

## [1.4.10] — 2026-10-19

### Fixed
- **TC Grey is never text on light backgrounds (Section 3b):** the TC Grey block listed "body text" in its heading and approved it for secondary body text and captions, which contradicted Section 2 and the pre-publication checklist. TC Grey `#DFDBDA` measures 1.37:1 on white, so it fails WCAG AA at any size. The heading now reads "borders, card fills, and dividers only," the intro states the no-text rule, and the body-text bullet is removed. The `de-slop` visual check already flagged TC Grey as text, so it needed no change.

## [1.4.9] — 2026-10-16

### Fixed
- **RibCore symbol (Section 13):** RIBCORE is registered in both Canada and the United States, so the product name now reads RibCore® by Trusscore® (it was RibCore™). Mirrored into `USAGE.md` and the `de-slop` voice check. NorLock stays NorLock™ by Trusscore®: only the NorLock logo is registered in either country, not the word. Wall&CeilingBoard™, SlatWall™ and DockDeck™ stay ™; no registrations were found for them. Checked against CIPO records and third-party USPTO mirrors; U.S. status still to be confirmed in USPTO TSDR.

## [1.4.8] — 2026-10-16

### Changed
- **TC Yellow never on black or TC Text (Section 2):** stated explicitly in the yellow text rule and the TC Yellow row of the contrast table. Both pass contrast (about 9.6:1), so this is a brand rule, not a contrast one; it was previously implied only by the background rule. Mirrored into the `trusscore-pptx` skill and the `de-slop` visual check.

## [1.4.7] — 2026-10-14

### Fixed
- **Stretched logos in decks.** Root causes: (1) Section 14b gave the content-slide footer as the tagline lockup at 1.66" × 0.37"; the master footer is actually the wordmark only at 1.62" × 0.24", so a logo placed to the written spec came out about 34% too tall. (2) The cover's bottom-right mark was described as the "solo truss mark" but is the T-icon (1.26 : 1); the truss-only file (2.71 : 1) placed in that box stretches to twice its height. The asset READMEs pointed to the truss-only file for the cover. (3) Nothing told builds to lock proportions, and both python-pptx and pptxgenjs distort an image given a width and a height.
- Corrected the cover and footer logo specs in Section 14b, the `trusscore-pptx` mirror, and the asset READMEs, with the proportions of each logo file.

### Added
- **Builder stretch guard (`trusscore_deck.py`):** `logo()` places a logo from the master template with proportions locked; `save()` refuses to save a deck containing a stretched picture; `check_images()` and `python trusscore_deck.py check deck.pptx` audit any deck, however it was built.
- **All-white logo restricted (Section 8).** The one-colour white logo is used only on TC Yellow backgrounds or in black-and-white print; slate and dark backgrounds use the reversed logo with the yellow truss. Previously Section 8 also allowed it on midtone backgrounds. Mirrored into the Do Nots, the Section 15 checklist, the asset READMEs, the `trusscore-pptx` skill, and the `de-slop` visual check.
- **Approved text and background contrast pairs (Section 2).** Replaced the Smart Text table with a full contrast table built from the accessible brand colours grid (`brand/color/accessible-brand-colors.webp`), with WCAG ratios, plus TC Blue, TC Green, the light tints, and the grey ramp. Fixes several failures the old rules allowed: white text on TC Green (2.96) and TC Blue (3.15, large only), TC Grey as secondary text (1.37), and `#8A9BAC` / `#6A7A88` as small muted text. Small muted text is now `#5A6B78` (already the dashboard secondary text). Mirrored into Section 14b, the Section 15 checklist, the `trusscore-pptx` skill, and the `de-slop` visual check.
- **Dark Navy `#0F1C27` added to the palette (Section 2):** the darker option when TC Slate is not dark enough, such as text on TC Yellow or a deeper dark surface. Added a Dark Navy background section with approved on-colours.
- **TC Text and TC Yellow never together:** no TC Text on yellow and no yellow on TC Text. Primary CTA buttons (yellow fill) now use TC Slate text instead of TC Text in all four button specs. Caption text on white was TC Grey (1.37:1) and is now TC Text or `#5A6B78`.
- **Backgrounds are always a brand colour:** white, an approved tint, TC Yellow, TC Slate, or Dark Navy. Never black, near-black, TC Text, or an off-palette dark, even when a format skill or template defaults to dark mode. Mirrored into the checklist, the `trusscore-pptx` palette override, and the `de-slop` visual check.
- **Builder contrast fixes (`trusscore_deck.py`):** card and flow role labels were TC Yellow on white/light grey (about 1.7:1) and are now `#5A6B78` (yellow stays on slate cards); status cards had green or yellow label text and now use a coloured truss marker with a TC Slate label; muted supporting text moved from `#6A7A88` to `#5A6B78`.
- "Logos — never stretched" section in the `trusscore-pptx` skill (how stretching happens, how to place logos, a proportions table); stretch check added to the deck review steps, the Section 15 checklist, Section 8 Do Nots, and the `de-slop` visual check.

## [1.4.6] — 2026-07-08

### Fixed
- **Bundled builder refinements (`trusscore_deck.py`), from a de-slop pass on the playbook:** callouts now keep their terminal period (they are full sentences, not bullet fragments); removed the yellow corner accent from `cards()` so cards carry no edge accent (aligns with the Section 14b no-edge-accent rule).

## [1.4.5] — 2026-07-08

### Added
- **Body type scale — auto-tier ladder (Section 14b + pptx skill):** content-slide body steps down a fixed ladder to fit the slide — 28/24 (default) → 24/20 → 20/16 (dense) — picking the largest step where all content fits; below the floor the slide is split or copy is cut, never shrunk past 16pt. Card labels, captions, callouts, and flow-node text sit at 16–22pt. Documented industry reference ranges (title 36–44, body 24–28, captions 18–20). The build scripts implement the ladder via a `pick_tier` estimator; PowerPoint auto-fit is a backstop only.
- **Bullet spacing rule (Section 14b + pptx skill):** override the master's wide indent so the truss glyph sits tight to its text (~0.28" hanging); sub-bullets indent ~0.28" further with the same gap.
- **Bundled builder `skills/trusscore-pptx/scripts/trusscore_deck.py`:** a canonical Python builder that enforces the spec in code — auto-tier type ladder (`pick_tier`), tight bullet spacing, two-level truss bullets, no terminal periods, the locked palette, and the master template. High-level API (`open_deck`, `cover`, `agenda`, `section`, `content`, `cards`, `stats`, `flow`, `status_row`, `callout`, `close`, `save`). The pptx skill now instructs builds to use it so sizing/spacing can't drift.

### Fixed
- Rebuilt the brand-system overview and the new AI Output Brand Alignment Playbook to the corrected type scale and bullet spacing (previous drafts rendered body copy too small at 16–20pt).

## [1.4.4] — 2026-07-07

### Added
- **No terminal period on bullet points (Section 12):** bullets are fragments and do not take an end period. Full-sentence callout boxes and body paragraphs still take normal end punctuation. Mirrored into the `trusscore-pptx` skill and the `de-slop` voice check (a bullet ending in a period is now a finding).
- **Two-level truss bullet structure (Section 12 + 14b):** documented the preferred label + supporting-copy pattern — label on the top-level bullet (solid truss glyph, no period), supporting copy on an outline-truss sub-bullet beneath it. Both bullet glyphs are built into the master body style (levels 1 and 2).
- **Agenda-slide rule:** documented when to include an agenda slide (from the `Agenda` layout, right after the cover) — decks with ~6+ content slides, 3+ distinct sections, or external/formal audiences get one; short (≤5-slide) or single-topic decks skip it. 3–6 sentence-case items mirroring the section titles. Added to the `trusscore-pptx` skill and Section 14b so agenda inclusion is a deliberate decision, not an omission by default.

## [1.4.3] — 2026-07-07

### Added
- **Review gate (Section 0):** added a standing rule to run the `de-slop` skill on any finished Trusscore deliverable (deck, doc, email, social post, landing page, dashboard, or designed asset) and apply fixes before delivery. Placed in the always-read Section 0 so it rides along on all Trusscore work, extending the review gate that `trusscore-pptx` already runs for decks to every deliverable type.

## [1.4.2] — 2026-07-07

### Added
- **Section 14b — stat-card-row emphasis variant:** a lone stat card stays white, but a *row* of cards may use varied fills (white, ramp grey, light-yellow tint, or full TC Slate) for rhythm, with exactly one dark-slate stand-out card carrying the key number (number in TC Yellow, label white). Guardrails: one slate card per row, never every card a different color, no yellow-plus-blue fills in one row, and this is fill-for-emphasis, not the banned edge stripe. Mirrored into the `trusscore-pptx` skill and the `de-slop` visual check so a slate emphasis card grades as Aligned.

## [1.4.1] — 2026-07-07

### Changed
- **Section 14b — title type corrected:** content-slide titles are **Aptos Light, 48pt** (confirmed from the master `titleStyle`), not "Aptos regular / no Light" as previously written. Added the title sizing rule: start at 48pt, reduce to fit only down to a hard floor of 32pt, and shorten the title rather than going below 32pt. The `trusscore-pptx` skill mirror was updated to match.
- **Section 14b — visual/text balance rule added:** decks must mix visual and text-forward slides (roughly half and half, one dominant treatment per slide, no more than two visually-heavy slides in a row, ~60% graphic-slide cap). Prevents both the all-bullets and all-cards failure modes. Mirrored in the `trusscore-pptx` skill.

### Fixed
- Re-synced the deployed `trusscore-pptx` SKILL so the card-border grey reads `#E1E5E8` (superseding `#E3E7EB`) and no "DRAFT" marker remains.

## [1.4.0] — 2026-07-07

### Added
- **`trusscore-pptx` skill:** new brand layer over the public pptx skill. Enforces Section 14b, builds new slides from the template's 26 named layouts, bundles the master template under `skills/trusscore-pptx/assets/`, and routes finished decks through de-slop for review.
- **`de-slop` skill (brought in-repo):** the copy + visual review gate now lives under `skills/de-slop/`. Populated its Trusscore standards from the brand skill and the example decks: `references/checks/visual.md` (all design surfaces — web, HTML dashboards, decks, docs, social, diagrams), `references/checks/voice.md`, and `references/contexts/marketing.md`. `company-fit.md` and the support/sales context profiles remain placeholders pending strategy/ICP inputs.
- **PowerPoint example decks** committed under `brand/pptx-examples/` as the reference source for the 14b revision.

### Changed
- **Section 14b (PowerPoint Visual Spec):** revised against two production decks. Added the slate-tinted neutral grey ramp (`#F5F6F7` → `#6A7A88`), a second heading dark (`#222B33`, alongside body `#111A22`), and a Slide Layouts menu (26 named layouts to build new slides from). Standardized the card border on `#E1E5E8` (supersedes `#E3E7EB`) and card radius at 6%. Extended the card top-stripe ban to left-side and any-side box/card borders, and banned all-caps kicker lines above/below headings (except the stat-card row label). Normalized near-duplicate colors to canon; reaffirmed `#DC3545` as the only decline red (flagged deck `#E05C5C`/`#C0392B` as off-spec) and rejected gold `#F4A700`.

## [1.3.0] — 2026-07-06

### Added
- **Logo library:** full master set added and organized — one-colour white, tagline lockups (slate, reverse, one-colour white), T-icons (slate, white, white+yellow), truss elements, PNG exports at 1x/2x/3x including favicons, and EPS print versions under `brand/logos/eps/`.
- **Sub-brand logos** → `brand/logos/programs/`: Trusscore University (primary and reverse, each with and without icon) and Trusscore Trusted Installer (slate, white).
- **Fonts:** Mulish variable and static fonts committed (SIL OFL).
- **Color:** Adobe Creative Cloud library `trusscore-brand-colours.cclibs`, plus generated `trusscore.ase` and `trusscore.aco` swatch files.
- **Docs:** `brand/product-images/README.md` pointer for the external photo library.
- **Skill assets:** bundled the lean logo subset the skill references (primary, reversed, one-colour white, tagline slate and reverse, truss element).

### Changed
- Normalized logo filenames to kebab-case, nested raster exports under `brand/logos/png/`, and refreshed the logos, programs, color, and fonts READMEs.

## [1.2.0] — 2026-07-06

### Added
- **Logo Rules (Section 8):** distinguished the two marks and their standalone rules. The **truss mark** (the shape) may be used alone as a graphic accent. The **T-icon** (truss-plus-T monogram) may stand alone only as a favicon or app tile; in every other use it must appear with the full logo visible or with "trusscore.com" nearby, since the brand is not recognised by the icon alone. Added a matching "Do Not" bullet.
- **Logo Rules (Section 8):** sub-brand and program logo section covering Trusscore Trusted Installer, Trusscore Community Partners, and Trusscore University — use the official pre-created logo file for each; never recreate, restyle, or generate a new version.

### Fixed
- **HTML Dashboard (Section 14c):** the reversed-white logo reference now points to the bundled `assets/logos/trusscore-logo-white.svg`, replacing the stale `RS5369_Trusscore_Logo_White__SVG01.png` filename.

## [1.1.0] — 2026-07-06

### Added
- **Typography (Section 7):** line-length measure (45–75 characters), `rem` and `font-display: swap` implementation guidance with the approved font stack, and a WCAG 2.2 AA text-contrast table.
- **Interactive and motion accessibility (Section 5):** 44×44px touch-target standard (24×24px hard floor), visible keyboard-focus states, and `prefers-reduced-motion` support.
- **Image production (Section 14):** dimension and file-weight budgets for web and email, WebP-first format guidance, retina/`srcset`, and image alt-text requirements.
- **Checklist (Section 15):** new Accessibility and Image production groups.

### Notes
- Sourced from the uploaded "Brand Typography & Image Guidelines." Dropped its fixed golden-ratio scale and Arial fallback (both conflict with Section 7), corrected the touch-target level (44×44 is AAA/platform, not the AA minimum of 24×24), fixed the large-text ratio to 3:1, and added measure, alt text, font-loading, and reduced-motion, which the source omitted.

## [1.0.0] — 2026-07-06

First version-controlled release. Consolidates the brand guidelines, the Cowork brand skill, and the master assets into one repository.

### Changed
- Adopted `trusscore-brand-guidelines` as the authoritative brand skill, replacing the older `brand-style-guide` skill (CMOS 17th edition).
- Editorial standard set to **Chicago Manual of Style, 18th edition (2024)**.
- Locked accent colors: **TC Blue `#009BD6`** and **TC Green `#6BA543`** — removed the prior "suggested" and "confirm needed" placeholders, and reconciled these values across Sections 2, 14b, and 14c.
- Renamed the body-copy color from **TC Text Slate** to **TC Text** (`#111A22`) throughout.

### Added
- Commercial and Agricultural campaign lines: **"Built to Last"** and **"Discover the Strength and Durability of Trusscore"** (both approved).
- Section 0: precedence of brand rules over format-skill defaults (docx, pptx, xlsx, pdf).
- Section 14b: PowerPoint visual spec, built from production XML.
- Section 14c: HTML dashboard spec, verified against production dashboards.
- Expanded Section 15 pre-publication checklist with PowerPoint and HTML dashboard items.

### Removed
- All left-border accent treatments — banned on every element and background, with no exception, to avoid a generic "AI output" look.
- Removed possessive uses of the brand name from the guidelines prose.

### Notes / follow-ups
- Add master logo SVGs to `skills/trusscore-brand-guidelines/assets/logos/` and to `brand/logos/`. The prior `RS5369_Trusscore_Logo_White__SVG01.png` contained only the truss mark; re-export the white lockup from the original source (Illustrator/Figma).
- Align the account-level brand preferences with this version (18th edition CMOS, locked colors, "Built to Last").
