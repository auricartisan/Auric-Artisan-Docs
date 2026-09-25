---
title: Gradient Library — Limits and accuracy
description: What the Gradient Library's banding verdicts, contrast figures and previews measure, and what they do not.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Limits and accuracy

## The banding verdict

- The checker samples 96 points along the ramp and compares neighbouring samples in OKLab. The verdict depends on the ratio of the largest step to the average step, so it does not change with the number of samples.
- The thresholds (3.2 and 5.5) were set from the collection's own labelled gradients, as the page explains. They are a good guide, not a guarantee: whether a step is visible also depends on the screen, its bit depth, the size of the gradient, image compression and the viewer.
- The checker models a plain CSS gradient: evenly spaced stops blended in sRGB. It ignores stop positions, colour hints, easing and `in oklch`-style interpolation you may use in your own CSS.
- The collection's verdicts were recorded when each gradient was generated, using its own positions, space and easing.

## Contrast

- Contrast uses the WCAG 2 formula on sampled colours: 24 samples for **White min** and **Black min**, 17 on the **Accessibility** tab, and 33 on the **Pair** tab. A very narrow dark or light band between samples could be missed.
- Passing contrast is one part of readable text; font size, weight and any texture behind the text also matter.

## Vision previews

The **Vision** tab uses approximate screen filters for complete deuteranopia, protanopia, tritanopia and achromatopsia, and a blur for low vision. They show the idea, not an exact simulation of any individual's sight.

## Scores and labels

The score, complexity, method and scheme are recorded with each gradient when it was generated. The score is a ranking aid, not a judgement of beauty or fitness for your purpose.

## Exports

- The SVG export draws a linear gradient at the gradient's angle across the image; for very steep angles it can differ slightly from how CSS fits the same angle to a box.
- The PNG export is drawn by your browser, so it reflects your browser's sRGB blending.

## What it is not

It is not a certified measurement of display performance, and it does not know how your gradient will be compressed or displayed.
