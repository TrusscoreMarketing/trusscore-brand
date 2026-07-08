---
name: trusscore-brand-guidelines
description: "Applies the official Trusscore brand colors, typography, voice, and editorial standards to any artifact, document, design, or copy. Use for ALL Trusscore work whenever brand colors, style guidelines, visual formatting, or Trusscore editorial standards apply. This is the authoritative Trusscore brand skill—always use this, not the generic brand-guidelines skill."
---

# Trusscore Brand Guidelines

## Overview

This skill encodes the official Trusscore brand identity from the Trusscore Style Guide (effective April 21, 2026) and the Trusscore Brand Guidelines PDF. Apply it to all artifacts, designs, documents, presentations, and copy produced for Trusscore.

**Keywords**: Trusscore, branding, brand voice, brand colors, typography, visual identity, corporate identity, editorial standards, style guide, marketing, copy, design

---

## 0. Precedence Over Format Skills — Read This First

### Review gate — run de-slop before delivering
Before delivering any finished Trusscore deliverable — a deck, document, email, social post, landing page, dashboard, or any designed asset — run the `de-slop` skill on it and apply the fixes it flags, then deliver. This is the standing quality gate for **all** Trusscore output, not just decks. de-slop detects and suggests; you own the fixes. Skip it only when the user explicitly says to skip, or for trivial conversational replies that are not a deliverable. (Format-specific skills such as `trusscore-pptx` already call de-slop as their final step; this rule extends the same gate to every other deliverable type.)

When producing a docx, pptx, or any other format-specific artifact for Trusscore, the format skill (docx/pptx/xlsx/pdf SKILL.md) governs **mechanics only** — file structure, XML validity, page sizing, table widths, QA rendering process. It does NOT govern brand decisions. Where a format skill states a default or a "never do X" for font, color, or layout that conflicts with this skill, **this skill wins, every time, with no exception.**

Two confirmed conflicts to actively override:

| Format skill says | This skill requires instead |
|---|---|
| docx SKILL.md defaults to Arial font, black titles | Use Aptos (Office documents). Titles use TC Slate `#3A4B5C`, not black. Apply explicitly in every `styles.default` and `Heading` override — do not rely on the docx skill's built-in default block. |
| pptx SKILL.md says "never default to Aptos" (cites missing metric-compatible substitute, risk on older Office installs) | Aptos is the correct Trusscore Office font and must be used for Trusscore pptx body and headings. The pptx skill's QA-rendering caveat is a real risk — LibreOffice-based QA preview may substitute a different-width font, so check rendered text bounds with extra slack (~10%) and don't trust tight-fit QA on Aptos text — but the font choice itself does not change. Do not substitute Calibri or Arial as the working font; Calibri is the documented fallback only for cross-version compatibility issues the user has explicitly flagged, not a default substitution Claude makes unprompted. |
| pptx SKILL.md's go-to "visual motif" suggestion is icons inside colored circles, repeated across every slide | Never use circle containers around icons in any Trusscore digital artifact (pptx included) — see Section 4. Circles are approved only for print merchandising. Default treatment is the bare Lucide icon: Slate stroke, no container, standard sizing per Section 4. |

### pptx color-pop rule (avoiding flat-deck fatigue without sliding back to generic)

Bare Slate icons are the default and must not be replaced with colored circles. But an all-Slate deck across 20+ slides can read as flat. One controlled yellow accent per slide is permitted — never more than one, and never stacked with another pop technique on the same slide. Pick based on what the slide is actually doing:

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
| docx/xlsx SKILL.md defaults to Arial (or "Arial, Times New Roman") "unless otherwise instructed" | This skill is the instruction. Aptos, every time, for Trusscore Office deliverables. |

**Standing rule:** before finalizing any Trusscore docx or pptx, re-check that the format skill's own stated defaults (font family, title color, background color, accent color) were explicitly overridden in code — not left to fall through. If this skill is silent on a specific mechanical point (e.g., table width units, XML schema order), defer to the format skill; mechanics are not brand decisions.

---

## 1. Brand Foundation

**Mission:** Trusscore is a material science company for sustainable building materials.

**Vision:** To create a market-leading, sustainable, branded, true painted-drywall-alternative.

**Campaign Line (Level 1 — residential consumer-facing):**
> Real Life Looks Good Here

Anchors homepage messaging, residential campaigns, and brand storytelling.
Supporting messages: *Built for the everyday moments. Life gets messy. Trusscore makes sure you're ready for it.*

**Campaign Lines (Commercial & Agricultural):**
> Built to Last
>
> Discover the Strength and Durability of Trusscore

Both lines are approved for commercial and agricultural messaging around durability, longevity, and cost of ownership. Never use the residential lines ("Real Life Looks Good Here," "Goodbye drywall, hello") in commercial, agricultural, or industrial contexts.

**Billboard/Hook Line (Level 2 — residential/renovation only):**
> Goodbye drywall, hello [Trusscore logo]

Rendered as one line where space allows. When broken to two lines, "Goodbye drywall, hello" sits on line one; the Trusscore logo sits on line two at the same width as the line above it. "Trusscore" is never set in type here—always the logo mark. Do NOT use in commercial, agricultural, or industrial contexts.

---

## 2. Colors

| Color Name     | HEX       | Usage |
|----------------|-----------|-------|
| TC Slate       | `#3A4B5C` | Primary brand color, headings, design elements |
| TC Text  | `#111A22` | Body text only — never use as a design element |
| TC Yellow      | `#FEB100` | Logo truss mark, graphics, accents — **NEVER for text on white** |
| TC Grey        | `#DFDBDA` | Backgrounds, neutral elements |
| White          | `#FFFFFF` | Reversed logo, light backgrounds |

**Critical accessibility rule:** TC Yellow (`#FEB100`) has a 1.9:1 contrast ratio on white — it fails WCAG and must never be used for body or headline text on white backgrounds unless a size threshold approved by the brand team has been met.

**TC Text (`#111A22`) is reserved for body copy and captions on light backgrounds only.** Do not use it as a heading colour, shape fill, background, or design element. It is never used on TC Yellow backgrounds — use TC Slate `#3A4B5C` instead.

**TC Grey (`#DFDBDA`) is approved for borders, card fills, dividers, and secondary body text only.** It is not approved as a section background fill due to its pinkish-warm undertone sitting outside the cool/warm tint families used for section backgrounds.

### Shape and Accent Color Cycling

For non-text shapes, graphic elements, dividers, icons, and decorative accents in generated artifacts, cycle through colors in this order to maintain visual interest while staying on-brand:

1. TC Slate `#3A4B5C`
2. TC Yellow `#FEB100`
3. TC Blue (see below)
4. TC Green (see below)

**Additional on-brand accent options that work with the palette:**

| Color | HEX | Notes |
|---|---|---|
| TC Blue | `#009BD6` | Cool mid-blue; pairs with TC Slate without competing |
| TC Green | `#6BA543` | Muted green; grounded, works in agricultural/commercial contexts |
| TC Light Slate | `#6B7F8E` | Lighter tint of TC Slate; good for secondary elements |
| TC Yellow Tint | `#FFF0C2` | Very light yellow for subtle background fills |

### Smart Text Color on Backgrounds

Apply text color based on background to ensure legibility:

| Background | Use Text Color |
|---|---|
| White / TC Grey / TC Yellow Tint / any light background | TC Text `#111A22` |
| TC Slate / TC Blue / TC Green / any dark background | White `#FFFFFF` |
| TC Yellow `#FEB100` | TC Text `#111A22` (TC Yellow on white fails WCAG; when yellow IS the background, dark text is required) |

