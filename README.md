# Trusscore Brand

Single source of truth for the Trusscore brand system: written guidelines, the Cowork/Claude brand skill, and the master logo, color, and font assets. Everything here is version-controlled so the whole team works from one authoritative, dated version.

## What's in here

```
trusscore-brand/
├── README.md                        This file
├── USAGE.md                         For the team — install and use the plugin
├── MAINTAINING.md                   For the maintainer — how to update the brand
├── CHANGELOG.md                     Every brand change, dated and versioned
├── .claude-plugin/
│   ├── marketplace.json             Marketplace catalog — lets Claude install this from GitHub
│   └── plugin.json                  Plugin manifest for the trusscore-brand plugin
├── skills/                          Machine-facing: packaged and installed via Cowork
│   └── trusscore-brand-guidelines/
│       ├── SKILL.md                 The authoritative brand guidelines
│       └── assets/
│           └── logos/               Logo files bundled with the skill (SVG)
└── brand/                           Human-facing: for people not using the skill
    ├── logos/                       Full logo export set, all formats
    ├── color/                       Swatch files (ASE/ACO), reference sheets
    └── fonts/                       Font licensing and download pointers
```

- **`skills/`** is what Cowork installs. The brand skill reads its logos from `skills/trusscore-brand-guidelines/assets/logos/` by relative path, so the files travel with the skill to everyone who installs it. Add other Trusscore skills as sibling folders under `skills/`.
- **`brand/`** is the human library — designers and marketers grabbing a logo, swatch, or the guidelines PDF. Treat these as exports from the same masters, kept in sync with the skill assets.

## Installing the skill (Cowork)

This repository is structured as a plugin marketplace. An organization admin installs it once for the whole team:

1. **Organization settings → Plugins → Add plugin → GitHub**, and point it at this repository.
2. Enable the **trusscore-brand** plugin for the org (or the relevant groups).

Cowork and Skills must both be enabled for the organization first. The plugin's skill and its bundled logo assets then appear in Cowork and chat for everyone with the plugin enabled.

No version is pinned in `plugin.json`, so **every commit merged to `main` propagates as the new version** — push a change and users pick it up. Use git tags (for example `v1.1.0`) and `CHANGELOG.md` for human-readable release tracking.

## Ownership and changes

- Brand owner: Trusscore Marketing
- All changes to `skills/` and `brand/` go through a pull request and a review before merge.
- `main` is protected. Tag every release with a semantic version (for example `v1.0.0`) and record it in `CHANGELOG.md`.
- The commit history is the record of what changed and when — this replaces ad-hoc "did my edit save?" checks.

## The no-possessive rule applies here too

Never write the possessive form of the brand name. Use "the Trusscore brand," "Trusscore assets," and similar. See `skills/trusscore-brand-guidelines/SKILL.md`, Section 13.
