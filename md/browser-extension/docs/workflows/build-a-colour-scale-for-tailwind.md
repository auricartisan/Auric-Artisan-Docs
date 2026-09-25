---
title: Browser extension — Build a colour scale for Tailwind
description: Turn one colour into a named, perceptually even Tailwind v4 scale from 50 to 950, check it, and keep it as a snippet.
product: Browser extension › Workflows
updated: 2026-09-25
---

# Build a colour scale for Tailwind

This workflow turns one colour into a full scale for a Tailwind v4 theme.

## 1. Choose the base colour

Open the Picker and set your colour: pick it from a page, type it, or choose it from History or Library.

## 2. Open the scale generator

1. In the Picker, open the **Scale** pane to preview an 11-step OKLCH scale.
2. Choose **Open the scale generator →**. Scale opens with your colour as the base.

## 3. Set up the scale

1. Keep the type on **Tailwind 50–950**. The chip reads **OKLCH · perceptual**: the steps are even in perceived lightness and the hue stays constant.
2. Type the **Scale name** you want in your classes, such as `brand` or `accent`.
3. Find the marked step: it is the one nearest your base colour.

## 4. Check the steps

1. Choose a step to see its values.
2. Choose **Contrast** in its card and check it against white or your dark background. Typically lighter steps suit backgrounds and darker steps suit text on white; confirm with the checker rather than assuming.
3. If your brand colour should sit on a specific step, choose that step and **Make base** to rebuild the scale around it.

## 5. Export

1. Choose **@theme** to copy a Tailwind v4 `@theme` block, or **Tailwind** for a Tailwind colour object.
2. Paste it into your CSS or config.
3. Choose **Tokens** instead if you keep colours as W3C design tokens.
4. Choose **Save** to keep the scale's CSS in Snippets for later.

**The result:** a named 11-step scale in your Tailwind theme, with the steps you checked for contrast.

## Related pages

- [Scale](../colour/scale.md)
- [Snippets](../code/snippets.md)
