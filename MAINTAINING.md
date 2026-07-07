# Maintaining the Trusscore Brand Repo

This repository is the single source of truth for the Trusscore brand system. Every rule, color, and asset flows to the team from here. This note is for whoever maintains it.

## The golden rule

Make every change in this repo. Do not edit the skill inside the Claude Plugins panel, and do not keep private copies of the guidelines. Those do not sync back and the brand will drift. If it is not committed here, it is not real.

## Making a change

1. Edit the relevant file: `skills/trusscore-brand-guidelines/SKILL.md` for rules, `skills/trusscore-brand-guidelines/assets/logos/` for logos.
2. Review the change against the brand standards before publishing (the SKILL.md Section 15 checklist, or ask Claude to run the copy or visual review).
3. Commit to `main` with a clear message describing what changed.
4. Add an entry to `CHANGELOG.md`.
5. Tag it if it is a named release (see Versioning).

## How changes reach the team

No version is pinned in `plugin.json`, so every commit merged to `main` becomes the new version. Installed users pick it up when their plugin updates — through the **Update** button on the plugin card in Customize → Plugins, which Claude may also surface automatically. When a meaningful change ships, tell the team to hit Update.

## Editing safely

- **Never write the possessive form of the brand name** ("Trusscore's"). Even this guide follows the rules it sets.
- After any large find-and-replace, confirm the section headings are all still intact. A multi-paragraph replacement can accidentally swallow the next heading — verify structure, do not trust the success message alone.
- If you edit through Claude Code, run `claude plugin validate .` before pushing to catch manifest or JSON errors.
- Keep `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` valid. The plugin will not install without them.

## Adding or updating assets

- **Logos:** add the SVG to both `skills/trusscore-brand-guidelines/assets/logos/` (bundled with the skill) and `brand/logos/` (human library), and keep the two in sync. Use descriptive names.
- **Fonts:** never commit Circular Std — it is commercially licensed. Mulish (SIL OFL) is fine. See `brand/fonts/README.md`.
- **Colors:** the authoritative values live in SKILL.md Section 2. If a value changes, update it there and everywhere it repeats (Sections 14b and 14c), then the swatch reference in `brand/color/`.

## Versioning

- `CHANGELOG.md`: add an entry for every change, dated.
- Git tags: use `vMAJOR.MINOR.PATCH` for named releases (for example `git tag v1.2.0 && git push origin v1.2.0`).
- Because no version is pinned, commits auto-propagate. Tags and the changelog are the human-readable record.

## Access and safety

- Keep `main` protected and require a pull-request review before merge.
- Give the marketing team read access; maintainers get write.

Brand owner: Trusscore Marketing.
