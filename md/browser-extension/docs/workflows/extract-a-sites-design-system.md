---
title: Browser extension — Extract a site's design system
description: Read a website's colours, CSS variables, fonts and type scale, and export them as W3C design tokens, Tailwind or CSS.
product: Browser extension › Workflows
updated: 2026-09-25
---

# Extract a site's design system

Use this workflow to study how a site is built, to start a theme from an existing product, or to audit whether a site uses its tokens consistently. Respect the site's rights: reading its CSS for study is one thing, copying its brand is another.

## 1. Read its tokens

1. Open the site and go to a representative page.
2. Open Code › **Tokens** and choose **Read the tokens**.
3. Read the summary: how many CSS variables, font families and sizes it found.
4. Scan **CSS variables**. Colour variables have swatches. Click one to copy `var(--name)`, or Shift-click to copy its value.
5. Look at **Fonts** (most used first) and **Type scale** (smallest first).

## 2. Export the tokens

Choose the format your project uses:

- **W3C tokens** for design-token tools. Colours, dimensions and other values are grouped.
- **Tailwind @theme** for a Tailwind v4 project.
- **CSS vars** for a plain `:root` block.
- **JSON** for everything, including fonts and sizes.

Each copies to the clipboard. Choose **Save snippet** to keep the CSS variables in Snippets.

## 3. Read the colours actually used

Variables show what a site declares; computed colours show what it uses.

1. Open Colour › **Page palette** and choose **Read the page's colours**.
2. Switch the mode to **Dominant (k-means)** to see eight representative colours, or **Sort by hue** to see families.
3. Compare the palette with the variables. Colours that appear in the palette but not among the variables may be hard-coded.

## 4. Export the palette

In Page palette, choose **@theme**, **Tailwind**, **SCSS**, **Tokens**, **CSS** or **oklch()**, or download **ASE** for design tools that read Adobe swatch files. **Save** keeps it in your library.

## 5. Check a few components

1. On Home, choose **Inspect** and click a button, a card and a heading.
2. For each, press `C` to copy its CSS, and read its typography and effects.

**The result:** the site's tokens, palette and key component styles, in the formats your project uses.

## Related pages

- [Tokens](../code/tokens.md)
- [Page palette](../colour/page-palette.md)
- [Code export formats](../code/code-export.md)
