---
title: HDR Gamut Plot — Compare broadcast gamuts
description: Compare Rec.709/sRGB, Display P3 and Rec.2020 by area and share of the spectral locus, and measure how much of each an image occupies.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Compare broadcast gamuts

## The three spaces

| Space | Red (x, y) | Green (x, y) | Blue (x, y) | White |
| --- | --- | --- | --- | --- |
| Rec.709 / sRGB | 0.640, 0.330 | 0.300, 0.600 | 0.150, 0.060 | D65 |
| Display-P3 | 0.680, 0.320 | 0.265, 0.690 | 0.150, 0.060 | D65 |
| Rec.2020 | 0.708, 0.292 | 0.170, 0.797 | 0.131, 0.046 | D65 |

All three share the D65 white. The P3 here is Display P3, not the DCI cinema version with its greener white.

## Read the share of the locus

1. On the **Lab** tab, read **Gamut metrics**.
2. **Share of locus** is each triangle's area divided by the area of the spectral locus in the same plane. In CIE 1931 xy the tool measures 33.6% for Rec.709, 45.6% for Display-P3 and 63.6% for Rec.2020.
3. Press `A` or change **Chromaticity axes** to **CIE 1976 u′v′**. The shares change because u′v′ spaces colours more evenly; the u′v′ figures are the fairer comparison.

The often-quoted 35.9%, 53.6% and 75.8% are against a smaller locus area than the one the tool draws. Neither set is wrong; the tool divides by the locus it shows. Its locus is the CIE 1931 2° observer's, tabulated at 65 points from 380 to 700 nm.

## Measure an image's colours

1. Under **Plot an image on it**, select **Drop a PNG or JPEG** and choose an image. Images larger than 1,024 pixels on a side are reduced for analysis.
2. Read the results under the button:
   - **Pixels on the diagram** — the analysed size, how many pixels were sampled and how many distinct chromaticities they contain;
   - **How much of each gamut it occupies** — for each space, the area of its triangle covered by the image's chromaticities (measured in xy, in cells 0.002 wide), as a percentage.
3. A note explains the result. For an ordinary untagged image every pixel falls inside all three gamuts, because such a file is read as sRGB and sRGB sits inside the other two.

**Occupancy** answers "how much of this gamut does the image use?". A grey ramp occupies 0%; a full sweep of the sRGB cube occupies about 99.9% of sRGB, 75.0% of P3 and 53.8% of Rec.2020.

The tool reports no luminance for the image. An 8-bit PNG or JPEG does not record what light its values stood for.

## Compare side by side

Open **Export**. Under **The three spaces, side by side**, a bar chart and table list each space's **Area**, **Share of locus** and **White** in the plane currently on the Lab tab.

## Result

You can state how much of the visible chromaticity range each broadcast gamut covers, in the plane you choose, and how much of each an image actually uses.
