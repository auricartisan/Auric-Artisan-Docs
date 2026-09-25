---
title: Accessibility Library — Reference
description: Every control, output and message in the Accessibility Color Pair Library.
product: Website › Library › Colour libraries › Accessibility Library
updated: 2026-09-25
---

# Accessibility Library reference

Everything on https://auricartisan.com/library/accessibility/.

## Heading

| Item | Content |
| --- | --- |
| Kicker | **Auric Artisan · Accessibility** |
| Headline | **What may I write on this?** |
| Facts | **Corpus 5,000,000**, **Seed 9001**, **Every figure computed in your browser** |
| **Read the API guide →** | The accessibility corpus API guide. |
| **Automate this** note | **8 API credits per call to POST /v1/accessibility/map**; **API docs**; × dismisses. |

## Control bar

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Ground** swatches | Set the background. | `#0D0D0D`, `#1D2A3E`, `#FFFCF7`, `#1B4D3E` | `#1D2A3E` |
| Colour picker | Any other ground. | Any colour | — |
| **Swap** | Puts the current foreground on the ground and moves the caret to the old ground. | — | — |
| **Target** | The contrast threshold. | **3:1**, **4.5:1**, **7:1** | **4.5:1** |
| **Territory** | Share of the map that clears the target. | 0% to 100% | — |

## The map

| Element | Meaning |
| --- | --- |
| Horizontal axis | Hue: **0° red**, **60° yellow**, **120° green**, **180° cyan**, **240° blue**, **300° magenta**, **360°**. |
| Vertical axis | OKLCH lightness, **0** to **1.0**. |
| Colour at each point | The most colourful sRGB colour at that hue and lightness. |
| Lines | **3:1** (dashed amber), **4.5:1 body** (solid green), **7:1 AAA** (dashed pale blue). |
| Dimmed area | Fails the current target. |
| Caret | The current foreground. Starts at hue 190°, lightness 0.78. |
| Pins | Your pasted colours; failures have a line to the target. |

| Input | Effect |
| --- | --- |
| Press and drag | Moves the caret. |
| `Left` / `Right` | Hue −5° / +5° (×5 with `Shift`). |
| `Up` / `Down` | Lightness +0.02 / −0.02 (×5 with `Shift`). |
| `Home` / `End` | Lightness 1 / 0. |

## Readout

| Item | Meaning |
| --- | --- |
| Specimen | "Readable at a glance" and a paragraph in the foreground on the ground. |
| Ratio | WCAG 2 contrast, two decimals. |
| Verdict | **clears AAA for body text** (≥ 7), **clears AA for body text** (≥ 4.5), **large text and UI only** (≥ 3), **fails every text threshold**. |
| **Foreground**, **Ground** | Hex codes. |
| **Lightness** | Foreground OKLCH lightness. |
| **Hue** | Foreground hue in degrees. |
| **APCA** | Lc, rounded. |
| **Vision margin** | Worst-case separation under ten simulated conditions, 0 to 1. |
| **To the line** | Lightness distance to the target line, or **unreachable at this hue**. |
| Advice | Inside / outside / unreachable sentence. |

## Picks

| Control | What it does |
| --- | --- |
| Heading | **N that work on this ground**, with the target and ground named. |
| Pick card | Specimen, ratio and hex. Select to move the caret to it. |
| **Copy as CSS** | Copies a `:root` block with `--ground` and `--fg-01` … `--fg-12`; shows **Copied** or **Copy failed**. |

Up to 12 picks, one per 30° of hue, each 10% of lightness inside the line.

## Or bring your own

| Element | Meaning |
| --- | --- |
| Paste box | Hex codes starting with `#`, 3 to 6 digits; up to 24; duplicates removed. |
| **Colour** | Swatch and hex. |
| **Here** | Contrast on the ground. |
| **Lightness** | OKLCH lightness as a percentage. |
| **Needs** | **nothing**, **+N% lightness**, or **unreachable**. |

## All of this from your own code

An example `curl` call to `https://api.auricartisan.com/v1/accessibility/corpus/stats` with an API key, and links **Read the guide**, **Endpoint reference**, **Get a key**.

## The index

| Control | What it does |
| --- | --- |
| Lookup box | A record id (`acc_…`) or a number. |
| **Look up** / `Enter` | Shows the record. |
| Record | Specimen; **Pair**, **Contrast**, **APCA**, **Auric SD**, **Recommended for**; seed, index and batch. |
| **Pairs that pass** / **Everything** | Browse filter. Default: **Pairs that pass**. |
| Count | **N shown · scanned M of 5,000,000**. |
| Pair card | Select to load the pair into the map. |

## Messages

| Message | When |
| --- | --- |
| **Paste hexes above to see them placed against this ground.** | Nothing pasted. |
| **Not a record id. They look like acc_91 — or paste an index.** | Unreadable lookup. |
| **Out of range. The corpus holds 5,000,000 records.** | Number too large. |
| **That is the end of the corpus.** | Browse reached the end. |
| **Copied**, **Copy failed** | After **Copy as CSS**. |
