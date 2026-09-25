---
title: Icon CDN — Privacy
description: What a page that uses the Icon CDN requests from it, and what the loader script does and does not do.
product: Services › Icon CDN
updated: 2026-09-25
---

# Privacy

## What your visitors' browsers request

| You use | Your visitors' browsers request from icons.auricartisan.com |
|---|---|
| The loader with placeholders | The loader, the index, the set list, one markup file per set and style, and Material data and fonts if used |
| Linked SVG files | Each file |
| Inline SVG, JSX, data URIs or a sprite you pasted | Nothing |

As with any file host, the CDN receives the ordinary information that comes with each request.

## What the loader does not do

The loader served at https://icons.auricartisan.com/icon-cdn.js:

- sets no cookies;
- writes nothing to the browser's storage;
- makes no requests other than the data and font files described above.

## Avoiding the CDN at run time

If you prefer your visitors' browsers never to contact the CDN, paste inline SVG or a sprite, or export a ZIP and serve the files yourself. See [Export and self-host](../docs/export-and-self-host.md).

## The Icon Library page

Recolouring, resizing and exports on the Icon Library page happen in your browser, and your selection is "Kept in this browser". For the auricartisan.com website as a whole, see the site's privacy policy at https://auricartisan.com/legal/privacy/.
