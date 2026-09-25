---
title: Color Science Lab — Overview
description: What the Color Science Lab is, who it is for, where to find it, and how to start with its Workbench, Compare, Gamut audit and Illuminants views and its 45 panel tools.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Science Lab

The Color Science Lab is a research workspace for colour science on the Auric Artisan website. It has five views. Four of them work on colours you enter and compute their results with published formulas: the **Workbench** resolves one colour into CIE XYZ, xyY, Lab, LCh, Oklab, Oklch and more under the illuminant and standard observer you choose; **Compare** measures the difference between two colours with ΔE 2000, ΔE 1994, ΔE 1976 and Oklab distance; **Gamut audit** checks a palette against sRGB, Display P3, Adobe RGB and Rec. 2020; and **Illuminants** shows how one colour shifts under seven standard lights.

The fifth view, the **Catalogue**, opens 45 tools in eight domains (colorimetry, chromatic adaptation, spectral analysis, appearance models, perceptual spaces, colour spaces, theory and history, and gamut and rendering) as floating panels. Each panel has the same controls (sample and compare colours, model, colour space, theory, white points, strength and colour temperature) and six tabs, and it reads out coordinates in any of 63 colour spaces. Up to five panels can be open, linked so that shared controls move together, arranged with a floating control centre, and exported as one image.

Everything is calculated in your browser. The coordinates are computed from standard formulas; some panel previews are illustrations of a model's effect rather than full implementations, which [Limits and accuracy](others/limits-and-accuracy.md) explains.

## Who it is for

- Colour scientists, imaging engineers and students who want to see conversions, white points and observers side by side.
- Designers and developers who need Lab, Oklch, xy or ΔE values, or want to know whether a palette survives a wide-gamut conversion.
- Print and product teams checking how a colour holds up under different lights.

## Where to find it

- Page: https://auricartisan.com/tool/color-science-lab/ (the short address https://auricartisan.com/model also opens it).
- No sign-in is needed. Saving panel presets uses your Auric Artisan Library.
- A related REST endpoint exists: the page notes **Automate this — 5 API credits per call to POST /v1/science/dossier**. See the [Public API](../../../../services/public-api/README.md).

## Quick start

1. Open https://auricartisan.com/tool/color-science-lab/. The **Workbench** view opens first.
2. Type a HEX code such as `#4F7FE0` in the **Specimen** box, or pick a preset swatch.
3. Read **Resolved coordinates**: XYZ, xyY, Lab, LCh, Oklab, Oklch, sRGB, HSL and CMYK.
4. Select illuminant **A** and watch the Lab values and the **Under other light** list change.
5. Open **Compare**, set a **Candidate** colour, and read ΔE 2000.
6. Open **Catalogue**, select a tool card such as **Bradford Adaptation**, and it opens as a floating panel.
7. Open a second tool, select the link button on both panels, and change the sample colour: both follow.

## What you can do

- Resolve a colour into nine notations under seven illuminants, two observers and three adaptation transforms.
- Measure colour difference four ways and see whether the gap is lightness, chroma or hue.
- Audit a palette of up to 16 colours for gamut headroom in four RGB working spaces.
- See a colour adapted to seven CIE illuminants with ΔE 2000 shifts.
- Open 45 colour-science tools as panels, each with an experiment canvas, metrics, chart, response graph, model diagram and a per-space dossier.
- Compare up to eight tools at once on a six-colour test palette, and explore a heat map, mind map, statistics and a catalogue of 63 colour spaces and 24 theories, exportable as JSON or CSV.
- Link, tile, split, cascade, stack, pin, dock and export panels.

## In this folder

- [docs/](docs/README.md) — how to use the lab.
  - [Getting started](docs/getting-started.md)
  - [The Workbench](docs/workbench.md)
  - [Compare two colours](docs/compare-two-colours.md)
  - [Gamut audit](docs/gamut-audit.md)
  - [Illuminants](docs/illuminants.md)
  - [The Catalogue and its panels](docs/catalogue-and-panels.md)
  - [The 45 tools](docs/tool-list.md)
  - [Catalogue Compare and Analytics](docs/catalogue-compare-and-analytics.md)
  - [Arrange, link, save and export panels](docs/arrange-link-save-export.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related](others/related.md)
  - [Privacy](others/privacy.md)
