---
title: Tonal Steps — Build a ramp
description: Choose a ramp engine, step count and easing, and judge how even the ramp is.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Build a ramp

## The engines

| Engine | How it builds the steps | Holds even | Easing γ |
| --- | --- | --- | --- |
| **HSL lightness** | Keeps your colour's HSL hue and saturation and steps HSL lightness evenly from 100 (white) to 0 (black) | HSL L, a coordinate rather than a perceptual quantity | Not used |
| **Equal luminance** | For each step, finds the HSL lightness (at your colour's hue and saturation) that gives a target relative luminance Y = (1 − t)^γ, from 1 (white) to 0 (black) | Relative luminance Y, the quantity WCAG contrast is built on (at γ = 1) | Bends the targets |

A third engine, **Equal contrast** (equal steps in WCAG ratio against black), is not offered on the Lab tab because it produces the same ramp as Equal luminance: equal steps in WCAG ratio are equal steps in luminance. The Ramps tab shows it with a "same ramp as equal luminance" badge, and it can still be reached with the `3` key or a saved link.

Both engines start at white and end at black. The **Mix in** setting does not affect the main ramp; it affects tints, shades, tones and key sets.

## Steps

1. On the **Lab** tab, enter the **Base colour** as a six-digit HEX (or use the picker, or **Random base**).
2. Choose **HSL lightness** or **Equal luminance** under **Ramp engine**.
3. Set **Steps** from 3 to 21 (default 11).
4. For Equal luminance, set **Easing γ** from 0.4 to 2.6 (default 1.0). At 1.00 the steps are evenly spaced in luminance. Higher values move steps towards the dark end, which usually looks more even; lower values crowd them towards white.
5. Read the step rows and the **Where the steps fall** chart.
6. Read the statistics:
   - **Base OKLab L** — your colour's perceptual lightness;
   - **Largest step** and **Smallest step** — the biggest and smallest OKLab L gaps between neighbouring steps;
   - **Evenness** — how far the step sizes stray from their average, as ±%. Smaller is more even.

The note under the statistics gives the ratio of the largest to the smallest step.

## Compare the engines

1. Open the **Ramps** tab.
2. Under **Compare**, keep **Every engine** to see all three, or choose **One at a time** for the Lab's engine only.
3. Under **Measure evenness in**, choose **OKLab L** (default), **CIELAB L\*** or **Relative Y**. A ramp even in one is rarely even in another.
4. Under **Endpoints**, choose **Include black** (default) or **Interior only**. The last step into pure black usually dominates the figure; the interior figure drops the first and last gaps. Both figures are shown, and the one you choose is emphasised.
5. Read each engine's row: its name, what it holds constant, its strip, and its evenness figures.
6. Read **Step sizes, as the chosen measure sees them** for a chart of the gaps, and **Where the ramp sits in chroma** for the ramp (with tints, shades and tones) plotted on the OKLab a–b plane. A ramp that only changes lightness traces a line there; one mixed towards white and black in a non-linear space does not.

The comparison uses the same base, step count, easing and mixing space as the Lab.

## Tips

- The equal-luminance engine is, perhaps surprisingly, the least even in OKLab L at γ = 1: equal steps in luminance are very unequal in perceived lightness, with the biggest jump at the dark end. The Ramps footer says so.
- For a ramp whose steps line up with WCAG thresholds, use Equal luminance and check the [Contrast](check-contrast.md) tab.
- Press `1` or `2` to switch engines, and `R` for a random base, when the focus is not in a field.

## Result

You have a ramp built by the engine you chose, with its step sizes measured, and a side-by-side view of how the engines differ.
