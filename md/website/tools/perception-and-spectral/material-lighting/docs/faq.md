---
title: Material Lighting (Material Under Light) — FAQ
description: Short answers to common questions about Material Under Light.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Material Under Light FAQ

## Are the materials measured?

No. All twenty presets are invented curves (a flat level plus bell-shaped bumps) and are marked **synthesised** everywhere. Load a measured file on the Data tab to use real data.

## Why is there no CRI or TM-30 score?

Both need specified sets of measured test colours and specific colour spaces that the tool does not hold. The figures an earlier version printed were wrong in ways the **Metrics** tab demonstrates, so they are withdrawn.

## So what does the ΔE₀₀ under the swatches mean?

How far this one material's colour moves between your light and the CIE reference light for its colour temperature, each taken against its own light's white. It describes the material in that light, not the light in general.

## Why does the swatch look warm under tungsten when L\*a\*b\* barely changes?

The swatch is un-adapted: it shows the light that actually leaves the surface, as a camera would record it. L\*a\*b\* is taken against the light's own white, so it measures the material relative to the light.

## Is the rendering physically accurate?

The spectral pipeline, observer, daylights, colour difference and the five lobes follow their published forms. The materials are invented, the scene is a single light and a single surface with no inter-reflection, and the sphere is a simple shaded preview. It is a teaching and exploration tool, not a renderer for production images.

## Can it show metamerism?

It shows one material at a time. Because it is spectral, you can compare two materials (for example a preset and a measured file) under two lights one after the other and see whether a match holds; it has no side-by-side metamerism index.

## What does Jz add?

The lightness of JzAzBz, a colour space designed for high-dynamic-range and wide-gamut signals, as a second view of lightness beside CIE L\*.

## Why does a metal go black with Oren-Nayar?

Oren-Nayar is a diffuse-only model and a conductor has no diffuse reflection. Choose a specular lobe for metals.

## How accurate is the measured colour temperature?

Within about ±11 to ±18 K below 7000 K, and much less accurate above; the readout shows the band. See [Compare with the reference light](compare-with-the-reference.md).

## Is my reflectance file uploaded?

No. It is read and used in the page only. See [Privacy](../others/privacy.md).
