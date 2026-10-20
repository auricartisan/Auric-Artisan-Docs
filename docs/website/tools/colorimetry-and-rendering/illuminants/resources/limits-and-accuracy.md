---
title: Illuminants — Limits and accuracy
description: Which Illuminants readings are standard values, which rest on stand-ins, and what the lab does not compute.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Illuminants limits and accuracy

The lab is a reference calculator that runs in your browser. It is not calibrated measurement software and not a substitute for official CIE or IES tools. This page says what each kind of reading rests on.

## Standard values you can rely on

| Reading | Rests on | Notes |
| --- | --- | --- |
| x, y, XYZ of A, D50, D55, D65, D75, E and blackbody sources | CIE 1931 2° colour matching functions (verbatim, 5 nm, 380–780 nm) | The D series is reconstructed from the verbatim daylight basis and lands on the published chromaticities to better than 0.0003 |
| CCT and Duv | Ohno's method over a Planckian locus computed through the same observer | Reported as valid only for 1,000–100,000 K and Duv within ±0.05 |
| Chromaticity in xy, u′v′ and uv | Exact conversions | — |
| Chromatic adaptation matrices | Published Bradford, CAT02, CAT16, HPE and Sharp matrices | XYZ scaling is included as the simplest case, not as a model of vision |
| Dominant wavelength and purity | The spectral locus of the 2° observer, from the D65 white | Undefined (shown as a dash) when the light is almost white |
| Monte Carlo uncertainty | JCGM 101:2008 method | Only as good as the budget you enter; inputs are treated as uncorrelated |

## Readings that rest on stand-ins

| Reading | Why it is not a standard value |
| --- | --- |
| Anything for F1 to F12 (spectrum, x, y, CCT, CRI) | The CIE fluorescent tables are not held; the spectra are smooth stand-ins and the mercury lines are not in the right places |
| CRI Ra and R1 to R14 | The 14 CIE 13.3 test colour samples are approximations |
| Metamerism index | Uses the same approximate test samples |
| Surface appearance | Uses eight simple educational reflectance curves, not measured materials |

The lab labels these wherever they appear ("stand-in", "not a standard value").

## Not computed at all

- **IES TM-30** (Rf, Rg and the colour vector graphic): the 99 colour evaluation samples are not held.
- **CIE S 026 α-opic quantities** (melanopic EDI and related ratios): the action spectra are not held.
- **The CIE 1964 10° observer**: its colour matching functions are not held.
- **MacAdam ellipses**: the measured ellipse parameters are not held.
- **CIE FL3, HP and LED illuminant families**: their tables are not held.

## Precision notes

- The Lab tab integrates at 5 nm over 380–780 nm. The source tables are tabulated at 5 nm (the daylight basis at 10 nm), so choosing 1 nm on the Methods tab does not add information; the Methods tab shows the deltas so you can see this.
- The sRGB swatches and HEX values are display previews. A white point shown as a swatch is not a calibrated target.
- Summary figures are rounded for display (CCT to the nearest kelvin, x and y to five decimals, Duv to five decimals).
- The kelvin values in the illuminant list are nominal labels; the computed CCT can differ slightly.
