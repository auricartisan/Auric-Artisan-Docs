---
title: Auric Artisan Icon Hub — Reference
description: Every command, keybinding, setting, view, collection, format and message in Auric Artisan Icon Hub 0.1.0.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Icon Hub reference

This reference describes version 0.1.0 as published on the Visual Studio Marketplace.

## Commands

Category in the Command Palette: **Auric Icon Hub**.

| Command | ID | What it does |
| --- | --- | --- |
| Open Icon Hub | `auricIconLib.openStudio` | Opens the full Hub panel. |
| Quick Search Icons | `auricIconLib.quickSearch` | Search box, then a Quick Pick of matches; runs your click action. |
| Smart Insert Icon | `auricIconLib.smartInsert` | Same flow as Quick Search; insertion follows the editor language. |
| Copy Icon As… | `auricIconLib.copyAs` | Pick an icon and a format; copies. |
| Save Icon As… | `auricIconLib.saveIcon` | Pick an icon; saves in your copy format. |
| Show Favorite Icons | `auricIconLib.showFavorites` | Quick Search limited to favorites. |
| Show Recent Icons | `auricIconLib.showRecents` | Quick Search limited to recent icons. |
| Refresh Icon Catalog | `auricIconLib.refreshCatalog` | Checks for compatible metadata now. |
| Clear Downloaded Icon Catalog | `auricIconLib.clearCache` | Returns to the bundled metadata. |
| Open Auric Icon Tool | `auricIconLib.openWebsite` | Opens https://icons.auricartisan.com in your browser. |
| Clear Icon Favorites and Recents | `auricIconLib.clearPersonalization` | Clears favorites and recents immediately, without a confirmation. |
| Export Selected Icons | `auricIconLib.exportSelected` | Opens the Hub for exporting; hidden from the Command Palette. |

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command |
| --- | --- | --- |
| `Ctrl` + `Alt` + `Shift` + `I` | `Cmd` + `Alt` + `Shift` + `I` | Quick Search Icons |

### Keys inside the Hub

| Key | Action |
| --- | --- |
| `Ctrl` + `K` / `Cmd` + `K` | Focus search |
| Arrow keys | Move between cards; move in dropdowns |
| `Enter` | Open the inspector for the focused card; choose a dropdown option |
| `F` | Star the focused card |
| `Home`, `End` | First or last dropdown option |
| `Escape` | Close a dropdown or the inspector |
| `Tab` | Stays inside the inspector while it is open |

## Settings

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricIconLib.clickAction` | string | `insert`, `copy`, `insertAndCopy` | `insert` | Action when an icon is chosen. |
| `auricIconLib.copyFormat` | string | `svg`, `jsx`, `reactComponent`, `html`, `dataUri`, `css`, `cdn` | `svg` | Default format for Copy and Save. |
| `auricIconLib.defaultSet` | string | `all`, `phosphor`, `tabler`, `lucide`, `remix`, `heroicons`, `feather`, `material` | `all` | Initial collection filter. |
| `auricIconLib.defaultStyle` | string | `auto` or a style ID | `auto` | Initial style filter. |
| `auricIconLib.size` | number | 8 to 512 | 24 | Output size in pixels. |
| `auricIconLib.color` | string | `currentColor` or `#rrggbb` | `currentColor` | Preview and output colour. |
| `auricIconLib.strokeWidth` | number | 0.5 to 4 | 2 | Stroke width. |
| `auricIconLib.density` | string | `compact`, `comfortable`, `showcase` | `comfortable` | Card density. |
| `auricIconLib.pageSize` | number | 24 to 240 | 72 | Cards per batch. |
| `auricIconLib.recommendations.enabled` | boolean | `true`, `false` | `true` | Shows the Smart Finder. |
| `auricIconLib.statusBar.enabled` | boolean | `true`, `false` | `true` | Shows the status bar item. |
| `auricIconLib.maxRecents` | number | 5 to 200 | 40 | Recent icons kept. |
| `auricIconLib.remoteRefresh.enabled` | boolean | `true`, `false` | `true` | Allow metadata checks from https://icons.auricartisan.com. |
| `auricIconLib.remoteRefresh.onStartup` | boolean | `true`, `false` | `true` | Check in the background when the Hub activates. |
| `auricIconLib.remoteRefresh.intervalHours` | number | 1 to 168 | 24 | Minimum hours between automatic attempts. |

