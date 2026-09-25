---
title: Accessibility Library — Overview
description: What the Accessibility Color Pair Library is, who it is for, where to find it, and how to find text colours that pass on any background.
product: Website › Library › Colour libraries › Accessibility Library
updated: 2026-09-25
---

# Accessibility Library

The Accessibility Library — the Accessibility Color Pair Library — answers one question: "What may I write *on this?*" You choose a background colour (the page calls it the **ground**) and a contrast target, and the page draws a map of every foreground colour, with a line showing exactly where text starts to pass. Contrast depends on both colours continuously, so the answer is a territory, not a list, and the boundary moves with hue: at the same lightness, yellow gives far more contrast than blue, so "just make it darker" means different things for different hues.

Around the map, the page gives you a concrete answer — up to twelve foreground colours, one per 30° of hue, that clear your target on your ground, ready to copy as CSS — and an audit for colours you already have: paste your palette and each colour is placed on the map, with how much lighter or darker it would need to be to pass.

Behind all of this is an index of 5,000,000 scored foreground and background pairs. Like the other libraries, it is defined by a seed rather than stored, so any record — for example `acc_91` — can be cited in an audit and recomputed by whoever reads it. Every figure is computed in your browser.

## Who it is for

- Designers choosing text, icon and UI colours for a given background.
- Accessibility specialists auditing a palette against a ground, or citing a reproducible pair.
- Developers who want a set of passing foregrounds as CSS custom properties.
- Anyone learning how contrast, lightness and hue interact.

## Where to find it

Open https://auricartisan.com/library/accessibility/ in a current browser. It is also listed as **Accessibility Library** ("Tested accessible color pairs") under **Libraries** in the site header's **Learn** menu. No account is needed.

## Quick start

1. Open https://auricartisan.com/library/accessibility/. The ground starts as `#1D2A3E` (a dark navy) and the target as **4.5:1**.
2. Choose a ground: one of the four preset swatches, or the colour picker for any colour.
3. Choose a target: **3:1**, **4.5:1** or **7:1**.
4. Drag on the map. The panel beside it shows your foreground on the ground, its contrast ratio and whether it passes.
5. Read **Territory** to see how much of the colour space passes on this ground.
6. Scroll to the picks and select **Copy as CSS** to take up to twelve passing colours.
7. Paste your own palette into **Or bring your own** to see which colours fail and by how much.

## What you can do

- See, for any background, every foreground colour that reaches 3:1, 4.5:1 or 7:1.
- Read a colour's WCAG contrast ratio, APCA lightness contrast (Lc), and how well it stays distinct under ten simulated vision conditions.
- Get up to twelve passing foregrounds across the hue circle, and copy them as CSS custom properties.
- Audit up to 24 of your own colours against the ground, with the lightness change each failure needs.
- Swap foreground and ground to ask the question the other way round.
- Look up any of five million scored pairs by id, and browse pairs that pass.
- Automate the same answers through the site's REST API.

## In this folder

- [docs/](docs/README.md) — how to use the Accessibility Library.
  - [Getting started](docs/getting-started.md), [Read the contrast map](docs/read-the-contrast-map.md), [Use the picks](docs/use-the-picks.md), [Check your own colours](docs/check-your-own-colours.md), [Look up and browse the index](docs/look-up-and-browse-the-index.md), [Reference](docs/reference.md), [Troubleshooting](docs/troubleshooting.md), [FAQ](docs/faq.md).
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md), [Shortcuts](others/shortcuts.md), [Limits and accuracy](others/limits-and-accuracy.md), [Related](others/related.md), [Privacy](others/privacy.md), [Release notes](others/release-notes.md).
