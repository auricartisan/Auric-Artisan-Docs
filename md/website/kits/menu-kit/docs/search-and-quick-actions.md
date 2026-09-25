---
title: Menu Kit — Search and quick actions
description: Search every page in the Menu Kit with forgiving matching, and run quick actions such as copying the page URL.
product: Website › Kits › Menu Kit
updated: 2026-09-25
---

# Search and quick actions

Typing in the Menu Kit's search box turns the menu into a ranked list of results, like a command palette. Results include pages from every tab and a set of quick actions.

## Search for a page

1. Open the Menu Kit. The cursor is already in **Search Auric Artisan…**. If it is not, press `/` or select the box.
2. Type a few letters, for example `gamut`.
3. The tiles are replaced by a list of up to 16 results, and a count such as **4 results** appears.
4. Press `Up arrow` or `Down arrow` to highlight a result, or move the pointer over it.
5. Press `Enter`, or select the result, to open it.

The kit closes and the page opens. If you pick the page you are already on, the kit just closes.

Each result shows the page's illustration or icon, its name, the section it belongs to, and **Open ↵** on the right.

## How matching works

- **Letters in order.** A result matches if the letters you type appear in its name in the same order, with anything in between. `clrlib` matches **Color Library**, and `tmap` matches **Tone Mapping**.
- **Section names count.** If the name alone does not match, the section and name together are tried, so `legal priv` finds **Privacy** in **Legal and Security**.
- **Descriptions count.** If neither matches, a page whose description contains your exact text still appears, lower down.
- **Ranking.** Matches at the start of words and runs of consecutive letters rank higher, tighter matches rank higher, name matches beat description matches, and pages you open often get a boost.
- **Mode.** Search respects the tool visibility mode, so tools hidden by the [Advanced Kit](../../advanced-kit/README.md) do not appear.
- **One result per page.** A page listed in several sections appears once.

When nothing matches, the list reads **No matches for** and your search in quotation marks.

## Quick actions

Quick actions appear in the same list when your search matches their name. They show **Action ↵** on the right.

| Action | Description shown | What it does |
|---|---|---|
| **Copy current URL** | Copy this page's link to the clipboard | Copies the address of the page you are on |
| **Scroll to top** | Jump to the top of the page | Scrolls the page to the top |
| **Go home** | Open the Auric Artisan home page | Goes to https://auricartisan.com |
| **Go back** | Browser back | Goes back one page in your browser history |
| **Reload page** | Refresh the current page | Reloads the page |
| **Open a random tool** | Jump to a random tool | Opens a randomly chosen tool page from the menu |
| **Toggle menu theme** | Switch this menu light / dark | Switches the Menu Kit between light and dark |

For example, type `copy` and press `Enter` to copy the page's address. The kit closes before running the action.

## Clear the search

- Select the cross at the right of the search box.
- Or press `Esc` once. A second `Esc` closes the kit.

Clearing the search brings back the tabs and tiles.

## Search the whole site instead

The Menu Kit searches its own list of pages. To search the text of pages across the site, or the web, use the site-wide search: press `Ctrl` + `K`, or go to https://auricartisan.com/search/. See [Search](../../../search/README.md) and [Site features](../../../site-features/README.md).

> **Note:** The footer hint **Ctrl K Search** refers to that site-wide search. Pressing `Ctrl` + `K` while the Menu Kit is open opens the site-wide search. Use `/` to reach the Menu Kit's own search box.

## Related

- [Find a page](find-a-page.md)
- [Menu Kit shortcuts](../others/shortcuts.md)
