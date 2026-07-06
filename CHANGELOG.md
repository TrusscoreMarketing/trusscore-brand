# Changelog

All notable changes to the Trusscore brand system are recorded here. Format follows [Keep a Changelog](https://keepachangelog.com); versions follow [Semantic Versioning](https://semver.org).

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
