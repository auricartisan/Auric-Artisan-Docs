---
title: LUT Lab — Getting started
description: Open LUT Lab, find your way around its six tabs, and try a first look.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# Getting started with LUT Lab

## Open the tool

Go to https://auricartisan.com/tool/general/tools/lut-lab/. The page opens on the **Lab** tab, showing the **Neutral wedge** scene before and after the **Teal and orange** look.

A note under the heading explains what the numbers on the page are measurements of. It has no close button on purpose.

## The screen at a glance

| Tab | What it is for |
|---|---|
| **Lab** | The scene, the transform, the before and after pair, and what the transform moved |
| **Method** | Five short explanations: sample order, interpolation, clipping, round trip and linear light |
| **Looks** | A card for each built-in look, with what it is and what it does to a test strip |
| **Data** | Every figure and what it rests on; the tab shows the number of entries (17) |
| **Export** | Kind and size of the table, the file preview, and the save and copy buttons |
| **Reference** | The published sources, marked by whether they run in the tool |

### The Lab tab

- **The left-hand panel** holds **The scene** (four scene buttons and a **Drop an image** box), **The look** (a menu, **Strength** and **Tone-map exposure**), **A .cube file** (a **Drop a .cube** box and **Clear the file**), and **Show** (the **What the transform crushed** switch and **Copy a link to this setting**).
- **The right-hand panel** holds **Before and after**, a key to the clip overlay, the cards under **What it moved**, and the hue circle under **Where it moved things to** with its own cards.

## Try a first look

1. On the **Lab** tab, select **Colour patches** under **The scene**. The pair shows 24 flat colour patches before and after.
2. Open the menu under **The look** and choose **Bleach bypass**. The right-hand image loses colour and gains contrast. The label above the pair reads **Bleach bypass**.
3. Move **Strength** to 50%. The look is blended halfway with the original.
4. Read **What it moved**. **mean ΔE₀₀** is the average colour difference between before and after; **clipped** is the share of pixels driven to pure white or black.
5. Look at the hue circle. Each hollow dot is a test colour before the look; the filled dot joined to it is where the look moved it.
6. Open the **Export** tab. Leave **Kind** on **3D cube** and **Size** on 33, and select **Save the .cube**. Your browser downloads `auric-bleach-bypass-33.cube`.

You now have a `.cube` of the look at half strength, ready to load in a program that reads `.cube` files.

## Next steps

- To understand sizes, domains and why the file header mentions 8 bits, read [LUT concepts](lut-concepts.md).
- To test a `.cube` you already have, read [Load a .cube file](load-a-cube-file.md).
- To test on your own picture, see [Apply a look](apply-a-look.md).
