---
title: Font CDN — Privacy
description: What a page that uses the Font CDN requests from it, and what the loader script does and does not do.
product: Services › Font CDN
updated: 2026-09-25
---

# Privacy

## What your visitors' browsers request

A page that uses the CDN makes requests to https://fonts.auricartisan.com and nowhere else for its fonts:

| You use | Your visitors' browsers request |
|---|---|
| A link tag or `@import` | The family stylesheet, then the font files the page actually uses |
| The loader with `data-families` or `load()` | The loader script, the family stylesheets, then the font files |
| `list()`, `search()` or `get()` | Also the catalogue data files |

As with any file host, the CDN receives the ordinary information that comes with each request.

## What the loader does not do

The loader served at https://fonts.auricartisan.com/font-cdn.js:

- sets no cookies;
- writes nothing to the browser's storage;
- makes no requests other than the stylesheets and data files described above.

## Self-hosting

If you prefer your visitors' browsers never to contact the CDN, download a kit and serve the files from your own site. See [Self-host a family](../docs/self-host-a-family.md).

## The Font Library page

Previews on the Font Library page are drawn in your browser from the CDN's files, and download kits are assembled in your browser. For the auricartisan.com website as a whole, see the site's privacy policy at https://auricartisan.com/legal/privacy/.
