---
title: Auric Artisan Font Hub — reference
description: Every Auric Artisan Font Hub command, keyboard shortcut, menu entry, panel control and setting, with types, defaults and ranges.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Reference: commands, keys and settings

This page covers Auric Artisan Font Hub 0.1.0: 16 commands, 2 keyboard shortcuts, one Activity Bar view and 13 settings. Command and setting IDs use the `auricFontLib` prefix, kept from the extension's earlier name.

## Commands

Fifteen commands appear under **Auric Artisan Font Hub:** in the Command Palette; **Show Logs** appears under **Auric Font Hub:**.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Open Font Hub** | `auricFontLib.openStudio` | `Ctrl` + `Alt` + `F` | Open the full studio in an editor tab |
| **Quick Pick Font** | `auricFontLib.quickPick` | `Ctrl` + `Alt` + `T` | Choose a family, then an action |
| **Add Font to Code** | `auricFontLib.insertEmbed` | — | Choose a family and add it to the active file in the default format |
| **Copy Font Embed As…** | `auricFontLib.copyEmbed` | — | Choose a family and a format, and copy the snippet |
| **Pick from Favorite Fonts** | `auricFontLib.showFavorites` | — | Quick Pick limited to favourites |
| **Pick from Recent Fonts** | `auricFontLib.showRecents` | — | Quick Pick limited to recent fonts |
| **Compare Selected Fonts** | `auricFontLib.compareSelected` | — | Compare up to four selected families |
| **Download Self-hosting Font Kit** | `auricFontLib.downloadKit` | — | Export a ZIP kit for chosen families |
| **Refresh Font Catalog from Auric CDN** | `auricFontLib.refreshCatalog` | — | Refresh catalogue data now |
| **Clear Favorites, Recents, and Selection** | `auricFontLib.clearPersonalization` | — | Clear all three, after confirmation |
| **Clear Downloaded Font Cache** | `auricFontLib.clearCache` | — | Empty the cache; the bundled catalogue stays |
| **Explore Fonts on AuricArtisan.com** | `auricFontLib.openWeb` | — | Open https://auricartisan.com/tool/font/ |
| **Focus Font Search** | `auricFontLib.focusSearch` | — | Move focus to the search box |
| **Show Logs** | `auricFontLib.showLogs` | — | Open the Font Hub log |
| **Preview Font Insertion** | `auricFontLib.previewInsert` | — | Show the proposed change as a diff, with Apply and Cancel |
| **Check Font CDN and Browser CORS** | `auricFontLib.checkCdn` | — | Run the CDN delivery check |

On macOS the two shortcuts are `Cmd` + `Alt` + `F` and `Cmd` + `Alt` + `T`.

## Where commands appear

| Place | Entries |
| --- | --- |
| Activity Bar | **Auric Font Hub**, with the **Font Hub** view |
| **Font Hub** view title bar | **Open Font Hub**, **Focus Font Search**, **Refresh Font Catalog from Auric CDN** |
| Editor context menu › **Auric Fonts** | **Quick Pick Font**, **Add Font to Code**, **Preview Font Insertion**, **Copy Font Embed As…**, **Open Font Hub** |
| Status bar | **Fonts** (opens Font Hub); hide with `auricFontLib.statusBar.enabled` |

### Quick Pick Font actions

After you choose a family: **Add font to code**, **Preview CDN insertion**, **Copy embed as…**, **Inspect in Font Hub**, **Download self-hosting kit**, **Toggle favorite**.

## Panel controls

