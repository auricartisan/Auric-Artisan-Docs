---
title: Gamut Mapping — Glossary
description: Plain-language definitions of the terms used in the Gamut Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Mapping glossary

**a\*, b\*** — the two opponent axes of CIELAB: a* runs green to red, b* blue to yellow.

**Adobe RGB (1998)** — a D65 space with a greener green primary than sRGB, encoded with a power of 563/256.

**Bisection** — finding a boundary by repeatedly halving an interval. The lab finds each gamut boundary this way along 360 hue directions.

**Bradford transform** — a chromatic adaptation transform used to move colours between white points.

**C\* (chroma)** — distance from the grey axis in CIELAB: how vivid a colour is.

**CIELAB** — a colour space with lightness L* and axes a* and b*, designed so equal distances are roughly equal perceived differences.

**Clipping** — forcing each out-of-range RGB channel to 0 or 1.

**Display P3** — a D65 space with the DCI-P3 primaries and the sRGB curve, used on many modern devices and in CSS Color 4.

**ΔE (delta E)** — a colour difference. ΔE*76 is plain distance in CIELAB; ΔE*94 and ΔE₀₀ (CIEDE2000) weight lightness, chroma and hue to match perception better.

**Gamut** — the set of colours a space or device can represent.

**Gamut boundary** — the edge of a gamut. On a slice it is a closed outline around the grey centre.

**Gamut mapping** — choosing what an out-of-gamut colour becomes in the target space.

**Gamut volume** — the size of a gamut in CIELAB, in units cubed.

**Halton sequence** — a low-discrepancy sequence of points that covers an area more evenly than random points.

**h° (hue angle)** — the angle around the grey axis in CIELAB.

**ICC rendering intent** — one of four ways an ICC colour-management system converts colours: perceptual, relative colorimetric, saturation and absolute colorimetric.

**L\* (lightness)** — CIELAB lightness, from 0 (black) to 100 (white).

**Monte Carlo estimate** — an estimate made from random samples, reported here with its standard error.

**OOG (out of gamut)** — outside the gamut of a given space.

**ProPhoto RGB (ROMM RGB)** — a very wide D50 space whose primaries include imaginary colours; encoded with a power of 1.8 and a linear toe.

**Rec. 2020 (BT.2020)** — the ultra-high-definition television space with near-spectral primaries.

**Slice** — a cut through CIELAB at one lightness.

**sRGB** — the standard web and display space (IEC 61966-2-1), with D65 white and a piecewise transfer curve.

**Standard error (SE)** — the typical size of the error in an estimate.

**Stratified sampling** — dividing the area into cells and placing one random point in each.

**Transfer function** — the curve between stored code values and linear light.

**White point** — the reference white a space is defined against: D65 or D50 here.
