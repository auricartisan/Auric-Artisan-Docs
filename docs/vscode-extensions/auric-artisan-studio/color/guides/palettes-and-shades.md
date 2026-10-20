---
title: Auric Color — Palettes and shades
description: Generate harmony palettes that meet a contrast target and perceptually even OKLCH shade scales, preview them, and export them as CSS, JSON or Tailwind.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Palettes and shades

The Studio's **Color** space has two generators: **Palette**, for sets of related colours that all meet a contrast target, and **Shades**, for a tonal scale of one colour. Both are in Auric Color.

## The Palette tool

### Open it

- Select a colour in the editor and run **Auric Artisan: Generate Accessible Palette** (also on the right-click menu when text is selected). The selection becomes the seed; if it is not a colour, the seed is `#2563EB`.
- Select **Palette** in a colour hover's **Open in Studio** row, or on the Overview.
- Open the Studio and choose **Color › Palette**, or **Open Studio: Palette** in the Command Center.

### Controls

| Control | Values | What it does |
| --- | --- | --- |
| **Seed** | Any colour | The starting colour |
| **Background** | Any colour (default white) | The surface every swatch must read on |
| **Harmony** | Complementary, Split complement, Analogous, Triadic, Tetradic, Square, Double split, Monochromatic | How the other colours relate to the seed on the colour wheel |
| **Min contrast** | 3:1 · UI / large, 4.5:1 · AA body, 7:1 · AAA body | The ratio every swatch must reach on the background |
| **Preview as** | Typical vision, Protanopia · no red, Deuteranopia · no green, Tritanopia · no blue, Achromatopsia · no color | Shows the swatches as seen with that colour-vision deficiency |

Each colour field has a swatch button that opens the Studio's pop-up picker, a text box and a copy button.

### How the palette is built

1. The harmony gives a set of hues from the seed:

| Harmony | Colours | Hue offsets from the seed |
| --- | --- | --- |
| Complementary | 2 | 0°, 180° |
| Split complement | 3 | 0°, 150°, 210° |
| Analogous | 5 | −30°, −15°, 0°, 15°, 30° |
| Triadic | 3 | 0°, 120°, 240° |
| Tetradic | 4 | 0°, 60°, 180°, 240° |
| Square | 4 | 0°, 90°, 180°, 270° |
| Double split | 5 | 0°, 30°, −30°, 150°, 210° |
| Monochromatic | 5 | Same hue, five lightness steps |

2. Each colour that does not reach the minimum contrast on the background has its lightness adjusted until it does, keeping its hue and chroma.

The strip shows each swatch's hex and ratio. A **✎** marks a swatch that was adjusted; hover it to see the original colour. Select a swatch to copy its hex (in a colour-vision preview, the real hex is copied, not the simulated one).

### Export and share

| Button | Output |
| --- | --- |
| **Export CSS** | `palette.css`: a `:root` block with `--brand-100`, `--brand-200` and so on, each with its ratio as a comment |
| **Export JSON** | `palette.json`: the harmony, background, minimum contrast, and each colour's hex, ratio and level |
| **Export Tailwind** | `palette.tailwind.js`: a Tailwind config that extends `colors` with a `brand` scale (`'100'`, `'200'` …) |
| **Copy hex list** | All hex values, comma-separated |
| **Audit as brand →** | Sends the seed and background to the [Brand](brand-audit.md) tool, with a readable text colour for the seed |

Exports open a save dialog in your first workspace folder, then open the saved file.

## The Shades tool

### Open it

- Select **Shades** in a colour hover's **Open in Studio** row or on the Overview.
- Open the Studio and choose **Color › Shades**, or **Open Studio: Shades** in the Command Center.

### What it shows

Enter a **Base color**. The tool builds an 11-step scale, 50, 100, 200 … 900 and 950, like Tailwind's naming. Each step has a fixed lightness in OKLCH, so the steps look evenly spaced, with the base colour's hue. Chroma is reduced towards the lightest and darkest steps so they do not look neon or muddy, and every step is kept inside the sRGB range.

Each cell shows the step and hex; hover it for its contrast on white. Select a cell to copy it.

**Role legibility** shows six common pairings and their ratios, green when they reach 4.5:1:

- 700 on 50
- 600 on 100
- white on 600
- 900 on 100
- white on 700
- 50 on 900

### Export

| Button | Output |
| --- | --- |
| **Export CSS** | `shades.css`: a `:root` block with `--shade-50` to `--shade-950` |
| **Export Tailwind** | `shades.tailwind.js`: a Tailwind config that extends `colors` with a `shade` scale |
| **Copy hex list** | All 11 hex values |

The same scale appears in the colour hover's **Shades** row and in the picker's **Generate › Shade ramp**.

## Related

- [Colour vision](colour-vision.md)
- [The brand audit](brand-audit.md)
- [The colour pickers](color-picker.md)
