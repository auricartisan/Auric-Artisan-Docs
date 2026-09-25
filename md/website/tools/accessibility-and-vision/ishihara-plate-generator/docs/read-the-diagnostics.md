---
title: Ishihara Plate Generator — Read the diagnostics
description: Understand each plate's quality score, its four weighted components, and how well it hides from each colour-vision deficiency.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Read the diagnostics

A good plate does two things at once: its figure is easy to see with typical colour vision, and it disappears for the deficiency it is meant to catch. The **Diagnostics** tab shows how well each plate does both.

"One number hides four measurements, so the score is shown taken apart. A plate fails when it is either invisible to normal vision or still legible to the deficiency it is meant to catch."

## How colour distance is measured

The generator works in **OKLab**, a colour space designed so that equal distances look roughly equally different. **ΔE** here is the straight-line distance between two colours in OKLab. On this scale, 0 means identical and a few hundredths is already a visible difference; figures such as 0.150 are clearly different colours.

- **Separation** is the ΔE between the average figure colour and the average background colour: how far apart they are for someone with typical colour vision.
- **Concealment** is that same distance recomputed after simulating protanopia, deuteranopia and tritanopia. The smaller it gets, the better the plate hides.

## The summary

At the top, **This batch** gives **Plates**, **Passing** (for example "9 of 10"), **Mean score** and **Weakest** (the lowest-scoring plate and its score).

## Each plate's card

- The plate's content, its type, palette and difficulty, a thumbnail, its **quality score** out of 100, and **Pass** or **Review**.
- Four component bars, each with its weight and its measured value:

| Component | Weight | What it rewards |
| --- | --- | --- |
| **Dot density** | .24 | A density close to the ideal of about 0.36 (the share of the plate covered by dots) |
| **Figure ratio** | .20 | A figure that takes up about 28% of the dots |
| **Separation** | .32 | A clear ΔE between figure and background for typical vision |
| **Concealment** | .24 | A figure that nearly vanishes through the most confusing deficiency, relative to its separation |

  A bar is highlighted when its component scores under 60%.

- **Through each deficiency — ΔE from the background**: the figure's distance from the background under **Protanopia**, **Deuteranopia** and **Tritanopia**. Here the small number is the good one; values under 0.03 are marked as hidden.
- A sentence such as "Hides best from deuteranopia; still most legible under tritanopia."

## When a plate passes

A plate passes when all of these hold:

- dot density is between 0.08 and 0.95;
- the figure takes between 5% and 65% of the dots;
- separation is above 0.01;
- the quality score is 45 or more.

Otherwise it is marked **Review**.

## Using the diagnostics

- A plate with low **Separation** may be invisible even to typical vision. Lower the difficulty, raise **Color separation** in **Fine tuning**, or try another palette.
- A plate with low **Concealment** is still legible through the deficiency. Choose a palette aimed at that deficiency, such as **Red vs Green** for red-green deficiencies, or raise the difficulty.
- The deficiency named in "Hides best from …" is the one the plate is best suited to demonstrate.

If no plates exist yet, the tab says "Nothing measured yet" with a **Go to the Lab** button.

> **Note:** These scores measure the plate as drawn on screen with simulated deficiencies. They do not make it a validated clinical test. See [Limits and accuracy](../others/limits-and-accuracy.md).
