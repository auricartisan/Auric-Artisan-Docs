---
title: Accessibility Library — Check your own colours
description: Paste your palette into "Or bring your own" to place each colour on the map and see how much lightness each failing colour needs.
product: Website › Library › Colour libraries › Accessibility Library
updated: 2026-09-25
---

# Check your own colours

**Or bring your own** audits a palette you already have against the current ground and target.

## Steps

1. Choose the ground your palette will sit on, and a target.
2. Click in the box under **Or bring your own** and paste your colours as hex codes, for example `#D3AF37 #8A6D16 #6B7280 #136B39 #B91C1C`. Separators do not matter: spaces, commas or new lines all work.
3. Wait a moment. Each colour is placed on the map as a pin at its real hue and lightness, and appears in the table.
4. Read the table (below). Failing colours also get a line on the map drawn up (or down) to the target line, showing the move they need.
5. Change the ground or target to re-check the whole palette at once.

**Result:** every colour in your palette placed on the map, with a pass or fail and the lightness change each failure needs.

## The table

| Column | Meaning |
| --- | --- |
| **Colour** | The swatch and hex code. |
| **Here** | Its contrast ratio against the current ground; failing ratios are marked. |
| **Lightness** | Its OKLCH lightness as a percentage. |
| **Needs** | **nothing** if it passes; otherwise **+N% lightness**, the change needed at its hue to reach the line; or **unreachable** if no lightness at its hue can pass on this ground. |

The "+N%" is the size of the change. On a dark ground it means lighter; on a light ground it means darker.

## Rules for pasting

- Colours must be hex codes that start with `#`, with 3 to 6 digits (`#ABC`, `#AABBCC`).
- Repeated colours are shown once.
- Up to 24 colours are placed; any beyond that are ignored.
- Other text in the box is ignored, so you can paste a line from a stylesheet.

With nothing pasted, the table says **Paste hexes above to see them placed against this ground.**

## Example

On the default navy ground at **4.5:1**, a mid grey such as `#6B7280` fails and shows a lightness it needs, while a light gold such as `#D3AF37` passes with **nothing** needed.
