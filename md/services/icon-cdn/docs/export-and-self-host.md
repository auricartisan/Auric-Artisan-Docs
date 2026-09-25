---
title: Icon CDN — Export and self-host
description: Export icons from the Icon Library as a ZIP of SVG files or an SVG sprite, download single icons, and host icons or the loader yourself.
product: Services › Icon CDN
updated: 2026-09-25
---

# Export and self-host

You do not have to load icons from icons.auricartisan.com at run time. The Icon Library can export them for your own project.

## Collect icons in your kit

1. In the Icon Library at https://auricartisan.com/tool/icon/, open an icon and choose **＋ Select**.
2. Selected icons collect in the **Your kit** tray, with a count. The tray notes that it is "Kept in this browser".
3. Choose **Hide** to put the tray away, and **Clear** to empty it.

## Download a ZIP

Choose **Download ZIP** in the tray. The file `auric-icons.zip` contains:

- one SVG per icon, in a folder per set, named `<name>-<style>.svg`;
- a `README.txt` noting the number of icons and that each uses `currentColor`;
- for Material icons, a text file per icon with its webfont character code instead of an SVG.

## Copy an SVG sprite

Choose **Copy sprite** in the tray. The Icon Library copies one hidden `<svg>` containing a `<symbol>` for each selected icon, with the icon's id as its `id`:

```html
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="lucide-house" viewBox="0 0 24 24">…</symbol>
</svg>
<!-- use: <svg><use href="#ID"/></svg> -->
```

Paste it once near the top of your page, then use any icon with:

```html
<svg width="24" height="24"><use href="#lucide-house"/></svg>
```

A sprite needs no script and no further requests, and icons in it still take `currentColor`.

## Download one icon

Open an icon and choose **Download .svg**. The file is named `<id>-<style>.svg` and uses your chosen colour and stroke.

## Link files directly

Every SVG icon is also served as a file under `https://icons.auricartisan.com/icon/<set>/…`; see [Embed an icon](embed-an-icon.md#direct-svg-files). You can download files from these addresses to host them yourself.

## Host the loader yourself

The loader works from any address. To serve it from your own site:

1. Copy `icon-cdn.js` and the `data/` files it uses (`sets.json`, `index.json`, the `bodies/` files for the sets and styles you need, and `material.json` with the Material fonts if you use Material) to a folder on your site, keeping the same layout.
2. Load the script from there. It finds its data next to itself, or set `data-base` on the script tag to point elsewhere.

See [Use the loader](use-the-loader.md#where-it-loads-from).

## Keep the licences

When you ship icons, keep each set's licence notice where its licence asks for it. See [Licences](../others/licences.md).

## Related pages

- [Embed an icon](embed-an-icon.md)
- [Licences](../others/licences.md)
