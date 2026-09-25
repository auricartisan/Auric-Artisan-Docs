---
title: Personalization Generator — Overview
description: What the Personalization Generator is, who it is for, where to find it, and how to turn a colour pool and a short brief into palettes, gradients, type, UI pairs, posters, design tokens and a live brand Studio.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Personalization Generator

The Personalization Generator turns the colours you like and a short brief into a whole visual system. You give it a **pool** of colours (your brand colours, colours you admire, a preset), pick a few style words and a use case, and describe what you want, such as *calm premium dashboard for creators*. It then runs a **sweep**: it samples hundreds or thousands of candidate palettes, scores each one for closeness to your pool, colour harmony, fit with your styles, variety, contrast and colour-vision safety, and keeps the best.

From the kept palettes it derives gradients in twelve styles, typography pairings, UI colour pairs, posters in twelve layouts, a full design-token system (semantic roles, tonal ramps, light, dark and high-contrast themes, a WCAG and APCA contrast audit and data-visualisation scales) and a **Brand Studio** that paints any palette across sixteen live mockups, from a dashboard to an email. Everything can be copied as CSS, downloaded as JSON or saved to your Library.

The sweep runs in your browser in small chunks, so the page stays responsive, and you can stop it at any time without losing what it has found.

## Who it is for

- Brand and product designers exploring colour directions from a starting set.
- Founders and small teams who want a coherent system without a designer on hand.
- Front-end developers who want tokens and CSS from a palette.
- Anyone who wants to see a palette on real interfaces before committing to it.

## Where to find it

- Page: https://auricartisan.com/tool/personalization-gen/ (the short address https://auricartisan.com/personalization also opens it).
- No sign-in is needed. Saving uses your Auric Artisan Library.
- The page notes the matching REST call: **Automate this — 14 API credits per call to POST /v1/personalize/system**. See the [Public API](../../../../services/public-api/README.md).

## Quick start

1. Open https://auricartisan.com/tool/personalization-gen/. A quick first sweep runs by itself, so there are results on screen straight away.
2. Open **Pool** and add one or two of your own colours with **Add**.
3. In **The brief**, type what you want, for example *warm editorial brand for a bookshop*.
4. Select **Generate** (or press `Enter` in the brief). Watch **The run** on the right.
5. Open **Palettes** to see the ranked results with their scores.
6. Select **Open in Studio** on a palette you like and look at the sixteen mockups.
7. Open **Export** and select **Copy CSS**, or **Download JSON** for everything.

## What you can do

- Build a colour pool by hand, from quick seed sets, from 17 presets, by expanding it automatically or by adding random related colours.
- Steer the search with 18 style chips, 5 intents, a preference note and scoring weights for diversity, accessibility and warmth.
- Run sweeps of 40 to 4,000 candidates, stop them, or run them endlessly.
- Get ranked palettes with score breakdowns, and gradients, type combinations, UI pairs and posters derived from them.
- Get a design-token system from the top palette, with a contrast audit and chart scales.
- Try any palette on sixteen Studio mockups, with theme, density, token inspection and live token swaps.
- Copy CSS for any result, export all tokens as CSS, download a JSON snapshot, and save results to your Library.

## In this folder

- [docs/](docs/README.md) — how to use the generator.
  - [Getting started](docs/getting-started.md)
  - [Build your colour pool](docs/build-the-pool.md)
  - [Tune the sweep](docs/tune-the-sweep.md)
  - [Run a sweep and read the results](docs/run-a-sweep.md)
  - [Palettes, gradients, typography, UI pairs and posters](docs/result-tabs.md)
  - [Design tokens](docs/design-tokens.md)
  - [Brand Studio](docs/brand-studio.md)
  - [Presets](docs/presets.md)
  - [Export, save and share](docs/export-and-save.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related](others/related.md)
  - [Privacy](others/privacy.md)
