---
title: SVG Recolour — Getting started
description: Open SVG Recolour, find your way around its six tabs, and recolour a first SVG.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# Getting started with SVG Recolour

## Open the tool

Go to https://auricartisan.com/tool/general/tools/svg-recolor/. The page, titled **SVG Recolour**, opens on the **Recolour** tab with a small sample SVG already loaded, so you can try every control straight away.

A note under the heading explains what the numbers on the page are measurements of. It has no close button on purpose.

## The screen at a glance

| Tab | What it is for |
|---|---|
| **Recolour** | Load the file, choose how colours are written, preview before and after, and remap each colour |
| **Mapping** | Every colour, where it is used, what it becomes, and how many places were written |
| **Check** | Contrast of every colour against a text colour, and the colours hardest to tell apart |
| **Data** | Every figure and what it rests on; the tab shows the number of entries (15) |
| **Export** | Save and copy buttons, the custom properties and the report |
| **Reference** | The published sources, and how the tool works step by step |

### The Recolour tab

- **The left-hand panel** holds **The file** (the **Drop an SVG** box, **Load the sample**, a box to paste markup, and **Read the markup**), **Write colours as**, **Show it as seen by**, and **Recolour from a harmony** with **Put every colour back**.
- **The right-hand panel** holds **Before, and after** (two previews on a chequerboard), **Every colour in the file** (one row per colour), and the cards under **What the file holds**.

## Recolour a first SVG

The sample contains six colour uses: a hex fill, an `rgb()` fill, the name `red`, a three-digit shorthand, a colour in a style sheet, and `currentColor`.

1. Under **Every colour in the file**, find the row for `#FF0000`, labelled **red · 1 place**.
2. Select the right-hand swatch in that row and choose a green. The **After** preview changes, the row's right-hand side shows the new hex value with **written in 1 place**, and the count on the far right reads **1 written**.
3. Find the row for `#E5484D` and set it to the colour that `#3E63DD` has, and set `#3E63DD` to the colour `#E5484D` had. The two rectangles trade colours.
4. The row for **currentcolor** is greyed out and reads **left alone**, because that colour comes from outside the file.
5. Read the heading of the **After** preview: for example **3 of 5 written**. Five of the six uses can be written; the sixth is `currentColor`.
6. Open the **Export** tab and select **Save the recoloured SVG**. Your browser downloads `recoloured.svg`, and a message confirms how many occurrences were written.

## Next steps

- To load your own file and understand what is found, see [Recolour an SVG](recolour-an-svg.md).
- To recolour everything at once, see [Recolour from a harmony](use-a-harmony.md).
- To check the result for legibility and colour vision, see [Check contrast and colour vision](check-contrast-and-colour-vision.md).
