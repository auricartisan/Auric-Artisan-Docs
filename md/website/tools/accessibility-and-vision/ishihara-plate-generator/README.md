---
title: Ishihara Plate Generator — Overview
description: What the Ishihara Plate Generator makes, who it is for, and how to generate, check and export your first plates.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Ishihara Plate Generator

The Ishihara Plate Generator makes dot plates in the style of the Ishihara colour-vision test: a circle of coloured dots in which a figure (a number, a letter, a symbol, a shape or a path to trace) stands out to typical colour vision and blends into the background for a particular colour-vision deficiency. The page describes them as "Dot plates that carry a figure to normal colour vision and hide it from a specific deficiency — generated, measured and scored on this device."

Every plate is scored as it is drawn. The generator measures how far apart the figure and background colours are for typical vision, then recomputes that distance through simulated protanopia, deuteranopia and tritanopia, and combines four measurements into a quality score. You can preview plates under each deficiency, build a standard set of 38 plates, and export plates as PNG or SVG with a seed that rebuilds any plate exactly.

Everything runs in your browser. There is no account, and nothing is uploaded.

> **Important:** The page states: "Not a colour-vision test. These plates are illustrative. A screen is not colour-calibrated and a real Ishihara examination is printed, lit and administered under controlled conditions. For diagnosis, see an eye-care professional."

## Who it is for

- Educators and students learning how colour-vision tests work.
- Designers and accessibility specialists demonstrating colour-vision deficiency to colleagues.
- Researchers and developers who need reproducible, seeded plates as figures or test material.

## Where to find it

- Address: https://auricartisan.com/tool/ishihara-plate-generation/

## Quick start

1. Open https://auricartisan.com/tool/ishihara-plate-generation/. Six starter plates are generated for you.
2. Choose a **Plate Type**, a **Color Palette** and a **Difficulty**.
3. Select **+ Generate**, or **×3** or **×6** for several plates at once.
4. On a plate card, switch between **Normal**, **Protan**, **Deutan** and **Tritan** to see how it looks under each deficiency.
5. Double-click a plate to open it full size.
6. Open the **Diagnostics** tab to see each plate's score taken apart.
7. Download a plate as PNG or SVG from its card, or open the **Export** tab to export every plate.

## What you can do

- Generate 7 plate types in 9 colour palettes (or at random), at 4 difficulty tiers.
- Make a custom plate with your own number, letter, symbol or shape, and an optional seed.
- Fine-tune dot count, plate shape, placement, dot style, card material, colour separation, edge blend, dot scale and texture grain.
- Preview plates under protanopia, deuteranopia and tritanopia.
- Read a quality score for each plate and its four components.
- Build the standard 38-plate set from a fixed seed.
- Export PNG (up to 4096 pixels), SVG (one circle per dot), a ZIP of every plate, and a seeds file to rebuild the batch.

## In this folder

- [docs/](docs/README.md) — how to use the generator
  - [Getting started](docs/getting-started.md) — the screen and your first plates
  - [Generate plates](docs/generate-plates.md) — the Lab: types, palettes, difficulty, custom plates, fine tuning and plate cards
  - [Read the diagnostics](docs/read-the-diagnostics.md) — the score and its four components
  - [Build the standard 38](docs/build-the-standard-38.md) — the fixed set
  - [Export plates](docs/export-plates.md) — PNG, SVG, ZIP and seeds
  - [Reference](docs/reference.md) — every control and output
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material
  - [Glossary](others/glossary.md)
  - [Keyboard shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools and reading](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
