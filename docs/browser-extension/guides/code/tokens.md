---
title: Browser extension — Tokens
description: Read a web page's design tokens — CSS custom properties, font families and type scale — and export them as CSS, W3C tokens, a Tailwind @theme block or JSON.
product: Browser extension › Code
updated: 2026-09-25
---

# Tokens

Tokens (Design Tokens) reads the design decisions a site has written down as CSS: its custom properties (CSS variables), the font families it uses and its type scale. Use it to learn a design system, to start a theme from an existing site, or to check that a site uses its tokens consistently.

## Read the tokens

1. Open the page, then Code › **Tokens**.
2. Choose **Read the tokens**.

A summary line appears, such as "86 CSS variables · 3 font families · 9 sizes". If the page defines no variables, a message says "No CSS variables found on this page". Some pages cannot be read, such as browser pages; the tool then says "Could not scan this page".

After a scan, the button is labelled **Scan design tokens**; choose it to read the page again.

## What it finds

| Section | What it lists | Limit |
|---|---|---|
| **CSS variables** | Every custom property the page's readable stylesheets define, with its value. Colour values get a swatch. | 240 |
| **Fonts** | The font families used by elements with text, most used first, each shown in its own font with a use count | 8 |
| **Type scale** | The font sizes used by elements with text, smallest first | 16 |

Fonts and sizes are counted across up to 4 000 elements. Stylesheets from another site that the browser does not let the page read are skipped.

## Copy one token

| On | Click | Shift-click |
|---|---|---|
| A CSS variable | Copies `var(--name)` | Copies its value |
| A font | Copies the full font-family list | — |
| A size | Copies the size | — |

## Export

The export buttons appear when the page has CSS variables. Each copies to the clipboard.

| Button | Output |
|---|---|
| **CSS vars** | A `:root { … }` block with every variable |
| **W3C tokens** | W3C design tokens JSON, grouped into `color`, `dimension` and `other`. Colours are resolved to HEX where possible. |
| **Tailwind @theme** | A Tailwind v4 `@theme { … }` block with every variable |
| **JSON** | Everything found: page title and address, variables, fonts and sizes |
| **Save snippet** | Saves the CSS variables to Snippets |

Example of the **W3C tokens** output:

```json
{
  "color": {
    "brand": { "$value": "#d3af37", "$type": "color" }
  },
  "dimension": {
    "radius-md": { "$value": "8px", "$type": "dimension" }
  }
}
```

## Related pages

- [Snippets](snippets.md)
- [Code export formats](code-export.md)
