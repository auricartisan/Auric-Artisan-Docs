---
title: M-Gradient Palette — Getting started
description: Open the M-Gradient Palette, find your way around its six tabs, and build a first ramp.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# Getting started with the M-Gradient Palette

## Open the tool

Go to https://auricartisan.com/tool/general/tools/m-gradient-palette/. The page, titled **Gradient Ramp**, opens on the **Ramp** tab with a 12-step ramp from a deep blue, `#0B3D5C`, to a gold, `#F2B134`.

A note under the heading explains what the numbers on the page are measurements of. It has no close button on purpose.

## The screen at a glance

| Tab | What it is for |
|---|---|
| **Ramp** | The controls, the ramp, the step-by-step differences, the figures and the hue circle |
| **Spaces** | All six routes by five easings, built and measured, and three ramps drawn side by side |
| **Contrast** | A text colour, and every step checked as a background with WCAG 2.2 and APCA |
| **Data** | Every figure and what it rests on; the tab shows the number of entries (15) |
| **Export** | Copy and save buttons, previews and the JSON reading |
| **Reference** | The published sources and the arithmetic |

### The Ramp tab

- **The left-hand panel** holds **The two ends** (a swatch and a hex box for each, **Swap the ends**, and **A starting point**), **Interpolate in** (six route buttons), **Shape** (**Steps** and the **Easing** buttons), and **Show it as seen by** (four vision buttons).
- **The right-hand panel** holds **The ramp** (one button per step), the bars of **ΔE₀₀ between adjacent steps**, the cards under **What the ramp measures**, and the circle under **Where the ramp goes in hue and chroma**.

## Build a first ramp

1. Under **A starting point**, choose **Ocean**. The ends become `#0B3D5C` and `#69D2E7`, and the ramp redraws.
2. Move **Steps** to 9. The ramp now has nine steps.
3. Under **Interpolate in**, select **sRGB**, then **OKLCH, short hue**. Watch the bars under **ΔE₀₀ between adjacent steps**: the flatter they are, the more evenly the steps are spaced to the eye.
4. Read **evenness** under **What the ramp measures**. Lower is more even.
5. Select a step in the ramp to copy its hex value.
6. Open the **Export** tab and select **Copy the custom properties**. Paste the result into your stylesheet:

```css
--ramp-01: #0B3D5C;
--ramp-02: #164E6D;
--ramp-03: #215F7F;
--ramp-04: #2B7190;
--ramp-05: #3784A2;
--ramp-06: #4397B3;
--ramp-07: #4FAAC5;
--ramp-08: #5CBED6;
--ramp-09: #69D2E7;
```

These are the nine steps of **Ocean** in **OKLCH, short hue** with **linear** easing. Here **evenness** reads 0.61, against 0.80 for the same ramp in **sRGB**.

## Next steps

- To understand why routes differ, read [Interpolation and gamut](interpolation-and-gamut.md).
- To find the evenest combination for your two colours, see [Compare routes and easings](compare-routes.md).
- To check text on your ramp, see [Check contrast and colour vision](check-contrast-and-colour-vision.md).
