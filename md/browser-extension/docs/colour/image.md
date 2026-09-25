---
title: Browser extension — Image
description: Build a palette from an image you drop, paste or choose, or from a capture of the visible tab, entirely on your device.
product: Browser extension › Colour
updated: 2026-09-25
---

# Image

Image builds a palette from a picture. The image is read on your device and never uploaded.

## Get a palette from an image

1. Open Colour › **Image**.
2. Choose how many colours to read: **6 colours**, **8 colours** (the default), **12 colours** or **16 colours**.
3. Give it an image, in any of these ways:
   - drop an image file on the drop area;
   - paste an image from the clipboard;
   - click the drop area (or focus it and press `Enter`) to browse for a file;
   - choose **Capture the visible tab** to use a screenshot of what the current tab shows.

The drop area accepts PNG, JPG, WebP and GIF. A file that is not an image is refused with "Not an image file". Some tabs cannot be captured, such as browser pages; the tool then says "Can't capture this tab".

The image appears with a line such as "8 colors from your image", and the colours below it. To keep extraction fast, the image is scaled down before its colours are counted, and similar colours are merged.

## Look at one colour

Choose a colour to open its detail card, with its name, values and the buttons **Pick**, **Contrast**, **Shades** and **Harmony**, as in [Page palette](page-palette.md).

## Use the palette

| Button | What it does |
|---|---|
| **Open in Page palette** | Loads the colours into Page palette, where every export is available |
| **Copy HEX** | Copies the colours as a HEX list, one per line |
| **Save palette** | Saves the colours to Saved › Library |

## Related pages

- [Page palette](page-palette.md)
- [Library](../saved/library.md)
