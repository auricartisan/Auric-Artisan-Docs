---
title: Settings panel — Limits and accuracy
description: What the accent contrast readout measures, how precise it is, and other limits of the Settings panel.
product: Website › Site features › Settings panel
updated: 2026-09-25
---

# Limits and accuracy

## The accent contrast readout

- **Formula.** Both rows use the WCAG 2 relative-luminance contrast formula, and the badges use the WCAG 2 thresholds (7:1, 4.5:1, 3:1).
- **Accent on background** compares your accent with the background colour of the page you are on, read from the page itself. On a page with a coloured or image background under a particular block, the real contrast in that block can differ.
- **Text on accent** compares your accent with the text colour the site places on it. The site chooses between a very dark and a very light text colour, whichever gives more contrast.
- **Precision.** Ratios are shown to two decimal places. Colours are treated as sRGB with no transparency.
- The readout is a guide for choosing an accent, not a certified accessibility audit. For a full check of a page, use the Analyzer or the Contrast Checker tools.

## The shade strip

The seven shades are three darker steps, your accent itself in the middle, and three lighter steps, made by mixing the accent towards black or towards white in sRGB. They are not a perceptual (OKLCH) ramp; use the site's shade and design tools for that.

## Storage and scope

- Settings are kept per browser and per device. They are not synced to your account.
- A private window starts from the defaults and forgets its changes when it closes.
- Saved colors holds at most 18 colours.
- The language setting is kept separately from the other settings and is not in the exported file.
