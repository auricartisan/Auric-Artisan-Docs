---
title: Accessibility Library — Look up and browse the index
description: Look up any of five million scored colour pairs by record id, read its WCAG, APCA and Auric SD scores, and browse pairs that pass.
product: Website › Library › Colour libraries › Accessibility Library
updated: 2026-09-25
---

# Look up and browse the index

**The index** is a set of five million foreground and background pairs, each scored. As the page explains, it is "defined by a seed rather than stored": any record is a function of the seed (9001) and its number, so a record cited in an audit can be recomputed by anyone who reads it.

## Look up a record

1. Scroll to **The index**.
2. Type a record id such as `acc_91`, or a plain number such as `325`, into the box (**A record id like acc_91, or an index like 325**).
3. Select **Look up**, or press `Enter`.

Record ids are `acc_` followed by the record's number in base 36; `acc_91` is record 325.

The result shows a specimen of the pair and:

| Fact | Meaning |
| --- | --- |
| **Pair** | Foreground on background, for example **#4E1229 on #D86062**. |
| **Contrast** | The WCAG 2 contrast ratio, for example **4.00:1**. |
| **APCA** | The APCA Lc value, rounded, for example **35**. |
| **Auric SD** | Auric Artisan's combined score from 0 to 100 and its grade, for example **43.6 · F**. |
| **Recommended for** | The strongest use the pair supports, for example **large-text**. |

The examples are the real values of `acc_91`. A note underneath gives the seed, the index and the batch it belongs to — "Anyone with the same three numbers recomputes the same pair, which is what makes this citable."

Messages: **Not a record id. They look like acc_91 — or paste an index.** for unreadable input, and **Out of range. The corpus holds 5,000,000 records.** for a number that is too large.

### The Auric SD score

A single score from 0 to 100 that weighs five things: WCAG contrast (30%), APCA contrast (30%), how distinct the pair stays under simulated vision conditions (20%), the gap in OKLCH lightness (10%), and the hue difference weighted by colourfulness (10%). Grades: **S** (90 or more), **A** (80 or more), **B** (70 or more), **C** (60 or more), **D** (50 or more), **F** (below 50).

### Recommended for

| Value | Meaning |
| --- | --- |
| `body-text-strict` | Passes a strict body-text test: score 85 or more, 7:1 or more, APCA 75 or more, and good separation under every simulated vision condition. |
| `body-text-WCAG3` | APCA 75 or more (body text in the draft WCAG 3 approach). |
| `body-text-AA` | WCAG 2 contrast 4.5:1 or more. |
| `large-text` | 3:1 or more. |
| `ui-only` | APCA 45 or more. |
| `spot-text` | APCA 30 or more. |
| `non-text` | APCA 15 or more. |
| `decorative` | None of the above. |

The list is checked from the top, so a pair gets the first value it qualifies for.

## Browse the index

Under the lookup, a grid of pair cards scrolls through the corpus.

- **Pairs that pass** (the default) shows only pairs that clear the current target.
- **Everything** shows every pair, most of which fail.

The line beside the switch counts **N shown · scanned M of 5,000,000**. A note under the grid explains what you are seeing — with **Pairs that pass**, roughly what percentage of scanned pairs clear the target — and that you can keep scrolling without the page slowing down, because only what is on screen is drawn. At the very end it says **That is the end of the corpus.**

Each card shows **Readable** and a sample sentence in the pair, its ratio, "foreground on background" and its record id. Hover for the id and ratio.

Select a card to load that pair into the map: its background becomes the ground, the caret moves to its foreground, and the page scrolls up to the map.

Changing the target while **Pairs that pass** is on restarts the browse from the beginning with the new target.

## API

The section **All of this from your own code** shows an example call to the site's public API and links to **Read the guide**, **Endpoint reference** and **Get a key**. See [Public API](../../../../../services/public-api/README.md).
