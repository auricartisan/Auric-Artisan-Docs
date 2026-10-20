---
title: Quick Converter — Convert a colour and compare two colours
description: Enter a colour in any common notation and copy it in fourteen formats; compare two colours by ΔE and contrast; check wide-gamut values; see the colour on charts.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Quick Converter

Quick Converter is the fastest way to restate one colour in many notations. Paste a HEX, RGB, HSL, HSV or OKLCH value and it shows fourteen conversions, each with a copy button, plus the colour's luminance and nearest name. Three more tabs compare the colour with a second colour, show its coordinates in wide-gamut display spaces, and plot it on charts.

Quick Converter is in the **Convert** category at the **Basic** level.

## Open it

In the Workspace view, select **Quick Converter** in **Open a tool**. It opens showing gold (#D3AF37).

## Screen tour

### Sidebar

- A large swatch showing the colour and its HEX code.
- An input box (placeholder *#D3AF37, rgb(…), hsl(…), oklch(…)*), a colour well and a dice button for a random colour.
- **Quick Info**: **Luminance** and **Nearest name**.

### Main area tabs

| Tab | What it shows |
| --- | --- |
| **Convert** | Fourteen notations, each with a copy button. |
| **Compare ΔE** | Two colours side by side with difference and contrast figures and a chart. |
| **Wide Gamut** | Linear coordinates in sRGB, Display P3, Rec.2020 and Adobe RGB, with in-gamut status. |
| **Visualize** | CIE 1931 position, hue wheel, a lightness ramp and a hue ramp. |

## Entering a colour

The input box understands:

- HEX with three or six digits, with or without `#`.
- `rgb(211, 175, 55)` and `rgba(…)` (the alpha value is ignored).
- `hsl(46, 64%, 52%)` and `hsla(…)`.
- `hsv(46, 74%, 83%)`.
- `oklch(76.6% 0.138 91.6)`, with lightness as a percentage or from 0 to 1.

The box converts as soon as its contents form a valid colour, and then rewrites itself as the HEX code. Because of this, typing a value character by character can convert too early (for example, `#D3A` is already a valid three-digit code). Paste complete values, or use the colour well.

The dice button picks a random colour from the whole RGB range.

## The fourteen formats

For #D3AF37 the **Convert** tab shows:

| Row | Example |
| --- | --- |
| **HEX** | `#D3AF37` |
| **RGB** | `rgb(211, 175, 55)` |
| **RGB %** | `rgb(82.7%, 68.6%, 21.6%)` |
| **HSL** | `hsl(46, 64%, 52%)` |
| **HSV** | `hsv(46, 74%, 83%)` |
| **OKLCH** | `76.55% / 0.1385 / 91.55°` |
| **OKLab** | `L 76.55% · a -0.0037 · b 0.1384` |
| **Lab (D65)** | `L 72.75 · a 0.95 · b 62.79` |
| **XYZ (D65)** | `X 0.4289 · Y 0.4479 · Z 0.1000` |
| **CIE xyY** | `x 0.4391 · y 0.4585 · Y 0.4479` |
| **CMYK** | `0, 17, 74, 17` |
| **CSS oklch()** | `oklch(76.6% 0.138 92)` |
| **CSS oklab()** | `oklab(76.6% -0.004 0.138)` |
| **CSS lab()** | `lab(72.8% 0.95 62.79)` |

The three **CSS** rows are ready to paste into a stylesheet. The other rows are readable summaries. Select the copy button beside any row to copy it; **Copied** appears.

What the less familiar notations mean:

- **OKLCH** and **OKLab**: a perceptual colour space. L is lightness, C is chroma (colourfulness), H is hue in degrees; a and b are the green–red and blue–yellow axes.
- **Lab (D65)**: CIE Lab with a D65 (daylight) white point. L runs from 0 to 100.
- **XYZ (D65)**: the CIE 1931 tristimulus values on which the other spaces are built, on a 0 to 1 scale.
- **CIE xyY**: chromaticity (x, y) plus luminance (Y).
- **CMYK**: a simple percentage conversion without an ink or paper profile.

## Tasks

### Convert a colour for a stylesheet

1. Paste your colour into the input box.
2. On **Convert**, select the copy button beside **CSS oklch()**, **CSS oklab()** or **CSS lab()**.

Result: a CSS colour function on your clipboard.

### Compare two colours

1. Open **Compare ΔE**.
2. Set **Color A** with its colour well or HEX box. Color A is the converter's main colour, so this also changes the sidebar and the **Convert** tab.
3. Set **Color B** with its colour well or HEX box. It starts as #1F2A3E.
4. Read the figures:

| Figure | Meaning |
| --- | --- |
| **ΔE 76** | The simple straight-line distance in Lab. |
| **ΔE 2000** | The modern perceptual difference. Around 1 is just noticeable; above about 10 is clearly different. |
| **WCAG ratio** | The contrast ratio and level (**AAA**, **AA** or **Fail** for normal text). |
| **ΔL (Lab)** | Difference in Lab lightness, B minus A. |
| **ΔL (OKLCh)** | Difference in OKLCH lightness, as percentage points. |
| **ΔC (OKLCh)** | Difference in OKLCH chroma. |
| **ΔH** | Hue difference in degrees, the short way round. |
| **Same hue?** | **Yes** when the hue difference is under 10 degrees. |

The chart **Both colors on CIE 1931 chromaticity** marks both colours.

Result: you know how different the two colours look and whether they work as text and background.

### Check wide-gamut values

1. Open **Wide Gamut**.
2. Read the four tiles: **Linear sRGB**, **Display P3 (linear)**, **Rec.2020 (linear)** and **Adobe RGB (linear)**. Each shows three linear channel values and **In gamut** or **Out**.

Because the input is an sRGB colour, it is in gamut for the wider spaces. The tiles are useful for seeing how the same colour is written in each space's linear values. The tab notes that the preview is sRGB-coded.

Result: the colour's coordinates in four RGB spaces.

### See the colour on charts

Open **Visualize**:

- **CIE 1931 chromaticity**: the colour's position.
- **Hue wheel (OKLCh hue)**: its hue.
- **All shades (L 0→1 at fixed C, H)**: a strip from black to white keeping the colour's chroma and hue.
- **All hues (H 0→360 at fixed L, C)**: a strip around the hue circle keeping the colour's lightness and chroma.

Colours that fall outside sRGB in the strips are clipped to the nearest displayable colour.

## Quick Info

- **Luminance**: WCAG relative luminance, 0 to 1, four decimals.
- **Nearest name**: the closest of 64 built-in colour names, with its HEX code and ΔE2000 distance, for example `Auric Gold (#D3AF37) ΔE 0.00` for the starting colour, because Auric Gold is one of the built-in names.

## Save to and restore from the Library

With Quick Converter focused, **Save to Library** saves the colour with all its formats. A saved converter item reopens in Quick Converter and **Loaded color from library** appears.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Input box | Sets the colour from text. | HEX, rgb(), rgba(), hsl(), hsla(), hsv(), oklch() | #D3AF37 |
| Colour well | Sets the colour with the browser's picker. | Any sRGB colour | #D3AF37 |
| Dice | Random colour. | Any RGB value | — |
| Copy buttons (Convert) | Copy one notation. | 14 rows | — |
| **Color A** well and HEX box | Sets the main colour from the Compare tab. | HEX | #D3AF37 |
| **Color B** well and HEX box | Sets the comparison colour. | HEX | #1F2A3E |
| Tabs | Switch the main area. | Convert, Compare ΔE, Wide Gamut, Visualize | Convert |

## Accuracy and limits

- Conversions start from 8-bit sRGB and use the standard sRGB, CIE and OKLab formulas with a D65 white point.
- Values are rounded for display; copying gives the rounded text shown.
- The Lab conversion here does not adapt to a D50 white point, so its numbers can differ slightly from tools that report Lab relative to D50 (as CSS `lab()` formally does).

## Related

- [Panel tools](README.md)
- [Color Picker](colour-picker.md)
- [Color Space Converter](../colour-tools/colour-space-converter.md), which covers more than thirty colour spaces
- [Import, export and the Library](../import-export-and-library.md)
