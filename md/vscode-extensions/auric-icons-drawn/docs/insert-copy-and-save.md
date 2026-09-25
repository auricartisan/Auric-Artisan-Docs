---
title: Auric Icons: Drawn — Insert, copy and save icons
description: Insert Drawn icons with language-aware output, copy them in nine formats, save SVG files, open the source and preview icon IDs on hover.
product: VS Code extensions › Auric Icons: Drawn
updated: 2026-09-25
---

# Insert, copy and save icons

## Insert from the library

1. Open a file and place one or more cursors, or select text to replace.
2. Select **Insert** on a card.
3. The icon is inserted at every cursor; multi-line output keeps the cursor line's indentation.

Without an open text editor you see "Open a text editor before inserting an SVG."

## Smart insert

With `auricIconsDrawn.library.smartInsert` on (the default), **Insert** adapts to the file:

| Editing in | Output |
| --- | --- |
| JavaScript, TypeScript, React JSX and TSX, MDX | JSX element |
| HTML, PHP, Handlebars, Vue, Svelte, Astro | HTML markup (the SVG) |
| Markdown | Markdown image |
| CSS, SCSS, Less | CSS background |
| JSON, JSONC, YAML, Python | Data URI |
| XML, SVG and any other language | Raw SVG |

With the setting off, **Insert** uses raw SVG. **Smart Insert Icon** always adapts.

From the keyboard: press `Ctrl` + `Alt` + `I` (`Cmd` + `Alt` + `I` on macOS) in a text editor, search, and choose an icon. With no search text the list starts with **Recommended for this file**.

## Copy in a chosen format

Run **Auric Icons: Drawn: Copy Icon As… (JSX, CSS, Markdown, Data URI, Image tag)**, choose an icon and a format:

| Format | What you get |
| --- | --- |
| Raw SVG | The SVG markup. |
| JSX element | The SVG with JSX attribute names. |
| React component | `export function IconName(props) { return (<svg {...props} …>); }` |
| Markdown image | `![Icon name](data:image/svg+xml,…)` |
| CSS background | `background-image: url("data:image/svg+xml,…");` plus no-repeat and contain sizing |
| Data URI | `data:image/svg+xml,…` |
| Image tag (self-contained) | `<img src="data:image/svg+xml,…" alt="Icon name" width="24" height="24">` |
| Icon name | The icon ID, such as `files-blank-document-drawn-0001`. |
| Catalog path | The icon's relative path in the catalog. |

On a card, **Copy** copies raw SVG, **JSX** a JSX element and **URI** a data URI.

## Save and open the source

- **Save** on a card, or **Save SVG As…**, opens a save dialog in your first workspace folder (or home folder) with the icon's file name. Select **Save icon**.
- The artwork, **Source** on a card, or **Open SVG Source** opens the SVG in a preview tab.

## Other commands

| Command | What it does |
| --- | --- |
| **Search Icons** | Choose an icon, then **Smart Insert (matches this file)**, **Insert SVG at Cursor**, **Copy SVG**, **Save SVG As…**, **Open SVG Source** or **Toggle Like**. |
| **Insert SVG at Cursor** | Choose and insert (smart insert applies when on). |
| **Copy SVG** | Choose and copy raw SVG. |
| **Insert from Likes** | Choose a liked icon and insert. |
| **Insert from Recent** | Choose a recent icon and insert. Also `Ctrl` + `Alt` + `R`. |
| **Toggle Like for an Icon** | Like or unlike an icon. |
| **Clear Likes, Recents and Learned Recommendations** | Confirm with **Clear** to reset. |

## Hover previews

Hover over a Drawn icon ID, such as `files-blank-document-drawn-0001`, in HTML, CSS, SCSS, Less, Vue, Svelte, Astro, JavaScript, TypeScript, React JSX and TSX, JSON, JSONC, Markdown, PHP, Handlebars or XML. The hover shows a 48-pixel colour preview, the name and description, ID, category and tags, and **Open in Icon Library**. Turn it off with `auricIconsDrawn.library.hoverPreview`.

## Result

The icon is in your file, on your clipboard or saved as an `.svg` file, and it appears under **Recent**.
