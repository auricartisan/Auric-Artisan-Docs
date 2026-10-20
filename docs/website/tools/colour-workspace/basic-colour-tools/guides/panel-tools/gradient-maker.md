---
title: Gradient Maker — Build and export a gradient
description: Build linear, radial and conic gradients with any number of stops, choose the colour space they blend in, add easing, and export CSS, SVG, PNG, JSON or Tailwind.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Gradient Maker

Gradient Maker builds CSS gradients. You set a type (linear, radial or conic), add colour stops along a track, and choose how the colours blend between stops. It shows a large live preview, charts of how lightness, chroma and hue change along the gradient, nine presets, and export options for code and images.

A **colour stop** is a colour pinned at a position along the gradient, from 0 % (the start) to 100 % (the end). **Interpolation** is the colour space the gradient blends in between stops: blending in sRGB (what CSS does by default) can pass through dull or dark middles, while blending in OKLCH keeps lightness and saturation more even. **Easing** changes the pace of the blend along the gradient.

Gradient Maker is in the **Generate** category at the **Basic** level.

## Open it

In the Workspace view, select **Gradient Maker** in **Open a tool**. It opens with a two-stop linear gradient from gold (#D3AF37) to deep blue (#1D2A3E) at 90 degrees.

## Screen tour

### Sidebar

- **Type**: **Linear**, **Radial** or **Conic**.
- **Angle**: the direction in degrees. Hidden for radial gradients.
- **Interpolation**: **sRGB (native CSS)**, **OKLCh (perceptual)**, **HSL** or **CIE Lab**.
- **Easing**: **Linear**, **Ease in**, **Ease out**, **Ease in-out** or **Sine**.
- **Reverse**, **+ Stop**, **Even** and **Random**.
- **Export**: **Copy CSS**, **SVG**, **1600px**, **4K**, **JSON** and **Tailwind**.

### Main area tabs

| Tab | What it shows |
| --- | --- |
| **Design** | The preview, the stop track, and the **Stops** list with a count, for example **Stops (3)**. |
| **Curves** | Four charts of the gradient's colour along its length. |
| **Presets** | Nine ready-made gradients. |
| **Export** | Read-only boxes with the CSS, SVG and JSON code. |

### The stop track and list

The track under the preview shows the gradient left to right with a round marker for each stop.

- Select an empty spot on the track to add a stop there. Its colour is a straight sRGB blend of the two stops either side of that point.
- Select a marker to highlight it.

The **Stops** list has one row per stop:

- A colour well: select it to choose a colour.
- A HEX text box: type a six-digit or three-digit HEX code.
- A position slider from 0 to 100 in steps of 0.5, with the position shown as a percentage.
- A **✕** remove button, shown while there are more than two stops.

## Tasks

### Build a three-colour gradient

1. Select **+ Stop**. A new stop with a random colour appears at 50 %.
2. In its row, type a HEX code or use the colour well.
3. Drag its position slider to where you want it.
4. Select **Even** to space all stops evenly.
5. Change **Type** to **Radial** to see a circular version, or back to **Linear** and set **Angle** (0 to 360).

Result: the preview shows your gradient and updates with every change.

### Make the blend perceptually smooth

1. Set **Interpolation** to **OKLCh (perceptual)**.
2. Open the **Curves** tab. Compare the **Lightness across gradient** chart with the sRGB result: the line becomes smoother.
3. Try an **Easing** such as **Ease in-out** to hold the end colours longer and move quickly through the middle.

Result: a gradient without a muddy middle. The CSS output now contains 20 generated stops that imitate the chosen blend, because CSS blends in sRGB unless told otherwise.

### Start from a preset

1. Open the **Presets** tab.
2. Select a preset. It loads and the panel switches back to the **Design** tab.
3. Edit its stops as you like.

The presets are **Sunset**, **Ocean**, **Aurora**, **Coral**, **Mint**, **Royal**, **Auric**, **Spectrum** and **Mono dark**.

Result: a starting gradient you can adjust.

### Export the gradient

1. Select **Copy CSS** to copy a declaration such as `background: linear-gradient(90deg, #D3AF37 0.0%, #1D2A3E 100.0%);`.
2. Or select **SVG**, **1600px** or **4K** to download a file.
3. For JSON, open the **Export** tab first, then select **JSON** (see the note below).

Result: code on your clipboard or an image in your downloads folder.

## Other buttons

- **Reverse** mirrors every stop's position, so the gradient runs the other way.
- **Even** keeps the order of the stops and spaces them evenly from 0 % to 100 %.
- **Random** replaces the colours with new ones (keeping the number of stops), evenly spaced in hue around a random starting hue, and spreads the stops evenly.

## Curves

The charts sample the gradient at 60 points, using the current interpolation and easing:

- **Lightness across gradient (samples 60 points)**: OKLCH lightness from 0 to 1.
- **Chroma across gradient**: OKLCH chroma from 0 to 0.4.
- **Hue rotation along gradient**: OKLCH hue from 0 to 360 degrees.
- **CIE 1931 path**: sample points on the chromaticity diagram, with the sRGB triangle drawn dashed.

## Export

| Button | Result |
| --- | --- |
| **Copy CSS** | Copies `background: <gradient>;`. |
| **SVG** | Downloads `gradient.svg`, 800 by 400 pixels. |
| **1600px** | Downloads `gradient.png`, 1600 by 800 pixels. |
| **4K** | Downloads `gradient.png`, 3840 by 1920 pixels. |
| **JSON** | Copies the JSON shown on the **Export** tab: type, angle, interpolation, easing, and each stop's HEX, position and OKLCH values. |
| **Tailwind** | Copies `backgroundImage: { 'gradient': '<gradient>' }` for a Tailwind theme. |

The CSS forms are:

```css
background: linear-gradient(90deg, #D3AF37 0.0%, #1D2A3E 100.0%);
background: radial-gradient(circle at center, #D3AF37 0.0%, #1D2A3E 100.0%);
background: conic-gradient(from 90deg at center, #D3AF37 0.0%, #1D2A3E 100.0%);
```

Notes on each format:

- **CSS**: with **sRGB (native CSS)** or **HSL** interpolation and **Linear** easing, the CSS lists your stops as they are, and the browser blends them in sRGB. With any other combination the CSS lists 20 generated stops that reproduce the chosen interpolation and easing.
- **SVG**: uses your stops as they are, blended in sRGB. SVG has no conic gradient, so a conic gradient is exported as a straight left-to-right gradient.
- **PNG**: with **sRGB (native CSS)** and **Linear** easing the image uses your stops directly; otherwise it uses 40 generated stops. Conic PNGs need a browser that supports conic gradients on a canvas.
- **JSON**: the **JSON** button copies the text in the **Export** tab's JSON box, which is refreshed only while that tab is open. Open the **Export** tab after your last change, then select **JSON**, to copy the current gradient.

Example of the JSON:

```json
{
  "type": "linear",
  "angle": 90,
  "interp": "oklch",
  "easing": "linear",
  "stops": [
    { "hex": "#D3AF37", "pos": 0, "oklch": { "L": 0.766, "C": 0.138, "H": 91.6 } },
    { "hex": "#1D2A3E", "pos": 100, "oklch": { "L": 0.283, "C": 0.041, "H": 258.8 } }
  ]
}
```

The copied JSON is indented over several lines and the OKLCH numbers carry more decimal places than shown here.

## Save to and restore from the Library

With Gradient Maker focused, **Save to Library** saves the gradient with its CSS, stops, type, angle, interpolation and easing. A saved gradient reopens in Gradient Maker with all of those settings, and **Loaded gradient from library** appears.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Type** | Gradient shape. | Linear, Radial, Conic | Linear |
| **Angle** | Direction for linear, starting angle for conic. | 0 to 360 degrees | 90 |
| **Interpolation** | Colour space for blending between stops. | sRGB (native CSS), OKLCh (perceptual), HSL, CIE Lab | sRGB (native CSS) |
| **Easing** | Pace of the blend. | Linear, Ease in, Ease out, Ease in-out, Sine | Linear |
| **Reverse** | Mirrors stop positions. | — | — |
| **+ Stop** | Adds a random stop at 50 %. | No fixed maximum | — |
| **Even** | Spaces stops evenly. | — | — |
| **Random** | New colours, even spacing. | Keeps the stop count | — |
| Track | Select empty space to add a stop; select a marker to highlight it. | 0 % to 100 % | — |
| Stop colour well | Sets a stop's colour. | Any colour | — |
| Stop HEX box | Sets a stop's colour by code. | 3- or 6-digit HEX | — |
| Stop position slider | Moves a stop. | 0 to 100, step 0.5 | — |
| Stop **✕** | Removes a stop. | At least 2 stops remain | — |
| Preset | Loads a preset. | 9 presets | — |
| Export buttons | Copy or download. | See Export | — |

## Accuracy and limits

- The preview and the copied CSS are the same gradient, so what you see is what you copy.
- Non-sRGB blends and easing are approximated with generated stops. Twenty stops in CSS and forty in PNG are enough to look smooth in normal use, but the result is a close imitation, not an exact curve.
- Colours outside the sRGB range during OKLCH or Lab blending are clipped to the nearest displayable colour.
- The HSL blend takes the shorter way round the hue circle.

## Related

- [Panel tools](README.md)
- [Palette Studio](palette-studio.md)
- [Gradient Library](../colour-tools/gradient-library.md) in the Colour Tools workbench
- [Import, export and the Library](../import-export-and-library.md)
- [Troubleshooting](../troubleshooting.md)
