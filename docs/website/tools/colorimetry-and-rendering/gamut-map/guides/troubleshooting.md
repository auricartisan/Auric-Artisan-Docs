---
title: Gamut Mapping — Troubleshooting
description: Fixes for common problems in the Gamut Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting Gamut Mapping

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The Mapped to Target slice does not change when I change method or strength | In the current version that slice is always drawn with chroma compression to the boundary | Judge methods with **Before / After**, the **Methods** tab or the batch list, which use your method and strength |
| Changing Compression Strength has no effect | Strength only applies to **Chroma compression**, and never changes a colour that is already in gamut | Choose Chroma compression and use an out-of-gamut colour |
| **Adapt white, then clip** gives the same result as **Clip in target RGB** | Both spaces share the D65 white, so there is nothing to adapt | Use ProPhoto RGB (D50) as one of the spaces to see a difference |
| The slice looks dull or clipped at the edges | Slices are painted in sRGB so your screen can show them; wider colours are displayed clipped | Expected. Use the probe and figures, not the painted colour, for wide-gamut values |
| The slice looks grainy or speckled | A low **Resolution**, or the **Stratified** sampler, which places points at random | Raise Resolution, or choose **Uniform grid** or **Halton** |
| The page is slow after raising Resolution | 512 × 512 samples per slice is a lot of work | Lower Resolution |
| My base colour's ring is not on the coloured area | The slice is at a different lightness from the colour | Set L* to the colour's L* shown in Base Colour Info |
| **Adaptive edge refinement** or **Axes & labels** does nothing | These controls are not applied in the current version | No workaround needed |
| The ΔE formula menu does not change the result | All three formulas are always shown | Read the one you need from the result line |
| A HEX typed into the ΔE Playground is ignored | The field needs a full `#RRGGBB` value, applied when you press Enter or leave the field | Type a six-digit value with `#` |
| Volume figures change each time | They are Monte Carlo estimates | Raise **Volume samples** to shrink the standard error |
| The batch says "No valid hex values found." | No line was a 3- or 6-digit HEX | Put one colour per line, for example `#FF00AA` |
| Batch Output for Rec. 2020 looks the same as for P3 | Output HEX is converted to sRGB for display | Use OOG and ΔE₀₀ to compare; the HEX is a screen preview |
| The JSON file has no numbers from the screen | **Everything as JSON** saves the settings only | Use the batch table or PNG images for figures |
| The link field stays empty | The link is built only when you select **Link** | Select **Link**, then **Copy** |
| Dropping a file on **Install a table** does nothing | The area is not active in the current version | No workaround |
