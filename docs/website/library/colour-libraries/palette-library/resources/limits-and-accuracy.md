---
title: Palette Library — Limits and accuracy
description: What the Palette Library's scans, samples and figures can tell you, and what they cannot.
product: Website › Library › Colour libraries › Palette Library
updated: 2026-09-25
---

# Limits and accuracy

## Scans and samples

- A filtered browse is a scan from the start of the collection. It shows the matches found so far, not all matches in five million. The counter always states how many palettes were looked at.
- Sorting orders a first stretch of 1,500 palettes (or the matches among them), not the whole collection.
- The **Harmony**, **Accessibility** and **Stats** tabs, and the **Visible page** export, use a sample of up to 2,000 palettes: the first 2,000, or the first matches found in up to 40,000. Percentages describe that sample. Because the sample always starts at the beginning of the collection, it is consistent from visit to visit but is not a random draw from all five million.

## Method labels and measured harmony

Each palette carries a method label (such as `triadic`). The colours are worked out from the palette's number, and the label does not guarantee a particular hue relationship. The **Palette summary** badge and **Hue span** on **Inspect** are measured from the actual colours; rely on those when the relationship matters.

## Contrast

- Contrast ratios use the WCAG 2 formula. They are exact for the colours as sRGB values.
- WCAG 2 contrast is one requirement for readable text. Font size, weight, and the surrounding design also matter. Newer measures such as APCA can rate some pairs differently.
- The ceiling of three mutually legible colours at 4.5:1 is a property of the contrast formula, not of this collection.

## Colour values

- OKLCH and CIE Lab values are standard conversions from sRGB with a D65 white point, rounded for display.
- **DeltaE avg** uses CIE76, which over-states differences between very saturated colours compared with newer formulas.
- The three-word colour names on **Inspect** come from fixed lightness, chroma and hue bands. They are handy descriptions, not standard colour names.

## Your screen

Swatches look different on different displays. The numbers are the same everywhere.

## What it is not

- It is not a palette generator that responds to your input. For that, see the palette tools in [Related](related.md).
- It is not an accessibility audit of a design.
