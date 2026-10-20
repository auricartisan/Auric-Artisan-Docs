---
title: Shade Library — Analyse the collection
description: Use the Harmony, Accessibility and Stats tabs to see how methods, profiles, text safety and token counts are distributed across your filtered scales.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Analyse the collection

These tabs describe every scale that matches your current search and filters — all 8,192 when nothing is set. Each is drawn when opened and redrawn after a filter change; select the tab again if it looks out of date. With nothing matching, each shows **No shade systems**.

## Harmony tab

| Card | What it counts |
| --- | --- |
| **Generation method** | Scales per method. |
| **Dominant hue bucket** | Scales per base hue. |
| **Shade profile** | Neutral, Hue Shift, Light, Deep and Balanced (see [Inspect a scale](inspect-a-scale.md)). |
| **Token count** | Scales with 5, 7, 9, 10, 11, 13, 16 or 21 tokens. |
| **Lightness & chroma profile** | Dark, Mid and Light; Muted, Balanced and Vivid. |

## Accessibility tab

### Shade-level WCAG summary

| Row | Meaning |
| --- | --- |
| **All tokens auto-AA** | Scales in which every token reaches 4.5:1 with automatic text. |
| **75%+ tokens auto-AA** | Scales in which at least three quarters of tokens do. |
| **White text coverage** | Scales in which at least 35% of tokens reach 4.5:1 with white text. |
| **Black text coverage** | The same with black text. |

In the full collection, 403 scales have every token at AA with automatic text.

### Active shade checks

The token contrast ladder for the open scale, or **Select a shade system to see per-token contrast.**

### Visible shade systems where every token gets AA auto text

Up to 24 matching scales where every token passes. Cards work as in the grid. If there are none: **No full auto-AA shade systems here**.

## Stats tab

| Card | Range | Bands |
| --- | --- | --- |
| **Avg lightness (OKLCH L)** | 0 to 1 | 10 |
| **Avg chroma (OKLCH C)** | 0 to 0.30 | 10 |
| **Hue spread** | 0° to 120° | 12 |
| **Token count** | 2 to 66 | 8 |
| **Score** | 0 to 1 | 10 |

Values beyond a range are counted in the last band.
