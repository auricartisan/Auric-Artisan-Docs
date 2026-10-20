---
title: Browser extension — Right-click settings
description: Turn the custom right-click menu on or off, let sites keep their own menus, control the browser menu entries, and set the quick bar, layout, row height, excluded sites and permissions.
product: Browser extension › Settings
updated: 2026-09-25
---

# Right-click settings

Settings › **Right-click** controls both the extension's custom right-click menu and its entries in the browser's own menu. How the menu works is in [Right-click menu](../on-websites/right-click-menu.md).

## Switches

| Switch | Default | What it does |
|---|---|---|
| **Custom right-click menu** | Off | Replaces the browser's menu on websites. Asks for three optional permissions; if you decline, it stays off. |
| **Step aside for a site's own menu** | On | A page's own right-click menu (Figma, Google Docs) wins. Off: the extension's menu takes every right-click. |
| **Items in the browser's menu** | On | Adds entries to the browser's own menu; see [Browser menu items](../on-websites/browser-menu-items.md) |

## Quick bar

The actions pinned across the top of the menu, with a count such as "5 / 6". "One-click actions across the top of the menu. Pin more with the star on any row."

- Remove one with its **✕** (**Unpin**).
- **Reset** restores the defaults: Back, Forward, Reload, Copy page URL and Copy screenshot.

When the bar is empty it reads "Empty: pin actions with the star".

## Menu layout

| Choice | Effect |
|---|---|
| **Focused** (the default) | What you clicked, then one row per group |
| **Everything** | Every group opened in one list |

## Row height

**Standard** (the default) or **Compact**.

## Never on

Sites where the browser's own menu always stays. Add and remove sites as in the Pickers list: type a site, choose **Add**, and remove it with **✕**. The message confirms "The browser's menu stays on example.com". Subdomains are included, the list holds up to 100 sites, and **auricartisan.com** is always on it ("has its own menu").

## Permissions

The three optional permissions, each marked **Allowed** or with an **Allow** button:

| Row | Permission | Needed for |
|---|---|---|
| **Paste** | clipboard | Paste in text fields |
| **Save as…** | downloads | Save link, image, media and screenshot through the browser's Save dialog |
| **Reopen closed tab** | sessions | Reopen closed tab |

"Asked for only for these three actions. Everything else in the menu needs none." To take a permission back, use the browser's extension details page. See [Permissions](../permissions.md).

## The menu's own gear

The gear in the menu's footer offers the quick bar, layout and row height too. Changes made in either place apply in both.

## Related pages

- [Right-click menu](../on-websites/right-click-menu.md)
- [For site owners](../on-websites/for-site-owners.md)
