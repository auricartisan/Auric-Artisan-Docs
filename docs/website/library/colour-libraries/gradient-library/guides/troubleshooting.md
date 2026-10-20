---
title: Gradient Library — Troubleshooting
description: Symptoms, causes and fixes for problems in the Gradient Library.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Troubleshooting

## "Could not load gradient library"

**Why:** The collection could not be downloaded — usually a dropped connection or a content blocker.

**What to do:** Check your connection, allow auricartisan.com in any blocker, and reload.

## "No gradients match"

**Why:** The search and filters together exclude everything. Some combinations are rare, for example **Extreme** complexity with **2 to 4 stops**.

**What to do:** Select **Reset**, then add filters back one at a time.

## My gradient says "It will step" but looks fine to me

**Why:** The check measures the ratio between the largest and the average step. On a small preview, a step can be hard to see; on a large hero area, on a different screen, or after image compression, it often shows.

**What to do:** Look at the ramp full-width on the screens you care about. If the worst step is at the dark end, lift the black slightly; otherwise add a stop near **Worst transition at**.

## The checker gives a different verdict from the same gradient in the collection

**Why:** The checker always paints evenly spaced stops blended in plain sRGB, the way a basic CSS gradient is drawn. The collection's gradients were generated with their own stop positions, interpolation space and easing, and their verdict describes that.

**What to do:** Treat the checker as "how will this look as a basic CSS gradient". To keep a collection gradient's smoothness, use its CSS exactly as exported.

## "Stop N is not a colour yet"

**Why:** The text in that stop's field is not a colour the page can read, such as a half-typed hex.

**What to do:** Finish or correct the value. Until then the stop is measured with its last valid colour; leaving the field puts that colour back.

## Selecting a Banding value on the Tags tab does nothing

**Why:** On the **Tags** tab, the **Banding** values are counts only.

**What to do:** Use the **Banding** filter on the **Library** tab.

## Vision, Accessibility or Pair say "Select a gradient"

**Why:** These tabs work on the open gradient.

**What to do:** Select a card first, then open the tab.

## The Stats tab has not changed after I filtered

**Why:** The tab is drawn when opened.

**What to do:** Select the **Stats** tab again.

## A share link opens the page but not the gradient

**Why:** The link was cut short or edited, or the page says **Shared gradient not in current library**.

**What to do:** Ask for the link again, or search for the gradient's name.

## Saved gradients have gone

**Why:** Saves live in this browser only, and the **Saved** tab keeps the latest 240.

**What to do:** Save them again, or export them as JSON or CSS to keep a permanent copy.

## Downloads do not start

**Why:** Some browsers block several downloads in a row, or ask before downloading.

**What to do:** Allow downloads from auricartisan.com when your browser asks.
