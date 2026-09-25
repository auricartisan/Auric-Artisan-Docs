---
title: Gamut Lab — FAQ
description: Short answers to common questions about the Gamut Lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Lab FAQ

## What is the difference between Display P3 and DCI-P3?

They share primaries. Display P3 uses the D65 white and the sRGB transfer curve; DCI-P3 (the cinema reference projector) uses a greener white at x 0.314, y 0.351 and a pure 2.6 gamma.

## Why do Rec. 2020 and Rec. 2100 have the same triangle?

Rec. 2100 (HDR television) uses the Rec. 2020 primaries and white. It differs in the transfer curve: PQ or HLG instead of the BT.2020 curve.

## Why does the ACES AP0 blue primary sit outside the diagram?

AP0 uses an imaginary blue primary so its triangle contains every visible colour. That makes it suitable for archiving, and it is why its share of the locus reads "> 100%".

## Why is the u′v′ share quoted rather than xy?

Equal distances on the xy diagram are not equal visual differences; it exaggerates greens. u′v′ is more uniform, so areas there compare more fairly.

## Is a bigger triangle always a bigger gamut?

Not exactly. The triangle ignores lightness. CIELAB volume counts how much colour a space holds at every lightness, which is why the lab measures it separately.

## Why does the spectral locus stop at 715 nm?

The lab builds the locus from the published colour matching functions at four decimals. Beyond about 715 nm the values are too small to give a reliable chromaticity, so those points are left out rather than distorting the areas.

## Are the MacAdam ellipses real data?

No. The overlay is an illustrative approximation of MacAdam's (1942) figure, useful for showing that ellipses vary in size and orientation. It is not a basis for reading discrimination thresholds.

## Can the lab convert or map colours between spaces?

No. It defines and measures spaces. Use [Gamut Mapping](../../gamut-map/README.md) to map colours.

## Where are my imported spaces stored?

In your browser's local storage for this site. They stay on this device and browser until you delete them with **Del** or clear site data.
