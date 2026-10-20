---
title: Auric Icons: Modern — Insert, copy and save icons
description: Insert Modern icons with language-aware output, copy them in nine formats, save SVG files, open the source and preview icon IDs on hover.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Insert, copy and save icons

## Insert from the Icon Library

1. Open a file in a text editor and place one or more cursors, or select text to replace.
2. In the Icon Library, select **Insert** on a card.
3. The icon is inserted at every cursor. Multi-line output keeps the indentation of the cursor's line.

If no text editor is open, you see "Open a text editor before inserting an SVG." When you work in the full editor-tab library, the icon goes into the first visible file editor.

## Smart insert

With `auricIcons.library.smartInsert` on (the default), **Insert** adapts to the language of the file:

| Editing in | Output |
| --- | --- |
| JavaScript, TypeScript, React JSX and TSX, MDX | JSX element |
| HTML, PHP, Handlebars, Vue, Svelte, Astro | HTML markup |
| Markdown | Markdown image |
| CSS, SCSS, Less | CSS background |
| JSON, JSONC, YAML, Python | Data URI |
| XML, SVG and any other language | Raw SVG |

With the setting off, **Insert** always inserts raw SVG. The **Smart Insert Icon** command always adapts, whatever the setting.

### Smart insert from the keyboard

1. In a text editor, press `Ctrl` + `Alt` + `I` (`Cmd` + `Alt` + `I` on macOS), or run **Auric Icons: Modern: Smart Insert Icon (matches active language)**.
2. A list opens. With no search text, it starts with **Recommended for this file**, then **All icons**. Each row shows the category and tags (and the collection when several are merged).
3. Type to search and choose an icon. VS Code confirms, for example "… inserted for the active language."

## Copy in a chosen format

Run **Auric Icons: Modern: Copy Icon As… (JSX, CSS, Markdown, Data URI, Image tag)**, choose an icon, then choose a format:

| Format | What you get |
| --- | --- |
| Raw SVG | The SVG markup. |
| JSX element | The SVG with JSX attribute names. |
| React component | `export function IconName(props) { return (<svg {...props} …>); }` |
| Markdown image | `![Icon name](data:image/svg+xml,…)` |
| CSS background | `background-image: url("data:image/svg+xml,…");` plus `background-repeat: no-repeat;` and `background-size: contain;` |
| Data URI | `data:image/svg+xml,…` |
| Image tag (self-contained) | `<img src="data:image/svg+xml,…" alt="Icon name" width="24" height="24">` |
| Icon name | The icon ID, such as `analytics-bar-chart-0042`. |
| Catalog path | The icon's relative path in the catalog. |

Smart insert can also produce **HTML markup**, which is the SVG markup itself.

On a card, **Copy** copies raw SVG, **JSX** copies a JSX element and **URI** copies a data URI.

## Save an SVG file

1. Select **Save** on a card, or run **Save SVG As…** and choose an icon.
2. A save dialog opens in your first workspace folder (or your home folder) with the icon's file name.
3. Choose a location and select **Save icon**.

The saved file is the artwork in the selected variant.

## Open the SVG source

Select the artwork on a card, **Source** on a card, or run **Open SVG Source**. The SVG file opens in a preview tab so you can read or copy its markup.

## Other Command Palette actions

| Command | What it does |
| --- | --- |
| **Search Icons** | Choose an icon, then an action: **Smart Insert (matches this file)**, **Insert SVG at Cursor**, **Copy SVG**, **Save SVG As…**, **Open SVG Source** or **Toggle Like**. |
| **Insert SVG at Cursor** | Choose an icon and insert it (smart insert applies when the setting is on). |
| **Copy SVG** | Choose an icon and copy raw SVG. |
| **Insert from Likes** | Choose from your liked icons and insert. |
| **Insert from Recent** | Choose from recent icons and insert. Also `Ctrl` + `Alt` + `R`. |
| **Toggle Like for an Icon** | Choose an icon and like or unlike it. |
| **Clear Likes, Recents and Learned Recommendations** | Asks for confirmation (**Clear**), then resets. |

## Hover previews

Type or find a Modern icon ID in code, such as `analytics-bar-chart-0042`, and hover over it. The hover shows a 48-pixel colour preview, the name and description, the ID, category and tags, and **Open in Icon Library**.

Hovers work in HTML, CSS, SCSS, Less, Vue, Svelte, Astro, JavaScript, TypeScript, React JSX and TSX, JSON, JSONC, Markdown, PHP, Handlebars and XML. Turn them off with `auricIcons.library.hoverPreview`. When Drawn or Playful is also installed, each extension previews only its own icons, so you never see two hovers.

## Result

The icon is in your file, on your clipboard or saved as an `.svg` file, and it appears under **Recent**.
