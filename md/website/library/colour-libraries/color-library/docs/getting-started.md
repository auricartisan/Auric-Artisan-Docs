---
title: Color Library — Getting started
description: Open the Color Library, learn what each section and tab does, and look up your first colour.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Getting started

This page takes you through opening the Color Library, what you see on screen, and a first task from start to finish.

## Open the page

1. Go to https://auricartisan.com/library/color/, or open the **Learn** menu in the site header and select **Color Library** under **Libraries**.
2. Wait for the atlas to load. While it loads, the grid area shows **Loading color atlas…**. When it is ready, the grid fills with colour tiles and the counter under it reads, for example, **1–48 of 8,192 colours**.

The page needs a network connection to load the atlas. If loading fails you see **Could not load color atlas** with the reason; see [Troubleshooting](troubleshooting.md).

## A tour of the screen

The page runs top to bottom in this order.

### The heading

The kicker reads **Auric Artisan · Colour** and the headline **Eight thousand colours, measured.** A line under it shows **Atlas 8,192**, **Spaces 7** and **Every figure precomputed**, and a link, **Read the API reference →**, to the site's public REST API documentation.

Under the heading you may see a note that starts **Automate this**. It names the REST API call that does the same job and how many API credits it costs, links to **API docs**, and has a dismiss button (×). Once you dismiss it, it stays hidden in this browser. API credits are separate from the tool tokens on your account; the note says so and links to the pricing page. See [Public API](../../../../../services/public-api/README.md) if you want to automate lookups.

### Start from a colour you already have

A text field with a colour swatch beside it, and a **Find its neighbours** button. Paste a colour in any CSS format and the atlas shows its five nearest catalogued colours. The field starts with `#D3AF37`, so results are already showing when the page opens. See [Find a colour's nearest neighbours](find-nearest-colours.md).

### Or from what it has to do

A row of seven requirement chips, such as **Readable on white** and **For typography**. Each chip shows the number of colours that would remain if you selected it. A line under the chips gives the running total. See [Choose colours by requirement](choose-by-requirement.md).

### Browse the atlas

A search box (**Search by hex (#a6e223) or id…**), a **Shuffle** button and an **Open a random colour** button. Under them, a second search row labelled **Filter inside results**, with a **Clear** button.

### The tabs

Five tabs sit under the search rows:

| Tab | What it shows |
|---|---|
| **Library** | The filters, the sort menu and the grid of colour tiles. Its badge shows how many colours match. |
| **The colour** | Everything about the colour you last opened. |
| **Stats** | Histograms of hue, lightness, chroma and contrast on white for the matching colours. |
| **Export** | Copy and download buttons for the open colour and for every matching colour. |
| **Saved** | The colours you have saved in this browser. Its badge shows how many. |

### The Library tab

- A row of filters: **Hue**, **Lightness**, **Chroma**, **Emotion**, **Art movement**, **AI mood**, **Design usage**, **WCAG** and **Sort by**, followed by **Reset** and **Export visible**.
- The grid. Each tile shows the colour with its hex code, the hex code again in the footer, the colour's emotion label and a star you select to save it.
- A counter under the grid, such as **1–48 of 8,192 colours**, and a **Back to top** button. The grid scrolls continuously; there are no pages to step through.

## Your first task: find out what your brand colour is good for

1. In **Start from a colour you already have**, select the text field and type your colour, for example `#76CDF6`.
2. Select **Find its neighbours**, or simply pause typing; the result updates on its own.
3. Read the first cell, labelled **your colour**. It shows your colour's contrast **On white** and **On black**. Values of 4.5:1 or more are marked as passing.
4. Read the five cells after it. Each shows an atlas colour, its ΔE distance from yours (for example **ΔE 1.20 — indistinguishable**) and its own contrast figures.
5. Read the sentence under the cells. It tells you whether colours around yours can carry text on a light page, on a dark page, or neither.
6. Select the closest neighbour. The **The colour** tab opens.
7. Read **What it can carry**. The two specimens show a line of text in the colour on white and on black, with the contrast ratio and a one-sentence verdict.

**Result:** you know whether your colour can be used for body text on light or dark backgrounds, which catalogued colours are visually the same, and where to read its values in every notation.

## Next steps

- [Browse, search and filter](browse-search-and-filter.md) to narrow the 8,192 colours.
- [Copy and export](copy-and-export.md) to take values into your code.
- [Save colours](save-colours.md) to keep a shortlist.
