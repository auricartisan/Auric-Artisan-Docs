---
title: Browser extension — Picker
description: Sample a colour from the screen or set one by hand, read it in twelve formats, and use the Picker's Specs, Harmony, Scale, Contrast, Vision and Code panes.
product: Browser extension › Colour
updated: 2026-09-25
---

# Picker

The Picker is the same colour picker auricartisan.com uses, with extra panes for accessibility and code. Open it from Colour › **Picker**, from Home › **Pick a colour**, from the colour of the day, or by choosing any colour swatch in Recent, History, Page palette, Image, Scale or Harmony.

## The colour core

- Spectrum (**Saturation and brightness**): Drag to set saturation and brightness
- **Hue** slider: Drag to set the hue
- **Opacity** slider: Sets transparency. The opacity is carried into every value you copy.
- Value field and **Colour format** menu: Shows the colour in one of twelve formats. Every field is editable. The format menu searches as you type (type "ok" for OKLAB and OKLCH).
- Copy button (**Copy the CSS value**): Copies the ready-to-paste CSS value in the current format

The twelve formats are **HEX**, **RGB**, **HSL**, **HSV**, **HWB**, **CMYK**, **LAB**, **LCH**, **OKLAB**, **OKLCH**, **XYZ** and **P3** (Display P3). The Picker starts in the format chosen in Settings › Tools › **Copy colours as** (HEX, RGB, HSL or OKLCH).

## Actions

- **Pick from page**: Starts the screen eyedropper. Click any pixel on the screen; press `Esc` to cancel. The colour loads into the Picker and joins your history.
- **Save to library** (the bookmark): Adds the colour to Saved › Library, or says it is already there
- **Check as text**: Opens Contrast with this colour as the text colour
- **Check as background**: Opens Contrast with this colour as the background

### When the eyedropper is not available

The screen eyedropper relies on a browser feature that Chromium browsers have and Firefox does not. The Picker first uses its own eyedropper, then asks the page to run one. Where neither exists, it shows: "This browser has no screen eyedropper. The Page palette tool reads every colour the page uses instead." Use [Page palette](page-palette.md), then choose a colour from it.

## The detail panes

In the popup the Picker is split: the core on the left and six tabbed panes on the right. In the side panel and the separate window it is one column, and the panes are sections one below another. The pane you last opened is remembered.

- **Specs** (Specifications): Luminance; contrast against white and black; WCAG pass levels; APCA on white and black; hue family; nearest CSS colour name; **Chroma room sRGB** and **Chroma room P3** (how much more saturated the colour can go before it leaves each gamut); CSS values. Click any value to copy it. **Copy as CSS variables** copies them as a block. **Open the converter →** opens Convert.
- **Harmony** (Harmonies): Complementary, analogous, split complementary, triadic and tetradic partners. **Rotate hue in** HSL (like most tools) or OKLCH (every partner keeps the same perceived lightness). Click a swatch to use it. **Open the full harmony builder →** opens Harmony.
- **Scale** (Tints & shades): An 11-step scale from 50 to 950, built in OKLCH so each step is an even perceptual jump and the hue does not drift. The step nearest your colour is marked. Click a step to use it. **Open the scale generator →** opens Scale.
- **Contrast**: How readable the colour is as text on **White**, **Black** or **Page** (the current page's background): the WCAG 2 ratio and the APCA score. If it fails AA, the closest colour that passes is one click away.
- **Vision** (Colour vision): The colour as people with the four main colour-vision deficiencies see it (protanopia, deuteranopia, tritanopia and achromatopsia), each with ΔE, the perceptual distance from what you picked. Under about 2 the difference is hard to notice.
- **Code**: Ready-to-paste code (see below)
- **Page** (On this page): The colours the current page uses, most frequent first (up to twelve). Click one to pick it. Side panel and window only.
- **Recent**: Colours you picked recently, kept in the extension. Side panel and window only.

### Code formats

| Row | Example output for a colour |
|---|---|
| **CSS** | `--brand: #d3af37;` |
| **CSS · wide gamut** | `--brand: oklch(…);` |
| **Tailwind v4** | `@theme { --color-brand: oklch(…); }` |
| **SwiftUI** | `Color(red: 0.827, green: 0.686, blue: 0.216)`, with `opacity:` when the colour is transparent |
| **Jetpack Compose** | `Color(0xFFD3AF37)` (alpha first) |
| **Android XML** | `<color name="brand">#FFD3AF37</color>` |

## Tips

- Every colour you finish choosing is added to your history, unless Settings › Tools › **Keep a colour history** is off.
- **Sound on pick** in Settings › Tools plays a short tick when a pick or copy lands.
- Colours are also sampled in the right-click menu (**Pick colour**, **Pick colour from image**) and copied straight to the clipboard; see [Right-click menu](../on-websites/right-click-menu.md).

## Related pages

- [Contrast](../check/contrast.md)
- [Harmony](harmony.md), [Scale](scale.md), [Convert](convert.md)
- [Code export formats](../code/code-export.md)
