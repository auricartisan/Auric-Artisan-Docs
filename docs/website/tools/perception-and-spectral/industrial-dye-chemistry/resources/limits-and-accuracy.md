---
title: Industrial Dye Chemistry (Dye in Solution) — Limits and accuracy
description: What Dye in Solution takes from published sources, what is its own, how precise it is, what it does not hold, and what it cannot tell you about safety.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Limits and accuracy

## What the tool is

A spectral model of a dye bath for learning and exploration. The physics and colorimetry follow published standards; the dyes are the tool's own inventions unless you load measured spectra. It is not a formulation system, a spectrophotometer, a fastness tester or a safety tool.

## The data register, in plain terms

| Entry | Status | What it means for you |
|---|---|---|
| CIE 1931 2° standard observer | Verbatim | Colours use the published 5 nm observer table, with no interpolated samples |
| CIE D-series eigenvector basis | Verbatim | D65 and D50 are reconstructed from the published daylight basis and land within 0.0003 of their published chromaticities |
| sRGB primaries and transfer curve | Verbatim | The swatch and gamut flag use the published sRGB definition |
| CIEDE2000 colour difference | Verbatim | Every ΔE₀₀ uses the full CIE 142-2001 formula |
| The Beer–Lambert law | Verbatim | Absorbance is ε × c × l, additive over dyes and forms, flagged above A = 1 |
| Henderson–Hasselbalch | Verbatim | The base fraction follows the standard relation |
| The two-species absorbance | Computed | Each dye is two forms weighted by pH, which is what produces an isosbestic point |
| The isosbestic point | Computed | Located precisely between samples, with a strength |
| Dominant wavelength and excitation purity | Computed | A proper chromaticity construction from the light's white point, with purples flagged |
| Colour inconstancy index | Computed | ΔE₀₀ for one bath between two lights; not a metamerism index |
| Special metamerism index | Computed | Described in the register; no control uses it in the current interface |
| The absorption band shape | Stand-in | Preset bands are Gaussians; real bands are asymmetric; loading a measured spectrum makes this Verbatim |
| The six dye presets | Stand-in | Plausible constants for classes of dye, never a named substance |
| The default sweep tolerances | Stand-in | ±2% concentration, ±0.1 mm path, ±5% ε are the tool's guess; replace them with yours |
| Kubelka–Munk on an opaque substrate | Stand-in | Described in the register; no cloth mode is offered in the current interface |
| The CIE fluorescent illuminants | Absent | F11 and the other F-series lights are not held and not imitated |
| Colourfastness and content testing | Absent | ISO 105-B02, ISO 105-C06, AATCC TM 61 and ISO 14184-1 are physical laboratory tests |
| GHS classification and PPE compliance | Absent | The page holds no hazard data; see Safety below |

## Precision

- The spectrum has 81 samples, 380–780 nm at 5 nm. Features narrower than about 10 nm are not resolved, and light below 380 nm or above 780 nm is ignored.
- Beer–Lambert is flagged, not corrected: above A = 1 the numbers are the law's, and a real solution would absorb less.
- Gaussian bands put the peak position and height about right and the wings wrong. Mixtures, whose colour depends on where bands overlap, are affected most.
- The swatch is limited to what sRGB can show; **Inside sRGB** says when it is clipped. L\*a\*b\* values are not clipped.
- Your own screen is assumed to be sRGB.

## What the tool does not do

- It models dye in solution, not on cloth, paper or other substrates.
- It does not compare two baths for metamerism in the current interface.
- It offers no fluorescent illuminants.
- It performs no fastness, wash or formaldehyde testing.
- It does not account for temperature, ionic strength, solvent, dye aggregation or fluorescence.

## Safety

This page models what a dye does to light. It holds no toxicological data, and a λmax and a molar absorptivity say nothing about toxicity. GHS hazard classification belongs to each substance, from its own data, and is published on the supplier's safety data sheet (section 2 for the classification, section 8 for exposure controls and personal protective equipment). The page's **Safety** tab also lists what always applies: gloves, eye protection and a lab coat for any dye work; reading the SDS before opening a container; and disposing of dye liquor through the waste stream your institution specifies. An earlier version of the page assigned hazard levels by chemical class and blocked exports until boxes were ticked; that gate was withdrawn.
