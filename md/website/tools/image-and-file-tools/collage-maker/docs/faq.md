---
title: Collage Maker — FAQ
description: Short answers to common questions about the Collage Maker.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Collage Maker FAQ

## Are my pictures uploaded?

No. Pictures are read in the page and drawn straight to a canvas in your browser. Nothing is sent to a server. See [Privacy](../others/privacy.md).

## What file types can I add?

Any image your browser can open. The drop box names JPG, PNG, WebP and GIF. The export is a still image, so an animated GIF contributes a single frame.

## How many pictures can I add?

The tool sets no fixed limit. Each picture is measured separately for the overlap figure, so very many large pictures make the page slower.

## Can I change the canvas size to something other than the presets?

No. There are six shapes, all 1200 pixels wide. To get a larger file, use **Scale** on the **Export** tab: 4× gives a canvas 4800 pixels wide.

## Can I choose a background colour other than white?

The switch offers transparent or white. A session file that carries another background colour will apply it when loaded, but the page has no colour control of its own.

## Why do the rounded corners appear in my export?

**Corner radius** clips the canvas itself, and the default is 18 px. Set it to 0 px for square corners.

## Why does the export not show the gold outline and the guides?

They are drawing aids shown only on screen. The export contains the pictures and the background, nothing else.

## Does "Fill the cell, crop" actually crop my pictures?

No. It scales each picture to cover its cell, but the part beyond the cell is not cut away; it overlaps the neighbouring pictures or hangs off the canvas. The **Overlap** and **Off-canvas** columns on the **Layout** tab show how much.

## Why is "canvas covered" lower than I expected for a PNG?

The figure reads pixels. Transparent parts of a PNG, and any picture set to 0% opacity, paint nothing and are not counted as covered.

## What is "the old readout said"?

The figure an earlier version of the tool gave: the sum of picture areas divided by the canvas area. It ignores overlap and anything off the canvas, so it is kept only for comparison. Use **canvas covered** instead.

## Does a session file contain my pictures?

No. It records positions, sizes, rotation, opacity, flips, visibility and the canvas settings. Keep your original files, add them in the same order, then load the session.

## Can I undo after clearing the canvas or removing a picture?

Yes. Both are single history steps, and **Undo** brings the pictures back. The history keeps up to 60 steps.

## Does the tool know how big my collage will print?

No. A canvas has pixels and no physical size. Print size depends on the output density you print at, which the tool does not ask for. The reading file lists physical print size and output density under `notHeld`.
