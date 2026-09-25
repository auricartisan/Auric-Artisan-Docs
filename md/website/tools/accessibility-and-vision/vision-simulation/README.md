---
title: Vision Lab — Overview
description: What the Vision Lab simulates, who it is for, and how to see a colour, a palette or an image through 78 vision conditions.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Vision Lab

The Vision Lab (page title: Vision Deficiency Lab) shows how colours, palettes and images look to people with 78 different vision conditions, from the common colour-vision deficiencies such as deuteranopia to cataract, glaucoma, macular degeneration and dozens of rarer retinal, optic-nerve and corneal conditions. Its masthead reads "Seventy-eight ways of seeing, simulated."

Seventeen of the conditions are **per-colour transforms**: every colour has an exact answer, computed in linear light with the published colour-vision models of Brettel (1997), Viénot (1999) and Machado (2009). The other sixty-one are **field effects**: they change where and how clearly you see (blur, lost regions, glare, distortion) rather than changing each colour. Every condition runs the same ten reference swatches, so two conditions can be compared fairly.

The lab has five views. The **Workbench** takes one condition apart on a colour, a palette or your own image. The **Catalogue** is every condition as a card that opens a detailed floating panel. **Compare** lays one source out under many conditions side by side. **Palette audit** checks every pair in your palette under all 17 colour conditions and suggests fixes. **Analytics** maps the whole collection by category and severity. Everything runs in your browser; images you add are never uploaded.

> **Important:** The page states: "Educational visualisation only. Not a medical simulation, a diagnostic tool, or a substitute for professional eye care — and screen colours are not calibrated."

## Who it is for

- Designers checking that a palette, chart or interface still works for people with colour-vision deficiencies.
- Accessibility specialists demonstrating the effect of low vision and field loss.
- Educators and students learning how different eye conditions affect sight.
- Colour scientists comparing simulation models.

## Where to find it

- Address: https://auricartisan.com/tool/vision-simulation/
- A single condition in the Workbench: `https://auricartisan.com/tool/vision-simulation/?vw=deuteranopia:100:brettel` (condition, severity 0–100, model).

## Quick start

1. Open https://auricartisan.com/tool/vision-simulation/. It opens on the **Workbench**, with Deuteranopia selected.
2. Under **Specimen**, choose **Interface**, **Palette** or **Image**.
3. Type your brand colour into **Base colour**, for example `#D3AF37`, and read what it becomes under the condition.
4. Pick another condition from the list on the right, for example Protanopia or Tritanopia.
5. Read **What collapses**: pairs of reference colours that stop being distinguishable.
6. Select **Compare this** to see the same source under several conditions at once.
7. Open **Palette audit** and enter your palette's colours to find every pair that merges.
8. Select **Copy link to this view** to share what you are looking at.

## What you can do

- Simulate 78 conditions in 11 categories, each with an estimated severity score and a prevalence note.
- Set severity from 0 to 100% and choose the Brettel, Viénot or Machado model for colour-vision conditions.
- See interface mock-ups, a ten-colour palette, or your own image under a condition, side by side with the original.
- Measure colour change with ΔE76 and CIEDE2000, and count reference pairs that stop being distinguishable.
- Open up to five detailed floating panels, with colour-appearance settings, chromaticity diagrams, metrics, snapshots and exports.
- Feed one image to every open panel, from your own file or 15 built-in samples and 4 test charts.
- Compare many conditions on one contact sheet.
- Audit a palette of up to 24 colours under 17 colour conditions, with suggested lightness fixes.
- Export the catalogue as JSON or CSV, panels as images, and share any view as a link.

## In this folder

- [docs/](docs/README.md) — how to use the Vision Lab
  - [Getting started](docs/getting-started.md) — the screen, the five views, and a first simulation
  - [Use the Workbench](docs/use-the-workbench.md) — one condition, taken apart
  - [Browse the Catalogue and panels](docs/browse-the-catalogue-and-panels.md) — cards, filters, favourites, floating panels and the source image
  - [Compare conditions](docs/compare-conditions.md) — the contact sheet
  - [Audit a palette](docs/audit-a-palette.md) — pairs that merge, and fixes
  - [Explore Analytics](docs/explore-analytics.md) — the matrix, map and statistics
  - [The 78 conditions](docs/the-78-conditions.md) — every condition, by category
  - [Links, saving and exports](docs/links-saving-and-exports.md)
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
