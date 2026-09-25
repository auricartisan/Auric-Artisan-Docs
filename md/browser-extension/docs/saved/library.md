---
title: Browser extension — Library
description: Save colours and palettes to the extension's library, reuse them, remove them and export them as JSON.
product: Browser extension › Saved
updated: 2026-09-25
---

# Library

The Library keeps the colours and palettes you choose to save. It is stored in your browser's extension storage and is not synced between devices.

## Add to the library

| From | Button | Adds |
|---|---|---|
| Picker | **Save to library** (the bookmark) | The current colour. If it is already there, the extension says so. |
| Page palette | **Save** | The whole palette |
| Image | **Save palette** | The image's colours |
| Harmony | **Save** | The harmony, labelled with its scheme |

The toolbar icon's badge shows how many colours are in the library.

## Use the library

Open Saved › **Library**. It has two sections.

### Colours

- **Click** a colour to copy it in the format set in Settings › Tools › **Copy colours as**.
- **Right-click** a colour, or focus it and press `Delete` or `Backspace`, to remove it.

"Nothing saved yet." appears while the section is empty.

### Palettes

- **Click** a palette to open it in Page palette, where every export is available.
- Choose its **✕** to delete it.

"No saved palettes." appears while the section is empty.

## Export

**Export** copies the whole library as JSON, with a `colors` list and a `palettes` list:

```json
{
  "colors": ["#d3af37"],
  "palettes": [{ "id": 1790000000000, "colors": ["#d3af37", "#1a73e8"], "label": "triadic" }]
}
```

To keep the library with your settings, history and snippets in one file, use Settings › Data › **Download a backup**.

## Limits

| What | Limit |
|---|---|
| Colours | 500 |
| Palettes | The newest 30 are kept when you save; a restored backup can hold up to 100 |
| Colours in a palette | 64 in a restored backup |

## Clear it

Settings › Data › **Clear history & library** removes all colours, palettes and your history, after you confirm. Snippets are kept.

## Related pages

- [History](history.md)
- [Data settings](../settings/data.md)
