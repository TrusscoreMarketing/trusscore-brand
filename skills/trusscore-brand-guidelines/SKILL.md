---
name: trusscore-brand-guidelines
description: "Applies the official Trusscore brand colors, typography, voice, and editorial standards to any artifact, document, design, or copy. Use for ALL Trusscore work whenever brand colors, style guidelines, visual formatting, or Trusscore editorial standards apply. This is the authoritative Trusscore brand skill—always use this, not the generic brand-guidelines skill."
---

# Trusscore Brand Guidelines

Encodes the official Trusscore brand identity (Style Guide effective April 21, 2026 + Brand Guidelines PDF). Apply to all Trusscore artifacts, designs, documents, presentations, and copy.

**Keywords**: Trusscore, branding, brand voice, brand colors, typography, visual identity, corporate identity, editorial standards, style guide, marketing, copy, design

This file is the always-loaded core: precedence, colors, typography-by-context, editorial rules, and the core checklist. Format-specific specs load on demand:

| Reference file | Load when |
|---|---|
| `references/docx.md` | Building or reviewing any Word/print document (.docx) |
| `references/pptx-spec.md` | Building or reviewing any PowerPoint (.pptx) — full Section 14b spec + color-pop rule |
| `references/dashboards.md` | Building or reviewing any HTML dashboard or report page (Section 14c) |
| `references/web-imagery.md` | Web/HTML pages, designed layouts, icons, buttons, imagery, overlays, spacing/divider decisions (Sections 3, 3b, 4, 5, 6, 7-web, 14) |

**Author-time rule:** if copy is destined for an outbound format (docx, pptx, web, email), apply this editorial core while drafting — not only at conversion time.

---

## 0. Precedence Over Format Skills — Read This First

### Review gate — run de-slop before delivering
Before delivering any finished Trusscore deliverable — deck, document, email, social post, landing page, dashboard, or designed asset — run the `de-slop` skill and apply the fixes it flags, then deliver. This is the standing quality gate for **all** Trusscore output. de-slop detects and suggests; you own the fixes. Skip only when the user explicitly says to, or for trivial conversational replies. (Format skills such as `trusscore-pptx` already call de-slop as their final step.)

When producing a docx, pptx, or other format-specific artifact, the format skill governs **mechanics only** — file structure, XML validity, page sizing, QA rendering. It does NOT govern brand decisions. Where a format skill states a default or a "never do X" for font, color, or layout that conflicts with this skill, **this skill wins, every time, with no exception.**

### Confirmed conflicts to actively override

| Format skill says | This skill requires instead |
|---|---|
| docx SKILL.md defaults to Arial font, black titles | Use Aptos (Office documents). Titles use TC Slate `#3A4B5C`, not black. Apply explicitly in every `styles.default` and `Heading` override — do not rely on the docx skill's built-in default block. |
| pptx SKILL.md says "never default to Aptos" (cites missing metric-compatible substitute, risk on older Office installs) | Aptos is the correct Trusscore Office font for pptx body and headings. The QA-rendering caveat is real — LibreOffice-based QA may substitute a different-width font, so check rendered text bounds with ~10% slack — but the font choice does not change. Never substitute Calibri or Arial unprompted; Calibri is the documented fallback only for compatibility issues the user has explicitly flagged. |
| pptx SKILL.md's go-to "visual motif" is icons inside colored circles on every slide | Never use circle containers around icons in any Trusscore digital artifact (pptx included). Circles are approved only for print merchandising. Default is the bare Lucide icon: Slate stroke, no container (`references/web-imagery.md` Section 4). One controlled yellow accent per slide is permitted instead — see the pptx color-pop rule in `references/pptx-spec.md`. |
| docx/xlsx SKILL.md defaults to Arial (or "Arial, Times New Roman") "unless otherwise instructed" | This skill is the instruction. Aptos, every time, for Trusscore Office deliverables. |

**Standing rule:** before finalizing any Trusscore docx or pptx, re-check that the format skill's own stated defaults (font family, title color, background color, accent color) were explicitly overridden in code — not left to fall through. If this skill is silent on a specific mechanical point (e.g., table width units, XML schema order), defer to the format skill; mechanics are not brand decisions.

---

## 1. Brand Foundation

**Mission:** Trusscore is a material science company for sustainable building materials.
**Vision:** To create a market-leading, sustainable, branded, true painted-drywall-alternative.

