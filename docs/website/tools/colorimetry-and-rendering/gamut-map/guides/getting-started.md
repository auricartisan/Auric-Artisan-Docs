---
title: Gamut Mapping — Getting started
description: Open the Gamut Mapping lab, learn its tabs, and read a CIELAB gamut slice.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Getting started with Gamut Mapping

## Open the lab

Go to https://auricartisan.com/tool/general/colorimetry/gamut-map/. The heading is **Gamut Mapping**. Everything is computed in your browser.

## Key ideas

- **CIELAB** describes a colour by lightness **L\*** (0 black to 100 white) and two opponent axes, **a\*** (green to red) and **b\*** (blue to yellow). **Chroma C\*** is the distance from the grey axis and **hue h°** the angle around it.
- A **gamut slice** is a cut through CIELAB at one L*. Seen from above, each RGB space's gamut at that lightness is an irregular shape around the grey centre. Colours outside the shape cannot be represented in that space.
- A colour is **out of gamut (OOG)** for a space when converting it to that space's linear RGB gives a channel below 0 or above 1.
- Each space has its own **transfer function** (the curve between stored values and light) and **white point**. The lab decodes a HEX value with the source space's own curve, and draws the slice on the source space's white.

## A tour of the screen

| Tab | What it is for |
| --- | --- |
| **Lab** | Choose the colour, spaces, method and slice, and see the mapping |
| **Boundary** | Boundaries of up to five spaces at five lightness levels, and volumes in CIELAB |
| **Methods** | The four mapping methods explained, with figures on the base colour or 12 probe colours |
| **Data** | The nine datasets the lab uses and their status |
| **Export** | PNG, JSON, a link to the exact state, and batch mapping |
| **Reference** | Standards, formulas, citations and research notes with a filter |

### The Lab tab

The left panel groups the controls: **Base Colour**, **Lightness Slice L\***, **Colour Spaces**, **Method**, **Compression Strength**, **Sampling**, **Overlays** and **ΔE Playground**.

The right side, **Gamut Mapping Results**, shows:

- **Source Slice** — every colour inside the source gamut at the chosen L*, drawn as an a*b* disc (a* across, b* up, both from −128 to +128);
- **Mapped to Target** — the same colours after mapping into the target;
- a statistics line with the slice areas and their ratio;
- a line naming the transfer function, the Lab white and the method;
- **Probe Point** — details of the point you last clicked;
- **Before / After (12 Test Colours)** — twelve vivid colours before and after mapping.

## Read your first slice

1. Keep the defaults: base colour `#247DEB`, L* 65, source **sRGB / Rec.709**, target **Display P3**.
2. Look at the **Source Slice**. The filled region is sRGB at L* 65. The thicker outline is the source boundary; the thinner outline (with **Mark out-of-gamut in source** on) is the target's boundary, so you can see where P3 extends beyond sRGB.
3. Select **Swap Source & Target**. Now the source is Display P3 and the target sRGB. The filled region grows, and the sRGB outline sits inside it.
4. Look at **Mapped to Target**. Colours outside sRGB have been pulled inside its boundary.
5. Click near the edge of the source slice. **Probe Point** shows L*, a*, b*, C*, h°, an sRGB value and HEX, and whether the point is in each space ("Yes" or "OOG").
6. Move **Lightness Slice L\*** from 20 to 90 and watch the boundaries change shape.

The slices are painted in sRGB so your screen can show them. Colours outside sRGB are displayed clipped, even though the geometry is correct.

## Next steps

- [Map a colour into a smaller gamut](map-a-colour.md)
- [Compare spaces and methods](compare-spaces-and-methods.md)
- [Map a list of colours](map-a-colour-list.md)
