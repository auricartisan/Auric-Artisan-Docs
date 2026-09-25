---
title: SVG Recolour — Check contrast and colour vision
description: Measure every colour in the SVG as a background for text with WCAG 2.2 and APCA, find the colours hardest to tell apart, and preview the artwork as seen with colour-vision deficiencies.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# Check contrast and colour vision

The **Check** tab measures the colours the file will have after your changes: the targets, not the originals.

## Contrast against a text colour

1. Open the **Check** tab.
2. Under **Text laid over the artwork**, select the swatch and choose the colour of any text that will sit on the artwork. The default is white, `#FFFFFF`.
3. Read **What can be read on it**. The note beside the heading gives the number of colours checked.

Each colour is treated as a background for text in the chosen colour:

| Column | Meaning |
|---|---|
| **Colour** | The colour's swatch and hex value |
| **WCAG** | The WCAG 2.2 contrast ratio, for example **4.54:1** |
| **Rating** | **AAA** (7:1 and above), **AA** (4.5:1), **AA large** (3:1) or **fail** |
| **APCA Lc** | The APCA-W3 0.1.9 lightness contrast; negative when the text is lighter than the colour |
| **Good for** | APCA's guidance by size of Lc, from **any text** to **not for text** (see the table below) |
| **It used to say** | The Lc an earlier version of this tool printed, struck through |

The two methods measure different things, so a row can pass one and fail the other. Neither is a verdict on the artwork; both describe text laid on that colour.

| Absolute Lc | **Good for** |
|---|---|
| 90 or more | any text |
| 75 or more | body text |
| 60 or more | large text |
| 45 or more | headlines only |
| 30 or more | non-text only |
| Below 30 | not for text |

Under **The Lc that was always zero**, a small table shows what the earlier version printed for four pairs against what APCA gives: the earlier version printed zero for every pair.

## The colours hardest to tell apart

**The two colours hardest to tell apart** compares every pair of colours in the file and reports the closest pair, measured with CIEDE2000, under four kinds of vision:

| Column | Meaning |
|---|---|
| **Seen as** | **normal vision**, **protanopia**, **deuteranopia** or **tritanopia** |
| **The two closest colours** | Swatches as seen under that vision, and the two original hex values |
| **ΔE₀₀ between them** | Their CIEDE2000 difference under that vision |
| **What that means** | **close to indistinguishable** (below 5), **tells apart with effort** (below 12), or **clearly different** |

The row with the smallest difference among the three deficiencies is highlighted. You need at least two colours for this check.

The same figure appears on the **Recolour** tab as the **closest pair** card, highlighted when it is below 8.

## The artwork under three dichromacies

**The artwork under three dichromacies** draws the recoloured file four times, as seen with **Normal vision**, **Protanopia**, **Deuteranopia** and **Tritanopia**, with **closest two** under each: the closest pair's difference, highlighted when below 8.

## Preview with a colour-vision deficiency on the Recolour tab

On the **Recolour** tab, under **Show it as seen by**, choose **Normal vision**, **Protan**, **Deutan** or **Tritan**. Both previews are redrawn as seen with that deficiency. The exports always use the true colours.

| Button | Simulates |
|---|---|
| **Protan** | Protanopia: no working long-wavelength (red) cones |
| **Deutan** | Deuteranopia: no working medium-wavelength (green) cones |
| **Tritan** | Tritanopia: no working short-wavelength (blue) cones |

The simulation follows Machado, Oliveira and Fernandes (2009) at full severity, in linear light. It shows complete loss of one cone type only; milder, more common forms are not shown.

## Using the results

- If two colours are **close to indistinguishable** under a deficiency, change one of them, usually in lightness, and check again.
- If text must sit on a colour, choose a text colour and target colour that pass the standard you work to, under both methods if you can.
- Colours the file does not hold, such as `currentColor`, are not checked, because their value comes from outside the file.
