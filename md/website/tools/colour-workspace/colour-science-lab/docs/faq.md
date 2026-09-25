---
title: Color Science Lab — FAQ
description: Short answers to common questions about the Color Science Lab.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Science Lab FAQ

## Are the numbers accurate enough for research?

The Workbench, Compare, Gamut audit and Illuminants views and the panels' coordinate readouts use published formulas (sRGB, CIE XYZ and Lab, Bradford, CAT02, CAT16, CIEDE2000, Oklab). They are exact within 8-bit sRGB input and floating-point rounding. Some panel **Result** previews are illustrations, not full model outputs. Read [Limits and accuracy](../others/limits-and-accuracy.md) before citing a figure.

## Can I enter spectral data or measured values?

No. Every input is an sRGB colour. The lab does not accept spectral reflectance or measured XYZ.

## Why does a HEX colour always show "inside" sRGB?

A HEX code is an sRGB colour by definition. The useful figure is the headroom, which the Gamut audit reports.

## What is the difference between the Catalogue's Compare and the Compare view?

The **Compare** view measures two colours. The Catalogue's **Compare** entry previews several tools on a test palette.

## Do I need an account?

No. Saving panels uses your Auric Artisan Library.

## Does the level switch affect other pages?

Yes. **Basic**, **Advanced** and **Both** follow the site-wide complexity mode, so changing it here changes it on other pages that use it.

## Related

- [Troubleshooting](troubleshooting.md)
- [Getting started](getting-started.md)
