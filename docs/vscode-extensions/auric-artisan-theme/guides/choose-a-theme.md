---
title: Auric Artisan Theme — Choose a theme
description: The six surface families, 54 variants and two high-contrast builds, and every way to switch between them.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Choose a theme

Auric Artisan Theme ships 54 built-in variants. A variant is one complete theme: a surface family (the neutral backgrounds and text) combined with an accent colour.

## The families

| Family | Surface | Polarity | Variants |
| --- | --- | --- | --- |
| Obsidian | Warm charcoal | Dark | 10 |
| Midnight | Near-black | Dark | 10 |
| Parchment | Warm cream | Light | 10 |
| Porcelain | Cool white | Light | 10 |
| Dusk | Violet-tinted dark | Dark | 6 |
| Forest | Green-tinted dark | Dark | 6 |
| High contrast | Gold, dark and light | One dark, one light | 2 |

### Accents per family

| Family | Accents |
| --- | --- |
| Obsidian, Midnight, Parchment, Porcelain | Gold, Sapphire, Rose, Amethyst, Patina, Emerald, Ember, Crimson, Iris, Graphite |
| Dusk | Gold, Sapphire, Rose, Amethyst, Iris, Graphite |
| Forest | Gold, Patina, Emerald, Ember, Rose, Graphite |
| High contrast | Obsidian Gold (High Contrast) is dark; Porcelain Gold (High Contrast) is light |

Every theme appears in VS Code as **Auric Artisan — Family Accent**, for example **Auric Artisan — Parchment Emerald**. The two high-contrast builds are **Auric Artisan — Obsidian Gold (High Contrast)** and **Auric Artisan — Porcelain Gold (High Contrast)**. See the [reference](reference.md#all-54-themes) for every theme and its ID.

> **Tip:** The variant's accent is only its starting point. You can re-key any variant onto any of 17 accents, or a custom colour, with the **Accent colour** dial.

## Ways to switch

### From the Command Palette

1. Run **Auric Theme: Switch Variant…**.
2. Type part of a name, such as "forest", to filter the list.
3. Select a theme. Each row shows its polarity and canvas colour, and the active theme is marked **current**.

### Cycle through all variants

Press `Ctrl` + `Alt` + `'` (`Cmd` + `Alt` + `'` on macOS), or run **Auric Theme: Cycle Variant**. Each press moves to the next of the 54 variants, in the order shown in the reference. If a non-Auric theme is active, cycling starts at Obsidian Gold.

### From the Auric Theme sidebar

1. Select **Auric Theme** in the Activity Bar.
2. Under **Variant**, open the searchable dropdown and pick a theme, or
3. Expand **Browse all swatches** to see compact family galleries. Each family is a collapsible group with a count and small colour-strip tiles. Select a tile to switch.

The sidebar remembers which families you expanded.

### From VS Code's own picker

Run **Preferences: Color Theme** (`Ctrl` + `K`, then `Ctrl` + `T`) and choose any **Auric Artisan —** entry.

## What happens to your customisations

- Dials (such as accent, surfaces and syntax palette) are stored in your VS Code user settings and follow you to every Auric variant.
- Colour slot overrides are stored per variant. Overrides you make on Obsidian Gold do not appear on Midnight Sapphire.
- When you switch to an Auric variant, your customisation is re-applied to it automatically.
- When you switch to a non-Auric theme, your customisations stop showing, because they are scoped to the Auric theme names. They come back when you switch back.

## Result

Your editor uses the Auric variant you picked, and the status bar item shows its short name.
