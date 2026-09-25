---
title: Gradient Library — FAQ
description: Short answers to common questions about the Gradient Library.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Gradient Library FAQ

## How many gradients are there?

8,192, with between 2 and 46 stops each. All of them are linear gradients.

## How smooth is the collection?

6,342 gradients (about 77%) are measured as smooth, 330 show subtle compression, and 1,520 carry a visible step risk.

## Can I check a gradient I made elsewhere?

Yes. Type its stops into **Will your gradient band?** in any CSS colour format. See [Check your own gradient](check-your-gradient.md).

## What does interpolation space mean?

The colour space in which the colours between two stops are worked out. Blending in sRGB (the CSS default) can produce muddy middles and uneven steps; blending in OKLab or OKLCH usually gives more even, brighter transitions.

## What is easing?

A curve that controls how fast a blend moves between two stops — steadily (**Linear**), or slowly at the ends and faster in the middle (**Sine In Out**, **Cubic In Out**, **Quart In Out**, **Smootherstep**).

## What does the score mean?

A quality score from 0 to 1 recorded for each gradient. The **Score** filter groups it into **Top quality** (0.70 or more), **Balanced+** (0.55 or more) and **Wild / experimental** (below 0.55). It is a ranking aid, not a guarantee.

## Can I put text on a gradient?

Yes, if it stays readable across the whole ramp. Use the **Pair** tab to test your text colour; see [Test vision, contrast and text](test-vision-contrast-and-text.md).

## Do I need an account?

No. Saved gradients stay in your browser and your Library.

## Is there an API?

Yes. The heading links to the Gradient Library API guide, and the **Automate this** note names the call (**GET /v1/gradient/library**). See [Public API](../../../../../services/public-api/README.md).
