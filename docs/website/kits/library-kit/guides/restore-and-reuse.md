---
title: Library Kit — Restore and reuse
description: Reopen saved items in the tool that made them, open them in other tools, edit their details and download them in many formats.
product: Website › Kits › Library Kit
updated: 2026-09-25
---

# Restore and reuse items

## Restore an item into its tool

Select a tile (or focus it and press `Enter`), or right-click it and choose **Restore into its tool**.

- If you are already on that tool's page, the item loads into the tool straight away and the Library Kit closes.
- If you are on another page, the site opens the tool's page and loads the item there.
- If the item cannot be restored into a tool, its details open instead.

## Open an item in a different tool

Many items can be used by more than one tool. For example, a palette saved in one tool can be opened in another tool that accepts palettes.

- Right-click the tile. Under **Open**, up to three entries read **Open in** followed by a tool's name.
- Or open the item's details: a **Use in** row lists every tool that accepts the item.

Selecting one opens that tool, on this page or another, with the item loaded.

## Open an item's details

Hover over the tile and select the pencil (**Open details**), or right-click and choose **Open details**. A details dialog opens over the page.

### What the details show

- The item's type above its name.
- A large preview: the image, the SVG, colour swatches with their values, the gradient or the colour. If there is nothing to preview you see **No image stored** with a hint.
- Editable fields: **Name**, **Description**, **Collection** (with **Unfiled** for none) and **Tags (comma-separated)**.
- The tool it came from, **Created** and **Updated** dates, and an **Open in tool** link when the item knows its tool page.
- **Use in** buttons for other tools that accept the item.
- **Saved option values**: a collapsible list of the tool settings saved with the item, up to 120 of them.

### Edit an item's details

1. Change the **Name**, **Description**, **Collection** or **Tags**.
2. Select **Save changes**.

Select **Cancel**, the close button, or press `Esc` to leave without saving.

### Download from the details

| Control | Downloads |
|---|---|
| **Download PNG** | The item's image as a file (PNG, or JPEG if that is how it was stored). Disabled when no image is stored |
| **Download SVG** | The item's vector image. Disabled when no SVG is stored |
| **Other format** list and **Download** | The item in the chosen format: **JSON (data + metadata)**, **NDJSON**, **CSV**, **XML**, **HTML**, **MD**, **TXT**, **PNG (image)** or **SVG (image)** |

Formats that the item cannot provide are marked **— unavailable**. File names are made from the item's name.

**Open in tool** in the footer restores the item into its tool, as above.

### Ishihara plates without an image

A plate saved without its image shows **No image stored**. If the plate's generation settings were saved, a **Re-render & save image** button rebuilds the image from them and stores it; the same seed produces the same plate. If the settings were not saved, an **Open Ishihara tool** link lets you save it again. To repair every such plate at once, use **Repair empty Ishihara plates** in [Settings](settings-sync-and-reports.md).

## Copy colours and names

Right-click a tile:

- **Copy 5 colours** (the number matches the item) copies its colour values separated by commas, such as `#1f2a44, #c79a3a`. It appears only for items with colours.
- **Copy item name** copies the name.

A message confirms, for example **5 colours copied**.

## Related

- [Share, export and import](share-export-and-import.md)
- [Compare items](compare-items.md)
- [Reference](reference.md)