Style IDs: Phosphor `thin`, `light`, `regular`, `bold`, `fill`, `duotone`; Tabler `outline`, `filled`; Lucide and Feather `regular`; Remix `line`, `fill`; Heroicons `24/outline`, `24/solid`, `20/solid`, `16/solid`; Material `outlined`, `round`, `sharp`, `regular`, `twotone`.

## Views and menus

| Place | Contents |
| --- | --- |
| Activity Bar | **Auric Icon Hub** container with the **Icon Hub** view. |
| View title bar | **Quick Search Icons**, **Refresh Icon Catalog**, **Open Icon Hub**. |
| Editor right-click | **Smart Insert Icon**, **Copy Icon As…**. |
| Status bar | Icon and "{count} Icons"; tooltip "Auric Icon Hub · {catalog source}"; opens the Hub. |

## Hub controls

| Area | Controls |
| --- | --- |
| Header | **Refresh**, **Website ↗**, open in editor tab |
| Views | **Library**, **Favorites**, **Recent**, **Selected** |
| Refine library | Set, style, category, licence, sort (**Relevance**, **Name**, **Set**) |
| Shape the output | **Size**, **Color** (picker), **Stroke** |
| Finder footer | **Reset filters** |
| Smart Finder | **Shuffle** |
| Card | Preview (inspector), star, check (select), **Insert**, **Copy** |
| Inspector | Style buttons, **Copy format**, CDN preview, **Insert**, **Copy**, **Save** |
| Selection tray | **Copy sprite**, **Export ZIP**, **Clear** |
| Grid | **Load more** |

## Collections

| ID | Name | Icons | Licence |
| --- | --- | --- | --- |
| `phosphor` | Phosphor | 1,512 | MIT |
| `tabler` | Tabler | 5,093 | MIT |
| `lucide` | Lucide | 1,714 | ISC |
| `remix` | Remix | 1,689 | Remix v1.0 |
| `heroicons` | Heroicons | 324 | MIT |
| `feather` | Feather | 287 | MIT |
| `material` | Material | 2,276 | Apache-2.0 |

Total: 12,895 icons, 32,802 indexed variants.

## Insertion by language

| Language IDs | Insert output |
| --- | --- |
| `html`, `vue`, `svelte`, `astro` | CDN placeholder; bridge connected |
| `javascriptreact`, `typescriptreact` | CDN placeholder (or React component); bridge connected |
| `javascript`, `typescript` | Named markup constant; bridge connected |
| `css`, `scss`, `less` | CSS (not available for Material) |
| `svg`, `xml` and others | SVG (not available for Material) |

## Limits

| Item | Limit |
| --- | --- |
| Icons per export | 200 |
| Metadata request timeout | 15 seconds |
| Metadata files | 5, under `/data/` |

## Messages you may see

| Message | Meaning |
| --- | --- |
| No writable editor selected; icon copied to the clipboard. | Insert fell back to Copy. |
| Material Icons are font-backed; generated HTML markup instead of SVG. | You asked for SVG or data URI for a Material icon. |
| The selected editor is read-only. Use Copy instead. | Insert was refused. |
| The editor could not accept this insertion. Use Copy instead. | The edit was rejected. |
| Insert Material icons into HTML or a web-framework file to connect your CDN. Use Copy for other formats. | Material insertion needs a web file. |
| Catalog metadata updated. Shipped artwork remains available offline. | Manual refresh succeeded. |
| Using offline catalog: … | Refresh failed; the local catalog is used. |
| Remote catalog refresh is disabled. | `remoteRefresh.enabled` is off. |
| Cache cleared; bundled catalog restored. | Downloaded metadata removed. |
| Select one or more icons | Export was started with an empty selection. |
