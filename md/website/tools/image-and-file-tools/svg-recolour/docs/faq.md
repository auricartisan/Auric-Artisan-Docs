---
title: SVG Recolour — FAQ
description: Short answers to common questions about SVG Recolour.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# SVG Recolour FAQ

## Is my SVG uploaded?

No. The file is parsed in the page and never sent anywhere. See [Privacy](../others/privacy.md).

## Can I swap two colours?

Yes. Set each colour's target to the other. Every change is planned from the original file before anything is written, so the swap works cleanly.

## Does it change colours written as names, like `red`?

Yes. Names, hex, `rgb()` and `hsl()` forms are all found and rewritten. The same colour written different ways appears as one row.

## Why is `currentColor` left alone?

It takes its value from the `color` of the page the SVG is placed in, so the file does not contain the colour. The tool counts it and leaves it as it is, which keeps icons that rely on it working.

## Does it recolour gradients?

Yes, through the `stop-color` of each gradient stop, which appear as their own rows. The shape that uses the gradient refers to it with `url()`, which is left alone.

## Does it recolour embedded images?

No. Pictures embedded in an SVG are pixels, not markup, and are not found or changed.

## Can I recolour several files at once?

No. The tool works on one file at a time.

## Are near-identical colours merged into one row?

No. Only exactly identical colours share a row, however they are written.

## Will the exported file look exactly like the After preview?

Yes, in colour: the preview is drawn from the same rewrite. The preview has active content removed, but the file keeps it.

## What does "near royalblue" mean?

It is the nearest CSS colour name, found by colour difference, to make hex values easier to read. An exact CSS name is shown without "near". Nothing depends on the name.

## Is the harmony a guarantee of good colours?

No. The harmonies are a convention from colour-wheel teaching. Check the result for contrast and colour vision on the **Check** tab.

## Does the colour-vision preview change the exported file?

No. It changes only what is drawn on screen.
