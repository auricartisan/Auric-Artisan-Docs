---
title: Auric Artisan Icon Hub — Insert, copy and save
description: How Icon Hub's Insert adapts to your file, the inspector and its formats, Quick Search and the Command Palette, and saving icons to files.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Insert, copy and save

## Insert

Select **Insert** on a card, or in the inspector. Icon Hub inserts at every selection in the active editor or, if you clicked into the Hub, the last text editor you used.

| Editing in | Insert produces |
| --- | --- |
| HTML, Vue, Svelte, Astro | A CDN icon placeholder element, and the CDN loader is connected. |
| React JSX or TSX | The CDN placeholder as JSX (or a React component if you chose one in the inspector), and the loader is connected. |
| JavaScript, TypeScript | A named, quoted markup constant, and the loader is connected. |
| CSS, SCSS, Less | A self-contained CSS declaration. |
| SVG, XML and other languages | Self-contained SVG markup. |

See [Connect the icon CDN](cdn-insertion.md) for what the loader is and what it needs.

- Material icons can only be inserted into HTML or web-framework files: "Insert Material icons into HTML or a web-framework file to connect your CDN. Use Copy for other formats."
- Read-only editors are refused: "The selected editor is read-only. Use Copy instead."
- A rejected edit is reported, not recorded as a success.
- With no editor, the output is copied and VS Code says "No writable editor selected; icon copied to the clipboard."

## The inspector

Select a card's preview to open the inspector. It shows a large preview, the set, name, category and licence, the available styles, a **Copy format** dropdown, a CDN snippet preview, and **Insert**, **Copy** and **Save**.

- Select a style button to switch the icon's style.
- The **Copy format** applies to **Copy** and **Save**. **Insert** always follows the editor language.
- `Escape` closes the inspector; `Tab` stays inside it.

## Formats

| Format | Setting value | SVG icons | Material icons |
| --- | --- | --- | --- |
| SVG | `svg` | Yes | No (HTML is used instead) |
| JSX | `jsx` | Yes | Yes |
| React component | `reactComponent` | Yes | Yes |
| HTML | `html` | Yes | Yes |
| Data URI | `dataUri` | Yes | No (HTML is used instead) |
| CSS | `css` | Yes | Yes |
| CDN snippet | `cdn` | Yes | Yes |

The CDN snippet looks like this:

```html
<i data-icon="set:name" data-style="…" data-size="24" data-color="currentColor" data-stroke="2" aria-hidden="true"></i>
<script src="https://icons.auricartisan.com/icon-cdn.js" defer></script>
```

Standalone SVG, data URI and CSS exports include the SVG namespace, so they work as separate files. SVG is sanitised before preview and export.

Set the default for **Copy** with `auricIconLib.copyFormat` (default `svg`), and what a card choice does with `auricIconLib.clickAction` (`insert`, `copy`, `insertAndCopy`; default `insert`).

## Save

Select **Save** in the inspector, or run **Auric Icon Hub: Save Icon As…**. A save dialog opens in your first workspace folder with a file name based on the icon. The file type follows the format:

| Format | Extension |
| --- | --- |
| SVG | `.svg` |
| CSS | `.css` |
| JSX, React component | `.jsx` |
| HTML, CDN snippet | `.html` |
| Data URI | `.txt` |

**Save Icon As…** from the Command Palette uses your `copyFormat` setting.

## From the Command Palette

| Command | Flow |
| --- | --- |
| **Quick Search Icons** (`Ctrl` + `Alt` + `Shift` + `I`) | Type a search ("Search Auric Icons"), pick from the matches, and your click action runs. |
| **Smart Insert Icon** | The same flow; also on the editor right-click menu. |
| **Show Favorite Icons** / **Show Recent Icons** | The same flow, limited to favorites or recent icons. |
| **Copy Icon As…** | Pick from all icons, then a format; copies. Also on the editor right-click menu. |
| **Save Icon As…** | Pick an icon, then save. |

## Result

The icon is in your file, on the clipboard or saved as a file, in the form you need, and it appears under **Recent**.