| Control | Where | What it does |
| --- | --- | --- |
| **Search** | Controls | Search family, designer, script, feature and licence |
| **Category** | Controls | Filter by category |
| **Sort** | Controls | Ten orders, from **Alphabetical** to **Variable first** |
| **Preview text** | Controls | Sample text on cards (up to 240 characters) |
| **Size** | Controls | Sample size, 18–96 px |
| **More filters** | Controls | Show **Properties**, **Weights**, **OpenType**, **Scripts**, **License**, **Source** chips |
| Scopes | Above results | **All**, **For you**, **Favorites**, **Recent**, **Variable**, **Selected** |
| **Find your font** | Above results | Design intent, industry, colour palette, **Prioritize accessibility**, **Prefer variable fonts**, **Rank fonts** |
| Density | Above results | Compact, comfortable, showcase |
| **Collections & recommendations** | Above results | Featured collections and recommendations |
| **Show more** | Below results | Load the next batch |
| **Check CDN health**, **CDN diagnostics**, **Run a live check** | Card, footer, help | Run the CDN check |
| **↻**, **↗**, **⚙** | Header | Refresh catalogue, open the web library, open settings |
| **Open studio ↗** | Sidebar header | Open the full studio |
| Card: heart, select | Each card | Favourite, add to selection |
| Card: **Add to code**, **Preview** | Each card | Automatic insertion, with or without a diff preview |
| Tray: **Copy embed**, **Insert**, **Compare**, **Download** | Selected tray | Act on the whole selection |
| Details: **Favorite**, **Select** | Details header | Favourite or select the open family |
| Details tabs | Details | **Specimen**, **Waterfall**, **Suitability**, **Pairings**, **Features**, **Develop**, **Glyphs**, **Charset**, **Styles**, **About**, **License**, **Use & Embed** |
| Details: **Copy**, **Insert**, **Save** | Develop, Use & Embed | Use the chosen format |
| Details: **Download kit** | Styles, Use & Embed | Export a kit for this family |
| Details: **Load full license text** | License | Show the full licence |

## Keys inside Font Hub

| Keys | What they do |
| --- | --- |
| `/` (outside a text field) or `Ctrl` + `K` | Focus and select the search box |
| `Escape` | Close the comparison, details or tray; otherwise clear the search |
| Arrow keys on a card | Move between cards |
| `Tab` | Stays within an open details panel, tray or comparison |

## Settings

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFontLib.defaultFormat` | string | `auto` | `auto`, `link`, `import`, `family`, `fontFace`, `loader`, `tailwind`, `scss`, `tokens`, `name` | Format used by **Add Font to Code**; `auto` adds the CDN stylesheet and a class |
| `auricFontLib.previewText` | string | `The quick brown fox jumps over the lazy dog` | — | Default sample text on cards |
| `auricFontLib.previewSize` | number | `36` | 18–96 | Default sample size in pixels |
| `auricFontLib.density` | string | `comfortable` | `compact`, `comfortable`, `showcase` | Card density in the sidebar and studio |
| `auricFontLib.pageSize` | integer | `48` | 24–144 | Families shown per batch |
| `auricFontLib.recommendations.enabled` | boolean | `true` | — | Show recommendations from role scores, style intent and local use |
| `auricFontLib.network.enabled` | boolean | `true` | — | Allow requests to fonts.auricartisan.com for metadata, previews and downloads |
| `auricFontLib.catalogRefresh` | string | `daily` | `manual`, `daily`, `always` | When to refresh the catalogue from the CDN |
| `auricFontLib.cache.maxAgeHours` | integer | `24` | 1–720 | How long cached CDN metadata counts as fresh |
| `auricFontLib.cache.maxMB` | integer | `512` | 64–4096 | Disk space in MiB for the cache; oldest items removed first |
| `auricFontLib.download.maxFamilies` | integer | `6` | 1–12 | Most families in one self-hosting kit |
| `auricFontLib.statusBar.enabled` | boolean | `true` | — | Show the **Fonts** status bar item |
| `auricFontLib.includeSystemFonts` | boolean | `false` | — | Include system-font metadata; previews depend on installed fonts |

### Format values

| Value | Label | Output |
| --- | --- | --- |
| `auto` | Automatic | CDN stylesheet plus `.auric-font-<id>` class, placed by file type |
| `link` | HTML stylesheet link | `<link rel="stylesheet" href="…/css/<id>.css">` |
| `import` | CSS @import | `@import url('…/css/<id>.css');` |
| `family` | CSS font-family | `font-family: '<Family>', <fallback>;` |
| `fontFace` | @font-face | `@font-face` rules per style |
| `loader` | AuricFonts loader | A script that loads the Auric font loader for the family |
| `tailwind` | Tailwind config | A `fontFamily` entry |
| `scss` | SCSS variable | `$font-<role>: '<Family>', <fallback>;` |
| `tokens` | Design tokens JSON | A typography token with family, fallback and CSS address |
| `name` | Family name | The family name only |

## Files Font Hub writes

| File | When |
| --- | --- |
| The active document | **Add to code**, **Insert**, **Apply** (left unsaved) |
| A snippet file you name | **Save** in the details panel |
| A ZIP kit you name | **Download kit** and related commands |
| Cache | VS Code's extension storage, not your project |

Output channel: **Auric Font Hub**.
