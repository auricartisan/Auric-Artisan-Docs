---
title: Collage Maker — Export, copy and save sessions
description: Save your collage as PNG or JPEG at the size you need, copy it to the clipboard, and save or reload the layout as a session file.
product: Website › Tools › Image and file tools › Collage Maker
updated: 2026-09-25
---

# Export, copy and save sessions

All exports are on the **Export** tab.

## What an export contains

The exported image is the canvas drawn again at the scale you choose. It contains:

- every visible picture, at its position, scale, rotation, opacity and flip;
- the background: transparent, or white when **Transparent background** is cleared;
- the rounded corners set by **Corner radius**, scaled with the export.

It does not contain:

- the guides, the selection outline, the corner handles or the chequerboard, which are only on screen;
- hidden pictures;
- any part of a picture outside the canvas. The **outside the canvas** card on the **Studio** tab tells you how much that is.

## Set the size and quality

Under **What to take**:

| Control | What it does | Range | Default |
|---|---|---|---|
| **Scale** | Multiplies the canvas size for the export | 0.25× to 4×, in steps of 0.25 | 1.00× |
| **JPEG quality** | Compression quality for JPEG only | 0.10 to 1.00 | 0.92 |

The **size** line shows the export size in pixels, for example `2400 × 1800` at 2×, and **background** shows transparent or the colour in use. Pictures are drawn from their own pixels, so exporting larger than 1× is sharp for pictures that were scaled down, and soft for any picture scaled above its own size.

## Save an image

1. Set **Scale** and, for JPEG, **JPEG quality**.
2. Select **Save the PNG** or **Save a JPEG**.
3. Your browser downloads `collage.png` or `collage.jpg`. A message confirms the format and file size, for example **Saved PNG · 2.4 MB**.

If there is nothing on the canvas, the message reads **Nothing on the canvas yet.** and nothing is saved.

### PNG or JPEG

The table under **What leaves this page** shows the real size of each file for your collage, measured by encoding it before you save.

| Format | Carries | Good for |
|---|---|---|
| PNG | Lossless pixels with transparency | A transparent background, text and hard edges |
| JPEG | Lossy pixels, no transparency | Photographs, where a smaller file matters |
| Session JSON | The layout, not the pictures | Coming back to the collage later |

> **Important:** JPEG cannot store transparency. Clear **Transparent background** on the **Studio** tab before saving a JPEG, so empty areas and rounded corners are white rather than left to your browser's encoder.

The same quality setting gives slightly different files in different browsers, because each browser has its own JPEG encoder.

## Copy to the clipboard

Select **Copy to the clipboard** to place a PNG of the collage, at the current export scale, on your clipboard. Paste it into another application.

- If your browser cannot put images on the clipboard, the message reads **This browser will not take an image from the clipboard.**
- If the browser refuses permission, it reads **The browser refused the clipboard.**

## Save and load a session

A session file records the layout so you can come back to it. It saves the canvas shape and size, padding, gap, corner radius and background, and for every picture its file name, position, own size, scale, rotation, opacity, flips and whether it is visible.

> **Important:** A session file does not contain the pictures. Keep the original files; you need them to reopen the collage.

### Save a session

1. Select **Save the session**.
2. Your browser downloads `collage-session.json`. The message reminds you: **Session saved. It describes the layout, not the pictures.**

### Load a session

1. On the **Studio** tab, add the same pictures, in the same order you originally added them. The session is applied to pictures by their position in the stack, bottom first.
2. On the **Export** tab, select **Load a session** and choose the `.json` file.
3. The canvas settings are applied, and each loaded picture takes the position, scale, rotation, opacity, flips and visibility stored for it. The message reads, for example, **Session applied to the 4 pictures you have loaded.**

Loading a session is one history step, so **Undo** returns to the layout you had before.

If you load a session before adding any pictures, only the canvas settings are applied. Add the pictures, then load the session file again. A file that the tool did not write produces the message **That is not a session file this page wrote.**

## Save the reading

**Save the reading** downloads `collage-reading.json`, a short record of what was measured, to keep beside the image. The same text is shown under **The reading that goes with it**. It holds:

- the canvas width, height and background;
- the number of pictures;
- under `measured`: `covered`, `overlapping` and `outsideCanvas` as fractions (0 to 1, four decimal places), and `at`, which says whether they were measured at export resolution or at a reduced size;
- under `choices`: whether enlarging past 100% was off, the snap step, and the JPEG quality;
- under `notHeld`: the things the reading does not know, physical print size and output density.

```json
{
  "tool": "Auric Artisan — collage",
  "canvas": { "w": 1200, "h": 900, "background": "transparent" },
  "pictures": 4,
  "measured": {
    "covered": 0.8123,
    "overlapping": 0,
    "outsideCanvas": 0,
    "at": "export resolution"
  },
  "choices": { "neverEnlargeBeyond": 1, "snapStep": 10, "jpegQuality": 0.92 },
  "notHeld": ["physical print size", "output density"]
}
```

The figures in this example are illustrative; your reading contains the values measured for your collage.

## What you should see

After saving, you have an image file at the size shown on the **Export** tab, without any on-screen guides or outlines, and optionally a session file and a reading to go with it.
