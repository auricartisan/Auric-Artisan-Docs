---
title: Icon CDN — Getting started
description: How the Icon CDN is organised, how icons are named, and how to put a first icon on a page.
product: Services › Icon CDN
updated: 2026-09-25
---

# Getting started

## How the CDN is organised

Everything is served from https://icons.auricartisan.com:

| Path | What it is |
|---|---|
| `/icon-cdn.js` | The loader script |
| `/icon/<set>/…` | The original SVG files, and the Material and Remix webfonts |
| `/data/sets.json` | The seven sets: styles, licence, grid and counts |
| `/data/index.json` | One record per icon, used for names and search |
| `/data/bodies/<set>.<style>.json` | The icon markup for one set and style, loaded by the loader as needed |
| `/data/material.json` | The code points for the Material webfont |
| `/LICENSE.md` | The licence reference for every set |

## Icon names

An icon is named by its set and its name, joined by a colon: `lucide:house`, `tabler:home`, `phosphor:heart`. The loader also accepts:

| Form | Example | Meaning |
|---|---|---|
| `set:name` | `tabler:home` | This icon from this set |
| `set-name` | `tabler-home` | The same |
| `name` | `home` | The first set with this name: Lucide, Phosphor, Tabler, Remix, Heroicons, Feather, then Material |

Names are the set's own icon names in lower case with hyphens. Different sets name things differently: Lucide calls it `house`, Tabler calls it `home`. The Icon Library shows every icon's name and gives you the exact tag with **Copy CDN tag**.

## Your first icon

1. Add the loader once, anywhere in the page:

   ```html
   <script src="https://icons.auricartisan.com/icon-cdn.js"></script>
   ```

2. Add a placeholder where the icon should go:

   ```html
   <button><i data-icon="lucide:house"></i> Home</button>
   ```

3. Load the page. When the page has loaded, the loader replaces the contents of every `data-icon` element with the icon's SVG.

The icon uses `currentColor`, so it takes the button's text colour.

> **Important:** The SVG markup the CDN serves has a `viewBox` but no width or height of its own. Without a size, browsers draw it at their default size for SVG, which is usually far too large. Always give icons a size, either with `data-size` or with CSS such as the rule below.

```css
[data-icon] svg { width: 1em; height: 1em; }
```

See [Style, size and colour](style-size-and-colour.md).

## Next steps

- [Collections](collections.md), to choose a set and a style.
- [Embed an icon](embed-an-icon.md), for ways that do not use the loader.
- [Use the loader](use-the-loader.md), for icons added after the page loads.
