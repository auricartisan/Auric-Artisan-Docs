---
title: LUT Lab — Glossary
description: Definitions of the terms used in LUT Lab.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# LUT Lab glossary

| Term | Meaning |
|---|---|
| 1D LUT | A table mapping each channel on its own, one row per input level |
| 3D LUT | A cube of grid points mapping every combination of red, green and blue to a new colour |
| 8-bit | 256 levels per channel, 0 to 255; the precision LUT Lab works in |
| ACEScct / ACEScg | Encodings from the Academy Color Encoding System for film work; not offered, because they need values above 1 |
| .cube | A plain-text LUT format defined by the Adobe / IRIDAS Cube LUT Specification 1.0 |
| CIEDE2000 (ΔE₀₀) | The CIE's standard formula for the size of a colour difference |
| CIELAB | A colour space of lightness L* and colour axes a* and b*, used here with a D65 white |
| Chroma (C*) | How colourful a colour is in CIELAB, its distance from grey |
| Clipped | A pixel with a channel driven by the transform to 0 or 255 that was not there before |
| Domain | The input range a `.cube` table covers, set by `DOMAIN_MIN` and `DOMAIN_MAX`; 0 to 1 by default |
| Exposure | In the tone-map, the factor the linear scene light is multiplied by before compression |
| Grid point | One of the sampled inputs of a LUT, at which the output is stored |
| Hue sweep | The ring of 72 test colours at L* 60, C* 40 used to measure hue, lightness and chroma shifts |
| Identity | A LUT that changes nothing |
| Interpolation | Estimating the output between grid points by blending the neighbouring points |
| Linear light | Values proportional to physical light, before the sRGB curve is applied |
| Look | A built-in transform in LUT Lab: a stylisation or a defined transform |
| LUT | Lookup table: a list of what each input colour should become |
| Reachable | The share of a table's domain that an 8-bit sRGB input can reach |
| Reinhard tone-map | A tone-mapping operator, L ÷ (1 + L), that compresses bright light smoothly |
| Round trip | Writing a table to a file and reading it back, to check nothing was lost |
| Sample order | The order of rows in a 3D `.cube`: red changes fastest, then green, then blue |
| Size | The number of grid points along each axis of a LUT |
| sRGB | The standard colour space for web and consumer images |
| Strength | How much of a look is blended with the original, 0% to 100% |
| Stylisation | A look designed because it looks good, with no definition to check against |
| Transform | A conversion between two defined things, which can be checked against its definition |
| Trilinear interpolation | Blending the eight grid points around an input along red, then green, then blue |
