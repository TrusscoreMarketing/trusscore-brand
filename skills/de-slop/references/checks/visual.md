---
type: check
layer: 2-company
status: active
last-refreshed: 2026-07-07
source: distilled from the trusscore-brand-guidelines skill (Sections 2, 3, 3b, 4, 6, 7, 8, 14, 14b, 14c) and the extracted pptx example-deck rules. Update when the brand skill changes.
---

# Check: visual (Trusscore)

Does the visual match the Trusscore design system for its surface. **One system governs everything this check grades: web and landing pages, HTML dashboards, slides and decks, docs and PDFs, social graphics, and diagrams.** Flag what is off, name the governing rule, and suggest the concrete change. Detect and suggest only, never rewrite.

## 1. Design language

Trusscore reads flat, sharp, and confident. Color and real photography carry the hierarchy, not decoration. The feeling is a trusted contractor who is also a good communicator: plainspoken, precise, no filler. Banned at the conceptual level: decorative shadows, gradients of any kind, gradient overlays on photos, circle containers on icons in digital, glow, bevels, and any effect that softens the geometric sharpness of the truss mark. White space is a feature, not empty space. Dense, cramped, or "every element decorated" layouts are off-brand even when the palette is right.

## 2. Color palette

Flat fills only. No gradients. Colors come from the documented system below. An off-palette color is a finding.

| Color | Hex | Usage |
|---|---|---|
| TC Slate | `#3A4B5C` | Primary: headings, structure, deck covers, dark section backgrounds |
| TC Text | `#111A22` | Body copy and captions |
| Heading dark | `#222B33` | Slightly lighter dark, headings only (not body) |
| TC Yellow | `#FEB100` | Accent only. Never text on white, never a full-width divider, never paired with TC Blue in the same section |
| TC Blue | `#009BD6` | Accent |
| TC Green | `#6BA543` | Accent, and the growth signal in trend indicators |
| White | `#FFFFFF` | Default background, reversed logo |
| TC Grey | `#DFDBDA` | Border, neutral |
| Grey ramp (slate-tinted neutrals) | `#F5F6F7`, `#EEF1F3`, `#E8EAEC`, `#E1E5E8`, `#DDE3E8`, `#CFD6DC`, `#8A9BAC`, `#6A7A88` | Panel fills, hairline dividers (`#E8EAEC`), card borders (`#E1E5E8`), muted labels/supporting text (`#8A9BAC`, `#6A7A88`) |
| Functional red | `#DC3545` | Decline signal in trend/delta indicators ONLY. Never a general accent |

**60-30-10 balance:** roughly 60% white/light, 30% TC Slate, at most 10% TC Yellow. Yellow over its ceiling, yellow as body text on white, or yellow beside blue in the same section is a finding.

**Hard rule: never a black or dark default background on web, dashboards, docs, or social.** The only dark surfaces are intentional TC Slate deck covers, section dividers, and defined slate zones. `#000000` as a background is a finding. Shadows and overlays use TC Slate at low opacity, never black.

**Functional-color exception:** red/green in trend indicators and dashboard status is a data signal, exempt from the yellow ceiling and accent bans. `#DC3545` (decline) and `#6BA543` (growth) are the only reds/greens used this way, and `#DC3545` appears nowhere else.

## 3. Typography

| Usage | Font |
|---|---|
| Web / digital (dashboards, HTML, artifacts) | DM Sans |
| Print | Circular Std |
| Office / PowerPoint | Aptos (set explicitly; the silent theme default Calibri Light is a finding) |
| Data, labels, captions | Same family, muted grey from the ramp |

Casing: H1, H2, and campaign headlines in Title Case (Chicago 18th ed.). Subtitles, body, H3+, social posts, and email subject lines in sentence case. Single-sentence headlines take no period. No more than a small number of weights per layout. Body text never below comfortable reading size for the surface. An off-system font (Arial, Calibri, Times as a design choice) is a finding.

