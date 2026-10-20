---
title: Ishihara Plate Generator — Generate plates
description: Use the Lab to choose a plate type, palette and difficulty, generate single plates or batches, make custom plates, fine-tune the dots, and read the plate cards.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Generate plates

Everything in this guide happens on the **Lab** tab.

## Choose what to generate

### Plate Type

| Type | What the figure is |
| --- | --- |
| **Number** | A number to read |
| **Letter** | A letter to read |
| **Symbol** | A symbol, such as a star or an arrow |
| **Number (Gradient)** | A number drawn with a colour gradient |
| **Shape** | A shape, such as a ring |
| **Multi-layer (Shape+Number)** | A shape and a number together |
| **Hidden Path** | A winding path to trace |

### Color Palette

The colour families the figure and background are drawn from. The names say which colours are set against each other.

- **Auto (Random)**, a palette chosen at random for each plate (default)
- **Red vs Green**
- **Green vs Brown**
- **Blue vs Purple**
- **Orange vs Green**
- **Teal vs Magenta**
- **Yellow vs Blue**
- **Sepia Mono**
- **Mixed Pastel**

### Difficulty

**Easy**, **Medium** (default), **Hard** or **Extreme**. Difficulty "Controls colour similarity between figure and background": the harder the plate, the closer the figure's colours are to the background's.

## Generate

| Button | What it does |
| --- | --- |
| **+ Generate** | Draws one plate with the current settings and adds it to the bench |
| **×1**, **×3**, **×6** | Generates 1, 3 or 6 plates in a row |
| **Custom** | Opens **Create Custom Plate** (below) |
| **Clear All** | Removes every plate from the bench ("All plates cleared") |
| **↓ Export All** | Downloads every plate as a ZIP (see [Export plates](export-plates.md)) |

Each new plate is announced, for example "Plate #8 generated — 5", and scored as it lands.

When the bench is empty it says "No plates on the bench" and offers **Generate a plate** and **Or build the standard 38**.

## Create a custom plate

Select **Custom** to choose the figure yourself.

1. Choose a **Plate Type**.
2. Type the **Content**: a number, a letter, or a symbol or shape name. The dialog lists the names it knows:
   - symbols: star, arrow, triangle, heart, diamond, circle, square, moon, sun, check, x, target, squareDot, dot, leaf, wave, shield;
   - shapes: pentagon, octagon, rounded-square, annulus, oval.
3. Choose a **Color Palette** and a **Difficulty**.
4. Optionally type a **Seed**. "Same seed + parameters = identical plate."
5. Select **Generate**. The page says "Custom plate #N generated".

Select **Cancel** to close the dialog without generating.

## Plate size

**Plate Size** sets how large plates are drawn on the bench: **S** (210 pixels), **M** (290 pixels, default), **L** (440 pixels) or **XL** (900 pixels). The size is remembered in this browser. It changes the view only; exports have their own sizes.

"Double-click a plate to open it full size."

## Fine tuning

Select **Fine tuning** to show more controls. They apply to plates you generate next.

| Control | What it does | Range or options | Default |
| --- | --- | --- | --- |
| **Dot Count** | Number of dots to render. More = finer texture. | 2,000–15,000 | 7,000 |
| **Plate Shape** | Overall shape of the plate | **Circle**, **Square** | Circle |
| **CVD Preview** | Redraws every plate as it might appear with a deficiency | **Off**, **Protanopia**, **Deuteranopia**, **Tritanopia** | Off |
| **Placement Engine** | How dots are packed | **Balanced**, **Organic**, **Precision**, **Dense** | Balanced |
| **Dot Style** | The look of each dot | **Mixed**, **Round**, **Soft Edge**, **Rings** | Mixed |
| **Material** | The card the plate is printed on | **Paper**, **Warm Card**, **Cool Card**, **Transparent** | Paper |
| **Color separation** | How far apart figure and background colours are pushed | 0–100 | 55 |
| **Edge blend** | How softly the figure's edge merges into the background | 0–100 | 42 |
| **Dot scale** | Size of the dots, as a percentage | 70–145 | 100 |
| **Texture grain** | Grain of the card surface | 0–100 | 35 |

## This batch

A summary above the bench counts the plates you have now:

| Figure | Meaning |
| --- | --- |
| **Plates** | Plates on the bench |
| **Rendered** | Plates drawn in this session |
| **Avg dots** | Average dots per plate |
| **Color space** | "P3 HDR" when your display supports wide-gamut colour, otherwise "sRGB" |
| **Avg QA** | Average quality score |

## The plate card

Each plate appears on a card with:

- its number and content, for example "#1 - 45";
- tags for its type, palette, difficulty, dot count, placement engine and dot style;
- **QA PASS** or a review mark, and the quality score as a percentage;
- a per-plate preview switch: **Normal**, **Protan**, **Deutan**, **Tritan**;
- figures: **Normal ΔE** (figure against background for typical vision), **CVD min** (the smallest of those distances through the three deficiencies), **Density**, **Figure** (the share of dots in the figure), **Seed** and **Material**;
- buttons: **Copy seed** ("Seed copied"), **Download PNG** and **Download SVG**.

See [Read the diagnostics](read-the-diagnostics.md) for what the figures mean.

## Open a plate full size

Double-click a plate, or focus it and press `Enter` or `Space`. The full-size view shows the content as its title, a line with type, palette, difficulty and dot count, and a footer with the plate number, QA score, **Separation ΔE**, **Concealment ΔE**, seed, and its position (for example "1 of 10"). It has the same **Normal**, **Protan**, **Deutan** and **Tritan** switch.

Press `Right` or `Left` for the next or previous plate, and `Esc` to close.

## Remember

Plates live only on this page. Reloading or leaving the page loses them. Keep a plate by exporting it or saving its seed.
