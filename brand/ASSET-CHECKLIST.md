# Trusscore Brand Asset Checklist

Status of the brand asset library. Checked = in the repo. Keep the skill `assets/logos/` folder lean; heavier items live in `brand/`.

---

## 1. Skill logo assets → `skills/trusscore-brand-guidelines/assets/logos/`

- [x] `trusscore-logo-slate.svg` — primary
- [x] `trusscore-logo-white.svg` — reversed (also the no-tagline version the dashboard uses, Section 14c)
- [x] `trusscore-logo-onecolour-white.svg` — for TC Yellow backgrounds
- [x] `trusscore-logo-tagline-slate.svg` — tagline lockup
- [x] `trusscore-logo-tagline-reverse.svg` — white tagline lockup (PowerPoint footer)
- [x] `trusscore-truss-element.svg` — solo truss mark (PowerPoint cover)

## 2. Full logo library → `brand/logos/`

- [x] SVG masters — primary, reversed, one-colour white, three tagline lockups, truss element + outline, three T-icons
- [x] PNG exports (`png/1x`, `png/2x`, `png/3x`) — logos, tagline lockups, one-colour white, favicons
- [x] EPS print versions (`eps/`)
- [ ] PNG for every remaining variant (current set covers the common ones)
- [ ] Favicon at exact icon sizes: 16, 32, 48, 180, 512 px (favicon PNGs exist at 1x/2x/3x; exact-size set still to export)
- [ ] PDF print versions (optional — EPS already covers print)

## 3. Program / sub-brand logos → `brand/logos/programs/`

- [x] Trusscore University — primary, primary+icon, reverse, reverse+icon
- [x] Trusscore Trusted Installer — slate, white
- [ ] Trusscore Community Partners — pending file

## 4. Color → `brand/color/`

- [x] `trusscore-brand-colours.cclibs` — Adobe Creative Cloud library
- [x] `trusscore.ase` (Adobe) and `trusscore.aco` (Photoshop) — generated from the brand hexes
- (Hex values locked in SKILL Section 2)

## 5. Fonts → `brand/fonts/`

- [x] Mulish — variable + static, OFL (committed)
- [x] Circular Std — pointer only in README (licensed, not committed)
- (Aptos ships with Office)

## 6. Guidelines + templates → `brand/`

- [ ] `Trusscore-Brand-Guidelines.pdf` — official human-readable guidelines
- [ ] `templates/` — branded PowerPoint master, letterhead .docx, email template(s)

## 7. Brand shapes → `brand/logos/`

- [x] Truss-mark elements — `trusscore-truss-element.svg`, `trusscore-truss-outline-element.svg`

---

## Kept out of the repo

- Product images and photography — stored in a DAM / shared Drive, linked from `brand/`, not committed (see `brand/product-images/README.md` if added)
- Licensed assets that cannot be redistributed (Circular Std, stock imagery)