## 4. Structural tokens

- **Shadows:** functional only. Cards, panels, and sections get NONE (border `0.5px solid #DFDBDA` instead). Shadows are allowed only on genuinely elevated UI (modals, dropdowns, tooltips, focus rings) and always use TC Slate at low opacity, never black. A decorative card/panel shadow is a finding.
- **Borders:** hairline. Card borders `0.75pt / #E1E5E8` (decks) or `0.5px #DFDBDA` (web). No heavy rules.
- **No left-side (or any-side) color-line accent** on headings, boxes, cards, quotes, or callouts. No card top-stripe. No single-side colored border on any shape. Set a box apart with a subtle background tint or a label above it. Any edge accent stripe is a finding.
- **Corner radius:** 4px on all web/UI elements (cards, buttons, tags, inputs, image frames). PowerPoint stat cards use 6% (`adj val 6000`). Never 0px (too industrial), never above the spec (too soft). Pills (999px) only when intentionally pill-shaped.
- **Icons:** Lucide outline only, 1.5px stroke, never filled, never mixed outline+filled. No circle containers in digital/web/doc/deck contexts (the print-retail circle exception does not apply to anything this check normally grades). Icon color: TC Slate on light, TC Yellow on slate or for emphasis.
- **Spacing:** generous white space, one idea per block. Cramped layouts are off-brand.

## 5. Per-surface application

| Surface | What on-brand looks like |
|---|---|
| Web & landing pages | White/light dominant, flat, sharp. Reversed-white logo asset (not styled text) top-left. Real photography carries hierarchy. 4px radius, hairline borders, no decorative shadows. |
| HTML dashboards (14c) | Divide into labeled zones rather than color-coding individual elements. KPI cards white with hairline border, no per-card accent stripe. Status colors functional only (same red/green convention as decks). Reversed-white logo asset top-left, ~14–18px. Never render "trusscore" as styled text in place of the logo file. |
| Slides & decks (14b) | Slate covers, white content slides, Aptos throughout. Footer logo lockup inherited from the master, never duplicated on a slide. Stat cards: white, `#E1E5E8` 0.75pt border, 6% radius, no shadow, no top-stripe. One TC Yellow keyword max per cover title. One callout (light-yellow `#FFF8EC` / yellow border) per slide max. Trend red/green only as data signals. Build new slides from the template's named layouts. |
| Docs & PDFs | White background, TC Slate headings, TC Text body, restrained. Same border/shadow/radius rules. |
| Social graphics | Real installs/spaces only. Text legibility from layout first (Tier 1 no overlay). If needed, TC Slate overlay at ≤25% (Tier 2) or a defined slate panel at ≥80% (Tier 3), never full-bleed, never gradient, never a yellow overlay, never black. |
| Diagrams | Lucide outline elements, slate/grey structure, yellow accent used sparingly and never as the only carrier of meaning. |

**Photography rule (all surfaces):** real spaces and real installs only. No stock that reads staged/aspirational, no AI-generated imagery presented as real, no color grading/tinting/hue-shift that misrepresents the finish. AI cleanup of a real photo is allowed; before/after AI images must be paired and labeled as before/after, never standalone. The product stays the hero.

## Grading

- **Aligned:** palette, fonts, and tokens all match the surface; one clear focal point; generous spacing; 60-30-10 held; real photography.
- **Drift:** a near-off hex (e.g. an undocumented grey close to the ramp), weak hierarchy, a slightly wrong border weight, cramped spacing, a missing accent, yellow slightly over budget.
- **Misaligned (any of these):** off-palette color; black/dark default background; non-brand or silent-default font; icon circle in digital; filled icons; any left/any-side accent border or card top-stripe; decorative shadow or gradient; gradient overlay or >25% or yellow or black overlay on a photo; all-caps kicker above/below a heading; yellow as body text on white or paired with blue in one section; stock or AI-as-real photography; the possessive or styled-text logo standing in for the logo asset.
