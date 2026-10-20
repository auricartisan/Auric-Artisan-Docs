---
title: Collage Maker — Limits and accuracy
description: What the Collage Maker measures, how precisely, and what it does not know.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Limits and accuracy

## What is measured, and how

| Figure | Method | Precision |
|---|---|---|
| **canvas covered** | The canvas drawn with and without the pictures; differing pixels counted | Exact at full size; see resolution below |
| **overlapping** | Each picture drawn alone; pixels painted by two or more counted | As above |
| **outside the canvas** | Each picture's corners after scale and rotation, clipped to the canvas | Exact geometry, no pixels involved |
| **Covered** on the **Layout** tab | Placed area minus pairwise overlap | Exact unless three pictures meet at one point, when it shows a dash |
| Export file sizes | The encoded file, measured before it is offered | Exact for your browser |

Coverage and overlap are read from the same drawing the export uses, so they describe the file you download at 1× scale.

### Measurement resolution

Canvases up to 1,440,000 pixels are measured at full size. Larger canvases (the **9 : 16** and **2 : 3** shapes) are measured on a proportionally smaller copy; the label above the canvas then reads **measured at** followed by the size used. The resulting percentages agree with a full-size measurement to well under a tenth of a percentage point.

### What counts as covered

A pixel counts as covered when any picture changes it. Fully transparent pixels in a picture and pictures at 0% opacity change nothing and are not counted. A picture at low opacity still changes the pixels it sits on, so it counts as covering them.

## Choices the tool makes for you

These are defaults, not rules. Each is listed on the **Data** tab as **This tool's choice**.

| Choice | Default | How to change it |
|---|---|---|
| Never enlarge a picture past 100% when arranging | On | **Enlarge a small picture to fill its cell** on the **Layout** tab |
| Snap step | 10 px | The step is fixed; switch snapping off with **Snap to a 10 px grid** |
| JPEG quality | 0.92 | **JPEG quality** on the **Export** tab |

The same JPEG quality setting produces slightly different files in different browsers, because each has its own encoder. The size shown on the **Export** tab is the size your browser actually produced.

## Limits

- **Canvas sizes.** Six shapes, all 1200 pixels wide. Export scale multiplies them from 0.25× to 4×.
- **Background.** Transparent or white. There is no background colour control.
- **Formats.** PNG and JPEG images, a JSON session and a JSON reading. There is no PDF, SVG or layered file export.
- **Colour.** The canvas works in the browser's standard colour handling (sRGB). It is not a colour-managed publishing workflow, and exported files are 8 bits per channel.
- **Physical size.** A canvas has pixels and no physical size. The tool does not convert to inches or millimetres, because that depends on an output density it does not ask for.
- **Session files** hold the layout only. The pictures must be added again, in the same order, before a session is applied.
- **History** keeps up to 60 steps, and is lost when you reload or leave the page.
- **Animated images** are exported as a still.
- **Performance.** There is no fixed limit on the number of pictures, but every change is measured from pixels, so many large pictures make the page slower.

## What the tool is not

The measurements say how much of the frame your pictures fill and where they overlap. They are not a judgement of composition or quality, and the tool gives no score.
