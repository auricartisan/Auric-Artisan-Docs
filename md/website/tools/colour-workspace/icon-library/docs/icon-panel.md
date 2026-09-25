---
title: Icon Library — The icon panel
description: Preview an icon large, switch its style, size, colour and stroke, copy it as SVG, JSX, a data URI or a CDN tag, download it, and read its details.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# The icon panel

Selecting an icon opens it in a panel.

## Where the panel sits

- **On a wide screen** (wider than about 1,180 pixels), the panel docks to the right edge as a column of the page. Nothing is covered, and selecting another icon shows that one instead.
  - Drag the grip on the panel's left edge to resize it (380 to 720 pixels; 460 at first). Double-click the grip to go back to 460. With the grip focused, `←` and `→` resize it, faster with `Shift`. The width is remembered.
- **On a narrower screen**, the panel is a sheet from the bottom at about 62% of the screen. Drag the grip up to open it to 94%, or down to close it. Tapping the dimmed page closes it.

Close the panel with **✕** or `Esc`.

## The header

- The icon's name, and a line with its set, licence, category (Tabler and Remix only) and number of styles.
- **＋ Select** adds the icon to **Your kit**; it then reads **✓ Selected**. See [Your kit and export](kit-and-export.md).
- **Download .svg** downloads the icon in the style the grid is showing, as it comes from the set, without your panel colour or stroke. Use **Download .svg** among the copy buttons for a restyled file.

## Preview controls

A large preview sits beside the controls. Changing these affects the preview; colour and stroke also change the code below.

| Control | Range | Notes |
| --- | --- | --- |
| **Style** | The icon's styles | Only when it has more than one. Switches the preview, code and copy buttons to that style. |
| **Size** | 16 to 160 px | Starts at the grid size. Changes the preview only. |
| **Color** | Any colour | The picker starts at the grid colour, or near-black; until you pick, the preview follows the text colour. **currentColor** goes back to that. |
| **Stroke** | 0.5 to 3 | Only for outline sets (Tabler, Lucide, Heroicons, Feather). Starts at the grid stroke. |

## Copy and download

| Button | What you get | Message |
| --- | --- | --- |
| **Copy SVG** | The SVG markup with your colour and stroke | **SVG copied** |
| **Copy JSX** | A React component named after the icon, passing props to the SVG | **JSX copied** |
| **Copy data-URI** | An `<img>` tag whose source is the SVG as a data URI, sized to the grid size | **data-URI copied** |
| **Copy CDN tag** | An `<i data-icon="set:name">` tag and the Icon CDN script that fills it | **CDN tag copied** |
| **Download .svg** | An SVG file named after the icon and style, with your colour and stroke | none |

The icons use `currentColor`, so without a chosen colour they take the colour of the text around them. Picking a colour replaces `currentColor` with that colour in the copied code.

## The code blocks

Under the preview, four blocks show the code in full, each with its own **Copy** (message **Copied**):

- **SVG**;
- **JSX / React**: `export const IconName = (props) => (…);`;
- **`<img>` data-URI**;
- **CDN (auto-inject)**: the tag with a `data-style` attribute when the style is not the set's default, and the loader script.

The blocks update when you change the colour or stroke.

For how the CDN tag and loader work, see [Icon CDN: embed an icon](../../../../../services/icon-cdn/docs/embed-an-icon.md).

## Details

At the foot of the panel: **Set** (linked to the set's own website), **License**, **Author**, **Category** and **Keywords** when the icon has them, and **Path**, which says which set and style the icon comes from.

## Material icons

Material icons are served as a webfont, so the panel works differently for them:

- the copy buttons are **Copy glyph**, which copies the icon's HTML character reference such as `&#xe88a;` (message **Glyph entity copied**), and **Copy CDN tag**;
- the code blocks are **HTML (CDN)**, a tag and the loader script, and **Webfont @font-face**, a rule for the Material font of that style with a class to apply it;
- **Download .svg** shows **Material is a webfont — use the embed code** instead of downloading;
- there is no stroke control.

## Related

- [Your kit and export](kit-and-export.md)
- [Icon CDN: style, size and colour](../../../../../services/icon-cdn/docs/style-size-and-colour.md)
- [Browse, search and filter](browse-and-filter.md)
