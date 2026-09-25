---
title: LUT Lab — Apply a look
description: Choose a test scene or your own picture, apply one of the six built-in looks, and set its strength and exposure.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# Apply a look

## Choose what to test on

Under **The scene** on the **Lab** tab, select one of four drawn scenes. Each is 320 × 180 pixels.

| Scene | What it contains | Good for spotting |
|---|---|---|
| **Neutral wedge** | A 16-step grey ramp above 16-step red, green and blue ramps | Banding, contrast changes and colour casts in greys |
| **Colour patches** | 24 flat patches: six hues at four lightness levels | Hue and saturation shifts across the colour wheel |
| **Skin tones** | Six skin-like tones from dark to light on a mid-grey surround | What a look does to faces |
| **Saturation field** | Hue across, from grey at the bottom to strong colour at the top | Hue twists and clipping in saturated colours |

The scenes are drawings, not photographs. They show the shape of a transform evenly, but they have no grain, lens flare or real-camera colour.

### Use your own picture

1. Drop an image on **Drop an image**, or select the box to choose one.
2. The picture is scaled to fit 480 × 270, keeping its proportions (it is never enlarged), and becomes the scene. A message confirms the size, for example **Loaded beach.jpg at 480×270**.
3. A fifth button with your file name appears among the scenes, selected.
4. To go back, select **Back to the drawn scenes**, or any of the four scene buttons.

Every figure on the page is then computed from your picture, and the **Data** tab marks the scene as your own file.

## Choose a look

Open the menu under **The look**.

| Look | Kind | What it does |
|---|---|---|
| **None** | — | Leaves the image unchanged |
| **Teal and orange** | Stylisation | Warms the highlights and cools the shadows. The look shown when the page opens |
| **Bleach bypass** | Stylisation | Pulls colours towards grey and raises contrast. Named after a film process it does not simulate |
| **Film soft** | Stylisation | Lifts the black point and lowers the white point, with a slight warm cast. Not based on a measured film stock |
| **Mono contrast** | Stylisation | Black and white from Rec. 709 luminance in linear light, then an S-shaped contrast curve |
| **Log-ish lift** | Stylisation | A 0.45 power curve with a lift and a gain, which brightens the image, lifting the shadows most |
| **Reinhard tone-map** | Transform | The Reinhard photographic tone-mapping operator, applied in linear light |

The label above the pair names the transform in force.

## Set the strength

**Strength**, from 0% to 100% (default 100%), blends the look with the original. At 50%, each channel of each pixel is halfway between its original value and the look's value. **Strength** applies to the looks only, not to a loaded `.cube` file.

## Set the tone-map exposure

**Tone-map exposure**, from 0.25× to 8× (default 2.00×), is active only for **Reinhard tone-map**; it is greyed out for every other look and for a loaded file.

The tone-map works in linear light: it decodes the sRGB value to light, multiplies it by the exposure, compresses it with Reinhard's formula L ÷ (1 + L), and encodes it back to sRGB. Higher exposure brightens the picture and compresses the highlights more; lower exposure darkens it. An 8-bit picture carries no record of how bright the original scene was, so the exposure is a choice rather than a measured value.

## Compare looks on the Looks tab

The **Looks** tab has a card for each look except **None**. The heading note counts them: five stylisations and one transform, plus two withdrawn.

Each card shows:

- the look's name and a badge, **Stylisation** or **Transform**;
- a strip of 18 test colours, a 12-step grey wedge and the six pure primaries and secondaries, before (top) and after (bottom);
- a sentence on what the look is;
- **mean ΔE₀₀**, **max hue** and **clipped** on the 72-colour hue ring (see [Read what a transform moved](read-what-it-moved.md));
- **Show it on the pair**, which applies the look and returns you to the **Lab** tab.

Under **Withdrawn**, two former features are explained: an ACEScct to ACEScg conversion, which an 8-bit canvas cannot hold, and a 32-bit float export. A table shows what the ACEScct decode produces for several input codes, and how many of the 256 codes would come out pure white.

## Show what the transform crushed

The **What the transform crushed** switch under **Show** (on by default) hatches the pixels the transform drove to white in pink and those driven to black in blue, on the right-hand image. See [Read what a transform moved](read-what-it-moved.md).

## What you should see

The right-hand image shows your scene with the look at the strength you chose, and the figures under the pair describe exactly that combination.
