---
title: Collage Maker — Read the measurements
description: What the canvas covered, overlapping, outside the canvas and history cards measure, and how to use the Measure and Data tabs.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Read the measurements

Under the canvas on the **Studio** tab, a row of cards headed **What is on the canvas** describes the collage. The figures update after every change.

## The five cards

| Card | What it reports | How it is found |
|---|---|---|
| **canvas covered** | The share of the canvas that pictures paint | Measured from the pixels |
| **overlapping** | The share of the canvas painted by two or more pictures | Measured from the pixels |
| **outside the canvas** | The share of total picture area that lies beyond the edges and will not be exported | Computed exactly from positions |
| **history** | How many steps you can undo, back to the start | Counted |
| **the old readout said** | The sum of every picture's area divided by the canvas area | Computed, for comparison only |

The **outside the canvas** card changes colour as a warning when more than 0.1% of picture area is off the canvas.

### canvas covered

The tool draws the canvas twice, once without the pictures and once with them, exactly as the export would. Every pixel that differs between the two drawings is a pixel a picture has put something on. The figure is that count divided by the number of pixels on the canvas.

Because it reads pixels, this figure notices transparency. A PNG cut-out with a transparent background covers only its visible part. A picture at 0% opacity covers nothing.

### overlapping

Each visible picture is drawn on its own, and the tool counts the pixels where two or more pictures have painted. The figure is that count divided by the pixels on the canvas.

### outside the canvas

The tool works out the four corners of each picture after its scale and rotation, clips that shape to the canvas rectangle, and compares what is left with the whole picture. The figure is the share of total picture area that falls outside. It needs no pixels, so it is exact. Hidden pictures are not counted.

A picture hanging off the edge may be exactly what you intended, for example a bleed. The figure is shown on its own so you can decide.

### the old readout said

This card keeps the figure an earlier version of the tool reported: the sum of all picture areas divided by the canvas area. It does not look at where the pictures are, so stacked pictures are counted twice and pictures dragged off the canvas are still counted in full. It is shown beside the measured figures so you can see the difference; do not rely on it.

## Measurement resolution

The measurement is made at the canvas size. For canvases larger than 1,440,000 pixels (for example **9 : 16 — 1200 × 2133**), it is made on a proportionally smaller copy to keep dragging smooth. The label above the canvas says which: **measured at full size**, or **measured at** followed by the size used. At the reduced size the figures agree with a full-size measurement to well under a tenth of a percentage point.

## The Measure tab

The **Measure** tab explains the method with worked examples that are laid out and measured live by the same code the **Studio** uses.

- **One number for three different collages** draws four pictures three ways, **Stacked**, **Spread out** and **Dragged off the canvas**, and shows what the old sum-of-areas figure says (**it said**) beside the measured coverage (**really**) for each. The sum gives the same answer for all three; only the spread-out arrangement is actually covered to that extent.
- Further panels describe how the undo history works, what is and is not written into an export, and two features that were withdrawn because they did not measure the collage.
- The left-hand panel lists **What is measured** (covered and overlapping by pixels, off-canvas by geometry, arrangements by laying them out) and has two buttons, **Bootstrap CI** and **Batch coverage**, that scroll to the notes on the withdrawn features.

## The Data tab

The **Data** tab lists every figure on the page and where it comes from. Each entry has a status:

| Status | Meaning |
|---|---|
| **Measured** | Read from the canvas the export will use |
| **Computed** | Worked out from the layout by arithmetic the entry states |
| **This tool's choice** | A default this tool picked, where someone else might reasonably choose differently |
| **Absent** | Named on the page but not held, with what it would take to hold it |

Use the **Status** buttons on the left to filter the list; each shows how many entries it holds. Select an entry to expand its explanation. The twelve entries cover canvas coverage, overlap, the off-canvas area, the arrangement comparison, the transform arithmetic, the grid cell size, the fitted scale, the export file size, the choice not to enlarge past 100%, the 10 px snap step, the 0.92 JPEG quality default, and physical print size, which the tool does not hold.

Below the list, **Two entries that are gone rather than reclassified** names the two withdrawn features.

## The Reference tab

The **Reference** tab lists the sources behind the tool: the HTML Canvas 2D standard, PNG (ISO/IEC 15948), JPEG (ISO/IEC 10918-1), affine transforms in the plane, and WCAG 2.2 target size and keyboard operation, each marked **Runs**, and one withdrawn citation. Under **The arithmetic**, a table gives the formulas for a picture's corners, the grid cell size, the fitted scale, and each of the three measurements.
