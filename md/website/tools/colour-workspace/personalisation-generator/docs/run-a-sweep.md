---
title: Personalization Generator — Run a sweep and read the results
description: Start, stop and repeat sweeps, follow their progress, and read The run panel and the Overview tab.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Run a sweep and read the results

A sweep samples a set number of candidate palettes (the **Search depth**), scores every one, and keeps the best (**Keep top**). From the kept palettes the generator then builds the gradients, typography, UI pairs, posters, tokens and Studio.

## Start a sweep

Do any one of these:

- select **Generate** under the brief;
- press `Enter` in the brief box;
- select **Run sweep** in **Tune**.

While it runs, **Generate** reads **Generating…**, the status line reads, for example, **Generating (320)…**, and the progress bar appears at the top of **The run** with a label such as **Sweep #3 — 320 candidates**, then **Sampling… 45%** and a line like **144/320 · 139 kept · ETA 0.4s**. The count of kept candidates there is everything that has survived so far, before the final cut.

The sweep works in small batches and lets the page redraw between them, so you can scroll, switch tabs and read results while it runs.

A new sweep replaces the previous results. To add to them instead, use **Endless**.

## Stop a sweep

Select **Stop** under the brief, or **Cancel** beside the progress bar. The sweep stops at the end of the current batch and keeps the best of what it had already found. The status reads, for example, **Cancelled after 192/320 (140ms).**

## Endless mode

Select **Endless** to keep sweeping. The button reads **Endless ✓** while it is on. A new sweep starts about two seconds after each one finishes, and each sweep's best palettes are merged into the existing results rather than replacing them. Duplicates are removed, and the list is capped at the 96 highest-scoring palettes.

Select **Endless** again, or **Stop**, to end it.

## When it finishes

The status reads, for example, **Done · 24 kept · 812ms**. The tab counts update, and the leader (the highest-scoring palette) becomes the first card in **Palettes**, the source of the **Tokens** tab, and the palette shown in **Studio**.

## The run panel

The right-hand column explains the last sweep.

### Where the sweep went

Four bars:

- **sampled**: the candidates generated (the search depth);
- **repeats**: candidates thrown out because they repeated one already seen (only when **Unique** is on);
- **ranked**: the candidates that were scored;
- **kept**: those that made the cut.

A note under the bars explains that contrast and colour-vision are weights in the score, not filters: a candidate that reads badly is ranked down, never discarded.

### Score distribution

A histogram of every ranked candidate's score, from the lowest on the left to the highest on the right, with the kept bars highlighted and the cut-off score marked. The line under it reads, for example, **24 of 318 ranked candidates cleared the cut.**, and says so if the sweep was cancelled.

### The leader, checked

The leader's swatches, its name and score, and three WCAG contrast checks between its own colours, each against the 4.5:1 bar for body text:

- **Lightest on darkest**
- **Mid on darkest**
- **Darkest on lightest**

Each shows an *Ag* sample and the ratio. This is measured directly from the colours, so it is a quick check of whether the leader can carry text at all.

## The Overview tab

**Overview** summarises the current results:

- five tiles: **Top score** (with the number of sweeps run), **Pool** (up to 14 swatches, the pool target and the selected styles), **Search space** (depth, keep, last sweep time and the total number of candidates sampled since the page opened), **Output** (counts of palettes, gradients, posters and type combos, and the use case) and **Avg score** (with the peak);
- **Top palette preview**: the leader's swatches (select one to copy its HEX), its relationship and source, **Copy hex list**, **Open in Studio**, **Add to pool** and **Save**, and a **Score breakdown** of **Preference**, **Harmony**, **Contrast** and **CVD / UI**;
- **Sweep diagnostics**: the average of those four scores across all kept palettes, plus **Intent**, **Mode**, **CVD-safe** and **Unique**;
- **Recent palettes**: the top six by name and score. Select one to open it in the Studio.

## Filter the results

Type in **Search results** above the tabs to show only the cards in the open tab that match, for example a palette name, a HEX value, a relationship such as *Triadic*, a gradient style or a font name. **Clear** empties the box. The filter applies to the tab you are on; switching tabs applies it to the new tab.

## Related

- [Palettes, gradients, typography, UI pairs and posters](result-tabs.md)
- [Tune the sweep](tune-the-sweep.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
