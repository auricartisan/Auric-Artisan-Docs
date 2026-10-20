---
title: Gradient Library — Check your own gradient
description: Enter your gradient's stops in "Will your gradient band?", read the verdict, find the worst step and fix it.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Check your own gradient

**Will your gradient band?** applies the collection's own banding measurement to stops you give it.

## What banding is

A gradient bands when part of it changes colour much faster than the rest, so the eye sees a step or an edge instead of a smooth flow. It is common at the dark end of a ramp: standard sRGB spends few of its values on the darkest shades, so a black-to-colour blend often lurches just after black.

## How the check measures

1. The page paints your stops the way a browser paints a plain CSS `linear-gradient`: evenly spaced, blended straight between neighbouring stops in sRGB.
2. It takes 96 samples along the ramp.
3. It measures the colour difference between each pair of neighbouring samples in OKLab, a colour space where equal distances look like roughly equal differences.
4. It divides the largest step by the average step. This **step ratio** is the verdict's basis. A perfectly even ramp has a ratio of 1.

| Step ratio | Verdict | Meaning |
| --- | --- | --- |
| Below 3.2 | **Smooth** | No transition is large enough to read as a step. |
| 3.2 to below 5.5 | **Some compression** | One part of the ramp is noticeably faster than the rest. |
| 5.5 or more | **It will step** | Expect a visible step. |

The page explains the thresholds: across 3,000 gradients the collection had already labelled, the ratio's median was 1.55 for smooth ones and 5.09 for step risks, and 3.2 and 5.5 are where those groups separate.

## Steps

1. Scroll to **Will your gradient band?**. It starts with three stops: `#000000`, `#0B3D91` and `#FFFFFF`.
2. For each stop, either click the swatch and pick a colour, or type into the text field. The field accepts any CSS colour: hex, `rgb()`, `hsl()`, `hwb()`, `lab()`, `lch()`, `oklab()`, `oklch()`, `color()` or a colour name.
3. To add a stop, select **Add a stop**. The new stop is added at the end, coloured halfway between the last two stops. You can have up to 12 stops.
4. To remove a stop, select × on it. A gradient keeps at least two stops, so × disappears when only two are left.
5. The verdict updates as you type. **Measure it** measures again on demand.
6. Read the result (below).

**Result:** a verdict, the step ratio, and the position of the worst step, marked on a preview of your ramp.

## Reading the result

- **The preview strip** shows your stops, evenly spaced, with a marker above the worst transition.
- **The verdict word** — **Smooth**, **Some compression** or **It will step** — with **step ratio** and the ratio to two decimals.
- **A note** that says what to do:
  - **No transition is large enough to read as a step.**
  - If the worst step is at the very start: **The largest step is at the dark end. sRGB compresses its darkest values, so even a plain black-to-white ramp steps there — interpolate in OKLCH, or start from a lifted black rather than #000.**
  - Otherwise: **The largest step is at N% along the ramp. Adding a stop near there, or interpolating in OKLCH, is usually the fix.**
- **The numbers:**

| Row | Meaning |
| --- | --- |
| **Mean step** | The average OKLab distance between neighbouring samples. |
| **Largest step** | The biggest one. |
| **Worst transition at** | Where the biggest step is, as a percentage along the ramp. |
| **Sampled** | **96 steps, sRGB**. |

## While you are typing

A half-typed colour, such as `#12`, is not yet a colour. The stop keeps its last valid colour, is marked as invalid, and a warning says, for example, **Stop 2 is not a colour yet — still measuring with its last one.** When you leave the field without finishing, the field is put back to the colour being measured.

## Fixing a gradient that steps

1. Note **Worst transition at**.
2. Add a stop close to that position with an in-between colour, or replace a pure black `#000000` start with a slightly lifted dark colour.
3. Measure again.
4. If the verdict is still **It will step**, consider blending in OKLCH in your CSS (for example `linear-gradient(in oklch, …)` in browsers that support it) and compare with gradients in the library that use **Oklch Short** or **Oklab** interpolation.

> **Note:** The check always measures plain sRGB blending with evenly spaced stops, because that is how a basic CSS gradient is painted. It does not know about stop positions or interpolation settings you might add in your own CSS.
