---
title: Harmony Library — Inspect a harmony
description: Read the Inspect tab: colour roles and names, the harmony summary, the colour-theory scheme, pair contrast and each colour's values.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Inspect a harmony

Open a harmony by selecting **Inspect** or the card, pressing `Enter` or `Space` on a focused swatch, selecting **Open a random harmony**, or opening a share link. Until then the tab shows **No harmony selected**.

## The colour strip

One column per colour, each with:

- its **role** in the scheme — for example **Base**, **Complement**, **Split-Low**, **Split-High**, **Triad ②**, **Triad ③**, **Ally**, **Comp-Ally**, **Right 90°**, **Left 90°**, **Accent**, **Warm-Shift**, **Cool-Shift**, **Ally-Comp**, **Temperature Mate**, or a numbered role such as **Analogous 1**, **Shade 1**, **Tint 3**, **Neutral 2**, **Hex 2**, **Pent 4** or **Phi 2**;
- a three-word descriptive name, such as **soft saturated teal** (tone, colourfulness and hue from OKLCH);
- its hex code.

Select a column to copy its hex code.

## Harmony summary

The card's badge shows the family.

| Row | Meaning |
| --- | --- |
| **Harmony ID** | For example `har_5k`. |
| **Global index** | The harmony's number. |
| **Scheme** | The method, for example `triadic`. |
| **Family** | complementary, polyadic, analogous, monochromatic or compound. |
| **Colors** | 2 to 7. |
| **Base hue** | The base colour's hue in degrees. |
| **Avg L\* (OKLCH)** | Average OKLCH lightness, 0 to 1. |
| **Avg chroma** | Average OKLCH chroma. |
| **Hue span** | Widest angle between two of its hues, 0° to 180°. |
| **DeltaE avg** | Average colour difference between pairs (CIE76). |
| **Adherence** | How closely the colours keep to the scheme's ideal hue angles, as a percentage. 85% or more is shown as good, 60% to 85% as a warning, below 60% as poor. |
| **Entropy** | Hue bands covered, divided by the number of colours (up to 10). |
| **Min pair contrast** | Lowest contrast between two of its colours. |
| **Max pair contrast** | Highest. 4.5:1 or more means at least one pair can carry body text. |

## Color-theory scheme

- A one-sentence description of the scheme, for example "Three hues spaced 120° apart — vibrant and well-balanced."
- **Canonical angles** — the scheme's ideal hue offsets from the base, for example **120° / 240°**.
- **Color roles** — the roles of all its colours, in order.
- **Base HSL** — the base colour's hue, saturation and lightness.

## Pair-by-pair WCAG contrast

Every pair of colours by role, for example **Base / Complement 1.72 : 1** for `har_0`. 4.5:1 or more is good for body text, 3:1 or more for large text.

## Quick export

**Copy HEX**, **Copy CSS vars**, **Copy SCSS**, **Copy Tailwind**, **Download JSON**, **Download ASE**, **Download SVG**, **Download PNG**, **Open in Coolors**, **Save to library** / **Unsave**, **Copy share link** and **Design tokens…**. See [Copy, export and share](copy-export-and-share.md).

## One card per colour

Headed by role and hex, with a badge of its contrast on white and on black. Rows: **Role**, **HEX**, **RGB**, **HSL**, **OKLCH**, **CIE L\*a\*b\***, **WCAG vs white**, **WCAG vs black**, and buttons that copy the hex and `rgb()` values.

Select any card heading to fold or unfold it.

## Why adherence is not always 100%

Colours are generated in HSL, where equal hue steps are not perfectly even to the eye, and some schemes deliberately shift saturation or lightness. **Adherence** measures the hue angles the colours actually have against the scheme's ideal ones, so you can see how strictly a harmony keeps to its theory. Across the collection, 6,521 harmonies score 85% or more.
