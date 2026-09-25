---
title: Material Lighting (Material Under Light) — Limits and accuracy
description: What Material Under Light takes from published sources, what is its own, how precise it is, and what it is not.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Limits and accuracy

## What the tool is

A spectral appearance bench for learning and exploration: one light, one flat material, one geometry, computed wavelength by wavelength. It is not a production renderer, a lighting-design certification tool or a colour-rendering meter.

## The data register, in plain terms

| Entry | Status | What it means for you |
|---|---|---|
| CIE 1931 2° standard observer | Verbatim | The published 10 nm table, unaltered; every other 5 nm sample is interpolated |
| CIE D-series eigenvector basis | Verbatim | D50, D55, D65, D75 and chosen daylights land within 0.0003 of their published chromaticities |
| sRGB primaries and transfer curve | Verbatim | The swatch uses the published sRGB definition, un-adapted |
| CIEDE2000 colour difference | Verbatim | Every ΔE₀₀ uses the full formula, against the light's own white |
| JzAzBz | Verbatim | The published constants |
| Planck's radiation law | Verbatim | Every blackbody is computed at the 81 samples |
| GGX microfacet distribution | Verbatim | The published form, including Smith masking |
| The other four reflectance lobes | Verbatim | Beckmann, Ward, Ashikhmin-Shirley and Oren-Nayar in their published forms |
| Correlated colour temperature | Computed | McCamy's formula, with error bands measured for the whole chain (±11 to ±18 K below 7000 K) |
| The reference illuminant for a source | Computed | The CIE 13.3 selection rule only, not the index built on it |
| Rendering shift | Computed | A colour difference for one material; never a property of the lamp |
| Exposure normalisation | Computed | A white diffuser in the same light and geometry reads Y = 1 |
| Illumination and view geometry | Computed | From the three angle controls, with the normal fixed vertical |
| The twenty pigment reflectances | Stand-in | Invented curves; loading a measured file makes this Verbatim |
| The sensitivity sweep | Stand-in | A perturbation the tool chooses, not repeat measurements |
| CIE colour rendering index | Absent | Withdrawn; needs the fourteen measured test colours and the specified colour space |
| TM-30 Rf and Rg | Absent | Withdrawn; needs 99 samples, CAM02-UCS and a gamut-area calculation |

## Precision

- 81 samples, 380–780 nm at 5 nm. Narrow emission lines (such as fluorescent or LED spikes) can fall between samples, and light outside 380–780 nm is ignored.
- The observer is interpolated from 10 nm to 5 nm.
- The CCT error bands are those in [Compare with the reference light](../docs/compare-with-the-reference.md).
- Clipped colours are flagged; L\*a\*b\*, Jz and ΔE₀₀ are computed before clipping.
- Your own screen is assumed to be sRGB.

## Model limits

- One light, one surface, no shadows, inter-reflections, subsurface depth, transparency or fluorescence.
- Refractive index is a single number for all wavelengths, and a conductor's Fresnel term is fixed at full reflectance, with its colour coming from the reflectance curve.
- The Ashikhmin-Shirley lobe is used in its isotropic form; Oren-Nayar in its qualitative approximation.
- The sphere is a preview seen head-on; the view angles apply to the readouts, not to the sphere.
- There are no fluorescent or LED illuminants.

## What the tool does not do

- It does not score light sources (no CRI, no TM-30).
- It does not compare two materials side by side for metamerism.
- It does not measure real materials; it uses invented curves unless you load a measured file.
