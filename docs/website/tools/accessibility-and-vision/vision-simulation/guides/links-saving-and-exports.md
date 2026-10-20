---
title: Vision Lab — Links, saving and exports
description: Share a Vision Lab view as a link, see what the lab remembers in your browser, and export results.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Links, saving and exports

## Share a view as a link

| From | Button | What the link restores |
| --- | --- | --- |
| Workbench | **Copy link to this view** | The Workbench, on the same condition, severity and model |
| Catalogue bar | **Copy link** | The level, category, open panels (linked or pinned) and source-image settings |
| Compare | **Copy link to this sheet** | The Compare sheet |

The Catalogue link restores the whole workspace: the level filter, the active category, the open panels (and which are linked or pinned), and the source-image settings. The Analytics CSV has the columns slug, name, category, complexity, severity_score, description and prevalence. **Export all CVD** records the base colour at several severities for each colour-vision type.

### The Workbench link

A Workbench link has the form:

```text
https://auricartisan.com/tool/vision-simulation/?vw=deuteranopia:60:vienot
```

The value is the condition's short name, then optionally the severity from 0 to 100, then optionally the model (`brettel`, `vienot` or `machado`). Opening such a link always opens the Workbench, whatever view you used last.

### The workspace link

The Catalogue's link adds `#v=` and an encoded value to the address. The lab keeps that part of the address up to date as you work, without adding history entries, so the address bar always holds a link to your current workspace. Built-in samples and test charts travel with the link; an image of your own does not, because it never leaves your device.

## What the lab remembers in your browser

- the view you last used;
- the Workbench's condition, severity, model, specimen and base colour;
- the Catalogue category you last browsed, and your **Favourites**;
- the Compare sheet;
- the Palette audit palette;
- panel snapshots you saved, and the panels you had open;
- where you left the **Vision Control** dock;
- on the free plan, today's simulation count.

All of it stays in this browser. Clearing the site's data resets it.

## Exports

| Where | Control | What you get |
| --- | --- | --- |
| Analytics | **Export JSON** | The catalogue of conditions, as `vd-catalog-<date>.json` |
| Analytics | **Export CSV** | Severity data, as `vd-severity-<date>.csv` |
| Vision Control › More panel actions | **Export a comparison PNG** | An image of the open panels side by side, as `vision-comparison-<date and time>.png` |
| A colour-vision panel | **Export all CVD** | A JSON file of the base colour under each colour-vision type, ending `-all-cvds.json` |
| A panel | **Copy HEX** / **Copy CSS** | The reference hex, or CSS variables for the reference and simulated colours, on your clipboard |
| Palette audit | **Copy the palette** | Your palette's colours, on your clipboard |

Some condition panels have exports of their own. For example, the Metameric Failure panel can download a comparison CSV, a JSON of all conditions and a PNG grid.

## Save to your library

The site-wide **Save** button at the bottom right of the page saves the current output to your Auric Artisan library. See [Library Kit](../../../../kits/library-kit/README.md).
