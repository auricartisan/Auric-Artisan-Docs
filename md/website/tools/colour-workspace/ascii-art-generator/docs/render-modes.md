---
title: ASCII Art Generator — Render modes and full screen
description: The Text, HTML, Canvas and SVG renders, the readouts under the art, and the full-screen view.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Render modes and full screen

The **Render** chips above the art choose how it is shown. The characters are the same in every mode; what changes is how they are drawn and what they can carry.

## The four renders

| Chip | Shows the art as | Colour | Filters | Best for |
| --- | --- | --- | --- | --- |
| **Text** | Plain characters in the page's text colour | No | Yes | Copying and pasting |
| **HTML** | Characters in coloured runs on your paper colour | Yes | No | Colour art on screen and the HTML download |
| **Canvas** | A picture drawn at the output font and size | Yes | Yes | A pixel-exact PNG |
| **SVG** | Vector text, one line per row | Yes | Yes | Scalable art and the SVG download |

- **Colour** means the render can show **From image** colour. See [Looks, colour and detail](looks-colour-and-detail.md).
- **Filters** means the render shows the filters from **Fine tuning**. The HTML render always shows the art before filters.
- Choosing **From image** switches to **HTML**, and choosing **Mono** switches back to **Text**. You can pick another chip afterwards.

The Text and HTML renders are scaled to fit the stage. The Canvas and SVG renders are drawn at the **Size** set under **Type** in **Fine tuning**, and shrink to fit the stage width if they are wider.

## The readouts

The footer under the art shows:

- **Grid**: columns × rows, for example **100 × 42**;
- **Chars**: the number of characters;
- **Render**: how long the last conversion took, in milliseconds.

The render time also appears beside the **Render** chips. The **Analysis** tab repeats these figures with the character set, glyph count, sampler and dithering. See [Charts, benchmark and Compare](charts-and-compare.md).

## Copy

**Copy** in the footer copies the plain characters to your clipboard, with filters applied, whichever render is showing. The message **Copied!** confirms it. To copy with colour for a terminal, use **Copy for terminal** in **Export**. See [Copy, export and batch](export.md).

## Full screen

**Full screen** opens the art over the whole window on a dark background.

- For the Canvas render, it shows the canvas picture.
- For the other renders, it shows the plain characters in gold, without colour.

Close it with **×** in the top-right corner.

## Related

- [Copy, export and batch](export.md)
- [Fine tuning](fine-tuning.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
