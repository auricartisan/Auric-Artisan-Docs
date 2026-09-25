---
title: Auric Color — Limits and accuracy
description: What Auric Color's colour engine and contrast checks measure, how accurate they are, and what they cannot see.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Auric Color limits and accuracy

## What is accurate

- **Colour conversions** read every CSS Color 4 and 5 syntax and write back to exactly the same colour in the token's own format.
- **Contrast ratios** use the WCAG 2.x formula; verdicts use the exact ratio, and a ratio just under a target is never shown rounded up to it.
- **APCA** uses APCA-W3 0.0.98G and matches that algorithm's published test values.
- **Colour difference** (CIEDE2000) matches all 34 published Sharma test pairs.
- **Colour-vision simulation** uses the Brettel 1997 method in linear light.
- **Translucent colours** are blended the way browsers blend them (8-bit alpha).
- **Contrast scanning** agrees with Chromium's rendering in 62 of 68 cases on the audit set used in development; the other six are deliberately skipped.

## What it cannot see

- Colours set by JavaScript at runtime, or by classes defined in another file.
- Which rule wins between two different selectors, inherited or computed values, pseudo-elements and component states.
- Text over images or gradients, gradient-clipped text and `currentColor` backgrounds.
- The rendered font size, so verdicts name the WCAG check rather than a size.
- Tailwind utility classes, integer colour literals such as `0xFF00FF`, and colours built from variables in other languages.

## What it is not

- Colour-vision simulations are previews for design decisions, not a diagnosis.
- APCA results are experimental and not a WCAG 3 conformance claim.
- A clean contrast check does not mean the page is accessible; many criteria need manual review.

## Size limits

- Files larger than 1 MB are not decorated or checked.
- Up to 5,000 colours per file get swatches.

For the full engine description, see the [Studio limits and accuracy page](../../others/limits-and-accuracy.md).
