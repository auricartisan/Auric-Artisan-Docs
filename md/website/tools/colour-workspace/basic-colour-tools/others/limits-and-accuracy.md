---
title: Basic Color Tools — Limits and accuracy
description: How the colour conversions, contrast checks, colour-vision simulations and scores in Basic Color Tools are calculated, how precise they are, and what they are not.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Limits and accuracy

Basic Color Tools and the Colour Tools calculate everything with published formulas in your browser. The results are good for design decisions and checks. They are not certified measurements, and a few of them are deliberate simplifications. This page says which.

## Colour values

- **Starting point.** Every panel tool works from 8-bit sRGB colours (the HEX codes you see). Values you type in other notations are converted to sRGB first.
- **Out-of-range colours are clipped.** OKLCH, OKLab and Lab can describe colours that sRGB cannot show. When a slider, ramp or harmony asks for one, the tools clip each channel to the displayable range. The HEX code shows the colour you actually get, which can be less saturated than the numbers suggest.
- **Rounding.** Readouts are rounded for display (for example, OKLCH chroma to three or four decimals). Copy buttons copy the rounded text.
- **White point.** Lab, XYZ and xyY use a D65 white point without adapting to D50. Tools that report Lab relative to D50 can show slightly different numbers.
- **CMYK.** The CMYK figures in Color Picker and Quick Converter come from a simple formula with no ink, paper or press profile. Use [CMYK Soft-Proof](../docs/colour-tools/cmyk-soft-proof.md) for a press-aware preview, and a real proof for print decisions.
- **Wide gamut.** Quick Converter's **Wide Gamut** tab shows linear coordinates for Display P3, Rec.2020 and Adobe RGB. The input is always an sRGB colour, and the page cannot show colours beyond sRGB.

## Contrast

- The seven panel tools use the WCAG 2.x contrast ratio: (lighter luminance + 0.05) divided by (darker luminance + 0.05), from 1:1 to 21:1.
- Levels: 4.5:1 is AA for normal text, 7:1 is AAA, 3:1 is AA for large text and for non-text parts such as focus indicators.
- A ratio says nothing about font size, weight or how the colours are used. A passing ratio is necessary for readable text, not a guarantee.
- Some Colour Tools also report APCA, a newer contrast model. APCA is not yet part of a published WCAG standard.

## Colour-vision simulation

- The panel tools simulate **deuteranopia**, **protanopia**, **tritanopia** and **achromatopsia** with simple 3 × 3 colour matrices applied to sRGB values.
- These show the general direction and size of the change. They do not show exactly what any person sees, and they model complete (dichromatic) deficiencies rather than the milder forms that are more common.
- The Colour Tools use their own shared set of filters; see [Accessibility Lab](../docs/colour-tools/accessibility-lab.md).

## Colour difference

- **ΔE 76** is the straight distance in Lab. **ΔE 2000** (CIEDE2000) corrects for how people actually perceive differences and is the one to use. A ΔE 2000 around 1 is just noticeable side by side; above about 10 the colours are clearly different.
- Nearest-name matches in Color Picker and Quick Converter use a short built-in list of 64 names, so the "nearest" name can still be quite far away. Check the ΔE shown with it.

## Generators and scores

- **Palette Studio** modes add random variation, so the same mode gives different palettes each time. The WCAG and accessibility modes search for colours that meet their targets but can fall short; the **WCAG Pairs** tab reports the real result.
- **Image extraction** samples a scaled-down copy of the image (400 pixels on the longest side) and groups colours with k-means from random starting points. Results can differ slightly between runs and will not include colours that cover only a few pixels.
- **Palette Remix** adds random variation controlled by **Remix energy**.
- **Color Battle** scores are a weighted heuristic (contrast 35, AA share 30, ΔE 20, colour-vision ΔE 15). Use them to compare palettes, not as a pass mark.
- **Gradient Maker** imitates OKLCH, HSL, Lab and eased blends with generated stops (20 in CSS, 40 in PNG). The imitation is close but not exact.

## Images

- **Collage Maker** exports at 3,840 pixels wide only when its preview is at least 800 pixels wide. Drop shadows, the checkerboard fade and the tilt of pinboard and polaroid cells show in the preview but not in the export.

## What these tools are not

- Not a colour-management system. The site shows sRGB colours as your screen and browser render them. An uncalibrated screen changes how colours look.
- Not an accessibility audit. Contrast and colour-vision checks cover colour only. For a full review, use the [Accessibility and vision tools](../../../accessibility-and-vision/README.md).
- Not a source of licensed colour-system data. Named-colour matches are approximations.

## Related

- [Glossary](glossary.md)
- [Troubleshooting](../docs/troubleshooting.md)
- [Supporting material](README.md)
