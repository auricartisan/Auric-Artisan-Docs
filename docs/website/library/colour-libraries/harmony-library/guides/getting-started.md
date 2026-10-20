---
title: Harmony Library — Getting started
description: Open the Harmony Library, learn the screen, and identify, inspect and export a first harmony.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Getting started

## Open the page

1. Go to https://auricartisan.com/library/harmony/, or open the **Learn** menu in the site header and select **Harmony Library** under **Libraries**.
2. While the page works out the collection, the grid shows **Loading harmony database…**. This takes a moment: all 8,192 harmonies are calculated in your browser so the filters can look at every one.
3. The grid fills and the counter reads, for example, **1–48 of 8,192 harmonies**.

If loading fails you see **Could not load harmony database**. See [Troubleshooting](troubleshooting.md).

## A tour of the screen

### The heading

Kicker **Auric Artisan · Harmony**; headline **Eight thousand schemes, and none of them stored.**; facts **Collection 8,192**, **23 methods** and **Derived, not stored**; and **Read the API guide →** to the Harmony Library's API guide.

A note starting **Automate this** may appear: browsing the collection is also available through the site's REST API — **3 API credits per call to GET /v1/harmony/library** — with a link to **API docs**. Select × to dismiss it.

### What harmony is this?

A row of colours, each with a swatch to click and pick, and a text field that takes any CSS colour. **Add a colour** and **Identify it** sit below, then the answer: the scheme your colours form, a fit score, and what else was considered. See [Identify your colours' harmony](identify-your-colours.md).

### Browse the collection

A search box (**Search by id, hex or method…**), **Shuffle**, **Open a random harmony**, and a second row, **Filter inside results**, with **Clear**.

### The tabs

| Tab | What it shows |
| --- | --- |
| **Library** | Filters, sort, the grid. The badge shows how many harmonies match. |
| **Inspect** | The harmony you last opened. |
| **Theory** | Distributions of schemes, families, hues, colour counts, adherence, lightness and chroma. |
| **Accessibility** | How many harmonies contain text-safe pairs. |
| **Stats** | Six histograms. |
| **Export** | Exports for the open harmony and for every matching harmony. |
| **Saved** | Harmonies you have saved. |

### A card

Each card shows the harmony's colours as a strip of swatches with hex codes (select a swatch to copy it), its id (such as `har_0`), its scheme (such as **Split complementary**), and **Inspect**, **Copy** and **Save** buttons.

## Your first task: name your brand palette's harmony, then find a text-safe alternative

1. In **What harmony is this?**, type your brand colours into the fields — use **Add a colour** or × until you have the right number.
2. Read the verdict, for example **a split complementary** with **fit 0.912**. A fit near 1 means your hues sit close to the scheme's ideal angles.
3. Read **Worst pair** and **Best pair**. If **Best pair** is below 4.5:1, no two of your colours can carry body text on each other.
4. In **Browse the collection**, type the scheme's name into the search box, for example `split_complementary`.
5. Open the **Accessibility** tab and look at **Has any AA pair (4.5+)**, then return to **Library**.
6. Select **Inspect** on a harmony and read **Pair-by-pair WCAG contrast** until you find one with a pair at 4.5:1 or more.
7. Under **Quick export**, select **Copy CSS vars**.

**Result:** you know which scheme your palette follows, and you have an alternative in the same scheme with at least one text-safe pair, ready in CSS.
