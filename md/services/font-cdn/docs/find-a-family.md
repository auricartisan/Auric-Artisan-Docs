---
title: Font CDN — Find a family
description: Find a family and its id for the Font CDN, on the Font Library page or from JavaScript, and read what the catalogue records about it.
product: Services › Font CDN
updated: 2026-09-25
---

# Find a family

## On the Font Library page

The Font Library at https://auricartisan.com/tool/font/ is the catalogue's front end. It renders every family in itself, lets you set your own words in it, and gives the embed code and kit for the ones you keep. Its main controls are:

- **Search fonts** ("Family, designer or foundry");
- sorting by Alphabetical, Accessibility score, UI score, Readability score, Most weights, Most glyphs, Variable first, or Surprise me;
- category tabs and filters;
- **Recommend**, a recommender for a brief;
- **Collections**, curated sets;
- **Selected**, the families you have gathered for a combined embed or kit.

Each family opens with tabs including **Specimen**, **Suitability**, **Pairings**, **Glyphs**, **Features**, **Styles**, **About**, **License**, **Charset**, **Develop** and **Use & Embed**. The page itself is documented with the website tools; see [Related](../others/related.md).

## From JavaScript

The loader can search the catalogue:

```js
const hits = await AuricFonts.search('mono');   // name, designer or category
const all  = await AuricFonts.list();
```

Each record in the catalogue includes, among other fields, the family's `id`, `name`, `group`, `category`, `weights`, whether it is `variable` and its `axes`, whether it has italics, whether it is monospace, its `license` key, `designer`, the scripts it covers and its character count.

For everything about one family, use `get()`:

```js
const meta = await AuricFonts.get('Alegreya');   // or the id, 'alegreya'
```

It returns the family's full metadata, including its styles and files, or `null` if there is no such family.

## Categories

Families are sorted into five categories: sans-serif, serif, display, handwriting and monospace. Categories are worked out from the fonts' own data and outlines, so a few families may sit in a category you would not choose; see [Limits and accuracy](../others/limits-and-accuracy.md).

## Related pages

- [Use the loader](use-the-loader.md)
- [Reference](reference.md)
