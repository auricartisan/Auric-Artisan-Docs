---
title: Gamut Mapping — Map a colour into a smaller gamut
description: Check whether a colour fits a target space, choose a mapping method and strength, and read the result.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Map a colour into a smaller gamut

## The four methods

All four are this tool's own methods. None is an ICC rendering intent.

| Method | What it does | Keeps | Gives up |
| --- | --- | --- | --- |
| **Chroma compression** | Holds L* and hue, and reduces chroma until the colour fits (found by bisection). **Compression Strength** sets how far: 1 lands exactly on the boundary, 0 keeps the original chroma and leaves the final clip to deal with it | Lightness and hue | Vividness |
| **Clip in target RGB** | Converts to the target's linear RGB and clamps each channel to 0–1 | Everything already inside the gamut | Detail and hue near the boundary; different out-of-gamut colours can collapse onto one |
| **Uniform RGB scale** | Divides all three channels by the largest, so the brightest channel becomes 1; if a channel is negative it falls back to clipping | The ratio between channels | Lightness: everything darkens together |
| **Adapt white, then clip** | Adapts from the source white to the target white with the Bradford transform, then clips. This is the shape of ICC relative colorimetric | The relationship to each space's white | Accuracy of out-of-gamut colours, which are clipped |

The last method only differs from **Clip in target RGB** when the two spaces have different white points. Of the five spaces, ProPhoto RGB uses D50; the others use D65.

## Steps

1. On the **Lab** tab, enter your colour under **Base Colour**: use the colour picker or type a HEX value such as `#00C853` in the field. **Random** picks a random colour.
2. Under **Colour Spaces**, set **Source** to the space the colour is defined in and **Target** to where it must go. The HEX value is interpreted in the source space, decoded with that space's own transfer curve.
3. Read **Base Colour Info**: L*, a*, b*, C* and h°, then whether the colour is inside the source space and inside the target space, each shown as **Yes** or **OOG**.
4. Set **Lightness Slice L\*** to the colour's L* (shown in Base Colour Info) so the white ring marking the base colour sits on the slice you are looking at.
5. Choose a **Method**.
6. For **Chroma compression**, set **Compression Strength** (0 to 1, default 0.90). An in-gamut colour is never changed, whatever the strength.
7. Read the effect in **Before / After (12 Test Colours)**: each row shows a vivid test colour on the left and its mapped result on the right.
8. To get exact numbers for your colour, open **Methods**, choose **The base colour** under **Compare on**, and read mean ΔE₀₀, max ΔE₀₀ and whether it was out of gamut for each method. Or add the colour to the batch list on the **Export** tab ([Map a list of colours](map-a-colour-list.md)).

## About the Mapped to Target slice

In the current version the **Mapped to Target** slice is always drawn with chroma compression all the way to the boundary, whichever method and strength you choose. The **Before / After** strip, the batch list and the **Methods** tab use your chosen method and strength. Use those to judge the method; use the slice to see the shape of the target gamut.

## Reading ΔE₀₀

ΔE₀₀ (CIEDE2000) measures how different the mapped colour is from the original. As a rough guide, which the lab also uses in its playground: below 1 imperceptible, 1–2 barely perceptible, 2–3.5 noticeable, 3.5–5 significant, and above 5 very different.

## Result

You know whether the colour fits the target, what each method turns it into, and how large the change is.
