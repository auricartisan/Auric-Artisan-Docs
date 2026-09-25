---
title: Font CDN — Self-host a family
description: Download a font kit from the Font Library, understand what it contains, and serve the family from your own site.
product: Services › Font CDN
updated: 2026-09-25
---

# Self-host a family

Instead of loading fonts from fonts.auricartisan.com, you can download a family and serve it from your own site. The Font Library builds a ready-to-use kit in your browser.

## Download a kit

For one family:

1. Open the family in the Font Library at https://auricartisan.com/tool/font/.
2. Choose **Download kit** ("Download N bundled font files with CSS and license notes"). The same button is in the **Styles** tab under **Download self-hosting kit**.
3. Your browser saves `<Family>-font-kit.zip`.

For several families:

1. Add them to your selection. They collect in the **Your kit** tray.
2. Choose **Download** in the tray (it reads **Download selected (N)**). The file is named `auric-font-selection-kit.zip` (or after the family when there is one).

The Font Library shows "Preparing download kit..." while it gathers the files, then "Downloaded" and the file name.

## What a kit contains

For each family, a folder with:

| File | What it is |
|---|---|
| `fonts/…` | Every font file the CDN serves for the family |
| `css/<family-id>.css` | `@font-face` rules pointing at `../fonts/`, and a `--font-<family-id>` variable with a fallback |
| `demo.html` | A page that shows the family, using the stylesheet |
| `README.txt` | The family, category, designer, licence, file list and three steps to use it |
| `LICENSE.txt` | The family's licence text, when the library has it |

If a file could not be fetched, the kit adds `DOWNLOAD_NOTES.txt` listing what is missing.

## Install it on your site

1. Unzip the kit and copy the family's folder into your site, for example to `/fonts/alegreya/`.
2. Keep the `fonts`, `css` and licence files together.
3. Link the stylesheet from your pages:

   ```html
   <link rel="stylesheet" href="/fonts/alegreya/css/alegreya.css">
   ```

4. Apply the family:

   ```css
   body { font-family: 'Alegreya', serif; }
   ```

   or use the variable the stylesheet defines, such as `var(--font-alegreya)`.

5. Open `demo.html` from the kit to check the files work.

## Point the loader at your copy

If you use `font-cdn.js`, you can host it with your own stylesheets and data and set its base address; see [Use the loader](use-the-loader.md#where-it-loads-from).

## Families that cannot be downloaded

Families tagged **Installed** are system fonts: the library lists them but does not serve their files, because their licences do not allow redistribution. For these, the download button reads **Installed only**, and the Font Library says "Only bundled library fonts can be downloaded".

## Keep the licence

Every kit includes the licence information for a reason: most open font licences require the licence to travel with the files. See [Licences](../others/licences.md).

## Related pages

- [Embed a family](embed-a-family.md)
- [Licences](../others/licences.md)
