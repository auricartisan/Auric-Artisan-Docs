---
title: Harmony Library — FAQ
description: Short answers to common questions about the Harmony Library.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Harmony Library FAQ

## What is a colour harmony?

A set of colours whose hues sit in a deliberate pattern on the colour wheel: opposite (complementary), evenly spaced (triadic, square, pentadic, hexadic), neighbouring (analogous) or one hue at different lightness (monochromatic).

## How many schemes are there?

23, in five families. See the list in the [Glossary](../others/glossary.md).

## Why "none of them stored"?

Each harmony is calculated from a fixed seed when needed, so the same id always gives the same colours, and anyone can recalculate it.

## Can it tell me my palette's harmony?

Yes: **What harmony is this?** matches 2 to 12 colours against every scheme with the same number of colours. See [Identify your colours' harmony](identify-your-colours.md).

## Does the colour order matter?

No. Each colour is tried as the base.

## Why does it ignore lightness?

Harmony schemes are defined by hue angles. Lightness and saturation are what make a scheme usable for text, which is why the page reports pair contrast separately.

## What does adherence mean?

How closely a harmony's actual hues keep to its scheme's ideal angles, from 0% to 100%.

## Do I need an account?

No.

## Is there an API?

Yes. The heading links to the Harmony Library API guide, and the **Automate this** note names **GET /v1/harmony/library**. See [Public API](../../../../../services/public-api/README.md).
