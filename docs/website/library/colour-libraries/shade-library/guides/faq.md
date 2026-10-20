---
title: Shade Library — FAQ
description: Short answers to common questions about the Shade Library.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Shade Library FAQ

## What is a shade scale?

One colour taken through lightness in named steps, from a near-white tint to a near-black shade. Light steps become surfaces, dark steps become text, and middle steps become fills and accents.

## What are tokens?

The named steps of a scale, such as `50`, `100` … `900`, `950`. The collection uses several naming patterns and has between 5 and 21 tokens per scale.

## What do the methods mean?

They are the ten generation styles: **Material Like**, **Tailwind Like**, **Brand System**, **Accessible Ui**, **Oklch Ramp**, **Neutral System**, **Ink Paper**, **Vivid Product**, **Duotone Shift** and **Temperature Shift**. **Tailwind Like** and **Material Like** follow the step naming of those design systems.

## What does "8% even" mean?

The page reports that only 8.2% of the scales have genuinely even steps — no step much larger than the average. Even steps make a scale predictable to use.

## Can every step carry text?

In 403 of the 8,192 scales, every token reaches 4.5:1 with automatic black or white text. In most scales the middle steps do not. See [Analyse the collection](analyse-the-collection.md).

## Can I use a scale in Tailwind?

Yes: **Copy Tailwind** gives a colour group keyed by token, and **Design tokens…** › **Tailwind Config** gives a full configuration file.

## Do I need an account?

No.

## Is there an API?

Yes. The heading links to the Shade Library API guide, and the **Automate this** note names **GET /v1/shade/library**. See [Public API](../../../../../services/public-api/README.md).
