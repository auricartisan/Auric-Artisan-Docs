---
title: Tone Mapping — Glossary
description: Plain-language definitions of the terms used in the Tone Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tone Mapping glossary

**ACEScg (AP1)** — a linear, wide-gamut working space from the Academy Color Encoding System, with a D60 white.

**Bradford transform** — a chromatic adaptation method used to move colours between white points.

**.cube** — the Adobe Cube LUT file format, used by many grading and video applications.

**Display-referred** — values relative to what a display can show, from 0 (black) to 1 (peak white).

**Dither** — tiny random noise added before quantising to 8 bits, to hide banding.

**EV (exposure value, stop)** — a factor of two in light.

**False colour** — an overlay that paints each pixel by its brightness band instead of its colour.

**Gamut mapping** — handling colours outside the target space: clipping, compressing or scaling them.

**Grade** — creative adjustments after the curve: contrast, saturation, lift, gamma, gain, temperature, tint, hue and vibrance.

**Hable filmic** — a filmic tone curve published by John Hable (2010).

**HLG** — hybrid log-gamma, an HDR transfer function (ARIB STD-B67).

**Histogram** — a count of pixels at each level.

**Lift, gamma, gain** — adjustments that mainly move the shadows, the mid-tones and the highlights.

**LUT (lookup table)** — a table that stores a colour transform. A 1D LUT maps each channel alone; a 3D LUT maps every RGB combination.

**Mid-grey** — scene value 0.18, the usual reference for exposure.

**Narkowicz fit** — a five-constant curve approximating the ACES look (2016).

**OETF** — the encoding curve applied to the output, such as sRGB or PQ.

**Out of gamut (OOG)** — a colour the target space cannot represent: a channel below 0 or above 1.

**PQ** — the perceptual quantiser, SMPTE ST 2084, an absolute HDR encoding up to 10,000 cd/m².

**Reinhard** — the tone curve L ÷ (1 + L) (Reinhard et al., 2002).

**Scene-referred** — values describing light in the scene, which can exceed 1.

**Tone mapping** — compressing scene luminance into the display's range.

**Uchimura (Gran Turismo)** — a tone curve with a toe, a linear section and a shoulder (Uchimura, 2017).

**Vectorscope** — a plot of colour direction and strength.

**Vibrance** — a saturation change weighted towards less saturated colours.

**Waveform** — a plot of brightness across the image, column by column.

**Working space** — the colour space in which the curve and grade are applied.
