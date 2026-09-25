---
title: Auric Artisan Font Hub — fonts for VS Code
description: What Auric Artisan Font Hub does, who it is for, how to install it and where to find every guide.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Auric Artisan Font Hub

Auric Artisan Font Hub is a typography workspace inside VS Code. It holds the Auric Artisan font library: 2,023 font families, 547 of them variable, with metadata bundled in the extension so you can browse offline. Search and filter the library, open a family's specimen, glyphs, OpenType features and licence, compare families side by side, and get recommendations for a design intent, an industry or a colour palette.

When you have chosen, Font Hub adds the font to your code from the Auric font CDN, `fonts.auricartisan.com`. **Add to code** adds a stylesheet link and a reusable class such as `.auric-font-inter` to an HTML, CSS or JavaScript file without touching your existing styles. **Preview** shows the change first in VS Code's own diff view, with **Apply** and **Cancel**. For other file types it copies an embed for you to place, and it offers every common format: HTML link, CSS `@import`, `font-family`, `@font-face`, Tailwind configuration, SCSS variables and design tokens. For self-hosting, it exports a ZIP kit with the font files, CSS, a demo page and the required licence notices, where the licence allows it.

Browsing works offline. Previews and downloads fetch from the Auric font CDN and are cached locally. No account is needed, and your searches, code and favourites are not uploaded.

## Who it is for

- Front-end developers choosing and adding web fonts.
- Designers checking a family's styles, glyph coverage, features and licence before committing to it.
- Teams building a design system who need tokens, Tailwind or SCSS entries for their fonts.
- Anyone who wants to self-host fonts with the right licence files.

## Where to find it

- Marketplace ID: `auric-artisan.auric-artisan-font-hub`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-font-hub
- Install from a terminal:

  ```text
  code --install-extension auric-artisan.auric-artisan-font-hub
  ```

- Requires VS Code 1.85 or newer. Version 0.1.0 at the time of writing.
- The same library on the web: https://auricartisan.com/tool/font/
- Settings and command IDs use the prefix `auricFontLib`, kept from the extension's earlier name, Font Library.

## Quick start

1. Install the extension.
2. Select **Auric Font Hub** in the Activity Bar, or run **Auric Artisan Font Hub: Open Font Hub** (`Ctrl` + `Alt` + `F`; `Cmd` + `Alt` + `F` on macOS).
3. Type a family, designer, script or feature in the search box, or narrow the list with **Category**, **Sort** and **More filters**.
4. Select a font card's name to open its details: specimen, waterfall, glyphs, features, styles and licence.
5. Open an HTML, CSS or JavaScript file in the editor, then choose **Preview** on the font card.
6. Review the proposed change in VS Code's diff view, then choose **Apply** (or **Cancel** to leave the file as it was). The edit is left unsaved, so you can undo it.
7. Apply the generated class in your markup, for example `<p class="auric-font-inter">`.
8. For a quick pick without the panel, press `Ctrl` + `Alt` + `T` (**Quick Pick Font**).

## What you can do

- Browse 2,023 families by category, weight, variable, italic and monospace properties, OpenType features, scripts, licence and source.
- Edit the specimen text and size, switch card density, and page through results.
- Inspect a family in twelve tabs: **Specimen**, **Waterfall**, **Suitability**, **Pairings**, **Features**, **Develop**, **Glyphs**, **Charset**, **Styles**, **About**, **License** and **Use & Embed**.
- Try variable axes and OpenType features live in the specimen.
- Rank families against a design intent, an industry and a colour palette with **Find your font**.
- Save favourites, return to recent fonts, select up to 12 families and compare up to four.
- Add fonts to HTML, CSS, SCSS, Less, PostCSS, JavaScript and TypeScript, with a native diff preview first.
- Copy or insert ten embed formats.
- Check the CDN and browser font delivery (CORS) with a built-in report.
- Export a licence-aware self-hosting kit as a ZIP.
- Use the shared Auric colour picker for palette editing, contrast checks and ramps.

## In this folder

- [docs/](docs/README.md) — task guides and the full reference.
  - [Getting started](docs/getting-started.md)
  - [Find and compare fonts](docs/find-and-compare-fonts.md)
  - [Font details](docs/font-details.md)
  - [Add a font to your code](docs/add-fonts-to-code.md)
  - [Check CDN and browser delivery](docs/cdn-and-browser-delivery.md)
  - [Export a self-hosting kit](docs/self-hosting-kit.md)
  - [Offline use, cache and network](docs/offline-cache-and-network.md)
  - [Moving from Font Library](docs/moving-from-font-library.md)
  - [Reference: commands, keys and settings](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Privacy](others/privacy.md)
  - [Related](others/related.md)
  - [Release notes](others/release-notes.md)