**Never place TC Yellow text on a white background.** If yellow text is required, it must be on a dark background (TC Slate or equivalent) where contrast is sufficient.


### 60-30-10 Colour Rule

All Trusscore layouts — digital, print, and generated artifacts — follow the 60-30-10 ratio. This is the governing principle for every colour decision in the system.

| Role | Ratio | Colours |
|---|---|---|
| Dominant | 60% | White, TC Grey `#DFDBDA`, light neutrals — backgrounds, page fills, whitespace |
| Secondary | 30% | TC Slate `#3A4B5C` — headers, dark sections, structural elements |
| Accent | 10% | TC Yellow `#FEB100` — CTAs, icons, highlights, decorative accents |

**Why this matters for TC Yellow specifically:** TC Yellow is a high-chroma colour that fatigues the eye at large scale. Its energy and impact come entirely from restraint. When yellow covers more than ~10% of visible surface area, it stops being an accent and becomes noise — and every other yellow element on the page loses its punch.

**Practical rules derived from 60-30-10:**

- Never use TC Yellow as a fill on more than one element type in the same visual section (e.g., not background + icons, not background + button, not icons + heading simultaneously)
- Large yellow backgrounds (full-width banners, hero sections, footer strips) count as the full yellow allocation for that layout — no yellow buttons, icons, or accent text in the same or immediately adjacent section
- A minimum of one neutral (white or TC Grey) buffer section is required between any two yellow-heavy elements in a multi-section layout
- Yellow accent uses (CTA button, icon stroke, section heading, decorative rule) may coexist only when yellow covers less than ~10% of visible surface area in total
- When in doubt: remove a yellow element, not add one

---

## 3. Spacing & Layout

### Base Spacing Unit
All padding, margins, and gaps between elements use an **8pt grid**. All spacing values should be multiples of 8 (8px, 16px, 24px, 32px, 48px, 64px). Use 4px only for tight internal component spacing (e.g., icon-to-label gap).

### Border Radius
Use **4px** across all UI elements — cards, buttons, tags, callout boxes, image frames, and form inputs.

**Rationale:** 4px respects the geometric sharpness of the Trusscore logo mark (the truss mark uses hard angles) while keeping elements modern rather than cold. 0px reads as too industrial/utilitarian; 8px starts to feel like a consumer app; 16px is too soft for the brand's confident, direct character.

| Element type | Border radius |
|---|---|
| Buttons | 4px |
| Cards | 4px |
| Tags / badges | 4px |
| Form inputs | 4px |
| Image frames | 4px |
| Pills (exception) | 999px — only when intentionally pill-shaped |

---

## 3b. Dividers, Lines & Section Treatments

### Governing principle
Text legibility and section hierarchy should be achieved through typography, whitespace, and colour — not through decorative lines or borders. Lines and accents are used sparingly and only when they carry meaning.

---

### Ruled lines

| Use | Weight | Colour | Style |
|---|---|---|---|
| Section dividers (horizontal rule) | 1px | TC Grey `#DFDBDA` | Solid |
| Card / panel borders | 0.5px | TC Grey `#DFDBDA` | Solid |
| Table row dividers | 1px | TC Grey `#DFDBDA` | Solid |
| Table header underline | 2px | TC Slate `#3A4B5C` | Solid |

TC Yellow is never used as a full-width horizontal rule. It cuts content off from the heading above it and creates the wrong visual grouping — binding the heading to the content below rather than introducing it. This is a known issue with the current website's blog header style and is not to be replicated.

---

### Heading treatments — by context

**Editorial content (blog posts, resource pages, long-form):**
Use pure typographic hierarchy — size, weight, and whitespace only. No decorative accent under or above headings. H2 at `clamp(20px, 3vw, 28px)` Bold with 32px of space above it is sufficient. The type does the work.

**Marketing content (homepage sections, campaign pages, product pages):**
Use a TC Yellow eyebrow label above H1 or H2 to introduce and contextualise the section. The eyebrow sits above the heading, never below it. All caps, `letter-spacing: 0.1em`, `clamp(11px, 1.2vw, 12px)`. This moves yellow to an introductory position rather than a separating one.

**Dark background sections (TC Slate):**
Use pure typographic hierarchy and colour contrast — white or TC Yellow headings on the slate field. No left border, accent bar, or decorative rule on the heading block.

---

### Left border accents — never use

Do not use a coloured or grey left border (`border-left` accent bar) on any element — headings, pull quotes, callout blocks, list items, or cards — on any background, including TC Slate. There is no approved exception.

**Use instead:**
- Pull quotes: larger type, TC Slate, generous whitespace — no border
- Callout blocks: TC Yellow 20% (`#FFF0C2`) fill with TC Slate text, or a four-sided card border (`0.5px solid #DFDBDA`) — never a single accent edge
- Headings: pure typographic hierarchy per the rules above

**Rationale:** The coloured left border is a default Claude output pattern. It appears on every heading and callout and immediately reads as generic AI output rather than Trusscore. Removing it entirely — not rationing it — is what keeps the design distinct.

---

### Truss mark geometry — angled design elements

The Trusscore logo truss mark is a true parallelogram with the following measured properties:

| Property | Value |
|---|---|
| Angle from vertical | 38° |
| Angle from horizontal | 52° |
| Width-to-height ratio | 2.56:1 |
| Skew ratio | 0.77 (54px shift over 70px height) |
| CSS equivalent | `skewX(-38deg)` |

These proportions must be honoured in any decorative use of the truss mark shape. Stretching the height or width distorts the geometry and makes it unrecognisable as the brand mark.

**Approved uses of the truss mark angle:**

- **Angled section transitions:** The clip between two sections can follow the 38° angle rather than a horizontal cut. No line — the geometry itself is the divider. For designed pieces and web layouts.
- **Parallelogram accent above headings:** A short parallelogram shape (width-to-height 2.56:1, skew 0.77) placed above a heading as a brand signature. TC Yellow, small enough to stay within the 10% yellow rule.
- **Merchandising section markers:** Three parallelograms in descending opacity (TC Yellow at 90%, 60%, 35%) used as section markers. For designed print pieces only — not generated digital artifacts.

**Never:**
- Alter the width-to-height ratio of the truss mark shape
- Use the parallelogram as a full-width divider (this increases its height and destroys the proportions)
- Add a border or outline to the parallelogram shape

---

### Background colour sections

Background fills on sections are permitted but must earn their place through content volume. A short section with a background fill looks patchy and draws attention to how little content it contains.

**Minimum threshold:** A section requires at least 3–4 lines of body copy (approximately 60+ words) before a background colour is appropriate. Sections shorter than this use whitespace separation instead.

---

### Approved background colours and permitted on-element colours

Each background has a defined set of approved text, icon, button, and border colours. Only these combinations are permitted.

**TC Grey `#DFDBDA` — borders, card fills, and body text only**
TC Grey is an official brand colour but has a pinkish-warm undertone that sits outside the cool/warm tint families used for section backgrounds. It is not approved as a section background fill. Approved uses:
- Card and panel borders: `0.5px solid #DFDBDA`
- Table row dividers: `1px solid #DFDBDA`
- Horizontal section rules: `1px solid #DFDBDA`
- Bullet and list indent markers
- Body text on light backgrounds (TC Grey `#DFDBDA` is approved for secondary body text and captions where a softer tone is needed)

---

#### White `#FFFFFF` — default
| Element | Approved colour |
|---|---|
| Headings (H1, H2, H3) | TC Slate `#3A4B5C` |
| Body copy | TC Text `#111A22` |
| Captions | TC Text `#111A22` or TC Grey `#DFDBDA` |
| Eyebrow / label | TC Yellow `#FEB100` |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Yellow fill, TC Text text |
| Secondary CTA button | TC Slate outline |
| Borders / dividers | TC Grey `#DFDBDA` |
| **Never** | TC Yellow as text |

