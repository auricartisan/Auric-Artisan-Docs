---
title: Palette Library — FAQ
description: Short answers to common questions about the Palette Library.
product: Website › Library › Colour libraries › Palette Library
updated: 2026-09-25
---

# Palette Library FAQ

## Are there really five million palettes?

Yes. Each of the 5,000,000 palettes is defined by its number and worked out when you view it. The same id always gives the same five colours.

## Why not store them?

Written out in full, the collection was 3.9 GB. Working palettes out as you scroll keeps the page fast and the download tiny.

## How do I get back to a palette I found?

Note its id (for example `pal_abc`) and type it into the search box, save it, or copy a share link.

## Why does a filter say "derived"?

Because the page has to work out palettes to test them. **96 matches from 1,500 derived** means it has looked at 1,500 palettes and 96 passed.

## Can every colour in a palette be used as text on every other?

No — not in this library or any other. There is only room for three lightness levels that are all 4.5:1 apart, so at most three colours can all be legible on each other, and in practice palettes here offer two. Use **Pair-by-pair WCAG contrast** on **Inspect** to find the pairs that work. See [Analyse the collection](analyse-the-collection.md).

## What do the method names mean?

They are the palette's generation-method labels: `complementary`, `triadic`, `analogous`, `tetradic`, `golden_ratio`, `random` and `monochromatic`. The badge on **Inspect** measures the hue relationship the colours actually have.

## Which export should I use?

- Pasting into CSS: **Copy CSS vars**.
- A Tailwind project: **Copy Tailwind**, or **Design tokens…** › **Tailwind Config**.
- Adobe apps: **Download ASE**.
- A design system or native app: **Design tokens…**.
- A presentation or mood board: **Download PNG** or **Download SVG**.

## Do I need an account?

No. Saving keeps palettes in this browser and in your Library without signing in.

## Is there an API?

Yes. The heading links to the Palette Library API guide, and the **Automate this** note names the call (**GET /v1/palette/library**, 3 API credits per call). See [Public API](../../../../../services/public-api/README.md).
