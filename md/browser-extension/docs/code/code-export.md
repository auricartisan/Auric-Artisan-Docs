---
title: Browser extension — Code export formats
description: Every format the extension can copy or download, which tool produces it, and what the output looks like.
product: Browser extension › Code
updated: 2026-09-25
---

# Code export formats

This page collects every format the extension exports, so you can find the tool that gives you the code you need. Unless a row says "downloaded", the output is copied to the clipboard.

## One colour

From the Picker's **Code** pane. Values below are for Auric gold, `#d3af37`.

| Format | Output |
|---|---|
| CSS | `--brand: #d3af37;` |
| CSS · wide gamut | `--brand: oklch(…);` |
| Tailwind v4 | `@theme { --color-brand: oklch(…); }` |
| SwiftUI | `Color(red: 0.827, green: 0.686, blue: 0.216)` |
| Jetpack Compose | `Color(0xFFD3AF37)` |
| Android XML | `<color name="brand">#FFD3AF37</color>` |

Transparent colours carry their opacity: SwiftUI adds `opacity:`, and Compose and Android put the alpha first.

The Picker's value field copies the colour as a CSS value in any of its twelve formats. History and Library chips copy in the format set in Settings › Tools › **Copy colours as**: HEX, RGB, HSL or OKLCH.

## A palette

From **Page palette** (and anything sent to it: Image, Harmony).

| Format | Output |
|---|---|
| HEX | One `#RRGGBB` per line |
| CSS | `:root { --color-1: #…; --color-2: #…; }` |
| oklch() | The same `:root` block with `oklch()` values |
| JSON | `["#…", "#…"]` |
| ASE | An Adobe Swatch Exchange file, downloaded |
| Tailwind | `module.exports = { theme: { extend: { colors: { "color-1": "#…" } } } };` |
| @theme | `@theme { --color-1: #…; }` |
| SCSS | `$color-1: #…;` |
| Tokens | W3C design tokens JSON |
| SVG | An SVG strip of swatches, as text |
| PNG | A PNG strip of swatches, downloaded |

Harmony's **Copy** gives a comma-separated HEX list, and Image's **Copy HEX** one HEX per line.

## A scale

From **Scale**, named after the **Scale name** you type (for example `brand`):

| Format | Output |
|---|---|
| CSS | CSS variables for each step |
| SCSS | SCSS variables for each step |
| oklch() | CSS variables with `oklch()` values |
| JSON | The steps as JSON |
| Tailwind | A Tailwind colour object |
| @theme | A Tailwind v4 `@theme` block |
| Tokens | W3C design tokens JSON |
| SVG | An SVG of the scale with labels, as text |
| PNG | A PNG of the scale with labels |

## A gradient

From **Gradient**: a `background:` declaration using `linear-gradient`, `radial-gradient(circle, …)` or `conic-gradient(from …deg, …)`.

## A page's tokens

From **Tokens**: a `:root` block of CSS variables, W3C design tokens JSON (grouped into colour, dimension and other), a Tailwind v4 `@theme` block, or the raw scan as JSON.

## An element

| From | Format |
|---|---|
| Inspector card, `C` key or **Copy CSS** | A CSS block for the element |
| Inspector, `S` key or **Selector** | A CSS selector |
| Inspector, `J` key or **JSON** | The element's snapshot as JSON |
| Code › Inspect › DOM › **Copy locator** | CSS selector, `document.querySelector(…)` or `page.locator(…)` |
| Code › Inspect › DOM › **Copy HTML** | The element's markup (up to 12 KB) |
| Right-click menu › **Copy selector** | CSS, JavaScript (`document.querySelector(…)`), Playwright (`page.locator(…)`) or XPath |
| Right-click menu › **Copy computed styles** | The element's computed styles as text |

## Checks and audits

| From | Format |
|---|---|
| Contrast › **Copy report** | A plain-text contrast report |
| Audit › **Export JSON** | The full audit as JSON |
| Audit › **Export CSV** | The contrast findings as CSV |
| Vision › **Capture** | A PNG of the filtered tab, downloaded |

## Saved data

| From | Format |
|---|---|
| Library › **Export** | Your colours and palettes as JSON |
| Snippets › **Export file** | Every snippet in a `.txt` file, downloaded |
| Settings › Data › **Download a backup** | A `.json` backup of settings, history, library and snippets, downloaded |
| Settings › Data › **Copy settings** | Your settings as JSON |

## Related pages

- [Reference](../reference.md)
- [Glossary](../../others/glossary.md)
