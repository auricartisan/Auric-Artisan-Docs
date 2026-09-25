---
title: Harmony Library — Overview
description: What the Harmony Library is, who it is for, where to find it, and how to identify your own colours' harmony and export a scheme.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Harmony Library

The Harmony Library is a collection of 8,192 colour harmonies built on 23 colour-theory schemes — complementary, split complementary, triadic, tetradic, square, analogous, monochromatic, hexadic, pentadic, golden ratio and more — grouped into five families. The headline says "Eight thousand schemes, *and none of them stored*": every harmony is worked out from a fixed seed when you need it, so an id such as `har_5k` always means the same colours, anywhere. It is, in the page's words, "a claim anyone can recompute".

A colour harmony is a set of colours whose hues sit in a deliberate pattern around the colour wheel — opposite each other, evenly spaced, or close neighbours. The library shows each harmony's colours with their roles in the scheme (base, complement, triad, accent and so on), how closely they keep to the scheme's ideal angles, and — the part a row of swatches cannot show — which of its colours can carry text on each other. Only about a quarter of the collection contains two colours you could set text with.

The library also works the other way round. In **What harmony is this?**, you type in colours you already use and it tells you which of the 23 schemes they form, how closely, and which other schemes look identical by hue alone.

## Who it is for

- Designers who want palettes grounded in colour theory, and want to know which colours are safe for text.
- Anyone who wants to name the harmony behind an existing brand palette.
- Front-end developers who need a scheme as CSS, SCSS, Tailwind or design tokens.
- Students learning how the classic colour-wheel schemes relate.

## Where to find it

Open https://auricartisan.com/library/harmony/ in a current browser. It is also listed as **Harmony Library** ("Color relationships") under **Libraries** in the site header's **Learn** menu. No account is needed.

## Quick start

1. Open https://auricartisan.com/library/harmony/.
2. In **What harmony is this?**, read the answer for the starting colours: three hues 120° apart, a triadic.
3. Replace them with your own colours and select **Identify it**.
4. Scroll to **Browse the collection** and set **Family** to **Analogous**.
5. Select **Inspect** on a card to see its roles, adherence and pair contrast.
6. Under **Quick export**, select **Copy CSS vars** and paste the variables into your stylesheet.
7. Select **Save to library** to keep the harmony.

## What you can do

- Identify which of 23 schemes any 2 to 12 colours form, with a fit score and the runners-up.
- Browse all 8,192 harmonies, jump to any by id, and search by id, hex, method or family.
- Filter by hue, chroma, lightness and family; sort by lightness, chroma, hue or number of colours.
- Inspect a harmony: colour roles, descriptive names, scheme description and canonical angles, adherence, pair contrast and every colour's values.
- Read distributions of schemes, families, hues, adherence and contrast on the **Theory**, **Accessibility** and **Stats** tabs.
- Copy as hex, CSS, SCSS or Tailwind; download JSON, ASE, SVG or PNG; open in Coolors; export design tokens; share a link.
- Save harmonies in your browser and your Library, and export whole filtered sets.

## In this folder

- [docs/](docs/README.md) — how to use the Harmony Library.
  - [Getting started](docs/getting-started.md), [Identify your colours' harmony](docs/identify-your-colours.md), [Browse, search and filter](docs/browse-search-and-filter.md), [Inspect a harmony](docs/inspect-a-harmony.md), [Analyse the collection](docs/analyse-the-collection.md), [Copy, export and share](docs/copy-export-and-share.md), [Save harmonies](docs/save-harmonies.md), [Reference](docs/reference.md), [Troubleshooting](docs/troubleshooting.md), [FAQ](docs/faq.md).
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md) (including all 23 schemes), [Shortcuts](others/shortcuts.md), [Limits and accuracy](others/limits-and-accuracy.md), [Related](others/related.md), [Privacy](others/privacy.md), [Release notes](others/release-notes.md).
