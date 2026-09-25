---
title: Icon Library — Your kit and export
description: Select icons into Your kit, and take them away as a ZIP of SVG files or a single SVG sprite.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Your kit and export

Icons you select gather in **Your kit**. The kit is kept in your browser on this device, so it is still there next time.

## Select icons

Open an icon and select **＋ Select** in its panel; it turns to **✓ Selected**, and the icon's tile in the grid is marked as selected. Select the button again to remove it.

Each icon is kept in the style the grid was showing when you selected it. To keep a different style, switch the style in the rail first.

## The Your kit tray

Once something is selected, a **Your kit** button with a count appears. Select it to open or close the tray: **Your kit** with the count and *Kept in this browser*, a list of your icons with a small preview, name and set (each with **✕** to remove it), and three buttons:

| Button | What it does | Message |
| --- | --- | --- |
| **Download ZIP** | Downloads all your icons as SVG files | **Downloaded** *n* **icons** |
| **Copy sprite** | Copies one SVG sprite containing all your icons | **SVG sprite copied** |
| **Clear** | Empties the kit | none |

**Hide** closes the tray. **Download selected** at the foot of the rail does the same as **Download ZIP** and shows the count, for example **Download selected (5)**; it is disabled while the kit is empty. With an empty kit, the messages read **Select some icons first**.

## The ZIP

The file is `auric-icons.zip`. Inside:

- a folder per set, holding one SVG per icon named after the icon and style, for example `lucide/bell-regular.svg`;
- `README.txt`, noting the number of icons and that each uses `currentColor` for fill or stroke, so you set the colour with CSS and the size with `width` and `height` or CSS.

The files are the icons as they come from their sets, without the size, stroke or colour you previewed. For a restyled single icon, use **Download .svg** or **Copy SVG** in the icon panel.

Material icons are a webfont, so each one appears in the ZIP as a short text note under `material/` giving its character reference, not as an SVG.

## The SVG sprite

**Copy sprite** copies a hidden `<svg>` block with one `<symbol>` per icon, each with the icon's identifier as its `id`, followed by a comment showing how to use it:

```html
<svg><use href="#lucide-bell"/></svg>
```

Paste the sprite once near the top of your page, then show any icon with a `<use>` that points at its identifier. Material icons are left out of the sprite.

## Related

- [The icon panel](icon-panel.md)
- [Icon CDN: export and self-host](../../../../../services/icon-cdn/docs/export-and-self-host.md)
- [Privacy](../others/privacy.md)