---

#### TC Slate 8% `#F3F5F7` and TC Grey 30% `#F8F7F7` — lightest tints
Same rules as white. Tint is too light to affect contrast meaningfully.

---

#### TC Slate 15% `#E8EBF0` and TC Grey 50% `#EEEDEC` — mid tints
| Element | Approved colour |
|---|---|
| Headings | TC Slate `#3A4B5C` |
| Body copy | TC Text `#111A22` |
| Eyebrow / label | TC Yellow `#FEB100` |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Yellow fill, TC Text text |
| Secondary CTA button | TC Slate outline |
| Borders / dividers | TC Slate `#3A4B5C` — TC Grey has insufficient contrast at this tint level |
| **Never** | TC Yellow as text — TC Grey borders |

---

#### TC Yellow 8% `#FFF8E8` — lightest yellow tint
| Element | Approved colour |
|---|---|
| Headings | TC Slate `#3A4B5C` |
| Body copy | TC Text `#111A22` |
| Eyebrow / label | TC Yellow `#FEB100` — small size only, not as a button |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Slate fill, white text |
| Secondary CTA button | TC Slate outline |
| Borders / dividers | TC Grey `#DFDBDA` |
| **Never** | TC Yellow CTA button — yellow on yellow tint loses contrast |

---

#### TC Yellow 20% `#FFF0C2` — callout weight
Reserved for callout boxes and highlighted stats only — not full section backgrounds.

| Element | Approved colour |
|---|---|
| Headings | TC Slate `#3A4B5C` |
| Body copy | TC Text `#111A22` |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Slate fill, white text |
| **Never** | TC Yellow text, TC Yellow button, TC Yellow eyebrow — all invisible against this background · TC Grey borders — insufficient contrast |

---

#### TC Yellow `#FEB100` — full brand accent
Maximum once per layout. Counts as full 10% yellow allocation. Neutral buffer section required before and after.

| Element | Approved colour |
|---|---|
| Headings — display size (36px+, Bold 700+, max 6 words) | White `#FFFFFF` — permitted at this size and weight only |
| Headings — all other sizes | TC Slate `#3A4B5C` |
| Body copy | TC Slate `#3A4B5C` — never TC Text, never white below 36px |
| Eyebrow / label | TC Slate `#3A4B5C` |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Slate fill, white text |
| Secondary CTA button | White outline (2px border) — paired with TC Slate primary only, never standalone |
| **Never** | TC Yellow text or elements — invisible · TC Text — use TC Slate instead · White body copy — fails contrast · TC Grey — lost against yellow |

**White on TC Yellow rule:** White text on TC Yellow is permitted only when all three conditions are met simultaneously: (1) minimum 36px display size, (2) Bold or ExtraBold weight (700+), (3) maximum 6 words — never a full sentence or body copy. Below this threshold, TC Slate `#3A4B5C` is the only approved text colour.

---

#### TC Slate `#3A4B5C` — strongest anchor
| Element | Approved colour |
|---|---|
| Headings | White `#FFFFFF` |
| Body copy | White `rgba(255,255,255,0.85)` |
| Captions | White `rgba(255,255,255,0.65)` |
| Eyebrow / label | TC Yellow `#FEB100` |
| Icons | TC Yellow `#FEB100` |
| Primary CTA button | TC Yellow fill, TC Text text |
| Secondary CTA button | White outline |
| **Never** | TC Text — invisible · TC Grey — insufficient contrast · TC Yellow as body text — permitted for eyebrow/label only |

---

### Alternating rhythm rule
When multiple sections use background fills in sequence, follow a light-to-dark or varied rhythm. Never place two high-weight backgrounds (TC Yellow, TC Slate) adjacent to each other — always separate with a light tint or white section.

Suggested sequence for multi-section layouts:
White → Slate 8% or Grey 30% → Slate 15% or Grey 50% → TC Slate → white

TC Yellow sections stand alone — never adjacent to TC Slate or another yellow-tinted section.

---

## 4. Icon Style

### Style
**Outline only.** Never filled. Consistent 1.5px stroke weight throughout.

### Library
**Lucide** — outline-only, consistent stroke weight, good coverage for construction, home, and commercial use cases. Default for all generated artifacts.

### Color
| Context | Icon color |
|---|---|
| Light background (white, TC Grey) | TC Slate `#3A4B5C` |
| Dark background (TC Slate) | TC Yellow `#FEB100` |
| Emphasis / active state | TC Yellow `#FEB100` |

### Sizing
| Use | Size |
|---|---|
| Inline with text | 20px |
| Standard UI | 24px |
| Feature / hero callouts | 32px |

### Container rules — context dependent

**Digital and web artifacts (default):** Bare icon, no container. Let the icon stand on its own. The typography and color carry the hierarchy.

**Print merchandising (exception):** Circle container is permitted and preferred when icons overlay photography — the ring creates contrast and stops the eye in retail scanning environments (e.g., aisle banners, shelf invaders). Use TC Yellow `#FEB100` ring, white fill, TC Slate icon at 1.5px stroke. Never add a circle container in digital contexts.

**Rationale:** The circle container pattern is dated in digital design (prevalent 2018–2020) and competes with the geometric sharpness of the Trusscore logo mark. In print retail, it serves a functional purpose — anchoring a callout at an image boundary — that justifies its use.

### What to avoid
- Filled icons
- Mixed outline and filled icons in the same artifact
- Circle containers in digital, web, or document artifacts
- Icon libraries other than Lucide unless explicitly specified
- Decorative icons that don't carry clear meaning

---

## 5. Buttons & CTAs

### Button system

| Tier | Background | Text | Border | Use for |
|---|---|---|---|---|
| Primary | TC Yellow `#FEB100` | TC Text `#111A22` | None | Main CTA — one per section maximum |
| Primary (on yellow bg) | TC Slate `#3A4B5C` | White `#FFFFFF` | None | Primary CTA when section background is TC Yellow |
| Secondary (light bg) | Transparent | TC Slate `#3A4B5C` | `1px solid #3A4B5C` | Supporting actions on white or grey backgrounds |
| Secondary (dark bg) | Transparent | White `#FFFFFF` | `1px solid #FFFFFF` | Supporting actions on TC Slate backgrounds |
| Destructive | Transparent | `#C0392B` | `1px solid #C0392B` | Delete, remove, irreversible actions only |

All buttons use **4px border radius** and **Circular Std Bold / Aptos Bold** at 13–14px.

### Primary button colour logic

TC Yellow is the default primary button colour in all contexts **except** when the section background is TC Yellow — in that case, switch to TC Slate fill with white text. This is the only context where TC Slate fill replaces TC Yellow as the primary.

This rule exists because TC Yellow on a TC Yellow background is invisible. The switch is automatic and based solely on background colour — not on hierarchy or importance.

### CTA placement rules

- **One primary CTA per section maximum.** Two yellow buttons in the same section compete with each other and dilute both.
- Primary CTAs should be the only yellow element in their immediate visual zone — do not pair a yellow button with yellow icons or yellow headings in the same card or section.
- Secondary buttons should always accompany a primary button, never appear alone as the only action (if there's only one action, it's primary).

### TC Yellow usage limits (governed by 60-30-10)

See Section 2 (60-30-10 Colour Rule) for the full governing principle. Button-specific implications:

