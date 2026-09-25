---
title: Color Library — Reference
description: Every control, filter, sort order, tab, output, file name and message in the Color Library.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Color Library reference

This page lists everything on https://auricartisan.com/library/color/. For step-by-step help, see the task guides in this folder.

## Heading

| Item | What it shows or does |
| --- | --- |
| Kicker | **Auric Artisan · Colour** |
| Headline | **Eight thousand colours, measured.** |
| **Atlas** | The number of colours: 8,192. |
| **Spaces** | 7 (HEX, RGB, HSL, CIE L\*a\*b\*, OKLab, OKLCH, CMYK). |
| **Every figure precomputed** | The figures come stored with each colour. |
| **Read the API reference →** | Opens the site's API documentation at https://auricartisan.com/library/documentation/api/. |
| **Automate this** note | Names the API call for the same job and its credit cost; links to **API docs**; can be dismissed. |

## Start from a colour you already have

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| Colour field | Takes a colour in any CSS format; results update as you type. | Hex (3, 4, 6, 8 digits), `rgb()`, `hsl()`, `hwb()`, `lab()`, `lch()`, `oklab()`, `oklch()`, `color()` (`srgb`, `srgb-linear`, `display-p3`), 148 CSS names, three bare numbers | `#D3AF37` |
| Swatch | Shows the colour the field was read as. | — | — |
| **Find its neighbours** | Runs the match now. | — | — |
| Result cells | Your colour, then the five nearest atlas colours with ΔE and contrast. Select a neighbour to open it. | — | — |
| Neighbourhood sentence | One of three verdicts on whether nearby colours carry text. | — | — |

### ΔE words

| ΔE (CIE76) | Word |
| --- | --- |
| Under 2.3 | **indistinguishable** |
| 2.3 to under 5 | **a close match** |
| 5 to under 10 | **visibly different** |
| 10 or more | **a different colour** |

## Or from what it has to do

| Chip | Test | Count alone |
| --- | --- | --- |
| **Readable on white** | Contrast on white 4.5:1 or more | 2,998 |
| **Readable on black** | Contrast on black 4.5:1 or more | 5,344 |
| **Vivid** | OKLCH chroma 0.18 or more | 2,707 |
| **Muted** | OKLCH chroma below 0.06 | 695 |
| **Calm** | Emotion label `calm` | 843 |
| **For typography** | Design usage `typography` | 819 |
| **As an accent** | Design tag `accent` | 822 |

Chips combine with AND. Each chip's number is what would remain if you toggled it. The line under the chips reports the matching count and its percentage of 8,192.

## Browse the atlas