**Campaign lines — scope is a hard rule:**
- **Residential consumer-facing (Level 1):** "Real Life Looks Good Here" — homepage, residential campaigns, brand storytelling. Supporting: *Built for the everyday moments. Life gets messy. Trusscore makes sure you're ready for it.*
- **Commercial & Agricultural:** "Built to Last" / "Discover the Strength and Durability of Trusscore" — durability, longevity, cost of ownership. Never use the residential lines in commercial, agricultural, or industrial contexts.
- **Billboard/hook (Level 2, residential/renovation only):** "Goodbye drywall, hello [Trusscore logo]" — one line where space allows; when broken to two lines, the logo sits on line two at the same width as line one. "Trusscore" is never set in type here — always the logo mark. Never in commercial/agricultural/industrial contexts.

---

## 2. Colors

| Color | HEX | Usage |
|---|---|---|
| TC Slate | `#3A4B5C` | Primary brand color, headings, design elements |
| TC Text | `#111A22` | Body text only — never a design element |
| TC Yellow | `#FEB100` | Logo truss mark, graphics, accents — **NEVER text on white** |
| TC Grey | `#DFDBDA` | Backgrounds, neutral elements |
| White | `#FFFFFF` | Reversed logo, light backgrounds |

Additional on-brand accents: TC Blue `#009BD6` (cool mid-blue), TC Green `#6BA543` (muted; agricultural/commercial), TC Light Slate `#6B7F8E` (secondary elements), TC Yellow Tint `#FFF0C2` (light callout fills). Shape/accent cycling order for non-text elements: Slate → Yellow → Blue → Green.

**Hard rules:**
- TC Yellow is 1.9:1 on white — fails WCAG; never body or headline text on white (dark backgrounds only, unless a brand-team-approved size threshold is met).
- TC Text `#111A22` is reserved for body copy and captions on light backgrounds. Never a heading color, shape fill, background, or design element; never on TC Yellow backgrounds (use TC Slate there).
- TC Grey `#DFDBDA` is approved for borders, card fills, dividers, and secondary body text only — never a section background fill (pinkish-warm undertone sits outside the section-tint families).
- Smart text color: light backgrounds (white / TC Grey / yellow tints) → TC Text; dark backgrounds (TC Slate / Blue / Green) → white; TC Yellow background → TC Text.
- All text meets WCAG 2.2 AA: 4.5:1 regular, 3:1 large text (24px+, or 18.66px+ bold) and UI graphics.

### 60-30-10 Color Rule

Governs every color decision, all media: **60%** white / TC Grey / light neutrals (backgrounds, whitespace) · **30%** TC Slate (headers, dark sections, structure) · **10%** TC Yellow (CTAs, icons, highlights). TC Yellow fatigues at scale; its impact comes from restraint — above ~10% of surface area it becomes noise. Derived rules:
- Never yellow-fill more than one element type per visual section (not background + icons, not background + button, not icons + heading)
- A large yellow background (hero, banner, footer strip) is the full yellow allocation for that layout — no other yellow in it or the adjacent section
- Minimum one neutral (white or TC Grey) buffer section between any two yellow-heavy elements
- Yellow accents may coexist only while total yellow stays under ~10% of surface area
- When in doubt: remove a yellow element, not add one

### Universal design bans (all formats — details in `references/web-imagery.md`)

- No colored or grey **left-border accent bars** on any element (headings, quotes, callouts, cards) — no exception; the generic-AI tell
- No **decorative shadows** — shadows only on genuinely elevated UI (modals, dropdowns, tooltips), always slate-based, never black
- No **gradient overlays** on photography; no color grading or tinting
- No **icon circle containers** in digital artifacts; Lucide outline icons only, 1.5px stroke
- No **TC Yellow full-width horizontal rule** under headings
- Spacing on an **8pt grid**; border radius **4px** on digital elements
- Truss-mark parallelogram only at true geometry (2.56:1, skew 0.77, 38° / `skewX(-38deg)`) — never stretched, never a full-width divider

---

## 7. Typography (by context)

| Context | Typeface | Weights |
|---|---|---|
| Print / Premium | Circular Std | Bold, Book, Light |
| Microsoft Office (docx, pptx, xlsx) | Aptos | Regular, Bold |
| Web / Digital | Muli Variable (Mulish) | 900, 700, 515, 440, 400 |

- Primary design font: Circular Std Book (body/descriptive copy); headings Circular Std Bold or Aptos Bold (Office)
- Fallback chain, first available: Circular Variable → Muli Variable → Mulish → Aptos (default for Microsoft programs). **Arial and Georgia are not approved fallbacks.**
- Circular Std Light: not approved for body copy or any text below 18px at screen resolution — use Book
- Full web type system (clamp() scale, line heights, letter spacing, measure, font loading, contrast tables): `references/web-imagery.md`. Word document sizes: `references/docx.md`. Deck sizes: `references/pptx-spec.md`.

