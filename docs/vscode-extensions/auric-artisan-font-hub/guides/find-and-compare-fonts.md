---
title: Auric Artisan Font Hub — find and compare fonts
description: Search and filter the Auric font library, get recommendations for a design intent, and keep favourites, recents and a selection to compare.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Find and compare fonts

## Search

Type in **Search** (placeholder **Family, designer, script, feature…**). It matches family names, designers, scripts, OpenType features and licence information. Press `/` or `Ctrl` + `K` anywhere in Font Hub to jump to it, and `Escape` to clear it.

Results appear as cards and load in batches of `auricFontLib.pageSize` (48 by default); **Show more** loads the next batch. If nothing matches, **No matching families** offers **Reset filters**.

## Category and sort

- **Category** — **All categories** or one of the library's categories: sans-serif, serif, display, handwriting and monospace.
- **Sort** — order the results:

| Sort | Order |
| --- | --- |
| **Alphabetical** | By family name |
| **Accessibility score** | Highest accessibility score first |
| **Readability score** | Highest readability score first |
| **UI score** | Highest UI and product score first |
| **Developer score** | Highest developer and code score first |
| **Editorial score** | Highest editorial score first |
| **Most weights** | Families with the most weights first |
| **Most glyphs** | Families with the most characters first |
| **Newest** | Most recently added first |
| **Variable first** | Variable families first |

## Advanced filters

Select **More filters** to show chips you can combine:

| Filter | Chips |
| --- | --- |
| **Properties** | **Variable**, **Italic**, **Monospace**, **4+ weights** |
| **Weights** | 100, 200, 300, 400, 500, 600, 700, 800, 900 |
| **OpenType** | The twelve most common feature tags in the library, such as `kern` or `liga` |
| **Scripts** | The fourteen most common character ranges, such as Basic Latin, Cyrillic or Devanagari |
| **License** | The eight most common licences, such as OFL or Apache 2.0 |
| **Source** | **Auric library**, and **System snapshot** when system fonts are included |

**Reset filters** clears them. Your search, filters, sort and scope are remembered when you close and reopen Font Hub.

## Preview text, size and density

- **Preview text** changes the sample shown on every card (up to 240 characters). The default comes from `auricFontLib.previewText`.
- **Size** sets the sample size from 18 to 96 pixels. The default is `auricFontLib.previewSize` (36).
- The density buttons switch between **Compact**, **Comfortable** and **Showcase** cards. The default is `auricFontLib.density`.

## Scopes

| Scope | Shows |
| --- | --- |
| **All** | Every family that matches |
| **For you** | Recommended families, ranked from role scores, style intent and your local use |
| **Favorites** | Families you marked with the heart, with a count |
| **Recent** | Families you recently inserted, copied, saved or downloaded, with a count |
| **Variable** | Variable families only |
| **Selected** | Families in your selection, with a count |

Turn recommendations off with `auricFontLib.recommendations.enabled`.

## Find your font

**Find your font** ranks families against what the type has to do. It uses measured traits and suitability scores, not popularity alone.

1. Select **Find your font** above the results.
2. Choose a **Design intent**: **UI & Product**, **Accessibility**, **Developer & Code**, **Editorial**, **Luxury**, **Friendly brand**, **Technical product** or **Bold display**.
3. Optionally choose an **Industry** to bias the ranking: **SaaS / Software**, **Developer / DevTools**, **Startup / Tech**, **E-commerce / Retail**, **Luxury / Fashion**, **Editorial / Publishing**, **Finance / Legal**, **Healthcare**, **Education**, **Food / Hospitality**, **Corporate / B2B** or **Creative / Agency**.
4. Optionally add a **Colour palette**: type up to eight hex colours (such as `#0F172A #F8FAFC #D7A638`) or add swatches with the colour picker. The palette's mood nudges the ranking.
5. Tick or untick **Prioritize accessibility** and **Prefer variable fonts**.
6. Select **Rank fonts**.

The shared Auric colour picker also offers contrast checks, generated ramps and a colour history for the palette.

## Collections and recommendations

**Collections & recommendations** is a collapsible section with featured collections of families and a row of recommendations.

## Favourites, recents and selection

- **Favourite** — the heart on a card, or **Favorite** in the details. **Pick from Favorite Fonts** lists them in a Quick Pick.
- **Recents** — Font Hub remembers fonts you use. **Pick from Recent Fonts** lists them.
- **Selection** — the select button on a card, or **Select** in the details, adds a family to your selection. The **Selected** button opens the tray.
- **Clear Favorites, Recents, and Selection** clears all three after confirmation.

Favourites, recents and selection are stored on your computer in VS Code's extension storage. They are not uploaded.

## The selection tray

| Button | What it does |
| --- | --- |
| **Copy embed** | Copy one combined embed for every selected family |
| **Insert** | Add the setup for every selected family to the active file (up to 12) |
| **Compare** | Open the comparison for up to four selected families |
| **Download** | Download a self-hosting kit for the selection |

## Compare families

1. Select two to four families.
2. Choose **Compare** in the tray, or run **Auric Artisan Font Hub: Compare Selected Fonts**.
3. The **Compare selected fonts** table shows each family side by side: **Category**, **Weights**, **Variable**, **Accessibility**, **Readability**, **UI & Product**, **Developer**, **Editorial** and **Glyphs**, with a specimen for each.

With fewer than two selected: **Select at least two font families to compare.** Only the first four are compared.

## Quick Picks

For keyboard-only use:

- **Quick Pick Font** (`Ctrl` + `Alt` + `T`) — search every family by name, designer, category, script or licence, then choose **Add font to code**, **Preview CDN insertion**, **Copy embed as…**, **Inspect in Font Hub**, **Download self-hosting kit** or **Toggle favorite**.
- **Pick from Favorite Fonts** and **Pick from Recent Fonts** — the same, limited to those lists.

Each entry shows the category, weights, whether it is variable, the designer, its accessibility score and its licence.

## System fonts

Turn on `auricFontLib.includeSystemFonts` to include metadata for common system fonts in the results. They are tagged **System snapshot**, their previews only work if the font is installed on your computer, and they cannot be added from the CDN or exported: copy their family name instead.

## Scores are guidance

Suitability and accessibility scores are catalogue estimates based on measured traits. They are not guarantees. Check your real text, languages, sizes and contrast in the finished product.
