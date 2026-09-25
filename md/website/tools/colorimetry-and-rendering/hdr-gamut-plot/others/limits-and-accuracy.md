---
title: HDR Gamut Plot — Limits and accuracy
description: How far the HDR Gamut Plot's curves, planes, shares and image readings can be trusted.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# HDR Gamut Plot limits and accuracy

## Exact to the standard

- **Primaries and white** of Rec.709/sRGB, Display P3 and Rec.2020.
- **PQ** with the ST 2084 constants written as the standard's exact fractions.
- **ICtCp** matrices, matching BT.2100.
- **HLG** with the BT.2100 system gamma (reference surround).

## Computed

- **Jzazbz** from Safdar et al. (2017), with its own quantiser.
- **Areas and locus shares** by the shoelace formula, divided by the tabulated CIE 1931 2° locus (65 points, 380–700 nm; area 0.33323 in xy against a published 0.334).
- **Tone-mapping operators** with published constants. "ACES Filmic" is Narkowicz's approximation, not the Academy's transform.
- **Image occupancy**, binned at 0.002 in xy.

## This tool's own

- The **dim and bright surround** multipliers for HLG (0.95 and 0.90). They are not in BT.2100 or BT.2390, and readings made with them are marked Adjusted.

## Not available

- **Image luminance.** 8-bit PNG and JPEG files carry no absolute luminance. HDR formats (OpenEXR, or PNG with PQ or HLG and mastering metadata) are not read.
- **The 10° observer.** The option has no effect.

## Current-version caveats

- **Working colour space**, **ICtCp marker** and **Tone mapping operator** do not change the output.
- The image's pixels are measured but not drawn on the diagram.
- The **EOTF comparison** chart is drawn at page load and does not follow the controls.
- The **Convert a list** feature scales each HEX value's channel numbers directly to the chosen luminance when computing ICtCp, without first converting sRGB to linear Rec. 2020 light. Treat its ICtCp figures as illustrative; its CIELAB figures are standard sRGB conversions.
- For the Planes tab, the gamma 2.4 curve's luminance is computed with a 2.2 exponent.
- Charts are drawn in sRGB; the tool does not display HDR images.
