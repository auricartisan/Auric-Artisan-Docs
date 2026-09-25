---
title: Shade Library — Overview
description: What the Shade Library is, who it is for, where to find it, and how to find and export a first shade scale.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Shade Library

The Shade Library is a collection of 8,192 shade scales (also called shade systems or colour ramps). A shade scale is one colour taken from very light to very dark in named steps — the familiar `50`, `100`, `200` … `900`, `950` of design systems such as Tailwind CSS or Material Design. The page puts the difference from a palette clearly: "A shade scale is not a palette. It is one colour taken through lightness so that some steps are surfaces and others are text on them."

The headline, "Eight thousand ramps, *and 8% of them even*", sums up what the page measures. All 8,192 scales run in one direction and all can carry text, but only 8.2% have genuinely even steps. The scales come from ten generation methods — from Material-like and Tailwind-like ramps to accessible-UI, neutral, ink-and-paper, duotone and temperature-shift systems — with 5 to 21 tokens each.

For each scale you can read every token's value in HEX, RGB, OKLCH and CIE Lab, see which tokens can carry body text with black or white text on them, and export the whole scale as CSS custom properties, SCSS, a Tailwind colour group, JSON, SVG, PNG or design tokens for eight platforms.

## Who it is for

- Designers and developers building a design system who need a full tint-and-shade scale for a brand colour.
- Front-end developers who want token-named CSS variables or a Tailwind colour group ready to paste.
- Accessibility specialists checking which steps of a scale can carry text.

## Where to find it

Open https://auricartisan.com/library/shades/ in a current browser. It is also listed as **Shade Library** ("OKLCH shade systems") under **Libraries** in the site header's **Learn** menu. No account is needed.

## Quick start

1. Open https://auricartisan.com/library/shades/.
2. Set **Base hue** to the hue of your brand colour, for example **Blue**.
3. Set **Method** to **Tailwind Like**.
4. Select **Inspect** on a scale.
5. Read the **Token contrast ladder** to see which steps carry text.
6. Under **Quick export**, select **Copy CSS vars**.
7. Paste the variables into your stylesheet.

## What you can do

- Browse, search and filter 8,192 scales by base hue, chroma, lightness and method.
- Sort by lightness, chroma, hue, score or number of tokens.
- Inspect a scale: token names, descriptive colour names, summary metrics, a contrast ladder and every token's values.
- Read distributions of methods, hues, profiles and accessibility across your filtered set.
- Copy a scale as hex, CSS, SCSS or Tailwind; download JSON, SVG or PNG; export design tokens; share a link.
- Save scales in your browser and your Library, and export whole filtered sets.

## In this folder

- [docs/](docs/README.md) — how to use the Shade Library.
  - [Getting started](docs/getting-started.md), [Browse, search and filter](docs/browse-search-and-filter.md), [Inspect a scale](docs/inspect-a-scale.md), [Analyse the collection](docs/analyse-the-collection.md), [Copy, export and share](docs/copy-export-and-share.md), [Save scales](docs/save-scales.md), [Reference](docs/reference.md), [Troubleshooting](docs/troubleshooting.md), [FAQ](docs/faq.md).
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md), [Shortcuts](others/shortcuts.md), [Limits and accuracy](others/limits-and-accuracy.md), [Related](others/related.md), [Privacy](others/privacy.md), [Release notes](others/release-notes.md).
