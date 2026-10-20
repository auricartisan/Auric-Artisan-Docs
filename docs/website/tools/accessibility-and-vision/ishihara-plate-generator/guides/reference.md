---
title: Ishihara Plate Generator — Reference
description: Every control, option, default and output of the Ishihara Plate Generator.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Ishihara Plate Generator reference

## Page

| Item | Detail |
| --- | --- |
| Address | https://auricartisan.com/tool/ishihara-plate-generation/ |
| Tabs | **Lab**, **Diagnostics**, **Set 38**, **Export** |
| API hint | 3 API credits per call to `POST /v1/ishihara/plate` |
| On load | Six starter plates are generated |
| Notice | "Not a colour-vision test. These plates are illustrative…" |

## Lab: main controls

| Control | Options | Default |
| --- | --- | --- |
| **Plate Type** | Number, Letter, Symbol, Number (Gradient), Shape, Multi-layer (Shape+Number), Hidden Path | Number |
| **Color Palette** | Auto (Random) or one of eight named palettes (see [Generate plates](generate-plates.md)) | Auto (Random) |
| **Difficulty** | Easy, Medium, Hard, Extreme | Medium |
| **+ Generate** | One plate | — |
| **×1**, **×3**, **×6** | Several plates | — |
| **Custom** | Opens **Create Custom Plate** | — |
| **Clear All** | Removes every plate | — |
| **↓ Export All** | ZIP of every plate | — |
| **Plate Size** | S (210 px), M (290 px), L (440 px), XL (900 px) | M |

## Create Custom Plate

| Field | Values |
| --- | --- |
| **Plate Type** | As above |
| **Content** | A number, a letter, or a symbol or shape name |
| **Color Palette** | As above |
| **Difficulty** | As above |
| **Seed (optional)** | Any whole number; the same seed and settings give an identical plate |
| **Cancel** / **Generate** | — |

Symbol names: star, arrow, triangle, heart, diamond, circle, square, moon, sun, check, x, target, squareDot, dot, leaf, wave, shield. Shape names: pentagon, octagon, rounded-square, annulus, oval.

## Fine tuning

| Control | Range or options | Default |
| --- | --- | --- |
| **Dot Count** | 2,000–15,000 | 7,000 |
| **Plate Shape** | Circle, Square | Circle |
| **CVD Preview** | Off, Protanopia, Deuteranopia, Tritanopia | Off |
| **Placement Engine** | Balanced, Organic, Precision, Dense | Balanced |
| **Dot Style** | Mixed, Round, Soft Edge, Rings | Mixed |
| **Material** | Paper, Warm Card, Cool Card, Transparent | Paper |
| **Color separation** | 0–100 | 55 |
| **Edge blend** | 0–100 | 42 |
| **Dot scale** | 70–145 | 100 |
| **Texture grain** | 0–100 | 35 |

## Plate card

| Item | Meaning |
| --- | --- |
| Heading | Plate number and content, for example "#1 - 45" |
| Tags | Type, palette, difficulty, dot count, placement engine, dot style |
| **QA PASS** and percentage | Pass or review, and the quality score |
| Preview switch | **Normal**, **Protan**, **Deutan**, **Tritan** |
| **Normal ΔE** | Figure against background for typical vision (OKLab) |
| **CVD min** | The smallest figure-to-background distance through the three deficiencies |
| **Density** | Share of the plate covered by dots |
| **Figure** | Share of dots in the figure |
| **Seed** | The number that rebuilds the plate |
| **Material** | The card stock |
| **Copy seed**, **Download PNG**, **Download SVG** | Actions |

## Full-size view

Opened by double-clicking a plate, or `Enter` or `Space` on it. Shows content, type, palette, difficulty, dots, plate number, QA score, **Separation ΔE**, **Concealment ΔE**, seed and position; the preview switch; `Left` / `Right` to move; `Esc` to close.

## This batch (Lab)

**Plates**, **Rendered**, **Avg dots**, **Color space** ("P3 HDR" or "sRGB"), **Avg QA**.

## Diagnostics

| Item | Detail |
| --- | --- |
| Summary | **Plates**, **Passing**, **Mean score**, **Weakest** |
| Components | **Dot density** (.24), **Figure ratio** (.20), **Separation** (.32), **Concealment** (.24) |
| Through each deficiency | ΔE from the background under Protanopia, Deuteranopia, Tritanopia |
| Pass rule | Density 0.08–0.95, figure 5–65% of dots, separation above 0.01, score 45 or more |

## Set 38

| Item | Detail |
| --- | --- |
| **Generate the set** | Builds 38 plates without touching the Lab |
| Composition | 24 numbers, 6 letters, 4 symbols, 2 shapes, 2 paths |
| Seed | 42 |

## Export

| Action | Output |
| --- | --- |
| Card **Download PNG** | `ishihara-plate-<number>-<content>.png`, 4,096 px |
| Card **Download SVG** | `ishihara-plate-<number>-<content>.svg` |
| **Export every plate**, **Download every .png**, **↓ Export All** | `ishihara-plates.zip`: PNG (2,048 px), SVG and JSON per plate |
| **Download every .svg** | One SVG per plate |
| **Download the seeds** | `ishihara-seeds.txt`: content, seed, type, palette, difficulty, dots, quality |

## Remembered in this browser

Only the **Plate Size**. Plates themselves are not kept between visits.
