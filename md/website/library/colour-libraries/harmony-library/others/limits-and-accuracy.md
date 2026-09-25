---
title: Harmony Library — Limits and accuracy
description: What the Harmony Library's identifier, adherence and contrast figures measure, and what they do not.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Limits and accuracy

## The identifier

- It compares hue only, measured as the HSL hue of each colour. Two palettes with the same hues but very different lightness get the same answer.
- Five schemes cannot be separated by hue (shades, tints and neutral from monochromatic 5; warm cool from complementary; triad shifted from triadic). The page names all of them rather than guessing.
- Very grey colours have an unstable hue: a tiny change in value can swing the hue angle a long way. Identifying a palette of near-greys gives an unreliable answer.
- It only compares schemes with the same number of colours as you entered.
- The fit bands (0.85 and 0.65) are guides for how deliberate a pattern looks, not rules of colour theory.

## The collection

- Colours are generated in HSL from each scheme's rule and a base colour whose saturation is between 45% and 95% and lightness between 35% and 80%. HSL hue steps are not perfectly even to the eye, which is one reason adherence varies.
- The **Base hue** filter uses the harmony's overall hue (a weighted average of its colours' OKLCH hues), which can differ from the base colour's own hue.
- Scheme descriptions are the page's short summaries of common colour-theory practice, not formal definitions.

## Contrast

Pair contrast uses the WCAG 2 formula. It is one requirement for readable text among several; size, weight and context matter too.

## Your screen

Swatches look different on different displays; the values do not change.
