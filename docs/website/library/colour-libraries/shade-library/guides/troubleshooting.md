---
title: Shade Library — Troubleshooting
description: Symptoms, causes and fixes for problems in the Shade Library.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Troubleshooting

## "Could not load shade library"

**Why:** The collection (about 2 MB) could not be downloaded.

**What to do:** Check your connection and any content blocker, and reload.

## I cannot find an evenness filter

**Why:** The page's introduction recommends filtering by evenness, but the current filter row has only **Base hue**, **Chroma**, **Lightness** and **Method**.

**What to do:** Narrow the list with the other filters, then compare **Min adjacent contrast** and the **Token contrast ladder** on **Inspect**: uneven scales show one or two big jumps between neighbouring steps.

## "No shade systems match"

**Why:** The filters together exclude everything, for example **Light** lightness with **Ink Paper**.

**What to do:** Select **Reset** and add filters back one at a time.

## Pasted CSS variables do nothing

**Why:** **Copy CSS vars** declares the variables on a class such as `.aa-shade-material-like-00001`, not on `:root`.

**What to do:** Change the selector to `:root`, or add the class to the element where you use the variables.

## The middle steps fail contrast

**Why:** In almost every scale, the middle steps (around `300`–`700`) are too close in lightness to both black and white to carry body text. That is expected: they are fills, borders and accents.

**What to do:** Use light steps for surfaces with dark text, dark steps for text or dark surfaces with light text, and check the **Token contrast ladder**.

## Bulk export buttons do nothing

**Why:** No scales match the current filters.

**What to do:** Widen the filters, then export again.

## A share link does not open the scale

**Why:** The link was cut short or edited; the page may say **Shared shade not in current library**.

**What to do:** Ask for the scale's id (for example `shade_000000`) and search for it.

## Saved scales have gone

**Why:** Saves live in this browser only (up to 500).

**What to do:** Save them again, or export them.
