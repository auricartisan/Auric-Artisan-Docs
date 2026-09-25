---
title: Icon CDN — Limits and accuracy
description: What the Icon CDN's names, categories, search and counts can and cannot tell you, and its practical limits.
product: Services › Icon CDN
updated: 2026-09-25
---

# Limits and accuracy

## Names and search

- Names are the sets' own. The same idea can have different names in different sets (`house` in Lucide, `home` in Tabler), and the same name can mean slightly different drawings.
- A name without a set, or a name the named set lacks, resolves to the first set that has it. Name the set, and copy names from the Icon Library, to be sure what you get.
- Search matches names, ids and each icon's search terms. It does not understand synonyms beyond those terms.

## Categories

Categories come from the sets that provide them. Almost half the icons (6,113) have no category, so browsing by category shows only part of the catalogue.

## Counts

- The catalogue counts 12,896 icons and 32,803 variants. An icon counts once however many styles it has.
- The licence reference counts SVG files in the upstream folders (21,736) differently from the catalogue, which merges variants into icons.

## Markup

- Served SVGs are normalised: their own width and height are removed, the `viewBox` is kept, and colours use `currentColor`. Size them yourself.
- Stroke width applies only to stroke-drawn icons.
- Material icons depend on their webfont loading; until it does, they may show as plain characters.

## The loader

- It fills placeholders once, when the page loads; call `inject()` for later ones.
- It downloads the catalogue index (about 1.9 MB) and one markup file per set and style you use, on first use.
- It does not report a missing icon as an error; the placeholder stays as it was.

## Related pages

- [Use the loader](../docs/use-the-loader.md)
- [Collections](../docs/collections.md)
