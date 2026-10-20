---
title: Browser extension — Scale
description: Generate Tailwind and Material colour scales, tints, shades and tones from one colour, inspect each step, and export the scale.
product: Browser extension › Colour
updated: 2026-09-25
---

# Scale

Scale (the Scale generator) turns one colour into a full set of steps you can use as a design system's colour scale. Open it from the Picker's Scale pane (**Open the scale generator →**) or search for "Scale".

## Build a scale

1. Set the base colour with its swatch or type a HEX value.
2. Choose the scale type:

   | Type | Steps | Built in |
   |---|---|---|
   | **Tailwind 50–950** (the default) | 11 steps, labelled 50 to 950 | OKLCH, fitted to the sRGB gamut |
   | **Material 50–900** | 10 steps, labelled 50 to 900 | OKLCH, fitted to the sRGB gamut |
   | **Tints** | 11 steps toward white | HSL |
   | **Shades** | 11 steps toward black | HSL |
   | **Tones** | 11 steps of saturation at the same lightness | HSL |

   A chip beside the name shows **OKLCH · perceptual** or **HSL**. The Tailwind and Material scales use even steps of perceived lightness with the hue held constant, so neighbouring steps look evenly spaced.

3. Type a **Scale name** (up to 32 characters; `brand` by default). Every export uses it.

Each step shows its label in black or white, whichever is more readable on it. The step nearest your base colour is marked, and its tooltip says "your color".

## Look at one step

Choose a step for its detail card: HEX, RGB, HSL and `oklch()` values with copy buttons, and:

- **Make base**: rebuild the scale around this step;
- **Pick**, **Contrast** and **Harmony**: open the step in that tool.

## Export

| Group | Button | Result |
|---|---|---|
| **Copy** | **CSS** | CSS variables named after the scale, copied |
| | **SCSS** | SCSS variables, copied |
| | **oklch()** | CSS variables with `oklch()` values, copied |
| | **JSON** | JSON, copied |
| **Framework** | **Tailwind** | A Tailwind colour object, copied |
| | **@theme** | A Tailwind v4 `@theme` block, copied |
| | **Tokens** | W3C design tokens, copied |
| **Export** | **SVG** | An SVG of the scale with its labels, copied |
| | **PNG** | A PNG of the scale with its labels |
| | **Save** | Saves the scale's CSS to Code › Snippets |

## Related pages

- [Picker](picker.md)
- [Snippets](../code/snippets.md)
- [Code export formats](../code/code-export.md)
