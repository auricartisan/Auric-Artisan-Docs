---
title: Palette Library — Reference
description: Every control, filter, sort order, tab, output, file name and message in the Palette Library.
product: Website › Library › Colour libraries › Palette Library
updated: 2026-09-25
---

# Palette Library reference

Everything on https://auricartisan.com/library/palette/.

## Heading

| Item | Content |
| --- | --- |
| Kicker | **Auric Artisan · Palette** |
| Headline | **Five million palettes, and a 660-byte file.** |
| **Collection** | 5,000,000 |
| Facts | **Five colours each**, **Derived, not stored** |
| **Read the API guide →** | Opens the Palette Library API guide in the documentation library. |
| **Automate this** note | **3 API credits per call to GET /v1/palette/library**; links to **API docs**; × dismisses it. |

## Browse controls

| Control | What it does | Default |
| --- | --- | --- |
| **Search by id or hex…** | An id (`pal_…`) or a number shows that one palette. Other words must each match the id, the method or a colour's hex. | Empty |
| **Shuffle** | Sets **Sort by** to **Random**. | — |
| **Open a random palette** | Opens any of the 5,000,000 palettes on **Inspect**. | — |
| **Filter inside results** box (**id, hex, method…**) | A second search, combined with the first. | Empty |
| **Clear** | Empties the second box. | — |

## Tabs

| Tab | Badge | Contents |
| --- | --- | --- |
| **Library** | **5M** | Filters, sort, grid, counter. |
| **Inspect** | — | The open palette. |
| **Harmony** | — | Method, hue, harmony and lightness/chroma distributions of the sample. |
| **Accessibility** | — | Pair-contrast summaries of the sample. |
| **Stats** | — | Four histograms of the sample. |
| **Export** | — | Selection and sample exports. |
| **Saved** | Number saved | Saved palettes. |

## Filters

| Filter | Options | Test |
| --- | --- | --- |
| **Dominant hue** | **All hues**, **Red** (340° to under 20°), **Orange** (20–50°), **Yellow** (50–80°), **Green** (80–160°), **Cyan** (160–200°), **Blue** (200–260°), **Purple** (260–300°), **Pink** (300–340°) | Chroma-weighted average of the five OKLCH hues. |
| **Chroma** | **Any chroma**, **Muted (< 0.07)**, **Balanced** (0.07 to 0.15), **Vivid (> 0.15)** | Average OKLCH chroma. |
| **Lightness** | **Any lightness**, **Dark** (below 0.40), **Mid** (0.40 to 0.70), **Light** (above 0.70) | Average OKLCH lightness. |
| **Method** | **All methods**, complementary, triadic, analogous, tetradic, golden_ratio, random, monochromatic | The palette's method label. |

## Sort by

| Option | Order |
| --- | --- |
| **Sort: original** | Palette number (default). Streams through the whole collection. |
| **Lightness ↑** / **Lightness ↓** | Average OKLCH lightness. |
| **Chroma ↑** / **Chroma ↓** | Average OKLCH chroma. |
| **Hue (rainbow)** | Dominant hue. |
| **Random** | Shuffled. |

Any sort other than **Sort: original** orders a first stretch of 1,500 derived palettes (or the matches among them).

## Library tab buttons

| Control | What it does |
| --- | --- |
| **Reset** | Clears both searches and every filter; sets **Sort: original**. |
| **Export visible** | Opens the **Export** tab. |
| **Back to top** | Scrolls to the start of the grid. |

## Card

| Part | Action |
| --- | --- |
| Swatch | Select to copy its hex. `Enter` or `Space` on a focused swatch opens the palette. |
| Id and method | Palette id and method label. |
| **Inspect** | Opens the palette on **Inspect**. |
| **Copy** | Copies the five hexes, comma-separated. |
| **Save** / **Saved** | Saves or unsaves. |
| Rest of the card | Opens the palette on **Inspect**. |

## Counter under the grid

| Text | Meaning |
| --- | --- |
| **1–48 of 5,000,000 palettes** | Unfiltered; the range currently shown. |
| **… · scroll reaches N; search an id for the rest** | The scrollbar cannot go beyond palette N. |
| **N matches from M derived** | Filtered; M palettes worked out so far, N match. |
| **· all five million looked at** | The scan reached the end. |
| **N matches, ordered within the first M derived** | Filtered and sorted. |
| **1 palette, by id** | An id is in the search box. |
| **No palette with that id** | The id is outside the collection. |

## Inspect tab

