---
title: M-Gradient Palette — Glossary
description: Definitions of the terms used in the M-Gradient Palette.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# M-Gradient Palette glossary

| Term | Meaning |
|---|---|
| APCA | Advanced Perceptual Contrast Algorithm; a lightness contrast measure in Lc units, signed by polarity |
| Chroma | How colourful a colour is, its distance from grey; in OKLCH, the C value |
| CIEDE2000 (ΔE₀₀) | The CIE's standard formula for how different two colours look |
| CIELAB | A colour space of lightness and two colour axes; used here only to compute ΔE₀₀ |
| Clipping | Forcing each channel into 0 to 255 separately, which also shifts hue; not used by this tool |
| Colour-vision deficiency | Reduced ability to tell some colours apart; simulated here as full protanopia, deuteranopia or tritanopia |
| Contrast ratio | The WCAG 2 measure of luminance difference, from 1:1 to 21:1 |
| Custom property | A CSS variable such as `--ramp-01`, holding one step's colour |
| Deutan | Deuteranopia: no working medium-wavelength (green) cones |
| Easing | A curve that decides where along the route the steps land |
| Evenness | The standard deviation of the differences between neighbouring steps; lower is more even |
| Gamut | The range of colours a space or device can show |
| Gamut mapping | Bringing an out-of-range colour back inside, here by reducing chroma at fixed lightness and hue |
| HSL | Hue, saturation and lightness: a cylinder built from sRGB |
| Hue route | Short or long way round the hue circle between the two ends |
| Interpolation | Choosing colours part of the way between two others |
| Lc | The unit of APCA lightness contrast |
| Linear RGB | Red, green and blue as amounts of light, without the sRGB curve |
| Long hue | The route round the hue circle that goes the longer way |
| Mean ΔE₀₀ | The average difference between neighbouring steps |
| OKLab | A perceptual colour space published by Björn Ottosson in 2020 |
| OKLCH | OKLab in polar form: lightness L, chroma C and hue H |
| Protan | Protanopia: no working long-wavelength (red) cones |
| Ramp | A row of steps between two colours |
| Relative luminance | The WCAG measure of brightness, from 0 for black to 1 for white |
| Short hue | The route round the hue circle that goes the shorter way, at most 180° |
| sRGB | The standard colour space for web and consumer screens |
| Step | One colour of the ramp |
| Tritan | Tritanopia: no working short-wavelength (blue) cones |
| WCAG | The Web Content Accessibility Guidelines; version 2.2 defines the contrast ratio used here |
