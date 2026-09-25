---
title: ASCII Art Generator — Reference
description: Every control, range, default, file and message in the ASCII Art Generator in one place.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# ASCII Art Generator reference

## Address

- https://auricartisan.com/tool/ascii/
- https://auricartisan.com/ascii opens the same page.

## Tabs

| Tab | Purpose |
| --- | --- |
| **Lab** | Source, look, colour, detail, fine tuning, and the art. |
| **Analysis** | Readouts, benchmark and six charts. |
| **Compare** | Ink measurements for all seven character sets. |
| **Export** | Seven download formats, Export all, and batch rendering. |

## Source

| Control | Values | Default |
| --- | --- | --- |
| Source | **Image**, **Text**, **Webcam** | Image |
| Image file | PNG, JPEG, GIF, WebP, BMP, SVG, TIFF; up to 20 MB | none |
| Large images | Scaled to at most 4,000 px a side and 12 megapixels | always |
| Text | any text | ASCII |
| Text font | monospace, Courier New, Consolas, Monaco, Fira Code, Source Code Pro | monospace |
| Text size | 8 to 128 px | 48 |
| Text weight | Normal, Bold, Black | Bold |
| **White on black** | on or off | off |
| **Keep converting every frame** | on or off | off |
| **Smooth between frames** | on or off | off |

## Look, colour and detail

| Control | Values | Default |
| --- | --- | --- |
| Look | **Classic**, **Blocks**, **Fine**, **Bold**, **Line art** | Classic highlighted |
| Colour | **Mono**, **From image** | Mono |
| **Ink** | any colour | #f0f0f0 |
| **Paper** | any colour | #0f0e0c |
| **Detail** | 20 to 300 columns | 100 |
| **Invert for dark paper** | on or off | follows the paper |

## Fine tuning

| Group | Control | Values | Default |
| --- | --- | --- | --- |
| Character set | Set | Standard, Detailed, Blocks, Minimal, Symbols, Lines, Braille | Standard |
| Character set | **Custom ramp** | 2 to 200 characters, light to dark | off |
| Shape | **Match the output font** | on or off | on |
| Shape | **Cell aspect** | 0.2 to 1.2 | set by the font |
| Shape | **Lock row count** | on or off, 10 to 300 rows | off, 50 |
| Tone | Brightness model | Luminosity (Rec.601), Average, Lightness (HSL) | Luminosity |
| Tone | **Gamma** | 0.2 to 3.0 | 1.0 |
| Tone | **Contrast** | 0 to 1 | 0 |
| Tone | **Saturation** | 0 to 2 | 0 |
| Sampling | Method | Area average (SAT), Bilinear, Point / Nearest | Area average |
| Sampling | Dithering | None, Floyd-Steinberg, Ordered (Bayer) | None |
| Sampling | Bayer matrix | 4×4, 8×8 | 8×8 |
| Edges | **Sobel glyph selection** | on or off | on |
| Edges | **Edge weight** | 0 to 1 | 0.65 |
| Type | Output font | monospace, Courier New, Consolas, Monaco | monospace |
| Type | Size | 6 to 32 px | 12 |
| Type | **Line height** | 0.8 to 2.0 | 1.0 |
| Type | **Kerning** | −2 to 4 px | 0 |
| Type | Render mode | Text, HTML, Canvas, SVG | Text |
| Filters | Check boxes | Flip X, Flip Y, Rotate 90°, Border, Frame, Brighten, Darken, Noise | all off |
| Filters | **Noise amount** | 0 to 1 | 0.1 |
| Advanced | **Thin out** | 0 to 0.95 | 0 |
| Advanced | **Seed** | whole number | 2654435769 |

## Character sets

| Set | Characters (light to dark) | Count |
| --- | --- | --- |
| Standard | space `.:-=+*#%@` | 10 |
| Detailed | space and 69 marks, letters and digits | 70 |
| Blocks | space `░▒▓█` | 5 |
| Minimal | space `.:#@` | 5 |
| Symbols | space `·•●◉⬤` | 6 |
| Lines | space and box-drawing characters | 23 |
| Braille | space and 255 Braille patterns | 256 |

## Stage

| Item | What it does |
| --- | --- |
| Render chips | **Text**, **HTML**, **Canvas**, **SVG** |
| **Grid** | Columns × rows |
| **Chars** | Number of characters |
| **Render** | Time of the last conversion |
| **Copy** | Copies the plain characters |
| **Full screen** | Shows the art over the whole window |

## Files

| File | From |
| --- | --- |
| ascii-art.txt | **Download .txt**, Export all |
| ascii-art.png | **Download .png**, Export all |
| ascii-art.svg | **Download .svg**, Export all |
| ascii-art.html | **Download .html** |
| ascii-research.json | **Download .json**, Export all |
| ascii-analysis.csv | **Download .csv**, Export all |
| ascii-art.ans | **Download .ans** |

## Messages

| Message | Meaning |
| --- | --- |
| **Rendering…** | A conversion is in progress. |
| **Unsupported file type: …** | The file is not one of the accepted image types. |
| **File too large (… MB). Max 20 MB.** | The file is over 20 MB. |
| **Failed to load image** | The browser could not read the file. |
| **Downscaled from … to …** | A large picture was scaled down before conversion. |
| **Copied!** | The art is on the clipboard. |
| **Nothing to copy** | Nothing has been converted yet. |
| **Nothing to export** | Nothing has been converted yet. |
| **Turn colour on first — ANSI carries the image's colours** | ANSI download needs **From image**. |
| **Load an image first** | The benchmark needs a picture. |
| **No inputs** | The batch box is empty. |
| **Camera permission denied. …** | The camera could not start. See [Troubleshooting](troubleshooting.md). |

## Related

- [Fine tuning](fine-tuning.md)
- [Glossary](../others/glossary.md)
- [Shortcuts](../others/shortcuts.md)