- A full-width TC Yellow hero or banner counts as the yellow allocation for that layout — use TC Slate primary buttons within it, and avoid yellow buttons in the immediately following section
- Yellow CTA buttons on white or slate backgrounds are the preferred way to introduce yellow as an accent — they cover minimal surface area and carry maximum action signal

### Interactive and motion accessibility

**Touch and click targets**
- **Trusscore standard: 44×44px** minimum for any interactive element — buttons, links, icons, form controls. This matches platform guidelines and is comfortable on touch.
- **Hard floor: 24×24px** (WCAG 2.2 AA, 2.5.8). Never smaller.
- **8px minimum spacing** between adjacent targets so they are not mis-tapped.

**Focus states**
Every interactive element must show a **visible keyboard-focus indicator** — never remove outlines without a replacement. Use the TC Yellow focus ring defined in Section 6: `0 0 0 3px rgba(254, 177, 0, 0.35)`. Prefer `:focus-visible` so the ring appears for keyboard users without cluttering mouse clicks.

**Reduced motion**
Respect `prefers-reduced-motion`. When a user has requested reduced motion, disable non-essential transitions, parallax, and auto-playing animation:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
```

---

## 6. Shadows & Elevation

**Rule: functional shadows only.** Decorative shadows on cards, panels, or sections are not permitted. Shadows are reserved exclusively for elements that are genuinely elevated above the page.

| Element | Shadow |
|---|---|
| Cards, panels, sections | None — border `0.5px solid #DFDBDA` only |
| Modals | `0 8px 32px rgba(58, 75, 92, 0.18)` |
| Dropdowns | `0 4px 16px rgba(58, 75, 92, 0.14)` |
| Tooltips | `0 2px 8px rgba(58, 75, 92, 0.12)` |
| Focus rings (inputs) | `0 0 0 3px rgba(254, 177, 0, 0.35)` — TC Yellow tint |

**Rationale:** The Trusscore website reads almost entirely flat, with color and photography carrying visual hierarchy. Decorative shadows on every card would fight the sharp, confident aesthetic. Reserving shadows for genuinely elevated UI elements keeps the system purposeful rather than decorative — consistent with the brand voice.

**Shadow color note:** All shadows use TC Slate (`#3A4B5C`) as the base color at low opacity, never black. This keeps shadows warm and on-brand rather than cold and generic.

## 7. Typography

### Typefaces by context

| Context | Typeface | Weights |
|---|---|---|
| Print / Premium | Circular Std | Bold, Book, Light |
| Microsoft Office | Aptos | Regular, Bold |
| Web / Digital | Muli Variable (Mulish) | 900, 700, 515, 440, 400 |

- **Primary design font:** Circular Std Book (preferred weight for body and descriptive copy)
- **Headings:** Circular Std Bold or Aptos Bold (Office)

### Font Fallback Chain

Use the first available font in this order:

1. Circular Variable
2. Muli Variable
3. Mulish
4. Aptos (default for Microsoft programs)

Arial and Georgia are not approved fallbacks for Trusscore.

---

### Type Scale — Semantic Roles with Fluid Sizing

Trusscore uses a **semantic role system** with fluid `clamp()` sizing rather than fixed pixel values or a rigid ratio scale. This ensures type scales gracefully between mobile and desktop without breakpoints, while maintaining clear hierarchy at every viewport width.

The approach is inspired by Apple's Dynamic Type system — named roles with intelligent scaling — adapted for web using CSS `clamp()`.

**Base size:** 15px (mobile) → 17px (desktop), scaling fluidly.

| Role | CSS clamp() value | Mobile floor | Desktop ceiling | Font | Weight |
|---|---|---|---|---|---|
| Display / Hero | `clamp(28px, 5vw, 48px)` | 28px | 48px | Circular Std / Muli Variable | Bold / 900 |
| H1 | `clamp(24px, 4vw, 36px)` | 24px | 36px | Circular Std / Muli Variable | Bold / 900 |
| H2 | `clamp(20px, 3vw, 28px)` | 20px | 28px | Circular Std / Muli Variable | Bold / 700 |
| H3 | `clamp(17px, 2.5vw, 22px)` | 17px | 22px | Circular Std Book / Muli Variable | Book / 600 |
| Body | `clamp(15px, 1.8vw, 17px)` | 15px | 17px | Circular Std Book / Muli Variable | Book / 400 |
| Eyebrow / Label | `clamp(11px, 1.2vw, 12px)` | 11px | 12px | Circular Std Bold / Muli Variable | Bold / 700 |
| Caption / Legal | `clamp(12px, 1.2vw, 13px)` | 12px | 13px | Muli Variable | 400 |

**Why clamp() rather than a fixed ratio:** A fixed ratio (e.g. 1.333) produces correct proportions but locks sizes — a 38px H1 on desktop may wrap aggressively on a 390px mobile viewport. `clamp()` sets a minimum floor that protects mobile legibility, a maximum ceiling for desktop, and fluid scaling between them. The proportional relationship between levels stays in the 1.25–1.333 range naturally.

### Hierarchy rules

Each level must be **visually distinct** from adjacent levels — not just a 2px nudge. The eye should be able to land on any level immediately without reading it. If H2 and H3 look similar, H3 needs to be smaller or lighter, not bigger.

- **Display:** Reserved for hero sections, campaign headlines, and full-bleed layouts only. Never used for in-page section headings.
- **H1:** One per page. The primary topic of the page or section.
- **H2:** Primary section anchors. Used for major content divisions.
- **H3:** Subsection headings within an H2 section. Lighter weight than H2 — Book not Bold.
- **Body:** All running prose. Comfortable line height (1.7) for readability.
- **Eyebrow / Label:** All caps, tracked out (letter-spacing: 0.1em), TC Yellow `#FEB100`. Sits above H1 or H2 to introduce and contextualise. Never used as a standalone label without an accompanying heading.
- **Caption:** Supplementary information, product specs, legal disclaimers. Never used for content that is essential to understanding the page.

### Mobile-first minimum sizes

These are hard floors — never go below them regardless of layout constraints:

| Role | Absolute minimum |
|---|---|
| Any heading | 17px |
| Body | 15px |
| Caption | 12px |
| Eyebrow / Label | 11px |

If a layout requires text smaller than these floors, the layout needs to change — not the text.

### Circular Std Light

Circular Std Light is not approved for body copy or any text below 18px at screen resolution. The thin strokes lose legibility on lower-density screens and in adverse lighting conditions. Use Circular Std Book instead.

### Line height

| Role | Line height |
|---|---|
| Display / H1 / H2 | 1.2 |
| H3 | 1.4 |
| Body | 1.7 |
| Caption | 1.5 |

### Letter spacing

| Role | Letter spacing |
|---|---|
| Eyebrow / Label | 0.1em (tracked out — always) |
| Display | -0.02em (tight — large type needs less space) |
| H1 / H2 | -0.01em |
| H3 / Body / Caption | 0 (default) |

### Measure (line length)

Body copy reads best at **45–75 characters per line**, with ~66 the target. Constrain running prose with a `max-width` (roughly `65ch`) rather than letting it span the full container. Lines longer than 75 characters lose the reader on the return sweep; shorter than 45 fragments the rhythm.

### Units and font loading

- Set the root at `html { font-size: 100%; }` (16px browser default) and size all type in **`rem`** so it scales with user settings. Use `em` only for spacing that should track its own font size.
- Load Circular and Mulish with **`font-display: swap`** so text renders immediately in a fallback and swaps in the brand font when it arrives — text is never invisible during load.
- Approved CSS stack (never Arial or Georgia — see the Section 7 fallback chain):

