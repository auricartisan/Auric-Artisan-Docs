---
title: Auric Artisan File Icons — Insert icons into code
description: Insert or copy File Icons artwork as inline SVG, JSX, an HTML image or a CSS background from the Studio, a native picker or a code hover.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Insert icons into code

File Icon Studio lets you reuse the shipped file and folder artwork in your own code.

## Output formats

| Format | Setting value | Output |
| --- | --- | --- |
| Inline SVG | `svg` | A self-contained `<svg>` element, 24 × 24 by default. |
| JSX | `jsx` | The SVG with JSX-compatible attribute names. |
| HTML image | `img` | A 24 × 24 `<img>` with the SVG embedded as a data URI. |
| CSS background | `css` | A `background-image` declaration with the SVG embedded as a data URI. |

`auricFileIcons.insertFormat` sets the default format (`svg`) for the native picker and the Studio.

> **Note:** Code output always uses the shipped artwork of the chosen style. Your Explorer colour, saturation, brightness and opacity settings do not change exported code. Add meaningful alternative text when an icon conveys information.

## From the Library tab

1. Open a writable text file and place the cursor. The Studio's target line shows "Insert target · {file}".
2. In File Icon Studio, open **Library**.
3. Set **Artwork style** (**Facet**, **Playful** or **Modern**) and **Show** (**Files & folders**, **Files** or **Folders**).
4. Type in **Search icons** (placeholder "TypeScript, React, src…", up to 150 characters). Press `/` to jump to the search box.
5. Choose a **Code format**: **Inline SVG**, **JSX**, **HTML image** or **CSS background**.
6. Tick **Open folder artwork** to show folders in their open state.
7. Hover over or focus a card, then choose **Insert**. Choose **Copy** to use the clipboard instead.

Insertion replaces selected text, works at multiple cursors and is a single undo step. It does not save the file and adds no surrounding quotes. **Copy** works without an open editor.

The grid loads more cards as you scroll; use **Load more icons** if it appears.

### The inspector

Open a card's inspector to see the exact output before using it. The **Icon inspector** dialog shows a large preview, the card's hover token, the style, format and kind (for example "Facet · SVG · File icon"), and the generated code.

| Button | Action |
| --- | --- |
| **Insert into code** | Inserts the code at your selections. |
| **Copy code** | Copies the code. |
| **Copy hover token** | Copies a token such as `:icon-file-typescript:` for use with code hovers. |

## From the Command Palette or editor menu

1. In a writable editor, run **Auric Artisan File Icons: Insert Icon into Code…**, or right-click in the editor and choose it.
2. A picker titled **Insert a file or folder icon** lists icons of the active Auric style (Facet if another theme is active), with their tokens.
3. Choose one. It is inserted in your `insertFormat`.

## From a code hover

1. Type a complete token such as `:icon-file-typescript:` or `:icon-folder-src:`. Copy valid tokens from the inspector.
2. Hover over the token.
3. Choose **Insert SVG**, **Insert JSX** or **Insert IMG**.

Only that token is replaced, in one undo step. Hovering alone never changes your file.

- Hovers prefer the active Auric Explorer style, and use Facet when another theme is active. If the icon is not in that style, an available style is used.
- If the document changes, closes or becomes hidden before you choose, hover again for a fresh action.
- Turn hovers on or off with **Enable code hovers** on the Workspace tab or `auricFileIcons.hover.enabled`. VS Code's own editor hovers must also be enabled.

## Result

The artwork is in your code, in the format you chose, taken from the shipped style you selected.
