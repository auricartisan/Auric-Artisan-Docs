---
title: Image Picker — Export and share
description: Copy the palette as hex, CSS custom properties or JSON, download it as SVG, JSON or CSV, and copy the page link.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Export and share

There are two places to take a palette away: **Take it with you** on the right of the **Workbench** tab, and **Download** on the **Actions** tab.

The page shows no confirmation after copying or downloading. Paste the text, or check your downloads, to confirm.

## What each export contains

| Export | Where | Contains | Pins included |
|---|---|---|---|
| **Hex** | Workbench | Palette hex values, comma separated | No |
| **CSS** | Workbench | Palette as CSS custom properties | No |
| **JSON** (copy) | Workbench | Full analysis | Yes |
| **SVG** | Workbench | A strip of palette swatches with labels, downloaded | No |
| **JSON** (download) | Actions | Full analysis, as `palette-analysis.json` | Yes |
| **CSV** | Actions | One row per palette colour, as `palette.csv` | No |

The heading **Take it with you** says **palette + pins**, but only the JSON carries the pins.

## Hex

Selecting **Hex**, or pressing `H`, copies the palette in order of share:

```text
#2E4A5C, #D9C7A8, #8A6A4F, #C0392B
```

## CSS

Selecting **CSS** copies a block of numbered custom properties:

```css
:root {
  --palette-01: #2E4A5C;
  --palette-02: #D9C7A8;
  --palette-03: #8A6A4F;
  --palette-04: #C0392B;
}
```

## JSON

Selecting **JSON** on the **Workbench**, or pressing `J`, copies the full analysis. **JSON** on the **Actions** tab downloads the same content as `palette-analysis.json`.

```json
{
  "image": {
    "width": 4032, "height": 3024,
    "canvasWidth": 667, "canvasHeight": 500,
    "label": "harbour.jpg"
  },
  "settings": {
    "clusterCount": 6, "quality": 4, "mergeThreshold": 0,
    "ignoreDark": false, "ignoreLight": false
  },
  "sampleCount": 41750,
  "palette": [
    {
      "hex": "#2E4A5C", "r": 46, "g": 74, "b": 92,
      "hsl": { "h": 203.5, "s": 33.3, "l": 27.1 },
      "lab": { "L": 30.04, "a": -4.96, "b": -13.89 },
      "lch": { "L": 30.04, "C": 14.75, "h": 250.3 },
      "luminance": 0.06251,
      "population": "24.13%",
      "count": 10074
    }
  ],
  "picks": [ { "r": 192, "g": 57, "b": 43, "hex": "#C0392B" } ],
  "exportedAt": "2026-09-24T10:15:00.000Z"
}
```

| Field | Meaning |
|---|---|
| `image` | Original width and height, working width and height, and the file name or address |
| `settings` | Clusters, quality (1 Fast to 5 Max detail), merge threshold, and the two ignore switches |
| `sampleCount` | Pixels sampled |
| `palette[].hex`, `r`, `g`, `b` | The colour |
| `palette[].hsl` | Hue in degrees, saturation and lightness in percent |
| `palette[].lab` | CIELAB, calculated for a D65 white |
| `palette[].lch` | CIELAB lightness, chroma and hue angle |
| `palette[].luminance` | WCAG relative luminance, 0 to 1 |
| `palette[].population`, `count` | Share of the samples as a percentage, and the number of samples |
| `picks` | Your pinned colours |
| `exportedAt` | When the export was made |

The values in the example are illustrative.

## SVG

Selecting **SVG** downloads `palette.svg`: one 60 × 60 swatch per palette colour with rounded corners, 4 pixels apart, with the hex value written under each. Open it in any drawing program or browser.

## CSV

On the **Actions** tab, **CSV** downloads `palette.csv`:

```text
#,Hex,R,G,B,H,S,L,Luminance,Population%,Count
1,#2E4A5C,46,74,92,203.5,33.3,27.1,0.06251,24.13,10074
```

| Column | Meaning |
|---|---|
| `#` | Position in the palette |
| `Hex`, `R`, `G`, `B` | The colour |
| `H`, `S`, `L` | HSL hue in degrees, saturation and lightness in percent |
| `Luminance` | Relative luminance, five decimal places |
| `Population%` | Share of the samples |
| `Count` | Number of samples in the cluster |

## Copy the page link

On the **Actions** tab, **Copy page link** copies the address of the page. It does not carry the picture, the settings or the palette; whoever opens it starts with an empty tool. To share a palette, send the JSON, CSS or SVG instead.

## Automate it

The same job, extracting a palette from an image, is available through the site's REST API as `POST /v1/palette/from-image`. The line under the page heading gives the current cost in API credits, and **API docs** opens the documentation for that endpoint at https://auricartisan.com/library/documentation/api/#ep-post-palette-from-image. API credits are a separate balance from the tokens that tools use. See [Public API](../../../../../services/public-api/README.md).
