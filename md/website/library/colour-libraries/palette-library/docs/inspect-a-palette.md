---
title: Palette Library — Inspect a palette
description: Read everything on the Inspect tab: the colour strip, the palette summary, pair-by-pair contrast and each colour's values.
product: Website › Library › Colour libraries › Palette Library
updated: 2026-09-25
---

# Inspect a palette

The **Inspect** tab turns one palette into a full report.

## Open a palette

- Select **Inspect** on a card, or select the card outside its swatches and buttons.
- Focus a swatch and press `Enter` or `Space`.
- Select **Open a random palette**.
- Open a share link someone sent you (see [Copy, export and share](copy-export-and-share.md)).

Before any palette is open, the tab shows **No palette selected** and explains what you will see.

## The colour strip

Five tall columns, one per colour. Each shows:

- a descriptive name made of three words — a tone, a colourfulness and a hue — for example **soft muted blue**;
- the hex code.

Select a column to copy its hex code.

| Word | Meaning (from OKLCH) |
| --- | --- |
| Tone: **deep**, **rich**, **soft**, **pale** | Lightness below 0.35, below 0.55, below 0.75, and 0.75 or more. |
| Colourfulness: **neutral**, **muted**, **saturated**, **vivid** | Chroma below 0.04, below 0.10, below 0.18, and 0.18 or more. |
| Hue: **red**, **orange**, **yellow**, **green**, **teal**, **blue**, **purple**, **pink** | The colour's OKLCH hue angle. |

## Palette summary

The **Palette summary** card carries a badge that classifies the palette from its real colours:

| Badge | When |
| --- | --- |
| **Neutral** | Average chroma below 0.05. |
| **Triadic** | The widest gap between any two hues is more than 90°. |
| **Analogous** | The widest gap is more than 30°. |
| **Monochrome** | The widest gap is 30° or less. |

The card's rows:

| Row | Meaning |
| --- | --- |
| **Palette ID** | The id, such as `pal_abc`. |
| **Global index** | The palette's number in the collection. |
| **Method** | The generation method the palette is labelled with. |
| **Colors** | 5. |
| **Avg L\* (OKLCH)** | The average OKLCH lightness of the five colours, 0 to 1. |
| **Avg chroma** | The average OKLCH chroma. |
| **Hue span** | The widest angle between any two of the five hues, in degrees (0 to 180). |
| **DeltaE avg** | The average colour difference between each pair of colours (CIE76, in Lab). Larger means more varied. |
| **Entropy** | How many different hue families the palette covers, as a fraction: the number of 36° hue bands its colours fall in, divided by 5. |
| **Min pair contrast** | The lowest WCAG contrast ratio between any two of its colours. |
| **Max pair contrast** | The highest. If it is 4.5:1 or more, at least one pair can carry body text. |

> **Note:** The **Method** row and the badge can disagree. The method is the label the palette carries in the collection; the badge is measured from the colours themselves. When you need a particular relationship between hues, trust the badge and the **Hue span**.

## Pair-by-pair WCAG contrast

All ten pairs of the five colours, each with its contrast ratio, for example **#1B2A4A / #F0E6D2 11.48 : 1**. Ratios of 4.5:1 or more are shown as good, 3:1 to 4.5:1 as a warning, and below 3:1 as failing.

Use this list to choose foreground and background pairs from the palette:

- 4.5:1 or more — normal body text (WCAG AA).
- 7:1 or more — normal text at AAA.
- 3:1 or more — large text (at least 18 point, or 14 point bold) and graphical objects such as icons.

## Quick export

A row of actions for this palette: **Copy HEX**, **Copy CSS vars**, **Copy SCSS**, **Copy Tailwind**, **Download JSON**, **Download ASE**, **Download SVG**, **Download PNG**, **Open in Coolors**, **Save to library** (or **Unsave**), **Copy share link** and **Design tokens…**. Each is described in [Copy, export and share](copy-export-and-share.md).

## One card per colour

Five cards, headed **Color 1** to **Color 5** with the hex code. The badge on each heading shows its contrast on white and on black, for example **6.6:1 / 3.2:1**. Each card lists:

| Row | Format |
| --- | --- |
| **HEX** | `#3A5F8C` |
| **RGB** | `rgb(58, 95, 140)` |
| **OKLCH** | Lightness as a percentage, chroma and hue, for example `47.87% 0.085 254.14` |
| **CIE L\*a\*b\*** | L, a and b, for example `39.54, 1.04, -28.90` |
| **WCAG vs white** | The contrast ratio against `#FFFFFF`. |
| **WCAG vs black** | The contrast ratio against `#000000`. |

Two small buttons under the rows copy the hex code and the `rgb()` value.

Select any card's heading to fold it away, and again to unfold it.

## Result

You know what each colour is called and measures, how varied the palette is, and exactly which of its colours can be used as text on which.
