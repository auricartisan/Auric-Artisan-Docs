---
title: ASCII Art Generator — Fine tuning
description: Every setting behind the Fine tuning button — character set and custom ramp, shape, tone, sampling and dithering, edges, type, filters and advanced options.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Fine tuning

Select **Fine tuning** at the bottom of the rail to open eight more groups. Each starts folded; select a group's heading to open it. Every change re-converts the art a moment later.

Changing anything here clears the highlight on the **Look** buttons, since the art no longer matches a named look.

## Character set

A menu of seven sets, each listed light to dark:

| Set | Characters | Count |
| --- | --- | --- |
| **Standard** | space `.:-=+*#%@` | 10 |
| **Detailed** | space and 69 punctuation marks, letters and digits | 70 |
| **Blocks** | space `░▒▓█` | 5 |
| **Minimal** | space `.:#@` | 5 |
| **Symbols** | space `·•●◉⬤` | 6 |
| **Lines** | space and box-drawing characters `─│┌┐└┘` and more | 23 |
| **Braille** | space and all 255 Braille patterns | 256 |

**Custom ramp** lets you type your own characters, lightest first and darkest last, up to 200. It needs at least two characters; with fewer, the set chosen in the menu is used. Start with a space so the lightest areas stay empty, for example ` .oO@`.

The **Look** strip in the rail always shows the set actually in use, custom ramp included.

## Shape

Character cells are taller than they are wide, so without correction the art comes out stretched.

| Control | Range | Default | What it does |
| --- | --- | --- | --- |
| **Match the output font** | on or off | on | Measures the output font and sets **Cell aspect** to match it. |
| **Cell aspect** | 0.2 to 1.2 | set by the font | Width of a cell divided by its height. Lower values give fewer rows. |
| **Lock row count** | on or off | off | Fixes the number of rows instead of working it out from the picture. |
| Rows | 10 to 300 | 50 | The fixed row count, when locked. |

Moving **Cell aspect** by hand works best with **Match the output font** off; while it is on, choosing another output font measures it again.

## Tone

| Control | Range | Default | What it does |
| --- | --- | --- | --- |
| Brightness model | **Luminosity (Rec.601)**, **Average**, **Lightness (HSL)** | Luminosity | How a pixel's colour becomes a single brightness. Luminosity weights green most, as the eye does. |
| **Gamma** | 0.2 to 3.0 | 1.0 | Above 1 lifts the mid-tones (lighter); below 1 deepens them. |
| **Contrast** | 0 to 1 | 0 | Stretches the picture's contrast before conversion. |
| **Saturation** | 0 to 2 | 0 | Boosts colour before conversion. Mainly affects **From image** colour. |

## Sampling

| Control | Options | Default | What it does |
| --- | --- | --- | --- |
| Sampling method | **Area average (SAT)**, **Bilinear**, **Point / Nearest** | Area average | How the pixels under each cell become one value. Area averaging uses every pixel and is the most faithful; point sampling is fastest but can shimmer on fine detail. |
| Dithering | **None**, **Floyd-Steinberg**, **Ordered (Bayer)** | None | Spreads the rounding error between neighbouring cells so smooth gradients show as texture instead of bands. |
| Bayer matrix | **Bayer 4×4**, **Bayer 8×8** | 8×8 | The pattern size for ordered dithering. |

Floyd–Steinberg gives an organic, grainy texture; ordered dithering gives a regular cross-hatch.

## Edges

| Control | Range | Default | What it does |
| --- | --- | --- | --- |
| **Sobel glyph selection** | on or off | on | Finds edges in the picture and, at strong edges, swaps in a thin line character of similar brightness. |
| **Edge weight** | 0 to 1 | 0.65 | How strongly edges steer the choice of character. |

The line characters it can use are the backtick, `-`, `/`, `|` and the backslash, and only those present in the current set. So it has most effect with **Detailed**, a little with **Standard** (which has `-`), and none with Blocks, Minimal, Symbols, Lines or Braille. The character is chosen by brightness, not by the direction of the edge.

The **Sobel edge field** chart in **Analysis** shows where the edges are.

## Type

| Control | Range | Default | What it does |
| --- | --- | --- | --- |
| Output font | monospace, Courier New, Consolas, Monaco | monospace | Font of the HTML, Canvas and SVG renders and of downloads. |
| Size | 6 to 32 pixels | 12 | Character size for the Canvas and SVG renders and downloads. |
| **Line height** | 0.8 to 2.0 | 1.0 | Row spacing. |
| **Kerning** | −2 to 4 | 0 | Extra space between characters, in pixels. |
| Render mode | **Text (plain)**, **HTML (color spans)**, **Canvas (rasterised)**, **SVG (vector)** | Text | The same choice as the **Render** chips above the art. |

On screen, the Text and HTML renders are scaled to fit the stage whatever size you choose.

## Filters

Eight check boxes, applied to the finished characters:

| Filter | Effect |
| --- | --- |
| **Flip X** | Mirrors left to right. |
| **Flip Y** | Mirrors top to bottom. |
| **Rotate 90°** | Turns the art a quarter turn clockwise. |
| **Border** | Surrounds the art with `#`. |
| **Frame** | Surrounds the art with a double-line box. |
| **Brighten** | Moves each Standard-set character one step towards `@`. |
| **Darken** | Moves each Standard-set character one step towards a space. |
| **Noise** | Replaces a share of the characters with random Standard-set characters. |

**Noise amount** (0 to 1, default 0.1) sets that share.

Filters work on the characters, not the picture, so:

- **Brighten**, **Darken** and **Noise** use the Standard characters; with other sets, Brighten and Darken leave characters they do not know unchanged, and Noise mixes Standard characters in;
- the **HTML** render does not show filters at all, although **Copy** and the TXT download include them;
- with **From image** colour, shape-changing filters (**Rotate 90°**, **Border**, **Frame**) make the Canvas and SVG renders fall back to one colour, and the flips can leave colours in their original places.

## Advanced

| Control | Range | Default | What it does |
| --- | --- | --- | --- |
| **Thin out** | 0 to 0.95 | 0 | Drops characters from runs of the same character. Lines become shorter, so the picture skews; use it for effect, not to save space. |
| **Seed** | a whole number | 2654435769 | Fixes the random choices of **Noise** and the position of the ordered-dither pattern, so the same seed gives the same result. |

## Related

- [Looks, colour and detail](looks-colour-and-detail.md)
- [Charts, benchmark and Compare](charts-and-compare.md)
- [Reference](reference.md)
