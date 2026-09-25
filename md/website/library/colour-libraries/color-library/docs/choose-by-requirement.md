---
title: Color Library — Choose colours by requirement
description: Use the seven requirement chips to narrow the atlas by what a colour has to do, and read what each requirement costs.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Choose colours by requirement

The **Or from what it has to do** section lets you ask for a job rather than for coordinates. Instead of "hue 199, chroma 0.10", you ask for "readable on white" or "for typography". Each requirement is a chip, and each chip shows how many colours would be left if you selected it, so you can see the cost of one more requirement before you add it.

## The seven requirements

| Chip | A colour passes when | Colours that pass on their own |
| --- | --- | --- |
| **Readable on white** | Its contrast on white is 4.5:1 or more (WCAG AA for body text). | 2,998 |
| **Readable on black** | Its contrast on black is 4.5:1 or more. | 5,344 |
| **Vivid** | Its OKLCH chroma is 0.18 or more. | 2,707 |
| **Muted** | Its OKLCH chroma is below 0.06. | 695 |
| **Calm** | Its emotion label is `calm`. | 843 |
| **For typography** | Its design-usage label is `typography`. | 819 |
| **As an accent** | Its design-tag label is `accent`. | 822 |

The last column is the number each chip shows when no other chip is selected, out of 8,192.

## Steps

1. Scroll to **Or from what it has to do**.
2. Read the numbers on the chips. Each is the count you would get by selecting that chip now.
3. Select a chip, for example **Readable on white**. It is highlighted, and the grid in **Browse the atlas** now shows only colours that pass.
4. Read the line under the chips. It now says, for example, **2,998 of 8,192 colours meet all of it — 36.6%.**
5. Read the other chips again. Their numbers have changed: each now shows how many colours would remain if you added it to the ones already selected.
6. Select a second chip, for example **Vivid**. The grid keeps only colours that pass both.
7. To remove a requirement, select its chip again.

**Result:** the grid shows only colours that meet every selected requirement, and the line under the chips states how many that is, as a count and a percentage of the atlas.

## How the chips combine

- Selected chips combine with AND: a colour must pass every one.
- **Vivid** and **Muted** cannot both be true, so selecting both leaves 0 colours. The chip shows this before you select it.
- The chips work together with everything else in **Browse the atlas**: the search boxes, the eight filters and the sort order. The chips are applied first, then the search and filters.
- The chips' own counts consider only the other chips, not the search or the filters, so the count on a chip can be higher than what the grid shows.
- With nothing selected, the line under the chips reads **8,192 colours. Add a requirement to see what it costs.**

> **Tip:** Selecting **Readable on white** is the reliable way to keep only colours with at least 4.5:1 on white. It applies the same threshold as the WCAG filter's **AA on white** option.

## Where the labels come from

**Calm**, **For typography** and **As an accent** test the descriptive labels each colour carries in the atlas. Those labels were assigned when the atlas was generated; they are a convenience for browsing, not a measurement. The contrast and chroma chips, by contrast, test measured values. See [Limits and accuracy](../others/limits-and-accuracy.md).
