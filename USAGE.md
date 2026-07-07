# Using the Trusscore Brand Plugin

This plugin gives Claude one skill that applies the full Trusscore brand system — colors, typography, voice, and editorial standards — to anything you make: documents, decks, dashboards, emails, social posts, and copy. This guide is for team members using it on an individual Max account.

## One-Time Setup

Each person installs the plugin on their own account (on a Max plan, plugins are personal — they do not install for the whole team at once).

1. Connect GitHub if you have not already: Customize → Connectors → GitHub. The brand repo is private, so this is required to install it.
2. Open Customize → Plugins → Personal plugins → click **+** → **Add marketplace** → add from GitHub → `TrusscoreMarketing/trusscore-brand`.
3. Install the **trusscore-brand** plugin and toggle it on.
4. Turn off anything that competes: the old `brand-style-guide` skill and the generic "Brand voice" plugin. Either can override the Trusscore rules.

## How to Use It Day to Day

Just work normally. Ask Claude for what you need and the skill applies automatically to Trusscore work:

- "Write a Trusscore email to contractors about install speed."
- "Make a one-page sell sheet on Trusscore® Wall&CeilingBoard™ for a garage."
- "Build a dashboard of our campaign numbers."
- "Draft five Instagram captions for the residential audience."

You can also invoke it explicitly by typing `/` in chat and choosing `trusscore-brand-guidelines`.

## What It Does for You

- **Editorial:** Chicago Manual of Style 18th edition, Oxford commas, no possessive of the brand name, correct product names, Title Case headlines with sentence-case subheads.
- **Voice:** plainspoken, benefits-first, and matched to the audience — homeowner, contractor, or commercial and agricultural.
- **Visual:** the color system and the 60-30-10 rule, the typography scale, 4px corners, Lucide outline icons, no generic "AI look," and the bundled Trusscore logos.

## Quick "Is It On Brand?" Check

The rules that matter most, so you can spot-check any output:

- Never write "Trusscore's" — rewrite the sentence instead.
- Use full product names on first reference: Trusscore® Wall&CeilingBoard™, Trusscore® SlatWall™, NorLock™ by Trusscore®, RibCore™ by Trusscore®, DockDeck™ by Trusscore®. Never WCB, SW, "plastic," or "PVC panels."
- Match the tagline to the audience: residential uses "Real Life Looks Good Here" and "Goodbye drywall, hello [logo]"; commercial and agricultural use "Built to Last" or "Discover the Strength and Durability of Trusscore."
- Colors: TC Slate `#3A4B5C`, TC Yellow `#FEB100` (accent only, never text on white), TC Blue `#009BD6`, TC Green `#6BA543`, TC Text `#111A22` for body copy.
- Do not use drywall as the comparison point in commercial or agricultural copy.

## Staying Current

The brand is maintained in the GitHub repo, so you always get the latest by updating the plugin. When a new version ships, open Customize → Plugins, find the Trusscore plugin, and click **Update**.

## If Something Looks Off-Brand

Ask Claude to review it against the Trusscore brand guidelines, or flag it to the brand owner (Trusscore Marketing) so the guidelines can be corrected at the source.
