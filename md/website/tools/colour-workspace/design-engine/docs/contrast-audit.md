---
title: Design System Generator — Check contrast with the audit
description: Read the always-visible audit rail, understand the score, open the full audit for both themes, and use the suggested fixes.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Check contrast with the audit

The audit is the evidence that a generated system meets its contrast target. It re-runs on every change, it covers both the light and the dark roles, and it reports two measures:

- the **WCAG 2.1 contrast ratio**, from 1:1 to 21:1, the measure most accessibility requirements use;
- the **APCA Lc** value, the Accessible Perceptual Contrast Algorithm proposed for WCAG 3, which handles light-on-dark and mid-tone pairs better. The tool shows its size (without a sign) as context, not as a pass or fail gate.

## The audit rail

The right-hand column, **The audit** (*live*), has four sections.

1. **The score**: a large number out of 100, *out of 100*, a line saying how the last change moved it (*first run*, *no change* or, for example, *+3 on that change*), and a pill: **all 12 pass** or **N failing**. Select the score to open the full audit. A line underneath says how many tokens changed on the last change, for example *14 of 177 tokens moved on that change.*
2. **Where the points went**: the four parts of the score as bars, and a sentence naming the weakest part.
3. **Light** (*wcag · apca*): the twelve pairings for the light roles. Each row shows a sample, the pairing, the kind of content and its requirement (*normal text · needs 7*), the ratio (green for pass, red for fail) and the Lc value.
4. **Dark**: *clean* or *N failing* for the dark roles, and **See the whole audit →**.

## The twelve pairings

Each pairing is held to the requirement that fits its content, not one number for everything.

| Pairing | Requirement | Why |
| --- | --- | --- |
| Body text (on `bg`) | Your target | Normal text |
| Muted text (on `bg`) | 4.5:1 | Still body copy, held to AA |
| Subtle text (on `bg`) | 3:1 | Large or secondary text |
| Text on surface | Your target | Normal text on a card |
| Text on muted bg | Your target | Normal text on a wash |
| On-primary label | 4.5:1 | Button label |
| Primary vs bg | 3:1 | A user-interface element |
| Strong border (on `bg`) | 1.4:1 | Decorative; it only has to be seen |
| Success solid | 3:1 | Labelled component |
| Warning solid | 3:1 | Labelled component |
| Danger solid | 3:1 | Labelled component |
| Info solid | 3:1 | Labelled component |

For the semantic solids the pairing is the solid colour with its automatic black or white label. Translucent tokens (the dark theme's borders, for example) are blended over the surface beneath them before they are measured, and the full audit marks them **composited**.

## The score

The score is a weighted total, kept between 40 and 100:

| Part | Up to | What it rewards |
| --- | --- | --- |
| **Accessibility** | 55 | The share of the twelve light pairings that pass. |
| **Vibrancy** | 18 | How much colour (OKLCH chroma) the primary step 500 kept after gamut mapping. |
| **Headroom** | 15 | How far body text clears your target. |
| **Hierarchy** | 12 | Full marks when body, muted and subtle text are three distinct tiers; 5 otherwise. |

The rail colours the score green from 85, amber from 70, red below. The Overview ring uses green from 85 and amber from 65.

Things to know about the score:

- It is computed from the light roles. The dark theme is audited, but it does not change the score.
- Loosening the contrast target rarely raises it: lighter text tiers are more likely to collide, and the headroom shrinks. For a higher score, try a more saturated style or a seed with more chroma.
- It measures contrast, colour and hierarchy, not taste. Two very different systems can score the same.

## The full audit

Select the score, or **See the whole audit →**, to open **The audit** view. **← Back to the system** returns to the tab you were on.

- **Theme audited**: **Light** or **Dark**, with a pill for each theme's result.
- **The engine's own requirements**: the twelve pairings for the chosen theme, each with ratio, Lc, requirement and a **PASS** or **CHECK** badge.
- **What would fix it** (only when something fails): for each failing pairing, the nearest step in the generated ramp that would clear the requirement, with its token name and new ratio. If nothing in the ramp can reach it, it says that the seed hue or the requirement has to move.
- **Every foreground on every surface**: a matrix of `text`, `text-muted`, `text-subtle`, `primary`, `border-strong` and the four semantic solids against `bg`, `bg-subtle`, `bg-muted`, `surface` and `elevated`. Gold meets your body-text target, green is 4.5:1 and above, amber is 3:1 and above (large text and UI only), red is below 3:1.
- **Color-vision preview**: primary, secondary, accent, success, warning and danger drawn four times: **Normal**, **Deuteranopia**, **Protanopia** and **Tritanopia**. Look for colours that stay distinct in the first row but merge in another.

## Tasks

### Get to all twelve passing

1. Look for red ratios in the rail, or open the full audit.
2. Read **What would fix it**. Often the fastest fixes are: raise or lower the **Contrast target** by one step, choose a less saturated **Style**, or try another **Seed**.
3. Watch the pill turn to **all 12 pass**.

Result: a system whose defined pairings all meet their requirements.

### Check the dark theme

1. Open the full audit and select **Dark** under **Theme audited**.
2. Read the pairings and the matrix.

Result: the same checks for the dark roles.

## What the audit does not cover

- Your layout: text over images, disabled states, focus rings on coloured buttons and hover states.
- Font size and weight, which change what a ratio means in practice.
- Other accessibility requirements such as focus order, target size, motion preferences and semantics.

For those, see the [Accessibility and vision tools](../../../accessibility-and-vision/README.md).

## Related

- [Set the brief](set-the-brief.md)
- [Component playground](component-playground.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
