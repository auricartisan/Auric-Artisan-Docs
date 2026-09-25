---
title: Personalization Generator — Build your colour pool
description: Add, generate, randomise, nudge and remove the colours the Personalization Generator builds palettes around, and read the pool statistics.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Build your colour pool

The pool is the set of colours the generator treats as *yours*. Every palette it keeps is scored partly on how close its colours sit to the nearest pool colour, so the pool is the strongest steer you have. It holds up to 240 colours.

Open the **Pool** tab. The heading reads **Personal Color Pool**, with the count, for example **Pool: 8/240**.

## Add one colour

1. Pick a colour with the colour well, or type a HEX value such as `#3C6E71` in the box next to it. Three-digit values such as `#3a7` also work.
2. Select **Add**.

The colour goes to the front of the pool. If it is already in the pool, nothing changes. An invalid value shows the message **Use a valid HEX color**.

## Remove a colour

Select any swatch in the grid. Each swatch shows an **×** and removes itself when selected. **Clear** empties the whole pool; there is no undo.

If you generate with an empty pool, the generator puts the eight starting colours back first.

## Grow the pool automatically

| Button | What it does |
| --- | --- |
| **Build 64** | Fills the pool up to your **Pool target** (64 by default; the label shows the current target). New colours are variations of your pool and of built-in reference palettes that match your styles, use case and brief. If the pool is already larger than the target, it is cut down to the target. |
| **+24 random** | Adds 24 looser variations drawn from the matching reference palettes. |

Set the pool target in **Tune** (**Pool target**, 5 to 240) or in the **Pool** box of the brief in Advanced mode.

## Quick seeds

The **Quick seeds** card adds small fixed sets to the end of the pool:

| Button | Colours added |
| --- | --- |
| **+ 4 UI** | #0F172A, #F8FAFC, #D3AF37, #1F2937 |
| **+ 4 Earthy** | #F4EFE4, #473B2F, #C46D3B, #8AA17E |
| **+ 4 Neon** | #10002B, #7B2CBF, #E0AAFF, #00F5D4 |
| **+ 4 Pop** | #FFFFFF, #000000, #E63946, #2D6CDF |
| **+ Grayscale** | seven greys from #0A0A0A to #F5F5F5 |

**Jitter** nudges every pool colour a little at random in OKLCH: up to about 6 degrees of hue, 0.02 of chroma and 0.03 of lightness either way. Use it to loosen a pool that is producing results too close to your inputs.

## Other ways to fill the pool

- **Add to pool** on any result card (palette, gradient, typography, UI pair or poster) puts that result's colours at the front of the pool.
- Loading a preset replaces the pool. See [Presets](presets.md).
- From your Library, a palette, gradient, colour or shade saved in another tool can be opened here. Its colours are added to the front of the pool and the **Pool** tab opens. See [Export, save and share](export-and-save.md).

## Read the pool statistics

The side cards describe the pool as it stands:

- **Pool statistics**: **Count**, **Target**, **Avg chroma**, **Avg lightness**, **Light range** and **Neutrals** (colours with less than 8% saturation). Chroma and lightness here are HSL saturation and lightness, in per cent.
- **Hue distribution**: twelve 30-degree bands around the hue wheel. A fuller band holds more colours; hover a band to see its count.
- **Lightness ladder**: one tick per colour. An even spread leaves room for readable text and background pairs.

## Tips

- Five to fifteen colours you really mean usually steer better than a pool of 200 automatic variations.
- Include at least one very light and one very dark colour. The generator looks for readable pairs, and a pool with no dark colours has fewer to offer.
- To lock a direction you like, select **Add to pool** on a good palette, then generate again.

## Related

- [Tune the sweep](tune-the-sweep.md)
- [Presets](presets.md)
- [Reference](reference.md)