| Block | Contents |
| --- | --- |
| Colour strip | Five columns with a three-word name and hex; select to copy. |
| **Palette summary** | Badge (**Neutral**, **Triadic**, **Analogous**, **Monochrome**); **Palette ID**, **Global index**, **Method**, **Colors**, **Avg L\* (OKLCH)**, **Avg chroma**, **Hue span**, **DeltaE avg**, **Entropy**, **Min pair contrast**, **Max pair contrast**. |
| **Pair-by-pair WCAG contrast** | Ten pairs with ratios. |
| **Quick export** | **Copy HEX**, **Copy CSS vars**, **Copy SCSS**, **Copy Tailwind**, **Download JSON**, **Download ASE**, **Download SVG**, **Download PNG**, **Open in Coolors**, **Save to library** / **Unsave**, **Copy share link**, **Design tokens…** |
| **Color 1** to **Color 5** | **HEX**, **RGB**, **OKLCH**, **CIE L\*a\*b\***, **WCAG vs white**, **WCAG vs black**, copy buttons. |

Select a card heading to fold or unfold it.

## Analysis tabs

| Tab | Cards |
| --- | --- |
| **Harmony** | **Generation method**, **Dominant hue bucket**, **Harmony classification**, **Lightness & chroma profile** |
| **Accessibility** | **Palette-level WCAG summary**, **Pair-level WCAG breakdown**, **How many of the five can be used together**, **The most usable in this sample** |
| **Stats** | **Avg lightness (OKLCH L)** (0–1, 10 bands), **Avg chroma (OKLCH C)** (0–0.30, 10 bands), **Hue spread** (0–360°, 12 bands), **Best pair contrast** (1–15:1, 14 bands) |

Sample: the first 2,000 palettes, or up to 2,000 matches from the first 40,000 when filtered.

## Export tab

| Card | Group | Buttons |
| --- | --- | --- |
| **Selection · id** | **Copy formats** | **HEX list**, **CSS variables**, **SCSS variables**, **Tailwind config** |
| | **Download** | **JSON**, **Adobe ASE**, **SVG strip**, **PNG strip** |
| | **External** | **Open in Coolors** |
| **Visible page** | **Bulk download** | **Download JSON (visible page)**, **Download CSV (visible page)**, **Download CSS variables**, **Download SCSS variables**, **Download compact JSON** |
| | **Sample formats** | **Download .txt hex list**, **Download tailwind.config.js fragment** |

## Files

| Output | File name | Size or shape |
| --- | --- | --- |
| JSON (one palette) | `<id>.json` | Full record with contrast table. |
| ASE | `<id>.ase` | Five RGB swatches `<id>_1` to `<id>_5`. |
| SVG | `<id>.svg` | 600 × 220. |
| PNG | `<id>.png` | 800 × 320. |
| Bulk | `palette-page-<count>-<date>.<ext>` | `json`, `csv`, `css`, `scss`, `txt`, `js`. |
| Design tokens | See [Copy, export and share](copy-export-and-share.md) | Eight formats; **Download all** makes `palette-<id>.zip`. |

## Design tokens dialog

| Control | What it does | Default |
| --- | --- | --- |
| **Token prefix** | The start of every token name. | `brand` |
| Format tabs | **W3C Design Tokens**, **CSS Variables**, **SCSS**, **Tailwind Config**, **Style Dictionary**, **Material UI Theme**, **iOS (SwiftUI)**, **Android colors.xml** | **W3C Design Tokens** |
| **Copy** | Copies the preview. | — |
| **Download** | Saves the current format. | — |
| **Download all** | Saves every format in one ZIP. | — |

## Share link dialog

| Control | What it does |
| --- | --- |
| Link field | The share address, selected and ready to copy. |
| **Copy** | Copies the link (**Copied!**). |
| **Share via…** | Opens your device's share sheet, where available. |
| **Open in new tab** | Opens the link. |
| **Close** / ✕ | Closes the dialog. |

## Messages

| Message | When |
| --- | --- |
| **Loading palette database…** | While the page prepares. |
| **Could not load palette database** | The collection description failed to load. |
| **Nothing matched yet** | No match found so far in a scan. |
| **No palette selected** | **Inspect** or **Export** before a palette is opened. |
| **No palettes** | An analysis tab found no matches in its sample. |
| **No saved palettes yet** | The **Saved** tab is empty. |
| **#HEX copied**, **Palette hexes copied**, **HEX list copied**, **CSS variables copied**, **SCSS variables copied**, **Tailwind config copied**, **Copied** | After copying. |
| **Downloaded** and a file name | After a download. |
| **Saved**, **Removed** | After saving or unsaving from **Inspect**. |
| **Nothing to export** | Bulk export of an empty sample. |
| **Could not encode PNG** | The browser could not make the PNG. |
| **Shared palette not found in current dataset** | A share link's palette could not be found. |

## Keyboard

| Key | Action |
| --- | --- |
| `/` | Focus **Search by id or hex…** (when not typing in a field). |
| `Enter` / `Space` | On a focused swatch: open its palette. |
| `Escape` | Close the share or design-tokens dialog. |
