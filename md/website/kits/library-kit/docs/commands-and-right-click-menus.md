---
title: Library Kit — Commands and right-click menus
description: Run any Library Kit action from the > command palette or from the right-click menus for items and for the panel.
product: Website › Kits › Library Kit
updated: 2026-09-25
---

# Commands and right-click menus

Two shortcuts put every Library Kit action within reach: a command palette in the search box, and right-click menus.

## The command palette

1. Select the search box.
2. Type `>`. The tiles are replaced by a list of commands, each with a short hint.
3. Type more to narrow the list, for example `> export`. Commands match on their name or hint.
4. Press `Up arrow` or `Down arrow` to move the highlight, and `Enter` to run the command, or select it with the pointer.

The search box clears when a command runs. If nothing matches you see **No matching command** — "Type part of a command name, or clear the > to search items instead."

### Commands

| Command | Hint shown |
|---|---|
| **New project** | Bundle several saved items into one project |
| **New collection** | Group saved items into a folder |
| **Import library file** | Merge a previously exported .json |
| **Export library snapshot** | Download everything as a single .json |
| **Sync now** | Push to every configured destination |
| **Library settings** | Storage, sync, defaults and data controls |
| **Compare items** | Open two saved items side by side |
| **Switch to list view** or **Switch to grid view** | Change how items are laid out |
| **Group by type** or **Stop grouping by type** | Collapsible sections per asset type |
| **Compact density** or **Comfortable density** | Fit more items on screen |
| **Multi-select items** or **Leave multi-select** | Act on several items at once |
| **Show archived items** or **Hide archived items** | Include archived items in normal views |
| **Empty the archive** | Permanently delete every archived item |
| **Show favorites** | Jump to the starred items |
| **Show archive** | Items you archived rather than deleted |
| **Browse collections** | Folders that group saved items |
| **Keyboard shortcuts** | Every key the panel understands |
| **Clear filters** | Back to every item, unfiltered |
| **Filter:** and a tool name | The number of items saved from that tool (up to 8 tools) |
| **Filter: #** and a tag | The number of items with that tag (up to 8 tags) |

Notes:

- **New project** creates an empty project item; see [Organise your library](organise-your-library.md).
- **Show archived items** changes the library preference; in the Library Kit, archived items remain on the **Archive** tab.
- **Group by type** moves grouping to the next setting in the Group button's cycle.

## Right-click an item

Right-click a tile. The menu is headed with the item's name, a strip of its colours if it has any, and a line with its type, tool and age.

| Group | Entries |
|---|---|
| **Open** | **Restore into its tool** (`Enter`), **Open details**, up to three **Open in** [tool] entries, **Compare with…** |
| **Organise** | **Favourite** or **Remove favourite**, **Rename…**, **Add to collection…**, **Duplicate**, **Archive** or **Restore from archive** |
| **Share & export** | **Copy N colours** (for items with colours), **Copy item name**, **Share a link…**, **Export JSON** |
| (below a line) | **Select this item**, **Delete** (`Del`) |

When several items are selected and you right-click one of them, the menu is headed **N selected** and offers **Favourite all**, **Archive all**, **Add all to collection…**, **Export all** and **Delete all**.

## Right-click the panel

Right-click empty space in the panel. The menu is headed **Library** with a line such as "12 items · 3 favourite · 2 collections".

| Group | Entries |
|---|---|
| **Create** | **New project**, **New collection**, **Import**, **Export all** |
| **View** | **Switch to list** or **Switch to grid**, **Multi-select items** or **Leave multi-select**, **Show archived** or **Hide archived**, **Clear search & filters** (disabled when nothing is filtered) |
| **Library** | **Sync now**, **Compare items…**, **Settings, sync & reports**, **Empty the archive** (disabled when the archive is empty) |

## How the menus behave

- Right-clicking inside a text box (such as the search box) shows your browser's normal menu, so copy and paste still work.
- The menu closes when you choose an entry, click elsewhere, press `Esc`, scroll or resize the window. `Esc` closes only the menu, not the panel.
- The menu follows the panel's light or dark theme.

## Keyboard shortcuts sheet

Select **Keys** in the footer, or run the **Keyboard shortcuts** command, to see:

| Keys | Action |
|---|---|
| Ctrl / ⌘ + Shift + L | Open or close the library |
| Esc | Clear the search, then close |
| ↑ ↓ ← → | Move between items |
| Enter | Restore the item into its tool |
| Delete | Delete the focused item |
| Ctrl / ⌘ + A | Select all (in multi-select) |
| Right-click | Full actions for an item or the panel |
| > … | Run a library command |

Close the sheet with its close button, `Esc`, or a click outside it.

## Related

- [Organise your library](organise-your-library.md)
- [Library Kit shortcuts](../others/shortcuts.md)
