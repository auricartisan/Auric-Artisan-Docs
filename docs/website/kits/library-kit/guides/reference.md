---
title: Library Kit — Reference
description: Every control, tab, option, dialog and message in the Library Kit.
product: Website › Kits › Library Kit
updated: 2026-09-25
---

# Library Kit reference

## Ways to open the kit

| Entry point | What it does |
|---|---|
| **Library** launcher | Opens or closes the kit. Shows a badge with the item count (up to **99+**) once the kit has loaded |
| **Library** button in the site header | Opens the kit |
| `Ctrl` + `Shift` + `L` (`Cmd` + `Shift` + `L` on a Mac) | Opens or closes the kit |
| `#library` at the end of a page address | Opens the kit on that page |
| `#library=all`, `recent`, `favorites` (or `favourites`), `projects`, `collections`, `archive`, `compare`, `settings` | Opens the kit on that tab |
| https://auricartisan.com/library/workspace/ | Opens the kit; links to this page elsewhere on the site open the kit in place |

## Title bar

| Control | What it does | Default |
|---|---|---|
| Six-dot grip | Drag, or focus it and use arrow keys (12 px; `Shift` for 1 px), to move the panel ("Move library panel") | Bottom-left corner |
| **Your Library** | Title; the title bar is also a drag handle | — |
| Item count | **N items** (not counting archived items). Hidden on narrow phone screens | — |
| **Panel options** | Opens **Keep open**, **Theme**, **Panel size**, **Minimize**, **Reset position** | — |
| **Close** | Closes the kit ("Close Library Kit.") | — |

Panel size: normal 680 px wide, expanded up to 940 px wide.

## Tabs

**All**, **Recent** (last 7 days), **Favorites**, **Projects**, **Collections**, **Archive**, **Compare**, **Settings**, and one tab per saved item type. Counts show on all but **Compare** and **Settings**. Default: **All**; the last tab is remembered.

## Search and toolbar

| Control | What it does | Values | Default |
|---|---|---|---|
| **Search your library…** | Filters items by name, description, tool, type and tags; `>` switches to commands | Text | Empty |
| Clear (cross) | Clears the search | — | — |
| Item count | **N items in** [tab] | — | — |
| **Sort** | Order of items | **Newest**, **Oldest**, **Name A–Z**, **Name Z–A**, **Type** | **Newest** |
| **Group** | Cycles grouping | By project, by type, none | By project |
| **View** | Grid or list | Grid, list | Grid |
| **Select** | Multi-select on or off | — | Off |
| Filter chips | **Collection:**, **Tool:**, **Tag:** and **Clear all** | — | None |

## Tiles

| Part | Meaning |
|---|---|
| Preview | Image, gradient, up to 8 swatches, a text sample, or a coloured plate with initials |
| Star | A favourite |
| Tick box | Shown in multi-select |
| Name | The item's name, or **Untitled** |
| Meta line | Type, tool and age |
| Hover actions (grid) | **Favourite** or **Remove favourite**, **Open details**, **Share**, **Delete** |
| Hover actions (list) | The same plus **Duplicate** and **Export JSON** |

Select a tile to restore it; in multi-select, to select it. A tile's tooltip reads its name followed by "right-click for actions".

## Collections tab

| Tile | What it does |
|---|---|
| **New collection** ("Group saved items") | Creates a collection |
| A collection (name, **Collection**, item count) | Shows its items on the **All** tab |

With no collections: **No collections yet** — "Collections group saved items into folders. Create one above, or from any item's right-click menu."

## Bulk bar (multi-select)

**Pick items to act on them** or **N selected**, then **All**, **Favorite**, **Collect**, **Archive**, **Export**, **Delete**.

## Footer

| Control | What it does |
|---|---|
| **New project** | Creates an empty project item |
| **Import** | Merges a library `.json` file |
| **Export** | Downloads `auric-library-backup.json` |
| Storage figure | Space the library uses; tooltip gives the number of stored entries |
| **Settings** | Opens the **Settings** tab |
| **Keys** | Shows the keyboard shortcuts sheet |

## Dialogs

| Dialog | Fields and buttons |
|---|---|
| **Rename item** | **Name**; **Cancel**, **Rename** |
| **New collection** | **Collection name** (starts **Untitled collection**); **Cancel**, **Create** |
| **New project** | **Project name** (starts **Untitled project**); **Cancel**, **Create** |
| **Add to collection** (or **Add N items to collection**) | **New collection…**, each collection, **No collection** |
| **Delete item?** / **Delete N items?** / **Delete N archived items?** | **Cancel**, **Delete** |
| Item details | **Name**, **Description**, **Collection**, **Tags (comma-separated)**, **Use in** buttons, **Saved option values**, **Download PNG**, **Download SVG**, **Other format** and **Download**, **Open in tool**, **Cancel**, **Save changes** |
| **Share link** | Link, **Copy**, **Share via…** (where supported), **Open in new tab**, **Close** |
| **Keyboard shortcuts** | List of keys; close button |

In the text dialogs, `Enter` confirms and `Esc` cancels.

## Compare tab

**Before** and **After** pickers, **Swap sides**, per-side summaries and the comparison. Image comparisons offer **Side**, **Wipe** and **ΔE heatmap**. See [Compare items](compare-items.md).

## Settings tab

**Preferences**, **Reporting**, **Sync & auto-update**, **Generate reports**, **Storage**. See [Settings, sync and reports](settings-sync-and-reports.md) for every option and default.

## Messages

| Message | Meaning |
|---|---|
| **Nothing saved here yet** — "Save a palette, gradient, type scale or report from any tool and it lands here." | The current tab is empty |
| **Nothing matched** — "Try a different word, or clear the search to see everything." | A search found nothing |
| **Renamed** | An item was renamed |
| **Created** "[name]" | A collection was created |
| **Moved N items to** "[name]" / **Removed from its collection** | Collection changes |
| **N colours copied**, **Name copied** | Copy actions |
| **This item has no colours to copy.** | The item has no colours |
| **Could not copy to the clipboard.** | The browser blocked copying |
| **Library snapshot downloaded** | Export finished |
| **Imported** [file] / **That file could not be imported.** | Import result |
| **Archive emptied** | Archive emptied |
| **Library returned to its default position.** | Panel position reset |
| **That item could not be shared.**, **That project could not be created.** | An action failed |
| **Sync is switched off — turn it on in Library settings.**, **No sync destinations configured yet.**, **Synced to N destinations**, **Synced N of M destinations — check settings.**, **Sync could not complete.** | Sync results |
| **Library storage is full. Some image data couldn't be saved.** | The browser's storage for the site is full |
| **Settings could not be loaded.**, **Comparison could not be loaded.** | A part of the kit failed to load |
