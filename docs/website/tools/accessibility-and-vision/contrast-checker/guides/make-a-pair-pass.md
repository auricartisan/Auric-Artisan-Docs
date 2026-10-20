---
title: Contrast Checker — Make a pair pass
description: Use Make it pass AA to find a passing text colour, understand how it chooses, and keep your brand hue.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Make a pair pass

**Make it pass AA** is the main button in the result area. It only appears while the pair fails body text AA (under 4.5:1), so seeing it is itself a signal that body text is failing.

## Use it

1. Enter a failing pair, for example text `#D3AF37` on background `#F7F3E6` (1.90:1).
2. Select **Make it pass AA**.
3. Read the status line. For this pair it says "Adjusted text to #836C22 (4.58:1)."

The result: the new colour is in the **Text colour** field and swatch, the pair is re-graded, the button disappears, and the address updates a moment later with the new pair.

## How it chooses

1. It looks at the background. If the background's relative luminance is above 0.5 it moves the text towards black; otherwise towards white.
2. It walks the text colour along a straight line towards that end, in about fifty small steps, checking the ratio at each step.
3. It stops at the first step that reaches 4.5:1. If none does, it uses pure black or pure white.

## What it will not do

- **It only aims at 4.5:1.** There is no option for 3:1 or 7:1. For AAA, use the button first, then keep darkening (or lightening) by hand while you watch the ratio.
- **It never changes the background.** Only the text colour moves. If the background is the colour you are allowed to change, select the swap button, use the fix, then swap back.
- **It does not keep your hue or saturation.** The path is a straight line towards black or white, so the result is usually a greyer relative of your colour. Treat it as a target, not a colour to ship.
- **It is close to minimal, not exactly minimal.** It takes the first of about fifty samples that passes.

## The mid-grey surprise

The direction is chosen by relative luminance, not by how light a colour looks. Mid grey `#808080` has a relative luminance of about 0.22, which counts as dark, so text on it is pushed towards white even though the grey looks like the middle of the range. That is correct WCAG behaviour. If you wanted the other direction, move the text colour towards black yourself and watch the ratio.

## Keep your brand colour

1. Select **Make it pass AA** to see how far the pair has to move, and note the colour and ratio it reports.
2. Go back to your original colour.
3. Change it a few digits at a time towards the suggested colour, keeping the hue, and watch the ratio.
4. Stop as soon as **Body text · AA** reads **Pass**, and leave some margin.

You end up with a colour that is still yours and that passes.

For suggestions that keep the hue automatically across a whole page, the [Analyzer](../../analyzer/README.md) offers a replacement for every failing pair that adjusts only lightness.
