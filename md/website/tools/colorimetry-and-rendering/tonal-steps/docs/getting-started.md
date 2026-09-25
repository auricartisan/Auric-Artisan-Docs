---
title: Tonal Steps — Getting started
description: Open Tonal Steps, learn its tabs, and build and read your first ramp.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Getting started with Tonal Steps

## Open the tool

Go to https://auricartisan.com/tool/general/gamut-and-rendering/tonal-steps-tints-shades/. The heading is **Tonal Steps**. Everything runs in your browser.

## Key ideas

- A **ramp** is a sequence of colours from light to dark built from one base colour.
- A **tint** is a colour mixed with white, a **shade** mixed with black, and a **tone** mixed with grey.
- **Relative luminance (Y)** is the physical brightness of a colour on a 0 (black) to 1 (white) scale. WCAG contrast ratios are calculated from it.
- **OKLab L** is a perceptual lightness from 0 to 1 (Ottosson, 2020): equal steps in it look roughly equally spaced. The tool uses it to show where your steps fall.
- **WCAG 2.2 contrast** is a ratio from 1:1 to 21:1 with thresholds of 3, 4.5 and 7. **APCA Lc** is a signed contrast value from the APCA-W3 0.1.9 algorithm; its sign shows which colour is lighter.

## A tour of the screen

A note at the top explains a correction the tool made: OKLab needs linear sRGB as input, and the page now provides it.

| Tab | What it is for |
| --- | --- |
| **Lab** | Build the ramp and see its steps, lightness chart, base colour details and optional sets |
| **Ramps** | Compare engines, measure evenness, see the ramp in chroma, and build key sets |
| **Contrast** | Every step's WCAG and APCA contrast against a colour you choose |
| **Data** | The eight datasets and formulas the tool rests on, with their status |
| **Export** | Download or copy the ramp, key set, contrast table or link; analyse a list |
| **Reference** | Standards, formulas, citations and notes, and a chromaticity diagram of the ramp |

### The Lab tab

The left panel holds **Base colour** (HEX field, picker and **Random base**), **Ramp engine**, **Mix in**, **Steps**, **Easing γ** and **Also show**.

The right side shows:

- the caption (steps, engine and mixing space) and a base note;
- the ramp as one strip;
- one row per step: swatch, HEX, OKLab L and contrast against white;
- four statistics: **Base OKLab L**, **Largest step**, **Smallest step** and **Evenness**;
- **Where the steps fall** — a chart of OKLab L across the ramp;
- **Base colour** — HEX, RGB, HSL, L\*a\*b\*, LCh, OKLab L, Y (luminance), and contrast against white and black with ratings;
- **The other sets**, when you tick any under Also show.

## Build your first ramp

1. Type `#2563EB` in **Base colour** (it is the default) and press `Enter` or move out of the field.
2. Keep **Ramp engine** on **HSL lightness** and **Steps** at 11.
3. Read the caption: "11 steps, HSL lightness, mixed in OKLab".
4. Read the base note. It says whether your base colour is one of the steps ("step 4") or "not a step". Usually it is not: HSL lightness steps land on 100, 90, 80 … 0, and the base is rarely exactly on one.
5. Read the step rows. The first step is white and the last black.
6. Switch the engine to **Equal luminance**. The steps now fall at equal intervals of relative luminance. In perceived lightness most of them sit in the light half, with a large final jump to black; the **Where the steps fall** chart shows it.
7. Move **Easing γ** above 1. The target luminances fall faster, so more steps land in the darker half and the ramp looks more evenly spaced; below 1 the steps crowd further towards white. Easing applies to the Equal luminance engine and the neutral ladder, not to HSL lightness.

## Next steps

- [Build a ramp](build-a-ramp.md)
- [Make tints, shades, tones and key sets](tints-shades-tones.md)
- [Check contrast](check-contrast.md)
- [Export tokens](export-tokens.md)