| Control | What it does | Default |
| --- | --- | --- |
| **Search by hex (#a6e223) or id…** | Every word must match the hex, id, emotion, art movement, mood or design usage. Part-words match. | Empty |
| **Shuffle** | Sets the sort to **Random**. | — |
| **Open a random colour** | Opens any colour from the whole atlas. | — |
| **Filter inside results** box | A second search, combined with the first. | Empty |
| **Clear** | Empties the **Filter inside results** box. | — |

## Tabs

| Tab | Badge | Contents |
| --- | --- | --- |
| **Library** | Number of matching colours | Filters, sort, grid. |
| **The colour** | — | The open colour's full record. |
| **Stats** | — | Four histograms of the matching colours. |
| **Export** | — | Selection and visible-set exports. |
| **Saved** | Number of saved colours | Your saved colours. |

## Filters (Library tab)

| Filter | Options | Test |
| --- | --- | --- |
| **Hue** | **All hues** | No test. |
| | **Red** | HSL hue 340° to under 20° |
| | **Orange** | 20° to under 50° |
| | **Yellow** | 50° to under 80° |
| | **Green** | 80° to under 160° |
| | **Cyan** | 160° to under 200° |
| | **Blue** | 200° to under 260° |
| | **Purple** | 260° to under 300° |
| | **Pink** | 300° to under 340° |
| | **Neutral / Gray** | OKLCH chroma below 0.04 (the hue options above need 0.04 or more) |
| **Lightness** | **Any lightness**, **Dark (L < 35)**, **Mid (35–70)**, **Light (> 70)** | CIE L\* |
| **Chroma** | **Any chroma**, **Muted** (below 0.07), **Balanced** (0.07 to 0.15), **Vivid** (above 0.15) | OKLCH chroma |
| **Emotion** | **All emotions**, calm, cheerful, cool, elegant, energetic, melancholy, mysterious, playful, romantic, warm | Emotion label |
| **Art movement** | **All movements**, Art Deco, Bauhaus, De Stijl, Fauvism, Impressionism, Minimalism, Pop Art, Romanticism | Art movement label |
| **AI mood** | **All moods**, dark, dreamy, futuristic, industrial, intense, joyful, luxurious, nostalgic, organic, serene | Mood label |
| **Design usage** | **All usages**, data-viz, gradient-end, gradient-start, icon-fill, illustration, packaging, shadow, typography, ui-surface, web-hero | Design usage label |
| **WCAG** | **Any WCAG**, **AA on white**, **AAA on white**, **AA on black**, **AAA on black** | AA: 4.5:1 or more; AAA: 7:1 or more |

The design tag (CTA, accent, background, earth-tone, jewel-tone, muted, neutral, pastel, primary, vibrant) has no filter of its own; the **As an accent** chip tests one of its values.

## Sort by

| Option | Order |
| --- | --- |
| **Sort: original** | By atlas id (default). |
| **Hue (rainbow)** | By HSL hue, ascending. |
| **Lightness ↑** | By OKLCH lightness, darkest first. |
| **Lightness ↓** | Lightest first. |
| **Chroma ↓** | Highest chroma first. |
| **Luminance ↓** | Highest relative luminance first. |
| **Random** | Shuffled. |

## Library tab buttons and grid

| Control | What it does |
| --- | --- |
| **Reset** | Empties both searches, resets every filter and sets **Sort: original**. Chips are kept. |
| **Export visible** | Opens the **Export** tab. |
| Tile | Shows the colour and hex; select it, or press `Enter` or `Space` on it, to open the colour. |
| Tile footer | Hex code, emotion label, save star (☆ to save, ★ to unsave). |
| Range line | For example **1–48 of 8,192 colours**; **Nothing to show** when empty. |
| **Back to top** | Scrolls the grid to its first colour. |

## The colour tab

| Block | Contents |
| --- | --- |
| Identity | Swatch, hex, **Atlas id** and labels; **Copy** and **Save** buttons. |
| **What it can carry** | Text specimens on white and black with ratios; a one-sentence verdict. |
| **Under other eyes** | **Normal vision**, **Protanopia** (red-blind), **Deuteranopia** (green-blind), **Tritanopia** (blue-blind), each with a hex code. |
| **Every space, and the metrics** | **RGB**, **HSL**, **CIE L\*a\*b\***, **OKLab**, **OKLCH**, **CMYK**, **Relative luminance**, **Chroma**, **Vividness**, **Perceptual uniformity**. |
| **Nearest in the atlas** | Five nearest colours with ΔE and a word. |

## Stats tab

| Card | Range | Bands |
| --- | --- | --- |
| **Hue (HSL)** | 0° to 360° | 12 |
| **Lightness (Lab L\*)** | 0 to 100 | 10 |
| **Chroma** | 0 to 0.40 | 10 |
| **Contrast on white** | 1:1 to 21:1 | 10 |

Select a card's heading to fold or unfold it.

## Export tab

### Selection

| Group | Button | Output |
| --- | --- | --- |
| **Copy formats** | **HEX** | `#76CDF6` style |
| | **RGB** | `rgb(118, 205, 246)` style |
| | **HSL** | `hsl(199 88% 71%)` style |
| | **Lab** | `lab(78.56% -15.21 -28.22)` style |
| | **OKLCH** | `oklch(80.89% 0.102 230.17)` style |
| | **CSS variables** | `:root` block with `--color-hex`, `--color-rgb`, `--color-hsl`, `--color-oklch` |
| **Download** | **JSON (full metadata)** | `<hex>.json` |
| | **SVG** | `<hex>.svg`, 480 × 280 |
| | **PNG** | `<hex>.png`, 800 × 480 |

### Visible set

| Group | Button | File |
| --- | --- | --- |
| **Bulk download** | **JSON (all metadata)** | `color-library-<count>-<date>.json` |
| | **JSON (compact: id + hex)** | `color-library-<count>-<date>.json` |
| | **CSV (flat)** | `color-library-<count>-<date>.csv` |
| | **.txt (one hex per line)** | `color-library-<count>-<date>.txt` |
| **Style formats** | **CSS variables** | `color-library-<count>-<date>.css` (`--color-<id>`) |
| | **SCSS variables** | `color-library-<count>-<date>.scss` (`$color-<id>`) |
| | **tailwind.config.js fragment** | `color-library-<count>-<date>.js` (`c<id>`) |

## Messages

| Message | When |
| --- | --- |
| **Loading color atlas…** | While the atlas loads. |
| **Could not load color atlas** | The atlas failed to load; the reason follows. |
| **No colors match these filters** | Nothing matches; with the hint **Try clearing the search or selecting "Any" on filters.** |
| **Not a colour this reads.** | The colour field could not read your text. |
| **No colour open** | **The colour** tab before any colour is opened. |
| **No color selected.** | **Export** before any colour is opened. |
| **No colors** | **Stats** with nothing matching. |
| **No saved colors yet** | **Saved** with nothing saved. |
| **HEX copied**, **RGB copied**, **HSL copied**, **Lab copied**, **OKLCH copied**, **CSS variables copied** | After a copy. |
| **Downloaded** and a file name | After a bulk download. |
| **PNG downloaded** | After a PNG download. |
| **Could not encode PNG** | The browser could not make the PNG. |
| **Nothing to export** | A bulk export with no matching colours. |

## Keyboard

| Key | Action |
| --- | --- |
| `/` | Focus the main search box (when not typing in a field). |
| `Enter` or `Space` | Open the focused tile. |
| `Tab` | Move between controls and tiles. |