```css
/* Headings and body — web/digital */
font-family: 'Circular Std', 'Mulish', system-ui, sans-serif;
/* Office/email fallback where Circular is unavailable */
font-family: 'Aptos', 'Mulish', system-ui, sans-serif;
```

### Text contrast (WCAG 2.2 AA)

All text must meet WCAG 2.2 Level AA against its background:

| Text | Minimum ratio |
|---|---|
| Regular text (under 24px, or under 18.66px bold) | 4.5:1 |
| Large text (24px+, or 18.66px+ bold) | 3:1 |
| UI components and meaningful graphics | 3:1 |

This is why TC Yellow `#FEB100` (1.9:1 on white) is never text on a light background — see Section 2. TC Text `#111A22` on white and white on TC Slate both pass comfortably.

---

## 8. Logo Rules

### Variants
- **Primary:** Wordmark with TC Yellow truss mark on white or light backgrounds
- **Reversed:** White wordmark with TC Yellow truss mark on dark/TC Slate backgrounds
- **One-colour:** All white or all slate for black-and-white print or midtone backgrounds where the yellow truss is compromised

### Marks used on their own

Two marks exist, and they follow opposite rules:

- **Truss mark** — the yellow parallelogram/truss shape. It may be used on its own as a graphic accent. See Section 3b for approved decorative uses and Section 14b for the solo truss mark on the PowerPoint cover. It is an accent, not a logo, and never carries brand identification by itself.
- **T-icon** — the combined monogram pairing the truss with the "T" letterform. It may stand alone in exactly one place: as a **favicon** (or the equivalent app or browser tile). In every other use it must appear with the full Trusscore logo visible, or with "trusscore.com" set nearby, so the company name reads. Trusscore is not recognised by the icon alone, so outside the favicon the T-icon never identifies the brand by itself.

**Favicons and app tiles:** the T-icon is the mark used here — this is its only standalone use. Everywhere else (avatars, watermarks, badges, headers, stamps), either pair the T-icon with the full logo or "trusscore.com," or use the full logo instead.

### Do Nots
- Never add elements to the logo
- Never adjust letter spacing in the wordmark
- Never change the case of the wordmark
- Never change wordmark color to anything other than TC Slate or white
- Never change the truss mark color to anything other than TC Yellow (or TC Blue/Green for approved special cases)
- Never use the T-icon (the truss-plus-T monogram) on its own except as a favicon — in every other use, pair it with the full logo or with "trusscore.com" nearby
- Never stretch or distort the logo in any way
- Never modify the tagline lock-up
- Never place the logo on busy patterns or backgrounds that compromise legibility

### Whitespace
Minimum clear space: 1× the height and 1.5× the width of the lowercase `t` in the wordmark on all sides.

### Tagline
- The tagline ("material + science") must only appear in the approved lock-up and must always be paired with the logo
- The tagline must NOT appear standalone
- Digital minimum tagline height: 10px cap height
- Print minimum tagline height: 8pt Circular Std
- When the logo is too small for legible tagline text, use the wordmark-only version

### Sub-brand and program logos

Trusscore runs several programs that have their own approved logo lockups: **Trusscore Trusted Installer**, **Trusscore Community Partners**, and **Trusscore University**.

The governing rule for all of them: **use the official, pre-created logo file for each program — never recreate, redraw, restyle, recolour, re-typeset, or generate a new version.** If the correct file is not available, use the parent Trusscore logo and request the official asset; do not approximate the sub-brand mark.

Shared rules for every sub-brand and program logo:

- Use only the supplied file (`brand/logos/programs/`). Do not alter its colour, proportions, lockup, or typography.
- Never build one yourself by adding program text to the Trusscore logo — the approved lockup is the only valid version.
- They inherit all parent brand rules: no possessive of "Trusscore," approved colours only, and correct clear space.
- Program-specific usage rules, when provided, are documented here.

---

## 9. Brand Voice

For spec sheets, installation guides, and warranty documentation, see Section 16 (Technical Documentation Standards).

**Voice character:** Friendly, plainspoken, helpful, confident, and smart — like a trusted contractor who's also a good communicator.

### Do Use
- Customer-first language
- Active voice and short sentences
- Problem/solution framing
- Benefits-first language
- "Life gets messy" (not "challenges occur")
- "Weekend warriors" — homeowner/residential audience ONLY; never in contractor, commercial, or agricultural copy
- "Magic marker masterpieces" (not "accidental marks")
- "Real life" (not "daily activities")

### Never Use
- "Synergy"
- "Guru" or "Expert"
- "Disruptor"
- "Game-changer"
- "Leverage" as a verb (use "use" instead)
- "Innovative solution"
- "Best-in-class" (prove it with specifics instead)
- "Plastic" — always use "material" or the specific product name

### Hedge Stacking
Applies to brand, marketing, and consumer-facing copy. Does not apply to technical documentation, spec sheets, installation instructions, or warranty language — see Section 16. Conditional phrasing like "performance may vary depending on installation conditions" is often accurate and required there, not a hedge.

In brand and marketing copy, do not stack more than one qualifier per claim. "Can help reduce," "may vary in some cases," and "in many situations" compound into vague, AI-flattened copy that commits to nothing.

**Fix:** Pick one. State the claim directly, or qualify it once with a specific condition.

- Not: "This can help improve moisture resistance in many cases."
- Use: "It's moisture-resistant."

- Not (in marketing copy): "Performance may vary depending on installation conditions."
- Use: "Installed correctly, it won't need to be replaced."

If the claim genuinely needs a caveat in marketing copy, make the caveat specific (a number, a condition, a timeframe) rather than a general softener.

---

## 10. Audience-Specific Tone

| Audience | Tone | Focus | Avoid |
|---|---|---|---|
| Homeowners | Warm, relatable, empowering | Real moments, family life, DIY accessibility, finished look | Technical specs, contractor jargon, product-first language |
| Contractors | Peer-to-peer, professional, results-oriented | Install speed, reliability, reputation protection | Consumer lifestyle language, "weekend warrior," buzzwords |
| Commercial / Agricultural | Technical, direct, ROI-focused | Durability, moisture resistance, washdown, cost of ownership | Residential lifestyle language, drywall as comparison point |
| Architects / Specifiers | Design-forward, technically precise, collaborative | Material data, code compliance, finish quality, spec accuracy | Consumer tone, vague claims without data, abbreviated product names |

---

## 11. Capitalization Standards

All capitalization follows **Chicago Manual of Style, 18th Edition (2024)**.

### Title Case
Use for: H1 page headlines, H2 section headers, campaign headlines, product names, marketing materials.

**Capitalize:** First and last words always; nouns, pronouns, verbs, adjectives, adverbs; prepositions with 5+ letters (About, Against, Before, Between, Through, Under, Without); both parts of hyphenated compounds (Moisture-Resistant, Pre-Finished).

**Lowercase:** Articles (a, an, the); coordinating conjunctions (and, but, for, nor, or, so, yet); prepositions with 4 or fewer letters (at, by, for, in, of, on, to, up, with); infinitive "to".

### Sentence Case
Use for: Subtitles directly under headlines, body copy, blog headlines, email subject lines, social media posts, H3+ subheadings, product descriptions.

Capitalize only: first word, proper nouns (Trusscore, Toronto), product names (Wall&CeilingBoard, SlatWall), first word after a colon or em dash when introducing a new sentence.

**Key rule:** Subtitles under main headlines always use sentence case for a conversational feel.

---

## 12. Punctuation Rules

### Headlines and Titles
Single-sentence headlines and titles: **no periods.**
Multi-sentence headlines: use periods between sentences.

### Em Dashes
**No spaces.** Always `word—word`, never `word — word`.

