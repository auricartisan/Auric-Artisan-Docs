---
title: ASCII Art Generator — Limits and accuracy
description: Known limits of the ASCII Art Generator and what its measurements can and cannot tell you.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Limits and accuracy

## Size limits

| Limit | Value |
| --- | --- |
| Image file | 20 MB |
| Image size used | Up to 4,000 pixels a side and 12 megapixels; larger pictures are scaled down |
| Width of the art | 20 to 300 characters |
| Locked row count | 10 to 300 rows |
| Custom ramp | 2 to 200 characters |
| Render timeline | The last 100 conversions |

## Sources

- The webcam source cannot currently be used on auricartisan.com, because the site does not allow camera access on its pages.
- An animated GIF is converted as a single still frame.
- TIFF opens only in browsers that can display TIFF images.
- The **Text** source draws with fonts installed on your device; a missing font is replaced by another.

## Fonts decide how the art looks

Character art depends on a monospaced font. The same characters look different in different fonts, and wrong in a proportional one. **Match the output font** measures the chosen output font to keep proportions right, but the place you paste the art into uses its own font.

The glyph density measurements in **Analysis** and **Compare** are made by drawing characters with the fonts on your device, so they can differ slightly from one computer to another.

## Colour

- **Text** and **Copy** carry no colour. Colour needs the HTML, Canvas or SVG render, or the ANSI file.
- The **HTML** render shows the art before filters and **Thin out**.
- With colour on, filters that change the shape (**Rotate 90°**, **Border**, **Frame**) and **Thin out** make the Canvas, SVG and ANSI output fall back to one colour, and **Flip X** and **Flip Y** do not move the colours with the characters.

## Filters

**Brighten**, **Darken** and **Noise** are built around the Standard characters. With other sets, Brighten and Darken change only the characters they know, and Noise adds Standard characters. **Thin out** removes repeated characters, so rows become uneven and the picture skews.

## Edge-aware selection

Edge-aware selection can only use the line characters in the current set, and chooses by brightness, not by the direction of the edge. It has no effect with the Blocks, Minimal, Symbols, Lines or Braille sets.

## Downloads

- The PNG, SVG and HTML downloads can reuse an earlier render unless the matching render is showing. See [Copy, export and batch](../docs/export.md).
- **Export all six** downloads five files; the HTML and ANSI files are separate.
- The SVG made from an HTML render embeds web content inside the SVG, which some design apps cannot open. The SVG made from the **SVG** render uses plain text elements.
- The JSON file does not contain the source picture and cannot be loaded back into the page.

## The benchmark

**Run benchmark** times ten conversions in your browser. Timings depend on your device, your browser and whatever else it is doing, so compare settings on the same device in the same session rather than across devices.

## Related

- [Troubleshooting](../docs/troubleshooting.md)
- [Fine tuning](../docs/fine-tuning.md)
- [Supporting material](README.md)
