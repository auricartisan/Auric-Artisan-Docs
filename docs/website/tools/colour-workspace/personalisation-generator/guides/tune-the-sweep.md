---
title: Personalization Generator — Tune the sweep
description: Style chips, use case, the brief, engine settings, scoring weights and filters, and what each one changes in the Personalization Generator.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Tune the sweep

Open the **Tune** tab to shape the next sweep. It has four cards (**Style chips**, **Intent & note**, **Engine** and **Scoring weights**) and a **Current configuration** summary. Changes apply to the next sweep; they do not change results you already have.

## Style chips

Eighteen chips: **Calm**, **Luxe**, **Playful**, **Tech**, **Earthy**, **Editorial**, **Neon**, **Minimal**, **Heritage**, **Pastel**, **Cyber**, **Sun**, **Monochrome**, **Botanical**, **Nordic**, **Sunset**, **Midnight** and **Coastal**. **Calm** and **Editorial** are on at first.

Select a chip to turn it on or off. You can combine several; at least one is always on, and turning the last one off switches **Calm** back on.

Each style describes a range of saturation, lightness and chroma, a warmth and a contrast level. With several chips on, the generator averages them. Styles affect the sweep in three ways:

- new colours are drawn towards the style's ranges;
- each palette gets a **style** score for how well its colours fall inside those ranges;
- built-in reference palettes that share your styles are drawn on more often.

## Use case

**Use case** has five options: **Ui** (the default), **Brand**, **Poster**, **Editorial** and **Dashboard**. It favours the colour relationships and reference palettes suited to that use, and, together with your styles, chooses the type systems offered in **Typography** and the Studio.

## The brief and the preference note

The brief box in the left column and **Preference note** in Tune are the same setting: typing in either one sets it.

The generator does not read the brief as a sentence. It splits it into words and compares each word with the names of about 80 built-in reference palettes, such as *Clay Garden*, *Quiet Finance*, *Night Market* or *Coast Studio*. A reference palette whose name contains one of your words is drawn on more often. So *garden*, *coast*, *console*, *finance* or *studio* have an effect; words that match no name have none.

Short words such as *a* or *for* also match parts of names, so a brief of a few distinctive words steers better than a long sentence. For a real change of direction, use the pool, the style chips and the use case.

## Engine settings

| Setting | Range | Default | What it does |
| --- | --- | --- | --- |
| **Pool target** | 5 to 240 | 64 | How many colours **Build** fills the pool to. |
| **Palette size** | 5 to 12 | 6 | Colours in each generated palette. |
| **Search depth** | 40 to 4,000, steps of 20 | 320 | Candidate palettes sampled per sweep. More finds better results but takes longer. |
| **Keep top** | 6 to 96 | 24 | How many of the best palettes survive the sweep. |

The same four settings appear in the left column in Advanced mode as **Depth**, **Pool**, **Size** and **Keep**. Moving a Tune slider updates those boxes. The **Keep** box accepts up to 120, but the generator never keeps more than 96.

## Scoring weights

| Weight | Range | Default | Effect |
| --- | --- | --- | --- |
| **Diversity** | 0 to 100 | 68 | How much the score rewards palettes whose colours are clearly different from one another. |
| **Accessibility** | 0 to 100 | 72 | How much the score rewards contrast and colour-vision safety. |
| **Warmth** | 0 to 100 | 52 | Pulls new colours towards warmer (higher) or cooler (lower) hues. It is averaged with your styles' own warmth. |

## Filters

Three check boxes, all on by default. They are in the **Scoring weights** card and, in Advanced mode, in the left column.

| Tune label | Left-column label | When on |
| --- | --- | --- |
| **CVD-safe penalty** | **CVD-safe** | Palettes whose colours become hard to tell apart under simulated protanopia, deuteranopia or tritanopia score lower. When off, every palette gets the same middling colour-vision score. |
| **UI contrast bonus (4.5:1)** | **Contrast** | Palettes with at least one colour pair of 4.5:1 or more score higher (the bar is 3:1 when off), and new candidates are built with a wider light-to-dark spread. |
| **Strict perceptual dedupe** | **Unique** | Candidates that repeat one already seen in the sweep are thrown out. With **Endless**, repeats of palettes you already have are thrown out too. |

Contrast and colour-vision safety are weights, not hard filters: a palette that reads badly is ranked lower, but it can still be kept if everything else about it scores well. Only repeats are discarded.

The two sets of check boxes set the same values, but the left-column boxes only pick up a change made in Tune after a reload. Use one place consistently.

## Simple and Advanced

The **Simple** and **Advanced** switch in the left column only shows or hides the search settings there. Every setting keeps working in both modes, and all of them are always in **Tune**.

## Current configuration

The right-hand card in Tune summarises the next sweep: up to ten pool colours, the selected styles, **Intent**, the four engine settings, the three weights and **Search space**, a rough count of possible palettes from your pool size and palette size. It has two buttons:

- **Run sweep** starts a sweep, the same as **Generate**.
- **Reset defaults** puts the engine settings, weights and filters back to their defaults. It does not change your pool, styles, use case or brief.

## Related

- [Build your colour pool](build-the-pool.md)
- [Run a sweep and read the results](run-a-sweep.md)
- [Reference](reference.md)
