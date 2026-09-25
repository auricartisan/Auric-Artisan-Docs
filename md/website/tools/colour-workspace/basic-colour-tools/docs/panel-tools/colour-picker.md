---
title: Color Picker — Pick one colour and read it every way
description: Pick a colour with a saturation-value plane, hue slider, eyedropper or HEX code, then copy it in eight formats and see harmonies, colour-vision previews, chromaticity and contrast.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Picker

Color Picker is for one colour at a time. You choose the colour with a saturation-value plane and a hue slider, the browser's colour well, a HEX code, a random button or the system eyedropper. The main area then shows the colour in eight notations, eight harmony sets built from it, how it looks under colour-vision deficiencies, where it sits on the CIE 1931 chromaticity diagram, and how well it contrasts with common backgrounds.

The picker works in **HSV** (hue, saturation, value): the hue slider picks the hue, and the square plane picks saturation (left to right) and value, or brightness (bottom to top).

Color Picker is in the **Pick** category at the **Basic** level.

## Open it

In the Workspace view, select **Color Picker** in **Open a tool**.

## Screen tour

### Sidebar

- A colour well and a HEX text box, side by side.
- **Pick** (tooltip **Use OS eyedropper**) and **Random**.
- The saturation-value plane, with a round marker.
- The hue slider, with a bar-shaped marker.

### Main area tabs

| Tab | What it shows |
| --- | --- |
| **Formats** | The colour in HEX, RGB, HSL, HSV, OKLCH, Lab, XYZ and CMYK, each with a copy button. |
| **Harmonies** | Eight rows of colours derived from the current hue. |
| **CVD** | The colour under normal vision and four colour-vision deficiencies, with the difference from the original. |
| **Chromaticity** | The colour on the CIE 1931 diagram and on a hue wheel. |
| **Info** | Key numbers, the closest named colour, and contrast against six backgrounds. |

## Ways to set the colour

| Method | How |
| --- | --- |
| Plane | Press on the plane and drag. Right is more saturated, up is brighter. |
| Hue slider | Press on the slider and drag left or right. |
| Colour well | Select the well and choose a colour in your browser's picker. |
| HEX box | Type a code such as `#1E90FF` and press `Enter` or select outside the box. |
| **Pick** | Opens the system eyedropper so you can sample any pixel on your screen. |
| **Random** | Chooses a random hue with fairly strong saturation and brightness. |
| Harmony swatch | On the **Harmonies** tab, select a swatch to make it the current colour. |

The eyedropper uses the browser's EyeDropper feature, which is available in Chromium-based browsers such as Chrome and Edge on desktop. Where it is missing, **Eyedropper not supported** appears; use the colour well or the HEX box instead.

## Tasks

### Get a colour's CSS in several formats

1. Set the colour with any method above.
2. On the **Formats** tab, select the copy button beside the format you need.

Result: the value is on your clipboard and **Copied** appears. For the colour #D3AF37 the formats read:

| Format | Example |
| --- | --- |
| HEX | `#D3AF37` |
| RGB | `rgb(211, 175, 55)` |
| HSL | `hsl(46, 64%, 52%)` |
| HSV | `hsv(46, 74%, 83%)` |
| OKLCH | `oklch(76.6% 0.138 92)` |
| Lab | `lab(72.8 0.9 62.8)` |
| XYZ | `0.429, 0.448, 0.100` |
| CMYK | `cmyk(0%, 17%, 74%, 17%)` |

Lab is CIE Lab (CIELAB) with a D65 white point. XYZ values are on a 0 to 1 scale (Y = 1 is white). CMYK is a simple device-independent conversion, not a press profile.

### Build a harmony set from one colour

1. Set your base colour.
2. Open **Harmonies**. Each row shows a set of swatches with HEX labels.
3. Select any swatch to make it the current colour. **Applied #HEX** appears and every tab updates.

The rows are computed in OKLCH, keeping the base colour's lightness and chroma and changing the hue:

