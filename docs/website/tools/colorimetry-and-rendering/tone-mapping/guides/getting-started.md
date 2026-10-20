---
title: Tone Mapping — Getting started
description: Open the Tone Mapping lab, learn its tabs and the eleven-step pipeline, and read your first mapped frame.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Getting started with Tone Mapping

## Open the lab

Go to https://auricartisan.com/tool/general/gamut-and-rendering/tone-mapping/. The heading is **Tone Mapping**. All processing happens in your browser.

## Key ideas

- **Scene-referred** values describe light in the scene. They start at 0 and can go far above 1; 0.18 is the conventional **mid-grey**, and 1.0 is often treated as diffuse white.
- **Display-referred** values run from 0 to 1, where 1 is the brightest the display shows.
- A **tone curve** (tone-mapping operator) maps scene values to display values. A good curve keeps mid-grey where you expect it and rolls highlights off gently instead of clipping them.
- **Exposure** is measured in **stops (EV)**. One stop doubles or halves the light, and it is applied before the curve, so it changes which part of the curve the scene lands on.

## A tour of the screen

A note at the top warns that two of the nine operators the page once offered were one-line stand-ins; see the Data tab.

| Tab | What it is for |
| --- | --- |
| **Lab** | The pipeline controls, the mapped frame and the curve |
| **Operators** | All nine operators on one table and one chart |
| **Scopes** | Histogram, waveform, vectorscope, false colour, A/B split and timing |
| **Data** | The eight datasets and transforms the lab rests on, with their status |
| **Export** | Curve and pipeline LUTs, CSV, a link, and HEX list mapping |
| **Reference** | Standards, formulas, citations and research notes with a filter |

### The pipeline

Every pixel goes through these steps in order:

1. Linearise (decode the source encoding)
2. Source → working, with white-point adaptation
3. Exposure
4. Low-level operator
5. Tone curve
6. Contrast, saturation, lift / gamma / gain
7. Temperature and tint
8. Hue and vibrance
9. Working → target, gamut mapping
10. Output OETF (encode for the display)
11. Dither

The Export tab refers to these step numbers.

### The Lab tab

The left panel groups the controls: source (**Source**, encoding, primaries, white), **Exposure**, **Tone curve** (with a custom curve option), **Low-level operator**, **Grade**, **Working → target** (working space, target primaries and white, gamut mapping, output OETF, out-of-gamut mark, dither), **Display peak**, **Source peak** and **Presets**.

The right side shows **The mapped frame** with its resolution and status chips, then **The curve, and where the scene sits on it** (the tone curve drawn over a histogram of the scene), statistics and a note.

## Read your first frame

1. The lab opens on **HDR test scene**, **Linear (scene)** encoding, Rec.709 primaries, D65, the **Hable filmic** curve and the **ACEScg AP1 (D60)** working space.
2. Look at the chips over the frame: the working and target spaces, the curve and the processing time; **Scene-referred** (because the source is linear) and **Photographic**; and **out of gamut** if any pixel left the target gamut.
3. Read the statistics:
   - **Mid-grey, curve** — what 0.18 becomes;
   - **Scene white at** — the input at which the curve reaches display white ("never" if it only approaches it);
   - **Working luma** — the working space's luminance weights;
   - **Display peak** — in nits.
4. Move **Exposure** to +2.0 EV. The frame brightens, and the histogram behind the curve shifts to the right.
5. Choose **None (clip)** under **Tone curve**. Highlights now clip hard at white.

## Next steps

- [Map a frame](map-a-frame.md)
- [Compare operators](compare-operators.md)
- [Read the scopes](read-the-scopes.md)
- [Export a LUT](export-a-lut.md)
