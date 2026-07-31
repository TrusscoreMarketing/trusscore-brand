# Trusscore Web, Layout & Imagery Standards (Sections 3, 3b, 4, 5, 6, 7-web, 14)

> On-demand reference for the `trusscore-brand-guidelines` skill. **Load when building anything web/HTML, a designed layout, an artifact with icons/buttons/imagery, or when choosing overlays, spacing, dividers, or photo treatments.** Content relocated verbatim from SKILL.md Sections 3, 3b, 4, 5, 6, the web half of 7, and 14.

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
Text legibility and section hierarchy should be achieved through typography, whitespace, and color — not through decorative lines or borders. Lines and accents are used sparingly and only when they carry meaning.

---

### Ruled lines

| Use | Weight | Color | Style |
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
Use pure typographic hierarchy and color contrast — white or TC Yellow headings on the slate field. No left border, accent bar, or decorative rule on the heading block.

---

### Left border accents — never use

Do not use a colored or grey left border (`border-left` accent bar) on any element — headings, pull quotes, callout blocks, list items, or cards — on any background, including TC Slate. There is no approved exception.

**Use instead:**
- Pull quotes: larger type, TC Slate, generous whitespace — no border
- Callout blocks: TC Yellow 20% (`#FFF0C2`) fill with TC Slate text, or a four-sided card border (`0.5px solid #DFDBDA`) — never a single accent edge
- Headings: pure typographic hierarchy per the rules above

**Rationale:** The colored left border is a default Claude output pattern. It appears on every heading and callout and immediately reads as generic AI output rather than Trusscore. Removing it entirely — not rationing it — is what keeps the design distinct.

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

### Background color sections

Background fills on sections are permitted but must earn their place through content volume. A short section with a background fill looks patchy and draws attention to how little content it contains.

**Minimum threshold:** A section requires at least 3–4 lines of body copy (approximately 60+ words) before a background color is appropriate. Sections shorter than this use whitespace separation instead.

---

### Approved background colors and permitted on-element colors

Each background has a defined set of approved text, icon, button, and border colors. Only these combinations are permitted.

**TC Grey `#DFDBDA` — borders, card fills, and body text only**
TC Grey is an official brand color but has a pinkish-warm undertone that sits outside the cool/warm tint families used for section backgrounds. It is not approved as a section background fill. Approved uses:
- Card and panel borders: `0.5px solid #DFDBDA`
- Table row dividers: `1px solid #DFDBDA`
- Horizontal section rules: `1px solid #DFDBDA`
- Bullet and list indent markers
- Body text on light backgrounds (TC Grey `#DFDBDA` is approved for secondary body text and captions where a softer tone is needed)

---

#### White `#FFFFFF` — default
| Element | Approved color |
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
| Element | Approved color |
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
| Element | Approved color |
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

| Element | Approved color |
|---|---|
| Headings | TC Slate `#3A4B5C` |
| Body copy | TC Text `#111A22` |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Slate fill, white text |
| **Never** | TC Yellow text, TC Yellow button, TC Yellow eyebrow — all invisible against this background · TC Grey borders — insufficient contrast |

---

#### TC Yellow `#FEB100` — full brand accent
Maximum once per layout. Counts as full 10% yellow allocation. Neutral buffer section required before and after.

| Element | Approved color |
|---|---|
| Headings — display size (36px+, Bold 700+, max 6 words) | White `#FFFFFF` — permitted at this size and weight only |
| Headings — all other sizes | TC Slate `#3A4B5C` |
| Body copy | TC Slate `#3A4B5C` — never TC Text, never white below 36px |
| Eyebrow / label | TC Slate `#3A4B5C` |
| Icons | TC Slate `#3A4B5C` |
| Primary CTA button | TC Slate fill, white text |
| Secondary CTA button | White outline (2px border) — paired with TC Slate primary only, never standalone |
| **Never** | TC Yellow text or elements — invisible · TC Text — use TC Slate instead · White body copy — fails contrast · TC Grey — lost against yellow |

**White on TC Yellow rule:** White text on TC Yellow is permitted only when all three conditions are met simultaneously: (1) minimum 36px display size, (2) Bold or ExtraBold weight (700+), (3) maximum 6 words — never a full sentence or body copy. Below this threshold, TC Slate `#3A4B5C` is the only approved text color.

---

#### TC Slate `#3A4B5C` — strongest anchor
| Element | Approved color |
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

### Primary button color logic

TC Yellow is the default primary button color in all contexts **except** when the section background is TC Yellow — in that case, switch to TC Slate fill with white text. This is the only context where TC Slate fill replaces TC Yellow as the primary.

This rule exists because TC Yellow on a TC Yellow background is invisible. The switch is automatic and based solely on background color — not on hierarchy or importance.

### CTA placement rules

- **One primary CTA per section maximum.** Two yellow buttons in the same section compete with each other and dilute both.
- Primary CTAs should be the only yellow element in their immediate visual zone — do not pair a yellow button with yellow icons or yellow headings in the same card or section.
- Secondary buttons should always accompany a primary button, never appear alone as the only action (if there's only one action, it's primary).

### TC Yellow usage limits (governed by 60-30-10)

See Section 2 (60-30-10 Color Rule) for the full governing principle. Button-specific implications:

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

---

## 7 (web). Typography — web type system

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

## 14. Visual Content Standards

### Photography
- Show real spaces, real people, real life in progress
- Avoid overly styled interior design photography
- Avoid dramatic lighting effects or color grading that misrepresents the product finish
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

- Overlay color: TC Slate `rgba(58, 75, 92, 0.20)` — never black
- Maximum opacity: 25% — if legibility requires more than 25%, use Tier 3 instead
- Apply uniformly across the full frame — no gradient, no fade, no directional darkening
- The photo must remain the dominant visual — the overlay is a whisper, not a statement
- Headline text must be large enough to be legible without relying on the overlay

#### Tier 3 — Flat transparent panel (split layouts, thumbnails, blog headers)
Use when text occupies a defined zone within the image rather than floating over the full frame.

- Panel color: TC Slate `rgba(58, 75, 92, 0.80)` — 80% minimum opacity
- Panel must cover a defined zone only — never full bleed
- No gradient at the panel edge — flat opacity, hard or soft edge, no fade
- The photo must remain fully visible and meaningful in the uncovered zone
- Do not add a border, line, or accent bar at the panel edge — this visually echoes panel seams and is off-brand

#### Never permitted
- Gradient overlays of any kind — they bury the photo and date the design
- Semi-transparent overlays above 25% opacity on full-frame images (use Tier 3 instead)
- Color grading, tinting, or hue-shifting photography
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

## Pre-publication checklist — web, layout & imagery

**Image & Overlay**
- [ ] No gradient overlays of any kind
- [ ] Full-frame overlays use TC Slate base color, maximum 25% opacity
- [ ] Panel overlays use TC Slate at minimum 80% opacity, defined zone only
- [ ] No overlay in TC Yellow
- [ ] No panel edge lines or accent bars (echoes panel seam complaint)
- [ ] Photography not color graded or tinted

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
- [ ] No left border accents anywhere — no colored or grey border-left bar on headings, callouts, quotes, lists, or cards on any background
- [ ] Background color sections contain minimum 60 words of body copy
- [ ] TC Yellow background section appears maximum once per layout with neutral buffer before and after
- [ ] Truss mark parallelogram used at 2.56:1 width-to-height ratio and 0.77 skew — never stretched
- [ ] Angled section transitions use 38° (CSS: skewX(-38deg)) — not approximated
