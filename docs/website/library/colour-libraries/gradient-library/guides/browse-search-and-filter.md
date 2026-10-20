---
title: Gradient Library — Browse, search and filter
description: Narrow 8,192 gradients by search, method, scheme, complexity, stops, interpolation, easing, score and banding, and sort the results.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Browse, search and filter

## Search

The box **Search by name, hex or scheme…** filters as you type. Every word must appear in at least one of these: the gradient's name, its type, its angle, any stop's hex code, its scheme, method, complexity, interpolation space, easing or banding label.

Examples:

- `aurora` — gradients of the Aurora scheme.
- `#7b36` — gradients with a stop whose hex starts `7B36`.
- `oklch smooth` — gradients blended in an OKLCH space and measured as smooth.

The **Filter inside results** row has its own box (**name, hex, scheme…**) and a **Clear** button. Its words are combined with the first box's.

Press `/` anywhere outside a text field to jump to the search box.

## Filters

All filters sit on the **Library** tab and combine with each other and with the search.

| Filter | Options | Meaning |
| --- | --- | --- |
| **Method** | **All methods** and twelve methods: Analogous, Aurora, Chaotic, Complementary, Duotone, Golden, Monochrome, Nebula, Prismatic, Spectral, Terrain, Thermal | How the gradient's colours were chosen. |
| **Scheme** | **All schemes** and the same twelve names | The scheme family, which also forms the first word of each gradient's name. |
| **Complexity** | **Any complexity**, **Simple**, **Detailed**, **Extreme** | How elaborate the gradient is. |
| **Stops** | **Any stops**, **2 to 4 stops**, **5 to 8 stops**, **9 to 16 stops**, **17 to 32 stops**, **33+ stops** | Number of colour stops. The collection ranges from 2 to 46. |
| **Interpolation** | **Any interpolation**, **Lch Short**, **Linear Rgb**, **Oklab**, **Oklch Long**, **Oklch Short** | The colour space the stops were blended in when the gradient was generated. |
| **Easing** | **Any easing**, **Cubic In Out**, **Linear**, **Quart In Out**, **Sine In Out**, **Smootherstep** | How the blend accelerates between stops. |
| **Score** | **Any score**, **Top quality** (0.70 or more), **Balanced+** (0.55 or more), **Wild / experimental** (below 0.55) | The gradient's quality score, from 0 to 1. |
| **Banding** | **Any banding**, **Low banding risk**, **Medium banding risk**, **High banding risk** | The measured banding verdict: smooth, subtle compression or visible step risk. |

> **Tip:** **Banding** is the filter the page recommends starting with: it is the one that narrows 8,192 gradients down to the ones you can use large on screen.

In the full collection, 6,342 gradients are measured as low risk, 330 as medium and 1,520 as high.

## Sort by

| Option | Order |
| --- | --- |
| **Sort: original** | Collection order (default). |
| **Score high to low** | Highest quality score first. |
| **Complexity high to low** | Highest complexity score first. |
| **Stops high to low** | Most stops first. |
| **Stops low to high** | Fewest stops first. |
| **Dominant hue** | By the gradient's overall hue, from 0°. |
| **Random** | Shuffled. |

## Buttons

- **Shuffle** — sets the sort to **Random**.
- **Open a random gradient** — opens any gradient from the whole collection on **Inspect**.
- **Reset** — clears both searches, every filter, and sets **Sort: original**.
- **Export visible** — opens the **Export** tab.
- **Back to top** — scrolls to the first card.

## The grid and cards

The grid scrolls continuously. The counter under it reads, for example, **1–24 of 1,212**, or **Nothing to show** when nothing matches; the grid then says **No gradients match** and **Try clearing a filter or searching a broader method, color, or complexity.**

Each card shows:

| Part | Meaning |
| --- | --- |
| Preview | The gradient, with its name and "scheme / interpolation space". |
| Score | The quality score, top right. |
| Stop strip | Up to 18 of its stops as flat colour. |
| Banding chip | **Smooth**, **Compresses** or **Steps**. |
| Stops chip | For example **7 stops**. |
| **CSS** | Copies the gradient's CSS (**CSS copied**). |
| **Save** / **Saved** | Saves or unsaves the gradient. |

Select a card, or focus it and press `Enter` or `Space`, to open it on **Inspect**.

## Result

The grid shows only gradients that match your search and filters, in the order you chose.
