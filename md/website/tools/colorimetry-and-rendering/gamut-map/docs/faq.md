---
title: Gamut Mapping — FAQ
description: Short answers to common questions about the Gamut Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Mapping FAQ

## Are these the ICC rendering intents?

No. ICC perceptual and saturation intents are lookup tables that a profile author builds for a particular device, so no general algorithm can reproduce them. The lab's four methods are named for what they do. **Adapt white, then clip** has the shape of ICC relative colorimetric; **Clip in target RGB** (no white adaptation) resembles absolute colorimetric clipping.

## Which method should I use?

For photographs, chroma compression usually looks most natural because it keeps lightness and hue. For logos and spot colours that must match exactly where they can, clipping keeps in-gamut colours untouched. The lab does not rank methods, because there is no agreed reference set of correct mappings; it reports what each does.

## Why is the slice painted in sRGB?

Most screens and browsers show sRGB reliably. The geometry (which colours are in each gamut) is computed exactly; only the painting is limited to what your screen can show.

## Why does ProPhoto RGB look lopsided?

ProPhoto RGB is defined against D50 and includes colours outside human vision. The lab adapts it onto the Lab plane's white with Bradford before testing its boundary, and its chroma can run past the ±128 range the slice draws.

## Why do the areas in the statistics line differ from percentages I see elsewhere?

They are areas of the a*b* slice at one lightness, not the "percentage of the spectral locus" often quoted from the xy diagram. For total size, use the volume on the Boundary tab.

## Is a ΔE₀₀ of 2 acceptable?

For critical work an average below 2 is a common target, and the lab's research notes suggest the same. It depends on your application.

## Can I load an ICC profile?

No. The Data tab shows an **Install a table** area, but it does not load files in the current version.

## Is anything uploaded?

No. All mapping runs in your browser.
