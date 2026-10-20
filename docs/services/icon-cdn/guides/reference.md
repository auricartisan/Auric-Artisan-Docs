---
title: Icon CDN — Reference
description: Every URL pattern, set, style, loader attribute, method and export of the Auric Artisan Icon CDN.
product: Services › Icon CDN
updated: 2026-09-25
---

# Reference

## Catalogue

| Fact | Value |
|---|---|
| Host | https://icons.auricartisan.com |
| Sets | 7 |
| Icons | 12,896 |
| Variants | 32,803 |
| Catalogue built | 3 June 2026 |
| Icons by licence | MIT 7,216; ISC 1,714; Remix v1.0 1,690; Apache 2.0 2,276 |

## URL patterns

| Pattern | What it serves |
|---|---|
| `/icon-cdn.js` | The loader |
| `/icon/<set>/…` | SVG files, and the Material and Remix webfonts |
| `/icon/remix/fonts/remixicon.css` | Remix Icon's own webfont stylesheet |
| `/data/sets.json` | Set metadata: label, licence, styles, default style, grid, counts, home, credit |
| `/data/index.json` | One record per icon: id, name, set, styles, category, search terms |
| `/data/bodies/<set>.<style>.json` | SVG markup for one set and style (a `/` in a style becomes `-`) |
| `/data/material.json` | Material code points by style |
| `/data/stats.json`, `/data/meta.json` | Catalogue statistics and build information |
| `/LICENSE.md` | The licence reference |

## Sets and styles

| Set | Styles (default first) | Grid | Stroke width applies |
|---|---|---|---|
| `lucide` | `regular` | 24 | Yes |
| `phosphor` | `regular`, `thin`, `light`, `bold`, `fill`, `duotone` | 256 | No |
| `tabler` | `outline`, `filled` | 24 | Yes |
| `remix` | `line`, `fill` | 24 | No |
| `heroicons` | `24/outline`, `24/solid`, `20/solid`, `16/solid` | 24, 20, 16 | Outline only |
| `feather` | `regular` | 24 | Yes |
| `material` | `outlined`, `round`, `sharp`, `regular`, `twotone` | Webfont | No |

Name resolution order when no set is given: Lucide, Phosphor, Tabler, Remix, Heroicons, Feather, Material.

## Placeholder attributes

| Attribute | Values | Default |
|---|---|---|
| `data-icon` | `set:name`, `set-name` or `name` | Required |
| `data-style` | A style of the set | The set's default |
| `data-size` | A number (pixels) or a CSS length | None: size it with CSS |
| `data-color` | Any CSS colour | `currentColor` |
| `data-stroke` | A number | The set's own width |

Filled placeholders get a `data-icon-done` attribute and are not processed again.

## Script configuration

| Setting | Meaning |
|---|---|
| `data-base` on the script | The address to load data from |
| `window.AURIC_ICON_BASE` / `window.AURIC_ICON_ASSET_BASE` | The same, set before the script loads |
| `<meta name="auric-icon-base">` | The same, in the page |

## AuricIcons API

The global `AuricIcons` (alias `AuricIconLoader`).

| Member | Parameters | Returns |
|---|---|---|
| `svg(name, options)` | `style`, `size`, `color`, `stroke` | Promise of the markup string, or `''` if not found |
| `inject(root)` | An element; default the document | Promise of the number of placeholders found |
| `get(name)` / `resolve(name)` | A name | Promise of the icon record, or `null` |
| `search(query, options)` | Text; `set`, `limit` | Promise of matching records |
| `list()` | — | Promise of every record |
| `sets()` | — | Promise of the set metadata |
| `slug(text)` | Text | Lower-case, hyphenated text |
| `base` | — | The data address (can be set) |
| `index` | — | The loaded index, or `null` before first use |

## Icon Library outputs

| Control | Output |
|---|---|
| **Copy SVG** | The SVG markup, with the chosen colour and stroke |
| **Copy JSX** | A React component that spreads its props onto the `<svg>` |
| **Copy data-URI** | An `<img>` with the SVG as a data URI, the chosen size and the icon name as `alt` |
| **Copy CDN tag** | A placeholder with `data-icon` (and `data-style` if not the default) and the loader script |
| **Download .svg** | `<id>-<style>.svg` |
| **Copy glyph** (Material) | The character entity for the webfont |
| Code panel (SVG sets) | **SVG**, **JSX / React**, **`<img>` data-URI**, **CDN (auto-inject)** |
| Code panel (Material) | **HTML (CDN)**, **Webfont @font-face** |
| **Download ZIP** (tray) | `auric-icons.zip`: SVGs by set, a README, and text files for Material icons |
| **Copy sprite** (tray) | A hidden `<svg>` with one `<symbol>` per selected icon |

## Icon Library controls

| Control | Range |
|---|---|
| **Size** | 16–160 px |
| **Stroke** | 0.5–3 in steps of 0.25, or **auto** |
| **Colour** | Any colour, or **currentColor** |
| **Style** | The icon's styles |

## Related pages

- [Use the loader](use-the-loader.md)
- [Collections](collections.md)