---

## 8. Logo Rules

- **Variants:** Primary (wordmark + TC Yellow truss on white/light) · Reversed (white wordmark + yellow truss on dark/TC Slate) · One-color (all white or all slate for B&W print or midtone backgrounds)
- **Truss mark** (yellow parallelogram) may stand alone as a graphic accent — it is an accent, not a logo, and never carries brand identification by itself
- **T-icon** (truss + "T" monogram) stands alone in exactly one place: favicon / app tile. Everywhere else, pair it with the full logo or "trusscore.com" nearby — Trusscore is not recognized by the icon alone
- **Clear space:** minimum 1× the height and 1.5× the width of the lowercase `t` in the wordmark, all sides
- **Tagline** ("material + science"): only in the approved lock-up, always paired with the logo, never standalone. Minimums: 10px cap height digital, 8pt Circular Std print. Below that, use the wordmark-only version
- **Sub-brand/program logos** (Trusted Installer, Community Partners, Trusscore University): use only the official pre-created file (`brand/logos/programs/`) — never recreate, redraw, restyle, recolor, or re-typeset. If unavailable, use the parent Trusscore logo and request the asset. They inherit all parent rules
- **Never:** add elements to the logo · adjust wordmark letter spacing · change wordmark case · color the wordmark anything but TC Slate or white · color the truss anything but TC Yellow (Blue/Green only for approved special cases) · stretch or distort · modify the tagline lock-up · place on busy backgrounds · render "trusscore" as styled text in place of the logo file

---

## 9. Brand Voice

(For spec sheets, install guides, warranty docs, see Section 16.)

**Voice character:** friendly, plainspoken, helpful, confident, and smart — a trusted contractor who's also a good communicator.

**Do use:** customer-first language · active voice, short sentences · problem/solution framing · benefits-first · "Life gets messy" (not "challenges occur") · "Weekend warriors" (homeowner/residential ONLY — never contractor, commercial, or agricultural copy) · "Magic marker masterpieces" (not "accidental marks") · "Real life" (not "daily activities")

**Never use:** "Synergy" · "Guru" or "Expert" · "Disruptor" · "Game-changer" · "Leverage" as a verb (use "use") · "Innovative solution" · "Best-in-class" (prove it with specifics) · "Plastic" — always "material" or the specific product name

**Hedge stacking** (brand/marketing/consumer copy only — technical docs exempt, Section 16): never stack more than one qualifier per claim. "Can help reduce," "may vary in some cases," "in many situations" compound into copy that commits to nothing. Fix: state the claim directly, or qualify it once with a specific condition (number, condition, timeframe). Not "This can help improve moisture resistance in many cases" — use "It's moisture-resistant."

## 10. Audience-Specific Tone

| Audience | Tone | Focus | Avoid |
|---|---|---|---|
| Homeowners | Warm, relatable, empowering | Real moments, family life, DIY accessibility, finished look | Technical specs, contractor jargon, product-first language |
| Contractors | Peer-to-peer, professional, results-oriented | Install speed, reliability, reputation protection | Consumer lifestyle language, "weekend warrior," buzzwords |
| Commercial / Agricultural | Technical, direct, ROI-focused | Durability, moisture resistance, washdown, cost of ownership | Residential lifestyle language, drywall as comparison point |
| Architects / Specifiers | Design-forward, technically precise, collaborative | Material data, code compliance, finish quality, spec accuracy | Consumer tone, vague claims without data, abbreviated product names |

## 11. Capitalization & Spelling

Chicago Manual of Style, 18th Edition.

- **Title Case** for H1 page headlines, H2 section headers, campaign headlines, product names, marketing materials. Capitalize first and last words always; nouns, pronouns, verbs, adjectives, adverbs; prepositions of 5+ letters; both parts of hyphenated compounds (Moisture-Resistant). Lowercase articles, coordinating conjunctions, prepositions of 4 or fewer letters, infinitive "to".
- **Sentence case** for subtitles under headlines (always — conversational feel), body copy, blog headlines, email subject lines, social posts, H3+ subheadings, product descriptions. Capitalize only the first word, proper nouns, product names, and the first word after a colon/em dash introducing a new sentence.
- **U.S. spelling in all customer-facing copy** — color, gray, center, aluminum — confirmed house practice from live trusscore.com product copy. Canadian/UK spellings are a finding.

## 12. Punctuation Rules

