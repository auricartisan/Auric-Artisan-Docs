---
title: M-Gradient Palette — Build a ramp
description: Set the two ends, use a preset, choose a route, steps and easing, and read everything on the Ramp tab.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# Build a ramp

Everything in this guide happens on the **Ramp** tab. The ramp and its figures update as soon as you change a control.

## Set the two ends

Under **The two ends**, the first row is the start colour and the second the end colour.

1. Select a swatch to open the colour picker and choose a colour, or
2. type a hex value in the box beside it and press `Enter` or move focus away. Three- or six-digit hex is accepted, with or without `#`, for example `F2B134` or `#abc`.

If the box holds something that is not a colour, it returns to the previous value and a message reads **That is not a colour.**

**Swap the ends** exchanges the start and end colours.

## Start from a preset

**A starting point** offers 25 named pairs. Choosing one sets both ends; the steps, route and easing stay as they are. The pairs are a starting point only and make no claim to be good ramps. The full list is in the [Reference](reference.md).

## Choose a route

Under **Interpolate in**, select one of six routes:

| Route | Space | Hue direction |
|---|---|---|
| **OKLCH, short hue** (default) | OKLCH | The shorter way round |
| **OKLCH, long hue** | OKLCH | The longer way round |
| **sRGB** | sRGB | — |
| **Linear RGB** | Linear RGB | — |
| **HSL, short hue** | HSL | The shorter way round |
| **HSL, long hue** | HSL | The longer way round |

See [Interpolation and gamut](interpolation-and-gamut.md) for how the spaces differ.

## Set the shape

| Control | What it does | Range | Default |
|---|---|---|---|
| **Steps** | The number of colours in the ramp, including both ends | 2 to 32 | 12 |
| **Easing** | Where along the route the steps land | linear, ease-in, ease-out, ease-in-out, step | linear |

The **step** easing gives only five distinct colours, so with more than five steps, neighbouring steps repeat.

## Read the ramp

The note above the ramp repeats your settings, for example **12 steps · OKLCH, short hue · linear**.

- **The ramp** shows one button per step. The first and last are labelled with their hex values underneath. Hover a step to see its hex value; select it to copy the value, and a message confirms, for example **#3E925C copied**.
- A **gold underline** under a step means its chroma was reduced to fit sRGB. The colour you get has the lightness and hue you asked for, on the edge of what sRGB can show.

## Read the differences between steps

**ΔE₀₀ between adjacent steps** draws one bar per gap: 11 bars for a 12-step ramp. Each is the CIEDE2000 difference between two neighbouring colours in the ramp. A line marks the mean, labelled with its value.

- Flat bars mean each step looks as far from the next as every other.
- A tall bar is a visible seam, where the ramp jumps.
- Bars are highlighted in two stronger colours when a difference reaches 2 and 5.

Hover a bar to see its value, for example **step 3 to 4: ΔE₀₀ 8.12**.

## Read the figures

| Card | Meaning |
|---|---|
| **mean ΔE₀₀** | The average difference between neighbouring steps |
| **evenness** | The standard deviation of those differences; lower is more even. The card is highlighted when it is under 15% of the mean |
| **largest jump** | The largest difference, with the steps it lies between, for example **step 10 → 11** |
| **moved to fit sRGB** | How many steps had their chroma reduced; the card is highlighted when any were |

With the default ends, 12 steps, **OKLCH, short hue** and **linear**, the figures are a mean of 8.26, an evenness of 0.69, a largest jump of 9.36 between steps 10 and 11, and 4 steps moved to fit sRGB.

## Read the hue circle

**Where the ramp goes in hue and chroma** plots every step in OKLCH: the angle round the circle is hue, and the distance from the centre is chroma. Spokes mark every 30°, the four quarters are labelled 0°, 90°, 180° and 270°, and the label on the outer ring gives the largest chroma in the ramp, which sets the scale. A gold line joins the steps in order.

- A route that crosses from, say, 350° to 10° draws a short arc across the 0° spoke, not a line across the whole plot.
- Steps whose chroma was reduced are outlined in amber.
- A ramp through grey passes close to the centre.

## View it with a colour-vision deficiency

Under **Show it as seen by**, select **Protan**, **Deutan** or **Tritan** to redraw the ramp, the hue circle dots and the contrast samples as they would look with protanopia, deuteranopia or tritanopia. **Normal vision** returns to the true colours. The figures, the copied values and the exports always use the true colours. See [Check contrast and colour vision](check-contrast-and-colour-vision.md).

## What you should see

A ramp whose bars are as flat as you need, a low **evenness**, and a hue path that goes where you intend, ready to export.
