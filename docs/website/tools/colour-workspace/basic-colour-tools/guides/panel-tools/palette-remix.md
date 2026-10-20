---
title: Palette Remix — Turn seed colours into variant palettes
description: Paste seed colours, choose a remix style, and get four controlled variant palettes you can copy as CSS, JSON or HEX.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Palette Remix

Palette Remix takes colours you already have, such as a brand palette, and makes four variations of them in one step. Each variation follows a recipe: it shifts hue, lightness and chroma by set amounts, spreads the colours a little across the palette, and adds as much random variation as you ask for.

Use it when you need alternatives that still feel related to the original: an editorial set, a darker mood, a set of UI neutrals or a complementary accent family.

Palette Remix is in the **Generate** category at the **Advanced** level. With the Catalogue's level set to **Basic** it is hidden.

## Open it

In the Workspace view, select **Palette Remix** in **Open a tool**. It opens with five seed colours already filled in and four remix sets shown.

## Screen tour

### Sidebar

- **Seed colors**: a text box, one colour per line to start with.
- **Remix style**: the recipe family.
- **Colors per palette**: how many colours each output palette has.
- **Remix energy**: a slider for how much random variation to add.
- **Remix** and **New seed** buttons.
- **Export**: **CSS**, **JSON** and **All HEX**.

### Main area

- **Output Palettes**, with a summary such as **5 seed colors → 4 remix sets**.
- Four cards, numbered 1 to 4. Each shows the recipe name, a short note, a row of swatches with HEX labels, and two buttons: **Copy** and **Use as seed**.

## Seed colours you can paste

The seed box accepts colours in these forms, in any mix:

- HEX with three or six digits, with or without `#`: `#D3AF37`, `d3af37`, `#FA0`.
- `rgb()` and `rgba()` with comma-separated numbers: `rgb(211, 175, 55)`.
- `hsl()` and `hsla()` with percentages: `hsl(46, 64%, 52%)`.
- `hsv()`: `hsv(46, 74%, 83%)`.
- `oklch()` with space-separated values; lightness may be written as 0 to 1 or as a percentage: `oklch(76% 0.13 87)`.

Separate colours with new lines, spaces, commas, semicolons or vertical bars. Duplicates are dropped and anything the tool cannot read is ignored. If nothing in the box is a valid colour, the tool falls back to its five default seeds.

When a palette needs more colours than you gave seeds, the seeds repeat in order.

## Remix styles

Each style produces four named sets.

| Style | Sets and their notes |
| --- | --- |
| **Editorial kit** | **Hero** (balanced brand-forward remix), **Ink** (deeper and moodier), **Glow** (soft highlight system), **Punch** (higher chroma accents) |
| **Analog drift** | **North** (cool-side analogous), **Core** (seed-respectful), **South** (warm-side analogous), **Mist** (low-chroma UI neutrals) |
| **Complement battle** | **Primary** (original contrast base), **Complement** (opposite hue family), **Split A** (split-complement left), **Split B** (split-complement right) |
| **Tonal system** | **Paper** (light surface tones), **Stone** (middle surfaces), **Metal** (dense interface tones), **Night** (dark-mode palette) |

Every set is computed in OKLCH. Lightness is kept between 0.10 and 0.95 and chroma between 0.015 and 0.32, so results stay usable.

## Tasks

### Remix a brand palette

1. Select the text in **Seed colors** and paste your own colours, one per line.
2. Select outside the box. The output updates.
3. Choose a **Remix style**, for example **Tonal system**. The four cards update at once.
4. Set **Colors per palette** to the number you need, from 3 to 9.
5. Move **Remix energy** to the left for faithful variations or to the right for looser ones.
6. Select **Remix** to roll new random variation with the same settings.

Result: four named palettes built from your colours, each with a one-line description of its purpose.

### Iterate on a result you like

1. On the card you like, select **Use as seed**. Its colours replace the seed box, the sets are rebuilt from them, and **Remix set moved into seed** appears.
2. Change the style or energy and keep going.

Result: a chain of remixes that moves steadily away from the original in the direction you choose.

### Start from random colours

1. Select **New seed**. The seed box fills with random OKLCH colours, as many as **Colors per palette**, and the sets rebuild.

Result: four remix sets from a fresh random starting point.

### Copy what you need

- Select a swatch to copy its HEX code.
- Select **Copy** on a card to copy that set's HEX codes, separated by spaces.
- Use the **Export** buttons for all four sets at once (below).

## Export

| Button | Result |
| --- | --- |
| **CSS** | Copies one `:root` block per set, with variables named `--remix-1-1`, `--remix-1-2` … for set 1, `--remix-2-1` … for set 2, and so on. |
| **JSON** | Copies an array of the four sets, each with `name`, `note` and `hexes`. |
| **All HEX** | Copies every HEX code from all four sets, one per line. |

Example of **CSS** output for the first set (your colours will differ):

```css
:root {
  --remix-1-1: #D8B23E;
  --remix-1-2: #1C1A31;
  --remix-1-3: #F2DDB6;
  --remix-1-4: #10182D;
  --remix-1-5: #FBF9F5;
}
```

## Save to and restore from the Library

With Palette Remix focused, **Save to Library** saves each of the four sets as a separate palette, named after the set. A saved remix set reopens in Palette Remix with its colours in the seed box, and **Loaded remix from library** appears.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Seed colors** | The colours to remix. Applied when you leave the box. | Any mix of the accepted formats | #D3AF37, #1A1A2E, #F5DEB3, #0F172A, #FFFFFF |
| **Remix style** | Chooses the recipe family. Updates at once. | Editorial kit, Analog drift, Complement battle, Tonal system | Editorial kit |
| **Colors per palette** | Number of colours in each set. Updates at once. | 3 to 9 | 5 |
| **Remix energy** | Random variation in hue, lightness and chroma. Updates at once. | 0 to 100 | 30 |
| **Remix** | Rebuilds the sets with new random variation. | — | — |
| **New seed** | Fills the seed box with random colours and rebuilds. | — | — |
| Swatch | Copies one HEX code. | — | — |
| **Copy** (card) | Copies that set's HEX codes, space-separated. | — | — |
| **Use as seed** (card) | Moves that set into the seed box and rebuilds. | — | — |
| **CSS**, **JSON**, **All HEX** | Copy all four sets. | See Export | — |

## Accuracy and limits

- Remix energy adds random variation, so the same settings give different results each time. Copy or save a result you want to keep.
- At the highest energy the hue can move by up to about 35 degrees in either direction on top of the recipe's own shift.
- The tool does not check contrast. To check a set, paste it into [Color Battle](colour-battle.md) or open it in [Palette Studio](palette-studio.md) through the Library.

## Related

- [Panel tools](README.md)
- [Palette Studio](palette-studio.md)
- [Color Battle](colour-battle.md)
- [Import, export and the Library](../import-export-and-library.md)
