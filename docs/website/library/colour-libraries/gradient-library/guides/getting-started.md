---
title: Gradient Library — Getting started
description: Open the Gradient Library, learn what each part of the screen does, and check, pick and export a first gradient.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Getting started

## Open the page

1. Go to https://auricartisan.com/library/gradient/, or open the **Learn** menu in the site header and select **Gradient Library** under **Libraries**.
2. While the collection loads, the grid area shows **Loading gradient library...**.
3. When it is ready, the grid fills with gradient cards and the counter under the grid reads, for example, **1–24 of 8,192**.

If loading fails you see **Could not load gradient library** and the reason. See [Troubleshooting](troubleshooting.md).

## A tour of the screen

### The heading

The kicker reads **Auric Artisan · Gradient** and the headline **Eight thousand ramps, and which of them band.** The line under it shows **Collection 8,192**, **Smooth 77%** and **Measured in OKLab**, and a link, **Read the API guide →**, to the Gradient Library's API guide.

A note starting **Automate this** may appear. It says browsing the collection is also available through the site's REST API — **3 API credits per call to GET /v1/gradient/library** — and links to **API docs**. Select × to dismiss it.

### Will your gradient band?

A row of colour stops, each with a colour swatch you can click to pick a colour and a text field you can type into, plus **Add a stop** and **Measure it**. Under them, the verdict for the ramp: a preview strip with a marker at the worst step, a word (**Smooth**, **Some compression** or **It will step**) and the numbers behind it. See [Check your own gradient](check-your-gradient.md).

### Browse the collection

A search box (**Search by name, hex or scheme…**), **Shuffle**, **Open a random gradient**, and a second search row, **Filter inside results**, with **Clear**.

### The tabs

| Tab | What it shows |
| --- | --- |
| **Library** | Filters, sort and the gradient grid. The badge shows how many gradients match. |
| **Inspect** | The gradient you last opened: preview, facts, CSS, stops, metrics and quick exports. |
| **Vision** | The open gradient under five kinds of vision. |
| **Accessibility** | Contrast measured across the open gradient. |
| **Pair** | A text colour tested over the open gradient. |
| **Tags** | Every method, scheme, complexity, interpolation space, easing and banding value, with counts. |
| **Stats** | Distributions for the gradients that match your filters. |
| **Export** | Exports for the open gradient and for every matching gradient. |
| **Saved** | Gradients you have saved. The badge shows how many. |

### A card

Each card shows the gradient as a large preview with its name (for example **Aurora Simple #00001**), its scheme and interpolation space, and its score in the corner. Under the preview, a strip of its stops. The footer has a banding chip (**Smooth**, **Compresses** or **Steps**), the number of stops, and two buttons: **CSS** (copy the CSS) and **Save**.

## Your first task: choose a smooth gradient for a hero banner with white text

1. In **Browse the collection**, set **Banding** to **Low banding risk**.
2. Set **Stops** to **2 to 4 stops** for a simple ramp.
3. Scan the cards and select one you like. The **Inspect** tab opens.
4. Open the **Pair** tab. The text colour starts as white.
5. Read **Status**. If it says **Passes AA in every sampled region**, white body text is readable across the whole gradient.
6. If it does not, try **Black**, or go back and pick a darker gradient.
7. Return to **Inspect** and select **Copy CSS**.
8. Paste the value into your stylesheet as the banner's `background`.

**Result:** a gradient measured as smooth, with a text colour that passes AA everywhere on it, in your stylesheet.
