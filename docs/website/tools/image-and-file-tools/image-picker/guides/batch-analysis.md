---
title: Image Picker — Analyse a list of hex colours
description: Use batch colour analysis on the Actions tab to get RGB, HSL, CIELAB, LCH, luminance and tone band for a list of hex colours.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Analyse a list of hex colours

**Batch colour analysis** gives the same figures the palette uses for any list of colours you type or paste. No picture is needed.

## Run a batch

1. Open the **Actions** tab.
2. In the box under **Batch colour analysis**, type or paste hex colours. Separate them with new lines, commas, semicolons or spaces. The `#` is optional.

```text
#D3AF37
#735244
#4A90D9
#E84855
#3BB273
```

3. Select **Run batch**.
4. A table appears under the box, one row per colour.

## The results table

| Column | Meaning | Example |
|---|---|---|
| **#** | Position in your list | 1 |
| **Swatch** | The colour | — |
| **Hex** | The colour as six-digit hex, in capitals | #D3AF37 |
| **RGB** | Red, green, blue, 0 to 255 | 211,175,55 |
| **HSL** | Hue, saturation, lightness | 46° 64% 52% |
| **Lab** | CIELAB lightness, a*, b*, for a D65 white | 72.8,0.9,62.8 |
| **LCH** | CIELAB lightness, chroma, hue angle | 72.8,62.8,89° |
| **Lum** | WCAG relative luminance, 0 to 1 | 0.4478 |
| **Tone** | Shadow, Midtone or Highlight | Midtone |

The example column shows the row for `#D3AF37`. The tone bands use the same limits as the **Workbench**: below 0.18 is a Shadow, below 0.65 a Midtone, and 0.65 or above a Highlight.

## Input rules

- Three-digit hex values such as `#abc` are expanded to six digits (`#AABBCC`).
- Entries that are not hex values are skipped.
- Use three- or six-digit hex. The box accepts four- and eight-digit values (with an alpha part), but they are not read as the colour you mean, so remove the alpha digits first.

## Messages

| Message | When |
|---|---|
| **Click Run batch to analyse colours.** | Before the first run |
| **Enter hex colours above.** | The box is empty |
| **No valid hex colours found.** | Nothing in the box is a hex value |

## Uses

- Check a brand palette's luminance and tone spread without an image.
- Get CIELAB and LCH values for a list of colours to paste into a specification.
- Compare colours you pinned from a picture: copy the JSON, take the `picks`, and paste their hex values here.
