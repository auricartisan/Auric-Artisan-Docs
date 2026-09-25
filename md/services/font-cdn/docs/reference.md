---
title: Font CDN — Reference
description: Every URL pattern, file, loader attribute, method and snippet of the Auric Artisan Font CDN.
product: Services › Font CDN
updated: 2026-09-25
---

# Reference

## Catalogue

| Fact | Value |
|---|---|
| Host | https://fonts.auricartisan.com |
| Families catalogued | 2,213 |
| Font files | 4,883 |
| Variable families | 550 |
| Families with italics | 401 |
| Served from the library | 2,023 families |
| Listed as Installed (not served) | 190 families |
| Categories | Sans-serif 780, serif 1,172, display 81, handwriting 97, monospace 83 |
| Groups | `A-F`, `G-L`, `M-R`, `S-Z` |
| Catalogue built | 2 June 2026 |

These figures come from the catalogue's own statistics, served at `/data/stats.json` and `/data/meta.json`.

## URL patterns

| Pattern | What it serves |
|---|---|
| `/css/<family-id>.css` | The family's stylesheet: a header comment and one `@font-face` rule per file |
| `/font/<group>/<FOLDER>/<file>` | Font files, referenced by the stylesheets |
| `/font-cdn.js` | The loader script |
| `/data/index.json` | One record per family |
| `/data/detail/<group>.json` | Full metadata for the families in a group |
| `/data/stats.json`, `/data/meta.json` | Catalogue statistics and build information |
| `/LICENSE.md` | The collection's licence reference |

The family id is the name in lower case, with quotation marks and apostrophes removed and other characters replaced by hyphens (`Roboto Slab` becomes `roboto-slab`).

## Stylesheet rules

| Property | Value |
|---|---|
| `font-family` | The family name |
| `font-style` | `normal` or `italic` |
| `font-weight` | One weight, or a range for variable fonts (for example `400 900`) |
| `font-stretch` | A percentage range, for variable fonts with a width axis |
| `font-display` | `swap` |
| `src` | The file URL with its format (for example `truetype-variations`) |

## Loader: script attributes

| Attribute | Meaning | Default |
|---|---|---|
| `data-families` | Families to load, separated by a vertical bar | — |
| `data-fonts` | Alias for `data-families` | — |
| `data-display` | `font-display` for faces added with `face()` | `swap` |
| `data-base` | The address to load stylesheets and data from | The script's own address |

Other ways to set the base address: `window.AURIC_FONT_BASE`, `window.AURIC_FONT_ASSET_BASE`, or `<meta name="auric-font-base">`.

## Loader: AuricFonts API

The global `AuricFonts` (alias `AuricFontLoader`).

| Member | Parameters | Returns |
|---|---|---|
| `load(spec)` | A spec or an array of specs | Promise of `{ id, family }` (or an array) when ready |
| `face(options)` | `family`, `url`, `local`, `weight`, `style`, `display`, `stretch` | Promise of the family name |
| `injectCss(cssText, id)` | CSS text, optional id | The added `<style>` element |
| `cssUrl(spec)` / `css(spec)` | A spec | The stylesheet URL |
| `whenReady(family, weights)` | Family name, optional weights | Promise that resolves when the fonts are usable |
| `list()` | — | Promise of every family record |
| `search(query)` | Text | Promise of records whose name, designer or category matches |
| `get(idOrName)` | Id or name | Promise of the full metadata, or `null` |
| `slugify(name)` | Name | The family id |
| `base` | — | The base address (can be set) |
| `index` | — | The loaded catalogue, or `null` before `list()`, `search()` or `get()` |

### Spec forms

| Form | Example |
|---|---|
| Name | `'Alegreya'` |
| Name with axis weights | `'Open Sans:wght@400;700'` |
| Name with weights and italic marker | `'Roboto:400,700i'` |
| Object | `{ family: 'Inter', weights: [400, 700] }` |

## Font Library snippets

### Use & Embed tab

| Snippet | Output |
|---|---|
| **Link** | `<link rel="stylesheet" href="…/css/<id>.css">` |
| **Import** | `@import url('…/css/<id>.css');` |
| **Script** | The loader script tag with `data-families` |
| **JS** | `AuricFonts.load('<Family>')` with a `font-family` assignment |
| **@font-face** | Rules for up to four styles, with absolute file URLs |
| **Usage** | A `.headline` rule with the family, a fallback and a weight |

### Develop tab

| Item | Output |
|---|---|
| Font-family stack (with safe fallbacks) | `font-family: '<Family>', <category fallbacks>;` |
| **CSS variables** | `:root { --font-<role>: <stack>; }` and a `body` rule |
| **Tailwind** | A `tailwind.config.js` `fontFamily` extension |
| **SCSS** | `$font-<role>: <stack>;` and a `body` rule |
| **Design tokens** | JSON: `font.family.<role>` with type `fontFamily` |
| **CSS @import** | The `@import` line and a `--font-<role>` variable |
| Modular type scale | Base 10–24 px (16 default) and a ratio from 1.125 to 1.618; **Copy CSS** |

`<role>` is `sans`, `serif` or `mono`, from the family's category. The fallback stacks are:

| Category | Fallback stack |
|---|---|
| Sans-serif | `ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif` |
| Serif | `ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif` |
| Monospace | `ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace` |
| Display | `ui-sans-serif, system-ui, sans-serif` |
| Handwriting | `'Segoe Script', cursive` |

The type-scale ratios are 1.125 (Major Second), 1.200 (Minor Third, the default), 1.250 (Major Third), 1.333 (Perfect Fourth), 1.414 (Augmented Fourth), 1.500 (Perfect Fifth) and 1.618 (Golden Ratio). The steps are named `xs`, `sm`, `base`, `md`, `lg`, `xl`, `2xl`, `3xl` and `4xl`.

## Downloads

| File | Contents |
|---|---|
| `<Family>-font-kit.zip` | One family: `fonts/`, `css/<id>.css`, `demo.html`, `README.txt`, `LICENSE.txt` |
| `auric-font-selection-kit.zip` | The same for each family in your selection |
| `DOWNLOAD_NOTES.txt` | Added when a file could not be fetched |

## Licence permissions shown per family

The **License** tab marks each of these as allowed, not allowed or unknown: **Commercial use**, **Modification**, **Redistribution**, **Private / personal use**, **Web embedding** and **Sell font on its own**. It also shows the licence name, a **License URL** where known, the original licence file, the copyright, and the **Full license** text.

## Related pages

- [Use the loader](use-the-loader.md)
- [Licences](../others/licences.md)
