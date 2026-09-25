---
title: Neuroscience (Visual Pathway) — FAQ
description: Short answers to common questions about the Visual Pathway.
product: Website › Tools › Perception and spectral › Neuroscience
updated: 2026-09-25
---

# Visual Pathway FAQ

## Is this a model of real neurons?

No. Each stage uses a standard form from the literature (a difference of Gaussians, a Gabor energy model, divisive normalisation, a projection in an opponent plane), but every constant is the tool's own and sizes are in pixels rather than degrees of retina. The maps show the shape of what each area does. The page marks itself "Educational, not physiological".

## Why are the tool's L and M cone curves on top of each other?

The built-in spectral table is the tool's own and puts both peaks at 590 nm. It only draws the figure. The cone signals the stages use come from a published matrix (Hunt-Pointer-Estévez) applied to CIE XYZ. You can install a published table on the **Data** tab to fix the figure.

## Are the opponent channels the DKL space?

No. They are differences of absolute cone signals (L − M, S − (L+M)/2) and a luminance channel of L + M. DKL uses cone contrast against a stated white and scaled isoluminant axes. See [Cones, opponent channels and the cone table](cones-and-opponent-channels.md).

## Why does a grey not read exactly zero on the chromatic channels?

It reads about 0.0002 at worst, because the published cone matrix is given to four decimals. That is the **Neutral off-axis** readout.

## What does "Sensitivity at this frequency" mean? Is it the chance I can see the grating?

It is a weighting curve that peaks at 1.0 at 4 c/deg and falls off either side. It is not a probability of detection; the page deliberately gives no detection figure. To measure your own threshold, use the [Psychophysical Experiment Engine](../../psychophysical-experiment-engine/README.md).

## Why do I need to enter a viewing distance and pixel pitch?

Cycles per degree depends on both. Without them, the same image has a different spatial frequency at every distance. Defaults are 57 cm and 0.248 mm.

## Can I load my own image?

No. The sources are the grating and the built-in test card. To run simulations over your own images, use [Perception and Vision](../../perception-and-vision/README.md).

## Can I simulate a milder colour vision deficiency?

Not on this page: **Colour vision** applies full dichromacy. Perception and Vision has a **Severity** control.

## Does the pupil control do anything?

Not in the current version. It is shown on the rail, but no map or readout uses it.

## Is there a spike raster or firing rate?

No. An earlier version drew a panel called a spike raster; it had no time axis and was withdrawn. Nothing on the page may be reported as a spike train or a firing rate.

## Does anything I enter leave my computer?

No. All processing is in the page. Files and copies are only created when you press an export or copy button. See [Privacy](../others/privacy.md).
