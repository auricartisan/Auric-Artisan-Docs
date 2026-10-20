---
title: Search and Spotlight — Limits and accuracy
description: What Spotlight searches, how its colour answers are computed, and its limits.
product: Website › Site features › Search and Spotlight
updated: 2026-09-25
---

# Spotlight limits and accuracy

## What is searched

- Spotlight searches the site's own search index: the titles, descriptions, tags, categories, addresses and text of the site's pages. It does not search inside your saved library items or inside tool results.
- The **Web** tab searches a curated set of trusted outside sources through the site's web search service, not the whole web.
- Scopes are decided by page address: **Tools** is every page under `/tool/`, **Docs** is under `/library/documentation/`, **Learn** is under `/library/learn/`, and **Pages** is everything else.

## Result limits

- Searches start at two characters.
- Spotlight lists up to 8 results; the full search page lists all of them.
- Up to six recent searches are kept.
- Web results are limited to 8.

## Colour answers

- Contrast ratios use the WCAG 2 relative-luminance formula and are shown to two decimal places.
- Only `#` plus six hex digits is recognised as a colour. Colours are treated as sRGB.
- The pass and fail verdicts use the WCAG 2 thresholds: 4.5:1 for AA body text, 7:1 for AAA body text and 3:1 for AA large text.
- The answer is a quick reading, not an audit. For a page-wide check, use the Analyzer.

## Language

The index holds the English text of pages. Searching in Hindi finds commands, but page results depend on English words.
