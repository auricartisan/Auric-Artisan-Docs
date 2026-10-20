---
title: Search — Understand the ranking
description: How site search orders results, the "Why it ranks here" panel, the field weights and the option to show a score on every result.
product: Website › Search
updated: 2026-09-25
---

# Understand the ranking

Site search orders results by relevance, and it shows its working. You can see why any result sits where it does, and switch on a score for every row.

## How results are scored

The page uses a ranking method called BM25F. Each page is split into six fields, and a match in a heavier field counts for more:

| Field | Weight |
| --- | --- |
| Title | ×6 |
| Tags | ×4 |
| Description | ×3 |
| Category | ×2 |
| URL | ×1.5 |
| Content | ×1 |

On top of that:

- Rare words count for more than common ones.
- Pages that contain more of your words, and have them close together, rank higher.
- Partial words (such as `grad` for "gradient") and corrected typos count, but less than exact words.
- Related words, shown dashed under the field, count at half weight.
- Pages you have opened from search before are nudged up, in this browser only.

The same table is printed on the page: open **Tools** at the end of the tab row and look under **Ranking**. It also shows the two tuning values, **k1 / b**, as **1.2 / 0.4**.

## Why it ranks here

Hover a result, or highlight it with the arrow keys, and a panel opens above the list. It shows:

- The kind of page and its title, address and description.
- **Why it ranks here** — the **BM25F score**, then each field that matched, with its weight and how many times your words appear in it.
- **Matched on** — the words that matched, with related words shown dashed.
- **Open the page**.

When a query produces an answer card, the card and the panel share the space above the list.

## Show the score on every result

Open **Tools** and tick **Show the score on every result**. Each result then shows:

- A bar for its score relative to the top result.
- The score as a number.
- Up to three fields it matched in, with the count for each. Heavier fields are emphasised.

This setting is remembered in this browser. Untick it to hide the scores again.

## Why a result you expected is missing

- The page may use a different word. Try a synonym, or a shorter form of the word.
- An operator may be ruling it out. The **Worth trying** list on the no-results screen names it.
- The page may be newer than the index in your browser. See [Troubleshooting](troubleshooting.md).
