---
title: Image Picker — Reference
description: Every tab, control, readout, export format and keyboard key in the Image Picker, with ranges and starting values.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Image Picker reference

Address: https://auricartisan.com/tool/general/tools/image-picker/

## Above the tabs

| Element | What it does |
|---|---|
| **Read the API reference →** | Opens the site's API documentation |
| **Automate this** line | The REST endpoint and its cost in API credits; **API docs** opens its documentation; **×** hides the line |

## Tabs

| Tab | Contents |
|---|---|
| **Workbench** | Loading, extraction settings, preview and eyedropper, palette, tone bands, contrast pairs, harmony, pins, quick exports |
| **Analysis** | Four charts of the current palette; the label shows **4** |
| **Actions** | JSON and CSV downloads, **Copy page link**, batch colour analysis |

## Workbench — The image

| Control | What it does | Accepts |
|---|---|---|
| Drop area (middle panel, before loading) | Loads a dropped image, or opens a file chooser when selected | Any image type; PNG, JPEG, WEBP, GIF, BMP named |
| **Replace** | Opens a file chooser to load a different picture | As above |
| Address field | The web address of an image | `https://…` |
| **Load URL** | Loads the address in the field; `Enter` in the field does the same | Images whose server allows cross-origin reading |
| File name and size line | The name, and original size → working size | — |

Pictures are scaled down to fit 800 × 500 pixels, never up.

## Workbench — Extraction

| Control | Values | Starting value |
|---|---|---|
| **Clusters** | 2 to 12 on the slider | 16 when the page opens |
| **Quality** | Fast (every 10th pixel), Quick (6th), Balanced (4th), Detailed (2nd), Max detail (every pixel) | Detailed |
| **Merge threshold** | 0 to 100, RGB distance | 0 |
| **Ignore dark** | Skips pixels with relative luminance below 0.03 | Off |
| **Ignore light** | Skips pixels with relative luminance above 0.97 | Off |

Sampling is capped at about 50,000 pixels by widening the grid. Pixels that are nearly transparent are skipped. Each change re-runs the extraction when the slider is released or the switch changes.

## Workbench — Run and history

| Control | What it does | Key |
|---|---|---|
| **Re-extract** | Runs the extraction again | `E` |
| **Reset** | Clears the picture, palette and pins, and shows the drop area again; settings are kept | `R` |
| **Extractions** | The number of extractions in this session | — |

## Workbench — Preview and palette

| Element | What it shows or does |
|---|---|
| **Preview** | The working copy of the picture. Hover to read a pixel; click to pin it |
| Eyedropper readout | Hex, RGB, HSL, relative luminance and pixel position under the pointer |
| **Pin** | Pins the colour under the pointer, if there is one |
| **Extracted palette** | Swatches largest share first: share, hex, HSL, relative luminance. Select to copy the hex |
| Palette heading | Number of clusters and number of samples |
| **Tone bands** | **Shadows** (below 0.18), **Midtones** (below 0.65), **Highlights** (0.65 and above) |

## Workbench — Readouts

| Panel | Contents |
|---|---|
| **Keyboard** (before loading) | `E` Re-extract, `H` Copy hex list, `J` Copy JSON, `R` Reset |
| **Pairs that carry text** | The eight highest-contrast pairs: swatches, ratio, rating (AAA, AA, AA-lg, Fail), hex values |
| **Harmony** | Up to 12 pairs at classic hue angles: Analogous, Tetradic, Triadic, Split-Complementary, Complementary |
| **Pinned** | Up to 24 pinned colours; select one to copy its hex |
| **Take it with you** | **Hex**, **CSS**, **JSON** (copy) and **SVG** (download) |

### Contrast ratings

| Rating | Contrast ratio |
|---|---|
| AAA | 7:1 or more |
| AA | 4.5:1 or more |
| AA-lg | 3:1 or more |
| Fail | Below 3:1 |

### Harmony angles

| Relationship | HSL hue difference |
|---|---|
| Analogous | 25° to 45° |
| Tetradic | 80° to 100° |
| Triadic | 110° to 130° |
| Split-Complementary | 140° to 165° |
| Complementary | 165° to 180° |

## Analysis tab

| Element | Contents |
|---|---|
| **Charting** panel | File name, working size and pixel count |
| **Cluster population** | Bar chart of each cluster's share |
| **Colour distribution** | Ring chart of shares, leading share in the middle |
| **Hue vs saturation** | Scatter of hue (0° to 360°) against saturation (0% to 100%) |
| **Relative luminance** | Bars from darkest to lightest, 0 to 1 |
| **⛶** button or double-click | Opens the chart full screen; close with **×**, `Escape` or a click outside |

## Actions tab

| Control | What it does |
|---|---|
| **JSON** | Downloads `palette-analysis.json` |
| **CSV** | Downloads `palette.csv` |
| **Copy page link** | Copies the page address; no picture or palette is included |
| Hex box | One hex colour per line, or separated by commas, semicolons or spaces |
| **Run batch** | Analyses the colours in the box |

## Export formats

| Export | File or clipboard | Format |
|---|---|---|
| **Hex** | Clipboard | `#RRGGBB` values, comma and space separated |
| **CSS** | Clipboard | `:root { --palette-01: #RRGGBB; … }` |
| **JSON** | Clipboard, or `palette-analysis.json` | `image`, `settings`, `sampleCount`, `palette`, `picks`, `exportedAt` |
| **SVG** | `palette.svg` | 60 × 60 swatches, 4 px apart, hex labels underneath |
| **CSV** | `palette.csv` | `#,Hex,R,G,B,H,S,L,Luminance,Population%,Count` |

Hex values are written in capitals. Pins appear only in the JSON. For field details, see [Export and share](export-and-share.md).

## Batch results

Columns: **#**, **Swatch**, **Hex**, **RGB**, **HSL**, **Lab**, **LCH**, **Lum**, **Tone**. CIELAB is calculated for a D65 white. See [Analyse a list of hex colours](batch-analysis.md).

## Keyboard

| Key | Action |
|---|---|
| `E` | Re-extract |
| `H` | Copy the hex list |
| `J` | Copy the JSON |
| `R` | Reset |
| `Escape` | Close a full-screen chart |

The letter keys work when focus is not in a text field, slider, switch or menu.
