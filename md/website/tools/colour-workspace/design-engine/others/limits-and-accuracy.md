---
title: Design System Generator — Limits and accuracy
description: What the Design System Generator calculates, how reliable the audit and score are, and where the output stops.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Limits and accuracy

## What is calculated

- Colours are built in OKLCH and converted to sRGB HEX codes. Steps outside sRGB have their chroma reduced by search until they fit, so no channel is clipped.
- Contrast ratios use the WCAG 2.x relative-luminance formula. Translucent tokens are blended over the surface beneath them before measuring.
- APCA values come from a compact implementation of the APCA formula. APCA is still a draft for WCAG 3, and its values are shown as context, not as a gate.
- Colour-vision previews use simple matrix simulations of deuteranopia, protanopia and tritanopia.

## What the audit covers

- Twelve pairings per theme: eight role pairings and the four semantic solids with their labels, each against the requirement for its content.
- A matrix of every foreground role against every surface role.

It does not cover your layout, font sizes and weights in use, text over images, focus rings on coloured backgrounds, hover and disabled states, or any accessibility requirement beyond colour contrast.

## What the score means

The score (40 to 100) blends accessibility (55), vibrancy (18), headroom (15) and hierarchy (12), from the light roles only. It is a heuristic for comparing systems, not a quality grade or a compliance result.

## What the generator does not do

- It does not know your brand, your audience or your competitors. The page's own note: *Generated, not designed.*
- Font pairings and icon families are chosen from fixed lists by tag matching.
- Token names are structural (for example `primary-600`, `space-4`). Rename them to your product's vocabulary if you prefer.
- Preview settings in the component playground are never saved, shared or exported.
- Export formats differ in coverage; see [Export tokens](../docs/export-tokens.md).
- Shared links, saved systems and your last visit do not restore the ramp shape or token naming.

## Previews depend on the network

Font specimens need the Auric font CDN or Google Fonts, and the real icon families need the Auric icon CDN. Without them the previews use system fonts and built-in icons. The tokens are unaffected.

## Related

- [Check contrast with the audit](../docs/contrast-audit.md)
- [Privacy](privacy.md)
