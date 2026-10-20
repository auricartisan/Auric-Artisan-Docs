---
title: Tonal Steps — Make tints, shades, tones and key sets
description: Build tints, shades, tones, a neutral ladder and 50–950 or 50–900 key sets, and choose the space they are mixed in.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Make tints, shades, tones and key sets

## The sets

| Set | How it is made | Number of swatches |
| --- | --- | --- |
| **Tints — toward white** | Your colour mixed with white in equal steps, from 0% (your colour) to 100% (white) | Steps + 1 |
| **Shades — toward black** | Your colour mixed with black, from your colour to black | Steps + 1 |
| **Tones — toward grey** | Your colour mixed with mid grey (#808080), from your colour to that grey | Steps + 1 |
| **Neutral ladder** | Greys from black to white; each value is (i ÷ (steps − 1))^γ | Steps |
| Key set 50–950 | Keys 50, 100 … 900, 950. Below 500 your colour is mixed towards white by (1 − key ÷ 500); 500 is your colour; above 500 it is mixed towards black by ((key − 500) ÷ 500) | 11 |
| Key set 50–900 | The same ladder with keys 50 to 900 | 10 |

The key sets borrow the Tailwind and Material key names only. They are not the Tailwind or Material palettes: Tailwind's colours are hand-tuned per hue, and Material's tonal palettes are specified in HCT at fixed tones.

## Mixing spaces

The **Mix in** setting chooses the space in which tints, shades, tones and key sets are interpolated. It changes the middle of a mix, not its ends.

| Choice | Effect |
| --- | --- |
| **OKLab** (default) | Perceptually even mixes; hues stay steady |
| **CIELAB** | Mixes in CIE L\*a\*b\* against D65 |
| **HSL** | Mixes in hue, saturation and lightness |
| **sRGB linear** | In the current version this produces the same mixes as OKLab |

## Steps

1. On the **Lab** tab, set the base colour, **Steps** and **Mix in**.
2. Under **Also show**, tick any of **Tints — toward white**, **Shades — toward black**, **Tones — toward grey** and **Neutral ladder**. **Full ramp** is on by default.
3. Read **The other sets**. Each set is titled with its swatch count. Each tile shows its HEX and, beneath it, its contrast ratio against black; hovering shows the HEX, luminance Y and that ratio.
4. For a key set, open the **Ramps** tab and choose **50–950** or **50–900** under **Key sets**. **Design-scale key sets** lists the ladder.
5. To export a key set, open **Export** and choose **The key set** ([Export tokens](export-tokens.md)).

## Result

You have tints, shades, tones, greys and a keyed ladder built from one colour, mixed in the space you chose.
