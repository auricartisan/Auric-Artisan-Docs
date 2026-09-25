---
title: M-Gradient Palette — Export a ramp
description: Copy the ramp as a CSS gradient, custom properties, a hex list or SVG, save an SVG, and save the JSON reading.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# Export a ramp

All exports are on the **Export** tab, under **Take it away**. They always use the true colours, whatever **Show it as seen by** is set to.

| Button | What you get |
|---|---|
| **Copy the CSS gradient** | A CSS `linear-gradient` from the two ends, in the space of your route |
| **Copy the custom properties** | One CSS custom property per measured step |
| **Copy the hex list** | The steps' hex values, one per line |
| **Copy the SVG** | An SVG gradient built from the measured steps |
| **Save the SVG** | The same SVG, downloaded as `ramp.svg` |
| **Save the reading** | A JSON record of the ramp and its measurements, downloaded as `ramp-reading.json` |

A message confirms each copy, for example **Custom properties copied** or **12 colours copied**. If the browser blocks the clipboard, it reads **The browser refused the clipboard.**

The table under **What leaves this page** gives the size of each form for your ramp and what each is good for.

## The CSS gradient

The CSS gradient asks the browser to do the blending, from your two ends:

| Route | Copied text |
|---|---|
| OKLCH, short hue | `background: linear-gradient(in oklch shorter hue, #0B3D5C 0%, #F2B134 100%);` |
| OKLCH, long hue | `background: linear-gradient(in oklch longer hue, #0B3D5C 0%, #F2B134 100%);` |
| HSL, short or long hue | As above, with `in hsl` |
| Linear RGB | `background: linear-gradient(in srgb-linear, #0B3D5C 0%, #F2B134 100%);` |
| sRGB | `background: linear-gradient(#0B3D5C 0%, #F2B134 100%);` |

The copied text is laid out over two lines, as shown in the preview.

> **Important:** The CSS gradient carries only the two ends and the space. It does not carry your step count or easing, and it is smooth rather than stepped. Browsers that do not support interpolation in a named space fall back to sRGB, which is no longer the ramp you chose. A browser also brings out-of-gamut colours back into range in its own way, which may differ from this tool's chroma reduction.

## The custom properties

The custom properties hand over the exact steps the tool measured:

```css
--ramp-01: #0B3D5C;
--ramp-02: #004B63;
--ramp-03: #005A67;
--ramp-04: #00686A;
--ramp-05: #00776B;
--ramp-06: #0E8666;
--ramp-07: #3E925C;
--ramp-08: #649C50;
--ramp-09: #88A441;
--ramp-10: #ACAA32;
--ramp-11: #D0AE2A;
--ramp-12: #F2B134;
```

This is the default ramp. Paste the lines inside a rule such as `:root { … }`. Use them for design tokens, and anywhere a browser might not support the space.

## The hex list

**Copy the hex list** copies the same steps as plain hex values, one per line, in capitals.

## The SVG

The SVG is 600 × 80 pixels: a rectangle filled with a linear gradient whose stops are the measured steps, spaced evenly from 0% to 100%. Use it to hand the ramp to a drawing program.

```text
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="80">
  <defs><linearGradient id="ramp" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0.00%" stop-color="#0B3D5C"/>
    …
    <stop offset="100.00%" stop-color="#F2B134"/>
  </linearGradient></defs>
  <rect width="600" height="80" fill="url(#ramp)"/>
</svg>
```

Between its stops, the SVG is blended by the program that displays it, usually in sRGB.

## The reading

**Save the reading** downloads `ramp-reading.json`, shown under **The reading that goes with it**:

| Field | Contents |
|---|---|
| `tool` | The tool's name |
| `ends` | The two end colours |
| `route`, `easing`, `steps` | Your settings; the route as an id such as `oklch-short` |
| `colors` | Every step's hex value |
| `measured` | `meanDeltaE00`, `evenness`, `largestJump` (three decimals) and `gamutMapped` (a count) |
| `contrast` | The algorithm (`APCA-W3 0.1.9`), the text colour, and each step's APCA Lc and WCAG 2 ratio |
| `notHeld` | What the reading does not cover: colour-vision deficiency below full severity |

The route ids are `oklch-short`, `oklch-long`, `srgb`, `linear`, `hsl-short` and `hsl-long`.

## Which to use

- For a design system or a data scale, use the **custom properties** or the **hex list**: they are exactly the measured steps.
- For a smooth background, use the **CSS gradient**, and check it in the browsers you support.
- For a drawing program, use the **SVG**.
- To record what was measured, or to hand the ramp to someone else to check, keep the **reading**.
