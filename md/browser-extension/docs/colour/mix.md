---
title: Browser extension — Mix
description: Mix two colours at any percentage in sRGB, linear RGB, LAB, OKLAB or HSL, or blend them with a blend mode, and copy the result.
product: Browser extension › Colour
updated: 2026-09-25
---

# Mix

Mix combines two colours, either by mixing them in a colour space or by blending one over the other.

## Use it

1. Open Colour › **Mix**.
2. Set colour **A** and colour **B** with their swatches or by typing a HEX value. They start as gold and blue.
3. Drag the **Mix** slider (0 to 100%, 50% by default) to set how much of B goes into the result.
4. Choose the colour space to mix in: **sRGB**, **Linear RGB**, **LAB** (the default), **OKLAB** or **HSL**.
5. Choose a blend mode: **Normal** (plain mixing, the default), **Multiply**, **Screen**, **Overlay**, **Darken** or **Lighten**.

An 11-step strip shows the path from A to B, and the result swatch shows the current mix.

6. Choose the result swatch to copy the mixed colour.

## Choosing a space

| Space | Good for |
|---|---|
| sRGB | Matching how most software and older CSS mix colours |
| Linear RGB | Physically based light mixing; midpoints look brighter |
| LAB | Perceptual mixing with even lightness steps |
| OKLAB | Perceptual mixing that keeps hues cleaner than LAB |
| HSL | Travelling around the hue wheel between two hues |

## Related pages

- [Gradient](gradient.md)
- [Glossary](../../others/glossary.md)
