---
title: Gradient Library — Reference
description: Every control, filter, sort order, tab, output, file name and message in the Gradient Library.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Gradient Library reference

Everything on https://auricartisan.com/library/gradient/.

## Heading

| Item | Content |
| --- | --- |
| Kicker | **Auric Artisan · Gradient** |
| Headline | **Eight thousand ramps, and which of them band.** |
| Facts | **Collection 8,192**, **Smooth 77%**, **Measured in OKLab** |
| **Read the API guide →** | Opens the Gradient Library API guide. |
| **Automate this** note | **3 API credits per call to GET /v1/gradient/library**; **API docs**; × dismisses. |

## Will your gradient band?

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| Stop swatch | Opens a colour picker for the stop. | Any colour | — |
| Stop text field | Takes any CSS colour. | Hex, `rgb()`, `hsl()`, `hwb()`, `lab()`, `lch()`, `oklab()`, `oklch()`, `color()`, names | `#000000`, `#0B3D91`, `#FFFFFF` |
| × | Removes the stop. Hidden when two stops remain. | — | — |
| **Add a stop** | Adds a stop at the end, halfway between the last two. | Up to 12 stops | — |
| **Measure it** | Measures again. | — | — |

| Output | Meaning |
| --- | --- |
| Preview strip and marker | The ramp, evenly spaced, with the worst step marked. |
| Verdict | **Smooth** (ratio below 3.2), **Some compression** (3.2 to below 5.5), **It will step** (5.5 or more). |
| **step ratio** | Largest step divided by the mean step. |
| **Mean step**, **Largest step** | OKLab distances between neighbouring samples, five decimals. |
| **Worst transition at** | Percentage along the ramp. |
| **Sampled** | **96 steps, sRGB**. |

## Browse controls

| Control | What it does |
| --- | --- |
| **Search by name, hex or scheme…** | Every word must match name, type, angle, a stop hex, scheme, method, complexity, interpolation, easing or banding. |
| **Shuffle** | Sort **Random**. |
| **Open a random gradient** | Opens any gradient on **Inspect**. |
| **Filter inside results** (**name, hex, scheme…**) | Second search, combined. |
| **Clear** | Empties the second search. |

## Tabs

**Library** (badge: matches), **Inspect**, **Vision**, **Accessibility**, **Pair**, **Tags**, **Stats**, **Export**, **Saved** (badge: saved count).

## Filters

| Filter | Options |
| --- | --- |
| **Method** | **All methods**, Analogous, Aurora, Chaotic, Complementary, Duotone, Golden, Monochrome, Nebula, Prismatic, Spectral, Terrain, Thermal |
| **Scheme** | **All schemes** and the same twelve |
| **Complexity** | **Any complexity**, **Simple**, **Detailed**, **Extreme** |
| **Stops** | **Any stops**, **2 to 4 stops**, **5 to 8 stops**, **9 to 16 stops**, **17 to 32 stops**, **33+ stops** |
| **Interpolation** | **Any interpolation**, Lch Short, Linear Rgb, Oklab, Oklch Long, Oklch Short |
| **Easing** | **Any easing**, Cubic In Out, Linear, Quart In Out, Sine In Out, Smootherstep |
| **Score** | **Any score**, **Top quality** (≥ 0.70), **Balanced+** (≥ 0.55), **Wild / experimental** (< 0.55) |
| **Banding** | **Any banding**, **Low banding risk** (smooth), **Medium banding risk** (subtle compression), **High banding risk** (visible step risk) |

## Sort by

**Sort: original** (default), **Score high to low**, **Complexity high to low**, **Stops high to low**, **Stops low to high**, **Dominant hue**, **Random**.

## Library tab buttons

| Control | What it does |
| --- | --- |
| **Reset** | Clears searches and filters; **Sort: original**. |
| **Export visible** | Opens **Export**. |
| **Back to top** | Scrolls to the first card. |
| Counter | `first–last of total`, or **Nothing to show**. |

## Card

| Part | Action |
| --- | --- |
| Preview | Name, "scheme / space", score. |
| Stop strip | Up to 18 stops. |
| Chips | Banding (**Smooth**, **Compresses**, **Steps**), stop count. |
| **CSS** | Copy CSS. |
| **Save** / **Saved** | Save or unsave. |
| Card | Select, `Enter` or `Space`: open on **Inspect**. |

