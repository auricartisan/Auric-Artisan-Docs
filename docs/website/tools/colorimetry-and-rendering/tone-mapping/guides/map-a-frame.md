---
title: Tone Mapping — Map a frame
description: Choose a source, set exposure and a tone curve, grade the result and set the output for your display.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Map a frame

## 1. Choose the source

1. Under **Source**, choose **HDR test scene**, **Exposure gradient**, **ColorChecker patches** or **Uploaded image**.
2. For **Uploaded image**, select **Choose a file** and pick an image. The file name replaces "no file" and a message confirms the load.
3. Tell the lab how the source was written:
   - encoding: **Linear (scene)**, **sRGB**, **PQ (ST 2084)**, **HLG (inverse OETF)**, **Gamma 2.2** or **Gamma 2.4**;
   - primaries: **Rec.709**, **Display P3**, **Rec.2020** or **ACEScg AP1**;
   - white point: **D65**, **D60** or **D50**.

An ordinary PNG or JPEG is 8-bit sRGB: choose **sRGB** encoding and **Rec.709** primaries for it. Its values stop at 1.0, so there are no true highlights above white for the curve to shape; use Exposure to push it into the curve's shoulder. The built-in scenes are generated with values above 1.

The chip over the frame says **Scene-referred** when the encoding is linear and **Display-referred** otherwise.

## 2. Set exposure

Move **Exposure** from −6 to +6 EV (steps of 0.1). Each stop doubles or halves the values before the curve. Watch the histogram behind the curve slide along it.

## 3. Choose a tone curve

Select one of the seven curves under **Tone curve**: **None (clip)**, **Reinhard**, **Uchimura / Gran Turismo**, **Hable filmic** (default), **Narkowicz fit**, **Log (soft)** or **Custom 1D curve**. See [Compare operators](compare-operators.md) for what each does.

To shape your own curve, tick **Use the custom curve instead** and set the three fields, in order **knee**, **mid** and **shoulder** (each 0 to 1; defaults 0.15, 0.5, 0.85). The curve is three straight segments: from 0 up to (knee, mid × knee), then to (shoulder, mid), then to (1, 1). Inputs above 1 give 1.

The three buttons under the curve chart — **Linear axis**, **Log axis** and **Film stops** — fill the custom curve's fields with presets (0.33, 0.5, 0.66; 0.05, 0.35, 0.7; and 0.15, 0.5, 0.85). They do not change the chart's axis, and they only affect the frame when **Use the custom curve instead** is ticked.

## 4. Optional low-level operator

**Low-level operator** applies a simple function to each channel before the tone curve, using parameters **a** and **b**:

| Choice | Function |
| --- | --- |
| **None** | No change (default) |
| **Add** | v + a ÷ 10,000 |
| **Multiply** | v × a |
| **Soft clip** | v ÷ (v + a) |
| **Power** | v^a |
| **Sigmoid** | 1 ÷ (1 + e^(−(v − b) × a × 10)) |
| **Exp** | 1 − e^(−v × a) |
| **Log** | log2(1 + v × a) ÷ log2(1 + a) |
| **Tanh** | tanh(v × a) |

Both parameters start at 0; most functions need a positive **a** to do anything useful.

## 5. Grade

The **Grade** row holds nine number fields, applied after the curve in the working space, in this order:

| Field | Range | Default | Effect |
| --- | --- | --- | --- |
| Contrast | 0 to 3 | 1 | Expands or compresses values around 0.5 |
| Saturation | 0 to 3 | 1 | Mixes towards or away from the working space's own luminance |
| Lift | — | 0 | Adds to every channel |
| Gamma | 0.1 to 4 | 1 | Raises each channel to 1 ÷ gamma |
| Gain | 0 to 4 | 1 | Multiplies every channel |
| Temperature | — | 0 | Positive warms (more red, less blue) |
| Tint | — | 0 | Positive adds green |
| Hue rotation | −180 to 180° | 0 | Rotates hue around the luminance axis |
| Vibrance | 0 to 3 | 1 | Changes saturation more for muted colours than for vivid ones |

## 6. Output

1. Choose the **Working space**: **ACEScg AP1 (D60)** (default), **Rec.709 (D65)**, **Display P3 (D65)** or **Rec.2020 (D65)**.
2. Choose the target primaries (**sRGB / Rec.709**, **Display P3**, **Rec.2020**) and target white (**D65**, **D60**, **D50**). Different white points are bridged with the Bradford transform.
3. Choose the gamut mapping: **Soft compress**, **Clip** or **Preserve hue** (scales the colour down by its largest channel, keeping channel ratios). In the current version Soft compress gives the same result as Clip.
4. Choose the output encoding: **sRGB**, **Gamma 2.2**, **Gamma 2.4**, **PQ** or **Linear**. With PQ, a display value of 1.0 is encoded as 10,000 cd/m².
5. Tick **Mark out-of-gamut pixels** to paint pixels that left the target gamut in magenta.
6. Tick **Dither the 8-bit output** to add a tiny amount of noise that hides banding.

## Presets

| Preset | Curve | Target | Display peak | Output | Source encoding |
| --- | --- | --- | --- | --- | --- |
| **SDR 100** | Hable filmic | sRGB / Rec.709 | 100 nits | sRGB | sRGB |
| **P3 600** | Hable filmic | Display P3 | 600 nits | sRGB | sRGB |
| **HDR 1000** | Narkowicz fit | Rec.2020 | 1,000 nits | PQ | Linear (scene) |

**Reset** reloads the lab with its default settings.

## Result

You have a frame mapped with the curve, grade and output you chose, with the chips and statistics telling you how it was made.
