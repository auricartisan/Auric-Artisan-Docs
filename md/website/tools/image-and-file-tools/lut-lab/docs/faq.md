---
title: LUT Lab — FAQ
description: Short answers to common questions about LUT Lab.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# LUT Lab FAQ

## Are my files uploaded?

No. Your `.cube` and your picture are read in the page and never sent anywhere. See [Privacy](../others/privacy.md).

## Which LUT formats can I use?

Only `.cube`, 1D or 3D, as defined in the Adobe / IRIDAS Cube LUT Specification 1.0. Convert other formats first.

## Will a .cube from LUT Lab work in my editing program?

It is written to the `.cube` specification: `TITLE`, `LUT_3D_SIZE` or `LUT_1D_SIZE`, `DOMAIN_MIN` and `DOMAIN_MAX`, and rows with red changing fastest. Programs that read standard `.cube` files should read it. The looks are designed for ordinary sRGB images, not log camera footage.

## What size should I choose?

33 is a common default. 17 is smaller and coarser, 65 larger and more faithful to curved looks. Sizes 2, 4, 6, 16, 18 and 52 put every grid point exactly on an 8-bit value.

## Why does the file say it is 8-bit when it has six decimals?

The tool reads and writes pixels at 8 bits, so every value it can produce is one of 256 levels. Six decimals is simply how the format writes numbers. The header says this because the format has no other way to record precision.

## Can I make a LUT with more precision than 8 bits?

Not in LUT Lab. A 32-bit float export was withdrawn because the tool has no floating-point path to fill it.

## Why is there no ACEScct or log conversion?

Such conversions need values far above the 0 to 1 range an 8-bit canvas holds. The ACEScct look was withdrawn for that reason; the **Looks** tab shows why.

## Is "Bleach bypass" a real film process simulation?

No. It is a stylisation named after the process, not a simulation of it. All five stylisations are hand-tuned curves; only the Reinhard tone-map is a defined transform.

## What does "clipped" count?

Pixels where the transform drove a channel to 0 or 255 that was not already there. Pixels that were already pure black, white or fully saturated and stayed that way are not counted.

## Can I adjust the strength of a loaded .cube?

No. **Strength** applies to the built-in looks. A loaded file is applied at full strength.

## Can I use LUT Lab to convert a 3D LUT to a different size?

Yes. Load the file, then export at the size you want. The new table is resampled with interpolation and rounded to 8 bits, so keep the original. Exporting a 3D file as a 1D curve keeps only what it does to greys.

## Does the tool show the LUT as a 3D cube?

No. It shows the effect on a scene, on 18 test colours on the **Looks** tab, and on a ring of 72 test colours.
