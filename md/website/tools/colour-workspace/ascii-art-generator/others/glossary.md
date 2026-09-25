---
title: ASCII Art Generator — Glossary
description: Terms used in the ASCII Art Generator and its documentation.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Glossary

| Term | Meaning |
| --- | --- |
| ANSI colour codes | Escape sequences that terminals read as colour instructions. The ANSI download uses 24-bit (true colour) codes. |
| Area average | A sampling method that averages every pixel under a character cell. The page labels it SAT, after the summed-area table that makes it fast. |
| Bayer matrix | A fixed grid of thresholds used for ordered dithering, here 4 × 4 or 8 × 8. |
| Bilinear sampling | Reads a cell's value by blending the four nearest pixels. |
| Braille pattern | One of the 256 characters made of up to eight raised dots, used here as fine texture. |
| Cell aspect | A character cell's width divided by its height. Used to keep the art in proportion. |
| Character set, ramp | The characters the art is drawn with, ordered from least ink to most. |
| Density | How much of a character's cell is covered by ink, from 0 to 1. |
| Dithering | Spreading the rounding error between cells so that smooth tones appear as texture rather than bands. |
| Edge-aware selection | Swapping in a thin line character where the picture has a strong edge. |
| Floyd–Steinberg | An error-diffusion dithering method that passes each cell's error to its neighbours. |
| Gamma | A curve applied to brightness before conversion. Here, above 1 lightens the mid-tones. |
| Glyph | A single character as drawn by a font. |
| Luminosity (Rec.601) | A brightness formula that weights red, green and blue as the eye does, green most. |
| Monospaced font | A font in which every character has the same width, so columns line up. |
| Monotonic | Of a character set: each character has at least as much ink as the one before it. |
| Point sampling | Reads a cell's value from a single pixel. Fastest, but can shimmer on fine detail. |
| Sobel operator | A standard way to measure how quickly brightness changes, used to find edges. |
| True colour | 24-bit colour, about 16.7 million colours. |

## Related

- [Reference](../docs/reference.md)
- [Supporting material](README.md)
