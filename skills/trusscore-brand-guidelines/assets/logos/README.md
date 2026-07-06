# Skill logo assets

Logo files the brand skill references by relative path. Keep these in sync with `brand/logos/` — these are the copies that ship inside the installed skill.

## Drop these files here (SVG preferred)

- `trusscore-logo-primary.svg` — slate wordmark + yellow truss mark (light backgrounds)
- `trusscore-logo-reversed-white.svg` — white wordmark + yellow truss mark (dark / TC Slate backgrounds)
- `trusscore-logo-onecolor-white.svg` — all-white lockup
- `trusscore-logo-onecolor-slate.svg` — all-slate lockup
- `trusscore-wordmark-primary.svg` — wordmark only, no tagline (small sizes)
- `trusscore-wordmark-reversed-white.svg` — white wordmark only, no tagline
- `trusscore-truss-mark-yellow.svg` — solo truss mark, TC Yellow

## Rules

- Use **SVG** exports from the original source (Illustrator/Figma), not rasters pulled from PowerPoint or slides.
- Use the descriptive names above, not coded filenames.
- Do not commit a lockup that is missing the wordmark. Verify each file renders the full mark before adding it.
- When the skill needs the reversed white logo (for example the dashboard header in Section 14c), reference `assets/logos/trusscore-wordmark-reversed-white.svg` — never render "trusscore" as styled text.
