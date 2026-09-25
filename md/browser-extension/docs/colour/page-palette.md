---
title: Browser extension — Page palette
description: Read every colour a web page uses, switch between views and sorting modes, inspect a colour, and copy or export the palette.
product: Browser extension › Colour
updated: 2026-09-25
---

# Page palette

Page palette reads the colours a web page actually uses, from its computed styles and its CSS variables, and turns them into a palette you can copy, export or save. It is also the way to sample page colours in Firefox, which has no screen eyedropper.

## Read a page's colours

1. Open the page, then open Colour › **Page palette**. (Home › **Palette**, or `Alt` + `Shift` + `E`, opens it and starts reading straight away.)
2. Choose **Read the page's colours**.

A line above the palette summarises the scan, for example "18 distinct · 42 unique · 1830 elements · 6 CSS vars": how many distinct colours remain after merging near-duplicates, how many unique values were found, how many elements were read, and how many colours came from CSS variables.

## What it reads

- Up to 6 000 elements on the page.
- Twelve colour properties of each: text colour, background colour, the four border colours, outline colour, SVG fill and stroke, box shadow, caret colour and text-decoration colour.
- CSS custom properties (variables) in the page's stylesheets whose value is a hex or `rgb()` colour. These count three times, so brand and theme colours rise to the top.
- Nearly invisible colours (under 5% opacity) are skipped, and near-duplicate colours are merged.
- Up to 48 colours are kept.

Stylesheets from another site that the browser does not let the page read are skipped.

## View and sort

- **Switch between strip and grid**: Strip (one scrolling row) or grid
- **Palette mode**: **Most used** (the default), **Dominant (k-means)** (eight representative colours), **Sort by hue**, **Sort by lightness**

## Look at one colour

Choose a colour to open its detail card:

- its nearest colour name;
- HEX, RGB, HSL and `oklch()` values, each with a copy button;
- its contrast on white and on black, with the WCAG level (AAA, AA, AA large or Fail);
- **Pick** (open in the Picker), **Contrast** (use as text colour), **Shades** (open in Scale) and **Harmony**.

Close the card with its close button.

## Copy and export

| Group | Button | Result |
|---|---|---|
| **Copy** | **HEX** | One HEX value per line, copied |
| | **CSS** | A `:root` block of `--color-1`, `--color-2` … variables, copied |
| | **oklch()** | The same `:root` block with `oklch()` values, copied |
| | **JSON** | A JSON array of the colours, copied |
| | **ASE** | An Adobe Swatch Exchange file (`auric-palette-` and the date `.ase`), downloaded |
| **Framework** | **Tailwind** | A `module.exports` Tailwind config that extends `colors`, copied |
| | **@theme** | A Tailwind v4 `@theme` block, copied |
| | **SCSS** | `$color-1: …;` variables, copied |
| | **Tokens** | W3C design tokens JSON, copied |
| **Export** | **SVG** | An SVG strip of swatches, copied as text |
| | **PNG** | A PNG strip of swatches, downloaded |
| | **Save** | Saves the palette to Saved › Library (the newest 30 palettes are kept) |
| | **Open** | Opens the palette on auricartisan.com's palette library, with the colours in the address |

**Open** sends the palette's hex colours to auricartisan.com in the page address; nothing else about the page is sent.

## Related pages

- [Image](image.md) for palettes from pictures
- [Library](../saved/library.md)
- [Code export formats](../code/code-export.md)