- **Headlines/titles:** single-sentence — no period. Multi-sentence — periods between sentences.
- **Em dashes:** no spaces, always `word—word`. Maximum two per content piece; beyond that, restructure (colon after a bold label, comma, or sentence break). This company standard **overrides** any generic "no em dashes ever" rule (e.g., de-slop's ai-writing check).
- **En dashes/hyphens:** no spaces. En dash for ranges (12–18 inches); hyphen for compounds (moisture-resistant). "DIY-friendly" is homeowner-only.
- **Oxford comma:** always, in every list of 3+.
- **Bullets — no terminal period.** Bullets are fragments; never end one with a period, even a full clause. Bold label + supporting copy: prefer two levels (label on the top-level solid-truss bullet, copy on an outline-glyph sub-bullet, no period after the label); a single-level bold lead-in with separator period ("**Brand guidelines.** The rulebook…") is acceptable. Exceptions keeping normal end punctuation: full-sentence callout/takeaway boxes, and body paragraphs. If 2+ bullets are full sentences needing punctuation, rewrite them as fragments.
- Fractions not decimals (1-1/4" not 1.25"); imperial units first.

## 13. Brand Name Usage Rules

- **No possessive — critical.** Never "Trusscore's" in any form. Rewrite: Trusscore panels, Trusscore performance, Trusscore delivers.
- **Product names, full with trademarks on first reference:** Trusscore® Wall&CeilingBoard™ · Trusscore® SlatWall™ · Trusscore® Trims (no ™ on Trims) · NorLock™ by Trusscore® · RibCore™ by Trusscore® · DockDeck™ by Trusscore®. Short forms OK on subsequent references (same page, 6+ appearances): Wall&CeilingBoard, SlatWall.
- **Never acceptable in any context:** WCB, W&C, SW, TC panels, TC boards, Trusscore boards, plastic panels, PVC panels.

---

## 15. Quick Reference Checklist (Pre-Publication)

**Editorial**
- [ ] No possessive form of Trusscore anywhere
- [ ] No spaces around em dashes; maximum two per piece
- [ ] Oxford comma in all lists of 3+
- [ ] No periods ending single-sentence headlines or bullets
- [ ] Title Case on H1/H2/headlines; sentence case on subtitles and body; U.S. spelling
- [ ] No banned buzzwords (game-changer, leverage, plastic, etc.)
- [ ] Audience tone matches the target (no homeowner language in commercial copy)
- [ ] Product names full with trademarks on first reference; no abbreviations (WCB, SW, etc.)

**Color**
- [ ] TC Yellow never text on any background; usage at or under 10% (60-30-10)
- [ ] TC Text only for body/captions on light backgrounds — never headings, fills, or on TC Yellow
- [ ] TC Grey only for borders, card fills, dividers, secondary text — never a section background
- [ ] Headings TC Slate on light, white on TC Slate
- [ ] No two yellow-heavy elements without a neutral buffer; white-on-yellow text only 36px+/Bold/max 6 words
- [ ] On-element colors match the approved background pairings (`references/web-imagery.md` Section 3b)

**Typography & Logo**
- [ ] Circular Std (design) / Aptos (Office) / Muli-Mulish (web) — never Arial or Georgia
- [ ] Tagline only in the approved lock-up; logo clear space respected; logo is the real asset file, never styled text

**Format-specific** — run the matching block before delivery:
- [ ] Word/print docs → `references/docx.md` checklist
- [ ] PowerPoint → `references/pptx-spec.md` checklist
- [ ] HTML dashboards → `references/dashboards.md` checklist
- [ ] Web pages, imagery, designed layouts → `references/web-imagery.md` checklist

---

## 16. Technical Documentation Standards

Applies to spec sheets, installation guides, warranty documentation. Section 9 governs brand/marketing/consumer copy; this governs technical content.

- **Structure — Jobs to Be Done:** organize around what the contractor needs to do, not the spec category. Headings name the task: not "Section 4: Saw Specifications" but "Cutting Panels for a Corner Install"; not "Fastener Requirements" but "Fastening Panels to Metal Studs".
- **Voice — active, action-oriented:** lead with the verb. Not "Panels should be cut using a fine-tooth blade" but "Cut panels with a fine-tooth blade." Not "A 1/8-inch gap is recommended" but "Leave a 1/8-inch gap between panels."
- **Hedge-stacking exemption:** Section 9's rule does not apply here. Conditional phrasing tied to a real variable ("performance may vary depending on installation conditions," "torque to manufacturer specification") is accurate and required, not a hedge.
