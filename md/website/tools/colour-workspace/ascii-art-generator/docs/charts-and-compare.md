---
title: ASCII Art Generator — Charts, benchmark and Compare
description: The measurements, charts and benchmark in the Analysis tab, and the character set comparison in the Compare tab.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Charts, benchmark and Compare

The **Analysis** and **Compare** tabs explain why the art looks the way it does. You do not need them to make art; they help when a result bands, looks flat or converts slowly.

## The Analysis tab

### This render

The left column repeats the facts of the last conversion:

- **Grid**, **Characters** and **Render** (time in milliseconds);
- **Character set**, and **Ramp** (the number of glyphs, for example **10 glyphs**);
- **Sampler** and **Dithering**.

### Benchmark

**Run benchmark** converts the current source ten times with the current settings and reports the average, for example **Avg: 18.4 ms (10 runs)**, and the **Min**, **Max** and **Spread**. Use it to see which setting makes conversion slow. With the Image source and no picture loaded, it reads **Load an image first**.

### The charts

Six charts. Each has a **⛶** button, and you can also double-click a chart, to open it full screen. Close the full-screen chart with **×**, `Esc`, or by selecting the dark background.

| Chart | What it shows | What to look for |
| --- | --- | --- |
| **Glyph density calibration** | The ink of each character in the current set, measured by drawing it at 32 × 32 pixels, sorted light to dark. | A smooth rise. Big jumps or flat runs mean some tones have no matching character. |
| **Character frequency** | How often each character appears in the latest output. | A spike at one end means gamma or contrast is crushing the mid-tones. |
| **Top character distribution** | The twelve most frequent characters as a ring, with the rest grouped as one slice. | Whether a few characters dominate the art. |
| **Sobel edge field** | The strength of edges in the source picture; bright means a strong edge. | Where edge-aware glyph selection can act. Where it is dark, **Edge weight** has nothing to work on. |
| **Sampling comparison** | The same source through area averaging, bilinear and point sampling. | Point sampling breaking fine detail into noise. |
| **Render timeline** | Conversion time for the last hundred conversions. | Where live updates stop keeping up with the sliders. |

The charts redraw after every conversion and when you open the tab.

## The Compare tab

**Measure all sets** draws every character of all seven sets at 32 × 32 pixels, measures how much ink each one has, and fills a table:

| Column | Meaning |
| --- | --- |
| Charset | The set: standard, detailed, blocks, minimal, symbols, lines or braille. |
| Glyphs | The number of characters, including the space. |
| Min density | The ink of the lightest character, from 0 to 1. |
| Max density | The ink of the darkest character. |
| Range | Max minus min. A wider range carries more contrast. |
| Monotonic | **✓** if every character has at least as much ink as the one before it, in the set's own order; **✗** if not. |

A set that is not monotonic has at least one character darker than the one after it, and a smooth gradient drawn with it shows bands. More glyphs carry more detail; a wider range carries more contrast. They are not the same thing.

The measurement uses the fonts on your device, so results can differ slightly between computers. Your custom ramp is not in the table; when it is in use, its densities show in the **Glyph density calibration** chart.

## Related

- [Fine tuning](fine-tuning.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Glossary](../others/glossary.md)
