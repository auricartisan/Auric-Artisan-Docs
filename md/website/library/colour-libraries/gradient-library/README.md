---
title: Gradient Library — Overview
description: What the Gradient Library is, who it is for, where to find it, and how to check your own gradient and export one from the collection.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Gradient Library

The Gradient Library is a collection of 8,192 generated colour gradients, each with its colour stops, the colour space it was blended in, its easing, a quality score and — the thing a thumbnail cannot show — a measured verdict on whether it bands. The page headline puts it plainly: "Eight thousand ramps, *and which of them band.*" About 77% of the collection is measured as smooth.

Banding is when a gradient that should flow shows visible steps or a hard edge. It often happens at the dark end of a ramp, or where two stops are far apart in lightness. The library measures every gradient for it, lets you filter by the verdict, and — through **Will your gradient band?** at the top of the page — applies the same measurement to any stops you type in. That makes the collection useful not only to shop from, but to check your own work against.

For any gradient in the collection you can read its stops and metrics, preview it under four kinds of colour vision deficiency and low vision, test text colours on top of it, and take it away as CSS, a CSS class, JSON, SVG, PNG, a Tailwind token or design tokens for eight platforms, or as a share link.

## Who it is for

- Designers and front-end developers choosing a gradient for a hero, button or background.
- Anyone who has a gradient already and wants to know whether it will band before shipping it.
- Accessibility specialists checking whether text on a gradient stays readable across the whole ramp.
- Students learning how interpolation space and easing change a blend.

## Where to find it

Open https://auricartisan.com/library/gradient/ in a current browser. It is also listed as **Gradient Library** ("Perceptual gradients") under **Libraries** in the site header's **Learn** menu. No account is needed.

## Quick start

1. Open https://auricartisan.com/library/gradient/.
2. In **Will your gradient band?**, read the verdict for the starting ramp (black, navy, white): it steps at the dark end.
3. Replace the stops with your own colours, in any CSS format, and read the new verdict.
4. Scroll to **Browse the collection** and set **Banding** to **Low banding risk**.
5. Select a card to open it on the **Inspect** tab.
6. Select **Copy CSS** and paste the `linear-gradient(...)` into your stylesheet.
7. Open the **Pair** tab and check that your text colour passes across the whole gradient.

## What you can do

- Measure any gradient you type in for banding, and see where its worst step is.
- Browse, search and filter 8,192 gradients by method, scheme, complexity, number of stops, interpolation space, easing, score and banding.
- Sort by score, complexity, number of stops or dominant hue, or shuffle.
- Inspect a gradient's stops, CSS and generator metrics.
- Preview it under deuteranopia, protanopia, tritanopia, achromatopsia and low vision.
- Measure contrast across 17 points of the ramp, and test any text colour over it.
- Explore the collection by tags, and read distributions on the **Stats** tab.
- Copy CSS; download a CSS class, JSON, SVG, PNG or Tailwind token; export design tokens; share a link.
- Save gradients in your browser and your Library, and download whole filtered sets.

## In this folder

- [docs/](docs/README.md) — how to use the Gradient Library.
  - [Getting started](docs/getting-started.md), [Check your own gradient](docs/check-your-gradient.md), [Browse, search and filter](docs/browse-search-and-filter.md), [Inspect a gradient](docs/inspect-a-gradient.md), [Test vision, contrast and text](docs/test-vision-contrast-and-text.md), [Tags and statistics](docs/tags-and-statistics.md), [Copy, export and share](docs/copy-export-and-share.md), [Save gradients](docs/save-gradients.md), [Reference](docs/reference.md), [Troubleshooting](docs/troubleshooting.md), [FAQ](docs/faq.md).
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md), [Shortcuts](others/shortcuts.md), [Limits and accuracy](others/limits-and-accuracy.md), [Related](others/related.md), [Privacy](others/privacy.md), [Release notes](others/release-notes.md).
