---
title: Color Science Lab — Limits and accuracy
description: What the Color Science Lab computes with published formulas, which previews are illustrative, and what it cannot do.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Limits and accuracy

## Computed with published formulas

- **Workbench**: sRGB decoding, CIE XYZ (D65, 2°), adaptation with the published Bradford, CAT02 and CAT16 matrices, Lab and LCh against the chosen white (with separate white points for the 2° and 10° observers), Oklab and Oklch, and gamut checks with the published matrices for sRGB, Display P3, Adobe RGB and Rec. 2020.
- **Compare**: CIEDE2000 written out in full, CIE94, CIE76 and Oklab distance.
- **Gamut audit** and **Illuminants**: the same matrices and CIEDE2000.
- **Panels**: the **Sample coordinates**, **Result coordinates** and the colour-space dossier come from a colour-space engine that implements each of the 63 spaces' conversions. The **Chromatic Adaptation** tools' Result colour uses real adaptation matrices, scaled by **Experiment strength**.

## Illustrative, not full models

In the panels of the Spectral, Appearance, Perceptual, Color Spaces, Theory and Rendering domains, the **Result** swatch (and the metrics derived from it, such as **dE76 after model**) is an illustration of the direction and size of the named model's effect, controlled by **Experiment strength**. It is not the output of a full implementation of CIECAM16, ICtCp, ACES or the other models named. The same applies to the Catalogue Compare matrix and the Heat Map's analysis-depth score, which is the lab's own rating.

Use the coordinate readouts and the four computed views for figures; use the illustrative previews to explore ideas.

## Inputs and precision

- Every input is an 8-bit sRGB colour. The lab cannot take spectral data, measured XYZ or out-of-sRGB values.
- Displayed values are rounded (two to four decimals).
- The CMYK row is a naive formula with no press profile.
- Colours drawn on screen depend on your display; they are not calibrated.

## What the lab is not

- Not a spectrophotometer or colour-management system.
- Not a substitute for spectral analysis when predicting metamerism: adaptation of an RGB colour does not capture how two real surfaces with different spectra behave.

## Related

- [The Workbench](../docs/workbench.md)
- [Privacy](privacy.md)