Maximum two per content piece. Beyond that, the construction is doing too much work—replace with a colon after a bold label, a comma within the clause, or a full sentence break.

### En Dashes and Hyphens
No spaces. En dash for ranges (12–18 inches). Hyphen for compounds (moisture-resistant, DIY-friendly).

"DIY-friendly" is homeowner-only. Remove from any mixed homeowner/contractor or contractor-only context.

### Oxford Comma
Always use the Oxford (serial) comma in lists of three or more items.

### Bulleted Lists — No Terminal Period
Do not end a bullet point with a period. Bullets are fragments, not sentences — drop the terminal period, even when the bullet is a full clause.

When a bullet has a **bold label plus supporting copy**, the preferred structure is two levels: put the label on the **top-level bullet** (solid truss glyph) and the supporting copy on a **sub-bullet** (outline truss glyph) beneath it, with no period after the label. A single-level bold lead-in with a separator period ("**Brand guidelines.** The rulebook…") is also acceptable, but the two-level version is preferred for decks. Either way, the *end* of a bullet never takes a period.

Exceptions that keep normal terminal punctuation: a callout/takeaway box written as a full sentence, and body paragraphs (prose, not a list). If two or more bullets in a list are full sentences that genuinely need end punctuation, rewrite them as fragments instead of adding periods.

---

## 13. Brand Name Usage Rules

### No Possessive Form — Critical Rule
Trusscore is a brand name and must NEVER appear in possessive form.

| ✅ Correct | ❌ Incorrect |
|---|---|
| Trusscore panels | Trusscore's panels |
| Trusscore performance | Trusscore's performance |
| Trusscore delivers | Trusscore's delivery |

### Product Names
Always write product names in full on first reference with trademark symbols:
- Trusscore® Wall&CeilingBoard™
- Trusscore® SlatWall™
- Trusscore® Trims (no trademark symbol on Trims)
- NorLock™ by Trusscore®
- RibCore™ by Trusscore®
- DockDeck™ by Trusscore®

Acceptable short forms on subsequent references (same page, 6+ appearances): Wall&CeilingBoard, SlatWall.

**Never acceptable in any context:** WCB, W&C, SW, TC panels, TC boards, Trusscore boards, plastic panels, PVC panels.

---

## 14. Visual Content Standards

### Photography
- Show real spaces, real people, real life in progress
- Avoid overly styled interior design photography
- Avoid dramatic lighting effects or colour grading that misrepresents the product finish
- People should look like users, not models
- Never use stock photography that reads as staged or aspirational — Trusscore photography is functional and real

### Image Orientation
| Context | Ratio | Notes |
|---|---|---|
| Hero / full-width banner | 16:9 or 21:9 | Homepage hero, aisle banner, video frame |
| Feature cards | 3:2 | Space tiles, product feature sections |
| Portrait / social | 4:5 | Instagram posts, stories |
| Square | 1:1 | Profile, thumbnail, avatar, product shots |
| YouTube thumbnail | 16:9 | See thumbnail rules below |

---

### Image and Text Treatment Rules

The governing principle: **text legibility must be achieved through layout and typography, not through image manipulation.** Overlays are a last resort, not a default.

#### Tier 1 — No overlay (preferred)
Use when photography has sufficient contrast for text to read cleanly on its own. If the words are legible without an overlay, do not add one. Always check this first.

#### Tier 2 — Full-frame subtle overlay (video frames, full-bleed heroes)
Use when a large headline sits over a full-bleed image and the photo's tonal range makes legibility inconsistent.

- Overlay colour: TC Slate `rgba(58, 75, 92, 0.20)` — never black
- Maximum opacity: 25% — if legibility requires more than 25%, use Tier 3 instead
- Apply uniformly across the full frame — no gradient, no fade, no directional darkening
- The photo must remain the dominant visual — the overlay is a whisper, not a statement
- Headline text must be large enough to be legible without relying on the overlay

#### Tier 3 — Flat transparent panel (split layouts, thumbnails, blog headers)
Use when text occupies a defined zone within the image rather than floating over the full frame.

- Panel colour: TC Slate `rgba(58, 75, 92, 0.80)` — 80% minimum opacity
- Panel must cover a defined zone only — never full bleed
- No gradient at the panel edge — flat opacity, hard or soft edge, no fade
- The photo must remain fully visible and meaningful in the uncovered zone
- Do not add a border, line, or accent bar at the panel edge — this visually echoes panel seams and is off-brand

#### Never permitted
- Gradient overlays of any kind — they bury the photo and date the design
- Semi-transparent overlays above 25% opacity on full-frame images (use Tier 3 instead)
- Colour grading, tinting, or hue-shifting photography
- Overlays in TC Yellow — reserved for graphic elements only, never image treatment

---

### Text on Image — Size and Content Rules

These rules apply to all contexts where text sits over or beside photography. **Mobile is the primary audience** — all sizing decisions must pass the mobile legibility test first.

#### Video frames and full-bleed heroes
| Element | Rule |
|---|---|
| Headline | Maximum 2 lines. Minimum 48pt equivalent (desktop), 32pt equivalent (mobile) |
| Subheading / category label | Optional. Maximum 1 line. All caps, tracked out, small — 11–13pt equivalent |
| Body copy | Not permitted on video frames. On mobile it will be unreadable — use a separate text section below the image instead |
| CTA button | Permitted. One maximum. Position in lower third |

#### Feature cards and thumbnails
| Element | Rule |
|---|---|
| Headline | Maximum 1 line preferred, 2 lines absolute maximum |
| Body copy | Maximum 2 lines at 12–13px. If it runs longer, the card needs a different format |
| Tags / labels | One per card maximum |

#### Mobile-first legibility test
Before finalising any image with text overlay, apply this check:
- Reduce the layout to 390px wide (iPhone standard viewport)
- Can the headline be read in under 2 seconds without zooming?
- Is there sufficient contrast between text and the image/overlay beneath it?
- Is there at least 16px of padding between text and the image edge?

If any check fails — increase text size, reduce copy, or switch to a lower-tier overlay treatment.

---

### Social Graphics
- One idea per graphic — if it needs two sentences to explain, it needs a different format
- All social graphics must pass the mobile legibility test above
- Instagram: 4:5 portrait, headline only, maximum 6 words
- Stories / Reels cover: 9:16, headline only, large type, high contrast

### Image production specs — dimensions and file weight

Aspect ratios are set above (Image Orientation). These are the **resolution and file-size budgets** to hit at export. Ship the smallest file that still looks sharp.

**Web**

| Use | Dimensions | Target size |
|---|---|---|
| Header / hero | 1920×1080px | under 500KB |
| Content image | 800–1200px wide | under 150KB |
| Product image | 800×800px | under 100KB |
| Thumbnail | 300×300px | under 30KB |

**Email**

| Use | Dimensions | Target size |
|---|---|---|
| Header | 600×300px | under 200KB |
| Product | 400×300px | under 150KB |
| Thumbnail | 150×150px | under 50KB |
| Logo | 300×150px max | under 25KB |

- **Per-image email cap: 200KB.** Keep total HTML under ~100KB so Gmail does not clip the message.
- **Retina:** provide 2x assets and serve with `srcset` / `sizes` so high-DPI screens stay crisp without over-serving small screens.

### File formats

| Format | Use for |
|---|---|
| WebP | Default for web photos and graphics — roughly 30–60% smaller than JPEG; provide a JPEG/PNG fallback |
| JPEG | Photographs where WebP is not supported |
| PNG | Graphics needing transparency, or flat graphics with hard edges |
| SVG | Logos, icons, and line art — scalable, tiny, the required format for the Trusscore logo (Section 8) |

