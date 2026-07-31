# Trusscore HTML Dashboard Spec (Section 14c)

> On-demand reference for the `trusscore-brand-guidelines` skill. **Load when building or reviewing any HTML dashboard or report page.** Content relocated verbatim from SKILL.md Section 14c.

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

## Pre-publication checklist — HTML dashboards

- [ ] `:root` CSS variables overridden from the generic build-dashboard defaults — not left as `#1a1a2e` header or Seaborn-style chart colors
- [ ] KPI/summary cards at the top are TC Slate fill with white text — not white cards, not left as the generic skill's shadow-based white default
- [ ] No box-shadow anywhere on cards or containers
- [ ] Border radius is 4px, not the generic skill's 8px default
- [ ] Chart series pull from the 5-color Trusscore sequence (Slate, Blue, Green, Yellow, Grey) in order — no off-palette 6th color added
- [ ] No colored top-border accent stripe on any card, slate or white
- [ ] Mulish set as the font stack, not left as system-fonts-only
- [ ] Red/green used only for positive/negative deltas — not as decorative chart colors elsewhere
- [ ] Header logo is the actual embedded logo image file — never styled text rendering "trusscore"