| Row | Hues or steps |
| --- | --- |
| **Complementary** | Base and base + 180° |
| **Analogous** | Base − 30°, base, base + 30° |
| **Triadic** | Base, + 120°, + 240° |
| **Tetradic** | Base, + 90°, + 180°, + 270° |
| **Split-comp.** | Base, + 150°, + 210° |
| **Square** | Base, + 90°, + 180°, + 270° |
| **Shades (L ramp)** | Five lightness steps (0.18, 0.32, 0.46, 0.60, 0.78) at the base hue and chroma |
| **Tints (C ramp)** | Five chroma steps (0.05 to 0.25) at the base hue and lightness |

**Tetradic** and **Square** use the same four hues here. Colours outside the sRGB range are clipped to the nearest displayable colour.

Result: a related colour set you can walk through one swatch at a time.

### Check a colour for accessibility

1. Open **Info**.
2. Read **Contrast against common backgrounds**: six tiles for **White** (#FFFFFF), **Off-white** (#F5F5F5), **Black** (#000000), **Near-black** (#1A1A1A), **Dark slate** (#0F172A) and **Auric gold** (#D3AF37). Each shows the WCAG contrast ratio and a level: **AAA** (7:1 or more), **AA** (4.5:1 or more) or **Fail**.
3. Open **CVD** to see the colour as simulated for **deuteranopia**, **protanopia**, **tritanopia** and **achromatopsia**. Each tile shows the simulated HEX code and **ΔE2000**, how different the simulated colour is from the original. Larger numbers mean a bigger change.

Result: you know which backgrounds the colour can carry text on and how much it shifts for colour-blind viewers.

## The Info tab

| Item | Meaning |
| --- | --- |
| **HEX** | The current colour. |
| **Luminance** | WCAG relative luminance, 0 (black) to 1 (white), four decimals. |
| **Lab L** | CIE Lab lightness, 0 to 100. |
| **OKLCh L** | OKLCH lightness as a percentage. |
| **Chroma** | OKLCH chroma. |
| **Hue** | OKLCH hue in degrees. |
| **Warm/Cool** | **Warm** for OKLCH hues below 60° or from 300° up, **Cool** from 180° to below 300°, **Neutral** in between. A rough guide only. |
| **Text on** | A **Sample** word in black or white, whichever the tool picks as readable on the colour. |
| **Closest named color** | The nearest of 64 built-in colour names, with its HEX code and ΔE2000 distance. |

## The Chromaticity tab

- **CIE 1931 chromaticity position (sRGB triangle = dashed gold)**: the horseshoe-shaped chart of all colours people can see, with the sRGB range drawn as a dashed gold triangle and your colour marked.
- **Hue wheel position**: your colour's OKLCH hue marked on a hue ring.

## Save to and restore from the Library

With Color Picker focused, **Save to Library** saves the colour with its formats and its harmony colours. A saved colour reopens in Color Picker and **Loaded color from library** appears.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Colour well | Sets the colour with the browser's picker. | Any sRGB colour | — |
| HEX box | Sets the colour by code on `Enter` or when you leave the box. | 3- or 6-digit HEX, with or without `#` | — |
| **Pick** | System eyedropper. | Needs browser support | — |
| **Random** | Random colour. | Saturation 50–100 %, value 40–90 % | — |
| Saturation-value plane | Sets saturation and value. | 0–100 % each | — |
| Hue slider | Sets hue. | 0–360° | — |
| Format copy buttons | Copy one format. | 8 formats | — |
| Harmony swatch | Applies that colour. | 8 rows | — |
| Tabs | Switch the main area. | Formats, Harmonies, CVD, Chromaticity, Info | Formats |

## Accuracy and limits

- Values are computed from 8-bit sRGB, so conversions round to the displayed precision.
- Colour-vision tiles use simple simulation matrices. They show the likely direction and size of the change, not an exact view for any one person.
- The named-colour match uses a short built-in list of 64 names. For larger naming systems, use [Color Name Finder](../colour-tools/colour-name-finder.md) or [Pantone & Named Lookup](../colour-tools/pantone-and-named-lookup.md).
- CMYK here is a formula without an ink or paper profile. For print previews, use [CMYK Soft-Proof](../colour-tools/cmyk-soft-proof.md).

## Related

- [Panel tools](README.md)
- [Quick Converter](quick-converter.md) for fourteen notations and two-colour comparison
- [Color Inspector](../colour-tools/colour-inspector.md), the in-depth single-colour tool of the Colour Tools workbench
- [Import, export and the Library](../import-export-and-library.md)
