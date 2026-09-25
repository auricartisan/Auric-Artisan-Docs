---
title: SVG Recolour — Recolour an SVG
description: Load an SVG, understand what colours the tool finds and where, remap and swap colours, choose how they are written, and read the Mapping tab.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# Recolour an SVG

## Load a file

On the **Recolour** tab, under **The file**, use any of these:

| Method | How |
|---|---|
| Drop | Drop an `.svg` file on **Drop an SVG** |
| Choose | Select **Drop an SVG** (or press `Enter` or `Space` while it has focus) and choose an `.svg` file |
| Paste | Paste SVG markup into the box under **Or paste the markup**, then select **Read the markup** |
| Sample | Select **Load the sample**; its markup also appears in the paste box |

A message confirms, for example **Loaded logo.svg** or **Loaded the pasted markup.** Loading a new file replaces the previous one and resets every mapping.

### If the file will not parse

The file must be well-formed XML. If it is not, nothing is changed, the message reads **That file will not parse as SVG, so nothing was changed.**, and a warning under the paste box gives the parser's own complaint. A file is never half-recoloured.

### Active content in the preview

An SVG can carry scripts, event handlers and `javascript:` links. Before drawing the previews, the tool removes `script`, `foreignObject` and `handler` elements, every attribute starting with `on`, and any `href` or `xlink:href` that starts with `javascript:`. If anything was removed, a notice above the previews lists it, for example `1 <script>, 2 onclick handlers`.

This applies to the previews only. The exported file is rewritten from your original file and still contains whatever it contained. See [Privacy](../others/privacy.md).

## What the tool finds

The tool looks for colours in eight paint properties:

`fill`, `stroke`, `stop-color`, `flood-color`, `lighting-color`, `color`, `solid-color`, `text-decoration-color`

It looks in three places:

- **presentation attributes**, such as `fill="#E5484D"`;
- **style attributes**, one declaration at a time, such as `style="fill: red; stroke: #000"`;
- **style sheets** inside `<style>` elements, one colour-valued declaration at a time.

Each place a colour appears is one **occurrence**. The tool reads these colour forms:

| Form | Examples |
|---|---|
| Six-digit hex | `#E5484D` |
| Three-digit hex | `#ABC` |
| Hex with alpha | `#E5484D80`, `#ABC8` |
| `rgb()` and `rgba()` | `rgb(62, 99, 221)`, `rgba(62 99 221 / 0.5)` |
| `hsl()` and `hsla()` | `hsl(220, 70%, 55%)` |
| CSS colour names | `red`, `rebeccapurple` and all 148 names |

Some values are paint but not a colour the tool can change. They are listed, counted and left alone:

| Value | Shown as |
|---|---|
| `none`, `transparent` | No paint |
| `currentColor` | Resolves from CSS outside this file |
| `inherit`, `initial`, `unset`, `revert`, `context-fill`, `context-stroke` | Resolves from outside this file |
| `url(#gradient)` | A reference, not a colour |

Colours written in other forms, such as `oklch()`, `lab()` or `var(--brand)`, are not recognised, and are neither counted nor changed.

## The colour list

**Every colour in the file** has one row per distinct colour, however many ways it is written, most-used first. `#F00`, `#ff0000`, `rgb(255,0,0)` and `red` are the same row.

| Part of the row | Meaning |
|---|---|
| Left swatch | The colour as it is now |
| Hex and note | The colour, with its CSS name or the nearest name prefixed "near", and how many places use it |
| Right swatch | What it should become; select it to choose |
| Right-hand hex and note | The target colour, and **unchanged** or **written in** N **places** |
| Count | How many places were actually written, or **—** when unchanged |

Rows greyed out are values with no colour to change: they read **left alone**, with the reason, and **not held**.

## Remap a colour

1. Select the right-hand swatch in the row.
2. Choose the new colour in the colour picker.
3. The **After** preview and the row update at once. Setting a colour back to its original value marks the row **unchanged**.

Every occurrence of that colour, in every form and every place, is rewritten. The heading of the **After** preview reads, for example, **4 of 5 written**: occurrences written out of those that can be written.

### Swap two colours

Set colour A's target to colour B, and colour B's target to colour A. The tool plans every change from the original file before writing anything, so the two colours trade places cleanly.

### Undo your changes

**Put every colour back**, under **Recolour from a harmony**, returns every target to its original colour. The message reads **Every colour back to what it was.**

## Choose how colours are written

Under **Write colours as**:

| Option | What is written |
|---|---|
| **Write hex** (default) | Every changed colour as six-digit hex in lower case, for example `#00aa00` |
| **Keep the source form** | Each changed colour in the form it was found in, as far as possible |

With **Keep the source form**:

- a colour written as a name is written as a name if the new colour has an exact CSS name, and as hex if it does not;
- `rgb()` stays `rgb()`, and `rgba()` keeps its alpha;
- `hsl()` stays `hsl()`, and `hsla()` keeps its alpha;
- hex written in capitals stays in capitals;
- a three-digit shorthand is written as full six-digit hex, because very few colours have a three-digit form.

In both styles, a hex colour with an alpha part, such as `#E5484D80`, is written as six-digit hex, so its transparency is lost when you change it. Only changed occurrences are rewritten; everything else in the file is left exactly as it was.

## What the file holds

| Card | Meaning |
|---|---|
| **elements** | Elements in the parsed document, including the root |
| **occurrences** | Places a colour value is written |
| **colours** | Distinct colours the tool can change |
| **left alone** | Values with no colour to change |
| **written** | Occurrences the export will carry as changed |
| **closest pair** | The smallest CIEDE2000 difference between any two colours under the three colour-vision simulations; highlighted below 8 |

The note above the previews repeats elements, occurrences and colours.

## The Mapping tab

The **Mapping** tab lists every colour with what will happen to it:

| Column | Meaning |
|---|---|
| Swatch | The original colour |
| **In the file** | The hex value, or the keyword for a value left alone |
| **Used** | Number of occurrences |
| **Becomes** | The target, or **unchanged** or **left alone** |
| **Written** | Occurrences written; highlighted when it equals **Used** |
| **Where, and what happened** | How many are attributes, in a style attribute or in a style sheet, and the forms they were written in |

The note under the table adds up the file: how many occurrences were written, how many left because nothing was asked of them, and how many could not be written, by keyword. The three always add up to the total.

Below it, **Two colours trading places** and **What the count used to mean** show, with measured examples, why an earlier version of the tool could not swap colours and miscounted them.

## What you should see

The **After** preview shows your new colours, each row reports **written in** N **places**, and the **written** count matches the number you expect.