## Inspect tab

| Block | Contents |
| --- | --- |
| Preview | Name; "scheme / space / easing"; **Copy CSS**. |
| Quick facts | **Type**, **Angle**, **Stops**, **Method**, **Complexity**, **Score**, **Space**, **Easing**, **Banding**, **White min**, **Black min**, **Hue** |
| **CSS** | The CSS value; **Copy CSS**, **Download CSS**, **Download SVG**. |
| **Color Stops** | Number, swatch, hex (select to copy), position. |
| **Generator Metrics** | **Scheme**, **Interpolation**, **Easing**, **Sample Count**, **Complexity Score**, **DeltaE Mean**, **Uniformity**, **Banding**, **Seed** |
| **Quick Export** | **Download JSON**, **Download Tailwind**, **Download PNG**, **Copy share link**, **Design tokens…**, **Save gradient** / **Remove saved** |

## Vision, Accessibility, Pair

| Tab | Contents |
| --- | --- |
| **Vision** | **Normal**, **Deuteranopia**, **Protanopia**, **Tritanopia**, **Achromatopsia**, **Low Vision** previews. |
| **Accessibility** | **Contrast Summary** (**White text min**, **Black text min**, **Auto text min**, **Best sampled max**, **Adjacent stop min**, **AA-safe samples**); **Sampled Stops** (17); **Reading Guidance**. |
| **Pair** | **Text color** picker and hex field; **White**, **Black**, **Gold**; preview; **Pair Result** (**Minimum contrast**, **Average contrast**, **Text color**, **Status**) and a CSS snippet. |

Pair text colour default: white. **Gold** is `#D3AF37`; **Black** is `#111111`.

## Tags and Stats

| Tab | Cards |
| --- | --- |
| **Tags** | **Methods**, **Schemes**, **Complexity**, **Interpolation**, **Easing**, **Banding** (whole-collection counts). |
| **Stats** | **Banding**, **Methods**, **Complexity**, **Stop Counts**, **Interpolation**, **Easing**, **Score Bands** (matching set). |

## Export tab

| Card | Buttons |
| --- | --- |
| **Active Gradient** | **Copy CSS gradient**, **Download CSS class**, **Download JSON**, **Download SVG**, **Download Tailwind token**, **Download PNG preview**, **Copy share link**, **Design tokens…** |
| **Visible Set** | **JSON with metadata**, **Minified JSON**, **CSS classes**, **CSV index**, **Tailwind tokens** |
| **Current CSS** | The open gradient's CSS. |

## Files

| Output | Name | Detail |
| --- | --- | --- |
| CSS class | `<name>.css` | `.aa-gradient-<name> { background: … }` |
| JSON | `<name>.json` | Full gradient. |
| SVG | `<name>.svg` | 1440 × 900. |
| Tailwind token | `<name>.tailwind.txt` | `"<name>": "<css>"` |
| PNG | `<name>.png` | 1600 × 1000. |
| Bulk | `gradient-library-<count>-<date>.<ext>` | `json`, `css`, `csv`, `txt`. |

## Messages

| Message | When |
| --- | --- |
| **Loading gradient library...** | While loading. |
| **Could not load gradient library** | Loading failed. |
| **No gradients match** | Nothing matches the filters. |
| **No gradient selected** | **Inspect** before opening a gradient. |
| **Select a gradient** | **Vision**, **Accessibility** or **Pair** before opening a gradient. |
| **No saved gradients** | Nothing saved. |
| **CSS copied**, **Copied** | After copying. |
| **Gradient saved**, **Gradient removed** | After saving or unsaving. |
| **Select a gradient first** | An export with no gradient open. |
| **Nothing to export** | A bulk export with no matches. |
| **PNG export failed** | The browser could not make the PNG. |
| **Shared gradient not in current library** | A share link's gradient could not be found. |
| **Two stops at least.** | The checker has fewer than two stops. |
| **Stop N is not a colour yet** | A checker field holds text that is not a colour. |

## Keyboard

| Key | Action |
| --- | --- |
| `/` | Focus the search box. |
| `Enter` / `Space` | Open the focused card. |
| `Escape` | Close the share or design tokens dialog. |
