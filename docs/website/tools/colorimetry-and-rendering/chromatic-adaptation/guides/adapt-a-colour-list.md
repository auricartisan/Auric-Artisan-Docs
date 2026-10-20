---
title: Chromatic Adaptation — Adapt a list of colours
description: Paste up to 50 HEX colours and get their adapted values, colour shift and L*C*h° at the current adaptation state.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Adapt a list of colours

**Batch Colour Analysis** on the **Export** tab applies the current adaptation to a list of colours — useful for checking how a brand palette shifts between D65 and D50, or under tungsten light.

## Steps

1. On the **Lab** tab, set the source and destination illuminants, the CAT method, the degree of adaptation D and the time. The batch uses the adaptation applied at the current moment of the timeline, exactly as the image does.
2. Open the **Export** tab and find **Batch Colour Analysis**.
3. Paste HEX colours into the box, one per line. Each must have six digits; the `#` is optional. Up to 50 lines are used; any more are ignored.
4. Select **Run Batch**. A message confirms how many colours were analysed.
5. Read the table:

| Column | Meaning |
| --- | --- |
| **Color** | Your input colour and its swatch |
| **Adapted** | The adapted colour as an sRGB HEX, clipped to the displayable range |
| **ΔE₀₀** | The CIEDE2000 difference between the colour's CIELAB value under the source white and the adapted colour's CIELAB value under the destination white. Green below 1, amber below 3, red from 3 up |
| **L\*** | Lightness of the adapted colour |
| **C\*** | Chroma of the adapted colour |
| **h°** | Hue angle of the adapted colour |

L*, C* and h° are computed against the destination white point.

## Tips

- Lines that are not six-digit HEX values (for example three-digit shorthand such as `#abc`) are skipped. If nothing valid is found, a message asks for valid HEX values.
- A low ΔE₀₀ means the transform keeps the colour's appearance almost unchanged relative to each white; a high one means the adapted value moved a lot.
- The table is not exported as a file. Select and copy it from the page if you need it elsewhere, or use **Export JSON** for the matrix that produced it.

## Result

You have each colour's adapted HEX, its shift in ΔE₀₀ and its lightness, chroma and hue under the destination light.
