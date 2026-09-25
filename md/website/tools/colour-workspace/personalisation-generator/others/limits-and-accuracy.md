---
title: Personalization Generator — Limits and accuracy
description: What the Personalization Generator's scores, contrast checks, colour-vision checks and previews can and cannot tell you.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Limits and accuracy

## The score is a ranking, not a verdict

A palette's score says how well it fits your settings: your pool, style chips, use case and weights. It is useful for sorting one sweep's candidates. It does not measure whether a palette is good in general, and scores from sweeps with different settings are not comparable.

## The brief is keyword matching

The brief is not understood as language. Its words are compared with the names of about 80 built-in reference palettes, and even short words such as *a* can match part of a name. The pool, style chips and use case have a much larger effect.

## Contrast and colour-vision are weights, not guarantees

- A palette with weak contrast or poor colour-vision separation is ranked lower, not removed. It can still be kept.
- The three contrast bars on a palette card all show the single best pair in the palette. A palette can have one strong pair and many weak ones.
- The colour-vision check simulates protanopia, deuteranopia and tritanopia. It does not model partial forms (such as deuteranomaly) or achromatopsia, and simulations only approximate what any one person sees.
- With **CVD-safe** off, every palette gets the same fixed colour-vision score.

Always check your final text and background pairs in context, with the WCAG and APCA figures in **UI Pairs** and **Tokens**, and with tools built for accessibility review.

## WCAG and APCA

WCAG ratios follow WCAG 2.1. APCA values are shown as the size of Lc, and the **Use for** labels are general guidance, not a formal conformance result. APCA is not part of WCAG 2.

## Tokens are generated, not designed

Roles are picked by rules (most colourful, least colourful, furthest hue). Status colours are made up near fixed green, amber, red and blue hues when the palette has none. Review every role before using the tokens in a product.

## Fonts are not downloaded

Typography cards, posters and the Studio name font stacks such as *'Playfair Display', Garamond, Georgia, serif*. The page does not load those fonts, so you see whichever font in the stack is installed on your device. Other people may see something different.

## Results are not reproducible

Each sweep uses a new random seed, so the same settings give different palettes each time. Save or download results you want to keep.

## Size and speed limits

| Limit | Value |
| --- | --- |
| Pool | 240 colours |
| Candidates per sweep | 40 to 4,000 |
| Palettes kept | 96 at most, even if **Keep** is set higher |
| Colours per palette | 5 to 12 |
| Derived gradients, UI pairs, posters | top 28 palettes |
| Derived typography | top 24 palettes |

Large sweeps run in small batches so the page stays usable, but they take longer on slower devices.

## Mockups and posters are illustrations

Studio mockups and posters show how colours sit together on typical layouts. They are not working components, and their text is sample copy.

## Related

- [Tune the sweep](../docs/tune-the-sweep.md)
- [Design tokens](../docs/design-tokens.md)
- [Supporting material](README.md)
