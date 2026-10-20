---
title: Ishihara Plate Generator — Getting started
description: Open the Ishihara Plate Generator, learn the screen, and generate and inspect your first plates.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Getting started with the Ishihara Plate Generator

## Open it

Go to https://auricartisan.com/tool/ishihara-plate-generation/. No account is needed. When the page loads, it generates six starter plates and says "Welcome! 6 starter plates generated."

## The screen, top to bottom

### Masthead

The kicker "Auric Artisan · Vision", the title **Ishihara Plate Generation**, and a one-line description. The description depends on the site-wide Simple or Advanced preference; in Simple mode it reads "Dot plates that carry a figure to normal colour vision and hide it from a specific deficiency — generated, measured and scored on this device."

A row of facts follows: 7 plate types, 9 colour palettes, 4 difficulty tiers, 3 CVD simulations, OKLab colour science, ΔE validation, PNG / SVG export, On-device, and a **Developer reference →** link.

### API hint

"Automate this — 3 API credits per call to `POST /v1/ishihara/plate`." It tells developers that plates can also be generated from the REST API, and that API credits are a separate balance from tool tokens. **API docs** opens the endpoint's documentation; **×** hides the hint on every tool page.

### The notice

"Not a colour-vision test. These plates are illustrative. A screen is not colour-calibrated and a real Ishihara examination is printed, lit and administered under controlled conditions. For diagnosis, see an eye-care professional."

### The four tabs

| Tab | What it is for |
| --- | --- |
| **Lab** | Generate plates and see them on the bench |
| **Diagnostics** | Each plate's score, taken apart |
| **Set 38** | Build the standard 38-plate set |
| **Export** | Export every plate as PNG, SVG, a ZIP or a seeds file |

## Your first plates

1. On the **Lab** tab, open **Plate Type** and choose **Number**.
2. Open **Color Palette** and choose **Red vs Green**.
3. Open **Difficulty** and choose **Easy**.
4. Select **+ Generate**. A new card appears on the bench, and the page says "Plate #7 generated —" followed by the number drawn.
5. On the new card, select **Protan** and then **Deutan**. The plate is redrawn as it might look to someone with protanopia or deuteranopia; the number should become harder to see.
6. Select **Normal** to return to the original.
7. Double-click the plate to open it full size. Press `Right` and `Left` to move between plates, and `Esc` to close.
8. Open the **Diagnostics** tab and find your plate: its score, whether it passed, and its four components.

The result: a scored plate you can download from its card as PNG or SVG.

> **Note:** Plates are not saved between visits. Export anything you want to keep, or keep its seed so you can rebuild it.

## Next steps

- [Generate plates](generate-plates.md) for every Lab control.
- [Read the diagnostics](read-the-diagnostics.md) to understand the score.
- [Export plates](export-plates.md) to keep your plates.