### Image alt text

Every content image carries descriptive **`alt` text** stating what the image shows and why it matters (e.g., "Finished garage with white Trusscore Wall&CeilingBoard on walls and ceiling"). Decorative-only images use empty `alt=""` so screen readers skip them. Never leave `alt` missing.

---

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

## 14c. HTML Dashboard Spec

The generic `build-dashboard` skill ships with placeholder tokens meant to be replaced per-brand — `--bg-header`, `--color-1` through `--color-6`, system-font stack, card shadows. Left unreplaced, these resolve to a dark navy header (`#1a1a2e`), a Seaborn-style chart palette, and drop shadows on every card — none of which is Trusscore. This section is verified against two production Trusscore dashboards (LinkedIn Performance Dashboard, SWAG Orders internal report, June 2026) rather than written from the generic skill alone.

**One correction already made once in this exact area, worth restating directly: do not put a colored top-border stripe on KPI cards.** Both production dashboards used a TC Yellow line across the top of every summary card when first built. This was identified as a generic-AI-dashboard tell — the same problem as the pptx stat-card top-border and the icon-in-colored-circle motif — and removed. If asked to replicate either dashboard's look, replicate everything except this one element.

**Override this CSS variable block at the top of every Trusscore dashboard**, replacing the generic `:root` block from the build-dashboard skill's Color System section:

```css
:root {
    /* Background layers */
    --bg-primary: #F8F7F7;
    --bg-card: #3A4B5C;
    --bg-card-light: #FFFFFF;
    --bg-header: #3A4B5C;

    /* Text */
    --text-primary: #111A22;
    --text-secondary: #5A6B78;
    --text-on-dark: #FFFFFF;
    --text-on-dark-muted: rgba(255, 255, 255, 0.65);

    /* Accent colors for data series — use in this order, do not introduce off-palette colors when more series are needed; collapse categories instead */
    --color-1: #3A4B5C;
    --color-2: #009BD6;
    --color-3: #6BA543;
    --color-4: #FEB100;
    --color-5: #DFDBDA;

    /* Status colors — functional only, same convention as pptx trend indicators (Section 14b) and xlsx financial models. Not decorative; do not use red/green as general accents elsewhere on the dashboard. */
    --positive: #6BA543;
    --negative: #DC3545;
    --neutral: #5A6B78;

    /* Spacing */
    --gap: 16px;
    --radius: 4px;
}

body {
    font-family: 'Mulish', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
```

**Specific overrides to the generic skill's defaults:**

| Generic skill default | Trusscore override | Why |
|---|---|---|
| `--bg-header: #1a1a2e` (dark navy) | `#3A4B5C` (TC Slate) | The generic dark header is off-palette navy; TC Slate is the equivalent dark Trusscore already uses for cover slides and dark sections elsewhere |
| `border-radius: 8px` (`--radius` default) | `4px` | Matches the 4px radius standard already set in Section 3 for digital artifacts — 8px reads softer/more generic than the Trusscore standard |
| `box-shadow: 0 1px 3px rgba(0,0,0,0.08)` on `.kpi-card`, `.chart-container`, `.table-section` | Remove entirely — `box-shadow: none` | Direct violation of Section 6 (no shadows except genuinely elevated elements like modals/tooltips) |
| KPI cards: white fill (generic skill default) | **TC Slate fill** (`--bg-card`), white text | Confirmed from two production dashboards — slate-filled summary cards are the actual Trusscore standard, not white cards with colored accents. This is more distinctive than a white-card pattern and should not be reverted to white. |
| Colored top-border stripe on KPI cards | Removed entirely | Generic-dashboard tell — see correction note above |
| `--color-1` through `--color-6`: Seaborn-style default chart palette | TC Slate, TC Blue, TC Green, TC Yellow, TC Grey — 5 colors, not 6 | The generic palette has no relationship to the brand. If a chart genuinely needs more than 5 series, restructure the data into fewer categories. |
| System font stack only | Mulish first, system fonts as fallback | Matches Section 7 |

### Page header

