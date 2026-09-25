---
title: Gamut Mapping — Limits and accuracy
description: What the Gamut Mapping lab computes exactly, what it approximates and what it does not do.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Mapping limits and accuracy

The lab is a visual and numerical explorer that runs in your browser. It is not an ICC colour-management engine and does not reproduce any vendor's conversion.

## Exact

- **Primaries and white points** of the five spaces are published values, held verbatim.
- **Transfer curves** are each space's own: the sRGB curve (sRGB and Display P3), the BT.2020 curve, Adobe RGB's 563/256 power law and ProPhoto's ROMM curve with its linear toe.
- **Boundaries** are traced by 24 bisection steps along 360 hue directions, accurate to about 0.00001 in chroma — far below what the plot can show.
- **ΔE formulas** follow CIE definitions; ΔE₀₀ follows the Sharma, Wu and Dalal implementation notes.

## Estimated

- **Gamut volume** is a Monte Carlo estimate with a standard error. It changes slightly each run and narrows as you raise the sample count.
- **Out-of-gamut tests** allow a tiny tolerance so that colours on the boundary count as inside.

## Not done

- **ICC perceptual and saturation intents** — these are profile lookup tables, not algorithms, and no profile is loaded.
- **Ranking methods** — there is no published reference set of correct mappings, so the lab reports what each method does.
- **Loading profiles or tables** — the Data tab's install area is not active.
- **Showing wide-gamut colours as they really are** — all painting is in sRGB.

## Current-version caveats

- The **Mapped to Target** slice always uses chroma compression to the boundary; the other mapping outputs follow your method and strength.
- **Adaptive edge refinement**, **Axes & labels** and the ΔE formula menu do not change the output.
- The slices show a* and b* from −128 to +128; ProPhoto RGB's chroma can exceed that range, so its outer boundary may run off the slice.
- **Output** HEX values in the batch list are sRGB display values, clipped to sRGB.
- The JSON export records settings, not results.
