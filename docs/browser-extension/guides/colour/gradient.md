---
title: Browser extension — Gradient
description: Build a linear, radial or conic CSS gradient from two or more stops, choose the interpolation space, and copy or save the CSS.
product: Browser extension › Colour
updated: 2026-09-25
---

# Gradient

Gradient builds a CSS background gradient and writes the declaration for you.

## Build a gradient

1. Open Colour › **Gradient**. It starts with two stops: gold at 0% and near-black at 100%.
2. For each stop, set its colour and its position with the slider or the number field (0 to 100%).
3. Choose **+ Stop** to add a stop between the last two. Choose a stop's **✕** button to remove it; a gradient keeps at least two stops.
4. Choose the type: **Linear**, **Radial** or **Conic**.
5. Set the angle in degrees (0 to 360). It sets the direction of a linear gradient and the starting angle of a conic one.
6. Choose the interpolation space: **sRGB**, **OKLCH** or **HSL**.

The preview and a colour track update as you change anything, and the CSS appears below them.

## Interpolation spaces

- **sRGB** uses your stops as they are; the browser blends between them. Blends between very different hues can look grey in the middle.
- **OKLCH** and **HSL** write out 13 evenly spaced stops calculated in that space, so the middle of the gradient stays vivid.

> **Note:** The OKLCH option currently mixes in OKLab, the rectangular form of the same colour space. Results are close to OKLCH but hue paths between distant hues can differ.

## The CSS

The output is a `background:` declaration, for example:

```css
background: linear-gradient(90deg, #d3af37 0%, #0d080b 100%);
```

Radial gradients are written as `radial-gradient(circle, …)` and conic ones as `conic-gradient(from 90deg, …)`.

## Buttons

| Button | What it does |
|---|---|
| **Copy** | Copies the declaration |
| **Save snippet** | Saves the declaration to Code › Snippets, titled by its type (for example "linear gradient") |
| **Random** | Makes a new gradient of 2 to 4 random stops at a random angle |
| **Reverse** | Reverses the order and positions of the stops |

## Related pages

- [Snippets](../code/snippets.md)
- [Mix](mix.md)
