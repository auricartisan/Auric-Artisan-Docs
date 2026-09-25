---
title: SVG Recolour — Troubleshooting
description: Symptoms you may meet in SVG Recolour, why they happen, and what to do.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# Troubleshooting SVG Recolour

## Loading

| Symptom | Why | What to do |
|---|---|---|
| **That file will not parse as SVG, so nothing was changed.** | The markup is not well-formed XML | Read the parser's message under the paste box; fix the markup (often an unclosed tag or a stray `&`) and try again |
| **Paste some SVG markup first.** | The paste box is empty | Paste the markup, then select **Read the markup** |
| My file is greyed out in the file chooser | The chooser offers `.svg` files | Drag the file onto **Drop an SVG**, or rename it with the `.svg` ending |
| A notice says active content was removed | The file contains scripts, event handlers or `javascript:` links | The previews are safe; remember the exported file still contains them |
| My mappings disappeared | Loading a file, markup or the sample resets every mapping | Set the targets again, or apply a harmony |

## Colours not found or not changed

| Symptom | Why | What to do |
|---|---|---|
| A colour I can see is not in the list | It is written in a form the tool does not read, such as `oklch()` or `var(--brand)` | Rewrite it as hex, `rgb()`, `hsl()` or a CSS name before loading |
| A colour inside a picture did not change | It is part of an embedded raster image, not markup | Recolour the raster image in an image editor |
| A row reads **left alone** | The value is `currentColor`, `none`, `transparent`, a keyword such as `inherit`, or a `url()` reference | Expected. `currentColor` takes its colour from the page the SVG is placed in |
| A gradient did not change | Its colours are in `stop-color` on the gradient's stops, listed as their own rows; the shape's `fill` is a `url()` reference | Change the rows for the stop colours |
| Few colours for a large file | The file is mostly embedded images, or uses `currentColor` | Check **left alone** and **occurrences** under **What the file holds** |
| A semi-transparent colour became solid | It was written as hex with an alpha part, which is rewritten as six-digit hex | Re-add the alpha afterwards, or write the original colour as `rgba()` and use **Keep the source form** |
| Colours I wrote as names came back as hex | **Write hex** is selected, or the new colour has no exact CSS name | Choose **Keep the source form**; names are kept only when the new colour has one |

## Previews and checks

| Symptom | Why | What to do |
|---|---|---|
| The previews are tinted | A colour-vision view is selected under **Show it as seen by** | Select **Normal vision** |
| The **Check** tab says two colours or more are needed | The file has fewer than two changeable colours | Nothing to compare |
| APCA Lc is negative | The text colour is lighter than the background colour | Expected: the sign shows polarity; **Good for** uses the size |
| WCAG and APCA disagree | They measure different things | Treat both as evidence |

## Exports

| Symptom | Why | What to do |
|---|---|---|
| **Nothing loaded.** | No file is loaded | Load a file first |
| The exported file still contains a script | Only the previews are stripped | Remove active content in an editor if you do not trust the file |
| The XML declaration or DOCTYPE is missing | Only the `<svg>` element and its contents are written | Add them back if your workflow needs them |
| Attribute quotes changed | The browser writes the markup back out | This does not change the drawing |
| **The browser refused the clipboard.** | Clipboard access was blocked | Allow clipboard access for the site, or use **Save the recoloured SVG** |
| **This browser will not take text from the clipboard.** | The browser cannot copy text | Use the save buttons |

For help with the site in general, see [Help](../../../../../help/README.md).
