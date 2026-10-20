---
title: Auric Artisan Icon Hub — Shape the output
description: Set icon size, colour and stroke width in Icon Hub, and use the custom colour picker with contrast tools.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Shape the output

Expand **Shape the output** ("Size, color and stroke"). The controls apply to the previews and to everything you insert, copy, save or export.

| Control | Effect | Range |
| --- | --- | --- |
| **Size** | Width and height of the output, in pixels. | 8 to 512 |
| **Color** | The icon colour. Until you choose one, artwork uses `currentColor` and follows the editor's text colour. | Any colour |
| **Stroke** | Stroke width for artwork drawn with strokes. | 0.5 to 4 |

Stroke only affects stroke-based artwork. It does not turn filled glyphs into outline icons.

These controls are for the current session. To change the starting values permanently, set `auricIconLib.size` (default 24), `auricIconLib.color` (default `currentColor`, or a six-digit hex colour) and `auricIconLib.strokeWidth` (default 2).

## The colour picker

Select the **Color** swatch to open the Auric colour picker. It includes:

- a colour spectrum;
- colour-space inputs;
- named colours;
- recent choices;
- shade ramps;
- harmonies;
- WCAG and APCA contrast checks against a background you choose, with tools to adjust towards AA or AAA;
- an eyedropper, where the host supports it.

The swatch tooltip reads "Icon colour {hex} — contrast, ramps and harmonies included".

## Result

Previews and output use your size, colour and stroke, so what you insert matches what you saw.
