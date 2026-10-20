---
title: Harmony Library — Analyse the collection
description: Use the Theory, Accessibility and Stats tabs to see how schemes, families, adherence and contrast are distributed across the harmonies you have filtered.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Analyse the collection

The **Theory**, **Accessibility** and **Stats** tabs describe every harmony that matches your current search and filters — the whole collection when nothing is set. Because all 8,192 harmonies are calculated when the page opens, these are complete counts, not samples.

Each tab is drawn when you open it and redrawn after the filters change. If a tab looks out of date, select it again. With nothing matching, each tab shows **No harmonies**.

## Theory tab

| Card | What it counts |
| --- | --- |
| **Color-theory scheme** | Harmonies per method. |
| **Family** | Harmonies per family. |
| **Dominant hue bucket** | Harmonies per overall hue: red, orange, yellow, green, cyan, blue, purple, pink. |
| **Color count** | Harmonies with 2, 3, 4, 5, 6 or 7 colours. |
| **Adherence to canonical scheme** | **High (≥ 0.85)**, **Medium (0.60-0.85)** and **Low (< 0.60)**. |
| **Lightness & chroma profile** | **Dark (L < 0.4)**, **Mid (0.4-0.7)**, **Light (> 0.7)**; **Muted (< 0.07)**, **Balanced**, **Vivid (> 0.15)**. |

In the full collection there are 1,070 complementary-family, 2,138 polyadic, 1,424 analogous, 2,136 monochromatic and 1,424 compound harmonies, and adherence is high for 6,521, medium for 1,608 and low for 63.

## Accessibility tab

### Harmony-level WCAG summary

| Row | Meaning |
| --- | --- |
| **Has any AA pair (4.5+)** | Harmonies with at least one pair at 4.5:1 or more. |
| **Has any AAA pair (7+)** | Harmonies with at least one pair at 7:1 or more. |
| **All pairs AA** | Harmonies in which every pair reaches 4.5:1 (up to 24 are counted and shown below). |

Across the full collection, 2,078 harmonies (about a quarter) have an AA pair, 1,588 an AAA pair, and only 7 have every pair at AA.

### Pair-level WCAG breakdown

Every pair in every matching harmony, counted as **AAA pairs (>= 7:1)**, **AA pairs (>= 4.5:1)** and **Below AA**.

### Visible harmonies where every pair passes AA

Up to 24 cards whose colours all reach 4.5:1 against each other. They work like grid cards. If there are none, the card says **No full-AA harmonies here**.

> **Tip:** Harmonies where every pair passes are rare because every colour then has to sit at a very different lightness. Most harmonies with a text-safe pair have one very light and one very dark member; filter by **Family** or search a scheme and look for **Has any AA pair**.

## Stats tab

Six histograms:

| Card | Range | Bands |
| --- | --- | --- |
| **Avg lightness (OKLCH L)** | 0 to 1 | 10 |
| **Avg chroma (OKLCH C)** | 0 to 0.30 | 10 |
| **Hue spread** | 0° to 360° | 12 |
| **Min pair contrast** | 1:1 to 12:1 | 11 |
| **Adherence** | 0 to 1 | 10 |
| **Colors per harmony** | 2 to 8 | 6 |

Values beyond a range are counted in the last band.
