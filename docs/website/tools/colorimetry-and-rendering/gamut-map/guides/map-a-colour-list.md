---
title: Gamut Mapping — Map a list of colours
description: Map up to 50 HEX colours at once and export images, settings and a link.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Map a list of colours

## Map the list

1. On the **Lab** tab, set the **Source** and **Target** spaces, the **Method** and, for chroma compression, the **Compression Strength**. The list goes through the same settings.
2. Open the **Export** tab and find **Map a list of colours at once**.
3. Enter HEX values, one per line (commas also separate them). Three-digit (`#F0A`) and six-digit (`#FF00AA`) forms are accepted, with or without `#`. Up to 50 are used.
4. Select **Run the list**.
5. Read the table:

| Column | Meaning |
| --- | --- |
| **Input** | Your colour and its swatch |
| **Output** | The mapped colour, converted to sRGB HEX for display on screen |
| **OOG** | **Yes** if the input was outside the target gamut, otherwise **No** |
| **ΔE₀₀** | The colour change caused by mapping |
| **Lab** | The input's L*, a*, b* |

A summary line gives the number processed, how many were out of gamut and the average ΔE₀₀. If no valid HEX is found, the panel says "No valid hex values found."

The **Output** HEX is an sRGB value for your screen. When the target is wider than sRGB (for example Rec. 2020), it is not the target-space code value.

## Export

| Button | What you get |
| --- | --- |
| **Source slice, PNG** | `gamut-map-gm-canvas-src.png`: the source slice at its drawn size, on the dark background, with outlines |
| **Mapped slice, PNG** | `gamut-map-gm-canvas-dst.png`: the mapped slice |
| **Everything as JSON** | `gamut-map-config.json`: source space, target space, method, strength, L*, resolution, sampler and a timestamp |
| **Link**, then **Copy** | A link that reopens this state |

The link records the source and target spaces, the method, L*, resolution, sampler, strength and base colour. Overlays and the ΔE Playground colours are not included. The JSON file holds settings only, not the figures on screen.

## Result

You have every colour in your list mapped with its out-of-gamut flag and ΔE₀₀, and files or a link to share the setup.