- Background: TC Slate (`--bg-header`)
- **The actual reversed-white logo asset** (`assets/logos/trusscore-logo-white.svg`, bundled with this skill), embedded as an image — top-left, small, height roughly 14-18px at dashboard scale. This is a hard requirement, not a description: never render "trusscore" as styled text in any weight, case, or letter-spacing as a substitute for the logo file. Styled text fails Section 8 on multiple points at once (wordmark letterforms don't match, no truss mark present, case/spacing not controlled) and is not a visually acceptable stand-in even when it looks superficially close. Per Section 8's tagline rule, use the wordmark-only version (no tagline) at this small size — the tagline lock-up is for contexts where it can render at a legible minimum height.
- Page title in white, bold, below or beside the wordmark (e.g., "LinkedIn Performance Dashboard")
- One-line subtitle in `--text-on-dark-muted`, directly below the title (e.g., "Organic company-page analytics")
- Optional: a short TC Yellow underline rule beneath the subtitle — single use, header only, not repeated elsewhere on the page. This is a restrained accent, not the same failure mode as the per-card top border, because it appears exactly once per dashboard rather than once per repeated element.
- For internal/operational reports (vs. external-facing performance dashboards), a breadcrumb trail (e.g., "TRUSSCORE / SWAG & Giveaways / Sales & Marketing") may sit above the title in `--text-on-dark-muted`, small caps

### KPI / summary cards

- Fill: TC Slate (`--bg-card`)
- Text: label in `--text-on-dark-muted` or a light grey, small caps or letter-spaced; value large and bold in white; supporting line small, muted
- No border, no shadow, no top accent stripe
- Corner radius: 4px
- Grid layout, evenly spaced, 3-5 cards per row depending on dashboard width
- Positive/negative deltas use `--positive`/`--negative` — this is the one functional color exception, same convention as elsewhere

### Section labels

Divide the dashboard into labeled zones instead of color-coding individual elements — this is the same principle as the pptx card-category fix in Section 14b, now confirmed as the real pattern in production:
- Small caps, letter-spaced, muted grey (`--text-secondary`), e.g., "REACH AND ENGAGEMENT OVER TIME," "WHO IS FOLLOWING"
- Sits directly above the row of cards/charts it labels, with breathing room above and below
- Do this instead of giving each card or chart its own accent color

### Chart and table cards (secondary content, not KPI summaries)

- Fill: white (`--bg-card-light`)
- Border: none required if section labels already separate zones clearly; a 1px `#DFDBDA` border is acceptable if cards need to read as distinct from the page background
- No shadow
- Chart title inside the card, small, bold, dark text
- This is a deliberately different treatment from KPI cards (white, not slate) — the contrast between slate summary cards and white content cards is itself part of the visual hierarchy: slate cards are "the headline numbers," white cards are "the supporting detail." Don't flatten this distinction by making everything one fill color.

### Chart-specific notes

- Use the 5-color `--color-1` through `--color-5` sequence for any multi-series chart (line, bar, stacked bar), in order
- Doughnut/pie charts: same 5-color sequence; TC Yellow used sparingly, ideally not on the largest or most-emphasized slice
- Donut charts may use a center label/callout for the dominant category (confirmed pattern: "Reactions, 2,442" centered in the donut hole) — this is a clean, functional device, not decorative
- Bar charts comparing categories (e.g., audience breakdowns by job function, seniority, location): horizontal bars, single color per chart is acceptable when the chart is one category dimension, not a multi-series comparison

### Data tables

- No zebra striping
- Header row: small caps, muted grey, bottom border only (no full grid)
- Numbers right-aligned
- Functional color in cells is permitted for genuinely meaningful signals (e.g., a projected/forecast column in TC Blue to distinguish it from historical actuals) — this is the same category as the red/green trend convention, not decorative
- Keep tables dense and plain; this is where detail lives, it doesn't need its own visual flourish

### Filters bar

The generic skill's filter styling assumes a dark header background (white text at reduced opacity, translucent white borders). Since the header is TC Slate, that styling works without modification.

---

## 15. Quick Reference Checklist (Pre-Publication)

Before publishing or delivering any Trusscore asset:

**Editorial**
- [ ] No possessive form of Trusscore anywhere
- [ ] No spaces around em dashes
- [ ] Oxford comma present in all lists of 3+
- [ ] No periods at end of single-sentence headlines
- [ ] Title Case on H1/H2/headlines; Sentence case on subtitles and body
- [ ] No banned buzzwords (game-changer, leverage, plastic, etc.)
- [ ] Audience tone is appropriate for the target (no homeowner language in commercial copy)
- [ ] Product names use full form with trademark on first reference
- [ ] No abbreviated product names (WCB, SW, etc.)

**Colour**
- [ ] TC Yellow not used as text on any background
- [ ] TC Text used for body copy and captions on light backgrounds only — never headings, never on TC Yellow
- [ ] TC Text not used as a shape fill, background, or design element
- [ ] TC Grey used for borders, card fills, dividers, and secondary text only — never as a section background fill
- [ ] Headings use TC Slate on light backgrounds, white on TC Slate backgrounds
- [ ] TC Yellow usage is at or under 10% of visible surface area (60-30-10 rule)
- [ ] No two yellow-heavy elements in adjacent sections without a neutral buffer
- [ ] White text on TC Yellow only at 36px+, Bold 700+, maximum 6 words
- [ ] TC Yellow CTA button not used on any yellow or yellow-tinted background — use TC Slate fill instead
- [ ] On-element colours match the approved pairing for the section background (see Section 3b)

**Typography & Logo**
- [ ] Font is Circular Std (design), Aptos (Office), or Muli/Mulish (web)
- [ ] Tagline only appears paired with the logo in the approved lock-up
- [ ] Logo has minimum clear space on all sides

**Image & Overlay**
- [ ] No gradient overlays of any kind
- [ ] Full-frame overlays use TC Slate base colour, maximum 25% opacity
- [ ] Panel overlays use TC Slate at minimum 80% opacity, defined zone only
- [ ] No overlay in TC Yellow
- [ ] No panel edge lines or accent bars (echoes panel seam complaint)
- [ ] Photography not colour graded or tinted

**Mobile legibility (apply to all image + text layouts)**
- [ ] Headline readable at 390px viewport width without zooming
- [ ] No body copy on video frames or full-bleed mobile layouts
- [ ] Minimum 16px padding between text and image edge
- [ ] Sufficient contrast between text and image/overlay beneath it

**Accessibility**
- [ ] Text meets WCAG 2.2 AA contrast — 4.5:1 body, 3:1 large text and UI
- [ ] Interactive targets are 44×44px (never below the 24×24px floor), 8px apart
- [ ] Visible keyboard focus state on every interactive element
- [ ] `prefers-reduced-motion` respected
- [ ] Body copy constrained to a 45–75 character measure
- [ ] Every content image has descriptive alt text; decorative images use `alt=""`

**Image production**
- [ ] Image dimensions and file weights within the Section 14 budgets
- [ ] WebP used for web images with a JPEG/PNG fallback
- [ ] 2x retina assets served via `srcset`
- [ ] Email images under 200KB each; total HTML under ~100KB
- [ ] Fonts loaded with `font-display: swap`

**Layout & Artifacts**
- [ ] Spacing follows 8pt grid
- [ ] Border radius is 4px (never 0 or 8+ in digital artifacts)
- [ ] Icons are outline style, Lucide library, no circle containers in digital
- [ ] Shadows only on genuinely elevated elements (modals, dropdowns, tooltips)
- [ ] Primary CTA is TC Yellow — unless background is TC Yellow, then TC Slate fill
- [ ] One primary CTA per section maximum

**Dividers, Headings & Section Treatments**
- [ ] No TC Yellow full-width horizontal rule under headings
- [ ] Editorial headings use pure typographic hierarchy — no decorative accent
- [ ] Marketing headings use TC Yellow eyebrow label above heading, not below
- [ ] No left border accents anywhere — no coloured or grey border-left bar on headings, callouts, quotes, lists, or cards on any background
- [ ] Background colour sections contain minimum 60 words of body copy
- [ ] TC Yellow background section appears maximum once per layout with neutral buffer before and after
- [ ] Truss mark parallelogram used at 2.56:1 width-to-height ratio and 0.77 skew — never stretched
- [ ] Angled section transitions use 38° (CSS: skewX(-38deg)) — not approximated

**PowerPoint (Section 14b)**
- [ ] Aptos set explicitly on every text run — not left to inherit the theme's Calibri Light default
- [ ] Title color is hardcoded `#3A4B5C` — not pulled from the theme's `accent1`/`dk2` swatch (which contains a one-digit typo, `#3A4B5B`)
- [ ] Stat/data cards are white with a thin neutral border — no colored top-border accent stripe
- [ ] Card category distinction comes from a section header label, not per-card color-coding
- [ ] Red/green trend indicators used only for actual up/down deltas attached to a number — never as decorative or category color
- [ ] No icon-in-colored-circle treatment (see Section 4 and pptx color-pop rule)
- [ ] Footer logo lockup inherited from the slide master — not duplicated manually on individual slides

**HTML Dashboards (Section 14c)**
- [ ] `:root` CSS variables overridden from the generic build-dashboard defaults — not left as `#1a1a2e` header or Seaborn-style chart colors
- [ ] KPI/summary cards at the top are TC Slate fill with white text — not white cards, not left as the generic skill's shadow-based white default
- [ ] No box-shadow anywhere on cards or containers
- [ ] Border radius is 4px, not the generic skill's 8px default
- [ ] Chart series pull from the 5-color Trusscore sequence (Slate, Blue, Green, Yellow, Grey) in order — no off-palette 6th color added
- [ ] No colored top-border accent stripe on any card, slate or white
- [ ] Mulish set as the font stack, not left as system-fonts-only
- [ ] Red/green used only for positive/negative deltas — not as decorative chart colors elsewhere
- [ ] Header logo is the actual embedded logo image file — never styled text rendering "trusscore"

---

## 16. Technical Documentation Standards

Applies to spec sheets, installation guides, and warranty documentation. This section governs structure and voice for technical content; Section 9 (Brand Voice) governs brand, marketing, and consumer-facing copy.

### Structure: Jobs to Be Done
Organize around what the contractor needs to do, not the product feature being described. Headings name the task, not the spec category.

- Not: "Section 4: Saw Specifications"
- Use: "Cutting Panels for a Corner Install"

- Not: "Fastener Requirements"
- Use: "Fastening Panels to Metal Studs"

### Voice: Active and Action-Oriented
Lead with the verb. The contractor is doing something; the sentence should start there, not with the product or a passive construction.

- Not: "Panels should be cut using a fine-tooth blade."
- Use: "Cut panels with a fine-tooth blade."

- Not: "A 1/8-inch gap is recommended between panels."
- Use: "Leave a 1/8-inch gap between panels."

### Hedge Stacking — Exemption
Section 9's hedge-stacking rule does not apply here. Conditional phrasing tied to a real variable ("performance may vary depending on installation conditions," "torque to manufacturer specification") is accurate and required in technical documentation, not a hedge to be removed.