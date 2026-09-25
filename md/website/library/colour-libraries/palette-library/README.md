---
title: Palette Library — Overview
description: What the Palette Library is, who it is for, where to find it and how to find and export your first palette.
product: Website › Library › Colour libraries › Palette Library
updated: 2026-09-25
---

# Palette Library

The Palette Library is a browsable collection of 5,000,000 five-colour palettes. The page headline is "Five million palettes, *and a 660-byte file.*": the collection is not stored as a list, because written out in full it would take 3.9 GB. Instead, every palette is worked out from a fixed starting number (a seed) the moment you scroll to it. The same palette id always gives the same five colours, on any computer, so an id such as `pal_abc` is a stable reference you can write down or share.

That design has one consequence the page is open about. Nothing can look at five million palettes at once, so a filter does not narrow a list — it starts a scan through the collection, and the counter under the grid tells you how many palettes were worked out to find the ones you are looking at. The analysis tabs (Harmony, Accessibility, Stats) likewise measure a sample and say how big it was.

For each palette you can read every colour in HEX, RGB, OKLCH and CIE Lab, check the contrast between every pair of its colours and against white and black, copy it as CSS, SCSS or Tailwind, download it as JSON, Adobe ASE, SVG or PNG, export it as design tokens for eight platforms, share a link to it, or save it to your Library.

## Who it is for

- Designers looking for palette ideas they can inspect and trust, not only look at.
- Front-end developers who want a palette as CSS variables, SCSS, Tailwind or design tokens.
- Accessibility specialists checking which colours in a palette can carry text on each other.
- Students exploring how colours are distributed across a very large generated collection.

## Where to find it

Open https://auricartisan.com/library/palette/ in a current browser. It is also listed as **Palette Library** ("Scientific color palettes") under **Libraries** in the site header's **Learn** menu. No account or installation is needed.

## Quick start

1. Open https://auricartisan.com/library/palette/. The grid fills with palettes, starting with `pal_0`.
2. Select a single colour in any palette to copy its hex code.
3. Choose **Vivid (> 0.15)** in **Chroma** and **Blue** in **Dominant hue**. The page scans the collection and shows matching palettes; the counter under the grid says how many were derived.
4. Select **Inspect** on a palette you like. The **Inspect** tab opens.
5. Read **Pair-by-pair WCAG contrast** to see which of its colours can carry text on each other.
6. Select **Copy CSS vars** under **Quick export**, and paste the result into your stylesheet.
7. Select **Save to library** to keep it.

## What you can do

- Scroll through all 5,000,000 palettes, or jump straight to any palette by its id.
- Search by id, hex code or generation method, and filter by dominant hue, average chroma, average lightness and method.
- Sort by lightness, chroma or hue, or shuffle.
- Inspect a palette: descriptive colour names, summary metrics, pair contrast and per-colour values.
- See how methods, hues, harmony types and contrast are distributed across a sample, on the **Harmony**, **Accessibility** and **Stats** tabs.
- Copy a palette as a hex list, CSS variables, SCSS variables or a Tailwind snippet.
- Download it as JSON, Adobe Swatch Exchange (ASE), SVG or PNG, or open it in Coolors.
- Export it as design tokens in eight formats, including W3C Design Tokens, Material UI, SwiftUI and Android.
- Share a link that opens the same palette for anyone.
- Save palettes in your browser and find them in your Library.
- Download a whole sample of palettes as JSON, CSV, CSS, SCSS, plain text or Tailwind.

## In this folder

- [docs/](docs/README.md) — how to use the Palette Library.
  - [Getting started](docs/getting-started.md) — open the page, the screen tour and a first palette.
  - [Browse, search and filter](docs/browse-search-and-filter.md) — scanning, the counter, ids, filters and sorting.
  - [Inspect a palette](docs/inspect-a-palette.md) — everything on the **Inspect** tab.
  - [Analyse the collection](docs/analyse-the-collection.md) — the **Harmony**, **Accessibility** and **Stats** tabs.
  - [Copy, export and share](docs/copy-export-and-share.md) — every copy format, download, design tokens and share links.
  - [Save palettes](docs/save-palettes.md) — the **Saved** tab and your Library.
  - [Reference](docs/reference.md) — every control, output and message.
  - [Troubleshooting](docs/troubleshooting.md) — symptoms, causes and fixes.
  - [FAQ](docs/faq.md) — short answers.
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md), [Shortcuts](others/shortcuts.md), [Limits and accuracy](others/limits-and-accuracy.md), [Related](others/related.md), [Privacy](others/privacy.md), [Release notes](others/release-notes.md).
