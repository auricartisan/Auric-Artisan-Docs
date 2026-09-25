---
title: Font CDN — Getting started
description: How the Font CDN is organised — family ids, stylesheets and font files — and how to put a first family on a page.
product: Services › Font CDN
updated: 2026-09-25
---

# Getting started

## How the CDN is organised

Everything is served from https://fonts.auricartisan.com:

| Path | What it is |
|---|---|
| `/css/<family-id>.css` | One stylesheet per family, with an `@font-face` rule for each style |
| `/font/…` | The font files the stylesheets point to |
| `/font-cdn.js` | The loader script |
| `/data/index.json` | The catalogue: one short record per family |
| `/data/detail/<group>.json` | Full metadata for the families in a group (`A-F`, `G-L`, `M-R`, `S-Z`) |
| `/LICENSE.md` | The licence reference for the collection |

You do not need to know the file paths inside `/font/`: the family stylesheet refers to them for you.

## Family ids

Every family has an **id**, used in its stylesheet URL. The id is the family name in lower case, with apostrophes and quotation marks removed and every run of other characters replaced by a hyphen:

| Family | Id | Stylesheet |
|---|---|---|
| Alegreya | `alegreya` | `https://fonts.auricartisan.com/css/alegreya.css` |
| Roboto Slab | `roboto-slab` | `https://fonts.auricartisan.com/css/roboto-slab.css` |
| Open Sans | `open-sans` | `https://fonts.auricartisan.com/css/open-sans.css` |

The Font Library's **Use & Embed** tab always shows the exact URL for a family.

## Your first family

1. Add the family's stylesheet to the `<head>` of your page:

   ```html
   <link rel="stylesheet" href="https://fonts.auricartisan.com/css/alegreya.css">
   ```

2. Use the family in your CSS, with a fallback:

   ```css
   body { font-family: 'Alegreya', serif; }
   ```

3. Load the page. The text appears in Alegreya once the font file has downloaded. Until then the browser shows the fallback, because the stylesheets use `font-display: swap`.

## What a family stylesheet contains

Each stylesheet starts with a comment naming the family, its licence and copyright, and how many files and weights it has, then one `@font-face` rule per file:

```css
/* Alegreya — Auric Artisan Font CDN
 * SIL Open Font License 1.1 · Copyright 2011 The Alegreya Project Authors (https://github.com/huertatipografica/Alegreya)
 * 2 file(s), weights 400 500 600 700 800 900, variable
 */
@font-face {
  font-family: 'Alegreya';
  font-style: italic;
  font-weight: 400 900;
  font-display: swap;
  src: url('../font/A-F/ALEGREYA/Alegreya-Italic%5Bwght%5D.ttf') format('truetype-variations');
}
@font-face {
  font-family: 'Alegreya';
  font-style: normal;
  font-weight: 400 900;
  font-display: swap;
  src: url('../font/A-F/ALEGREYA/Alegreya%5Bwght%5D.ttf') format('truetype-variations');
}
```

A variable family, like this one, covers a whole weight range with one file per style. A static family has one rule per weight and style.

## Next steps

- [Embed a family](embed-a-family.md) for the other ways to embed.
- [Use the loader](use-the-loader.md) to load several families with one tag, or from JavaScript.
- [Self-host a family](self-host-a-family.md) to serve the files from your own site.
