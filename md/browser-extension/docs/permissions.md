---
title: Browser extension — Permissions
description: Every permission Auric Artisan asks for, when the browser asks, why each is needed, and how to review or revoke them.
product: Browser extension
updated: 2026-09-25
---

# Permissions

When you install Auric Artisan, the browser warns that it can "read and change your data on all websites". This page explains exactly what the extension declares, when each permission is asked for, and what it is used for.

## The short version

- The tools work on whatever page you use them on, so the extension needs access to all sites.
- A small script loads on each page and waits. Until you start a tool, it only reads your settings and listens for your commands. It does not read your content or change the page.
- Everything that changes a page, the website pickers and the custom right-click menu, is off until you turn it on.
- Three extra permissions are asked for only if you turn on the custom right-click menu.
- Nothing is sent anywhere. See [Privacy](../others/privacy.md).

## Asked for at install

| Permission | What the browser calls it | Why it is needed |
|---|---|---|
| Host access to all sites | Read and change your data on all websites | The page tools work on any page you choose; the optional pickers and menu must be ready before you use a page |
| `activeTab` | — | Access to the tab you are on when you use the popup, a shortcut or a menu item |
| `scripting` | — | Starts the page script in tabs opened before install, and runs the eyedropper in the page when needed |
| `storage` | — | Keeps your settings, history, library, snippets and pinned tools in your browser |
| `clipboardWrite` | — | The copy buttons: colour values, CSS, selectors and exports |
| `contextMenus` | — | Adds the extension's entries to the browser's own right-click menu (you can turn them off in Settings › Right-click) |
| `sidePanel` (Chromium only) | — | Docks the workspace in the side panel |

Firefox gets the same list without `sidePanel`. Its sidebar needs no permission. The Firefox package also declares to Mozilla that it collects no data.

## Asked for only when you turn on the custom right-click menu

When you turn on Settings › Right-click › **Custom right-click menu**, the browser asks for three optional permissions. If you decline, the menu stays off.

| Permission | Only for | Without it |
|---|---|---|
| `clipboardRead` (read the clipboard) | **Paste** in text fields | Paste shows an **Allow** chip |
| `downloads` (manage downloads) | **Save link as…**, **Save image as…**, **Save media as…** and **Save screenshot** | Those rows show an **Allow** chip |
| `sessions` (recently closed tabs) | **Reopen closed tab** | The row shows an **Allow** chip |

**Save page as…** works without `downloads`: it then saves the page's current HTML as a file instead of using the browser's Save dialog.

Nothing else in the extension asks for these. You can grant them one at a time in Settings › Right-click › **Permissions**.

## Where the page script does not run

- Browser pages (such as `chrome://` and `about:` pages) and the extension stores, where browsers forbid it.
- Frames inside a page: the script runs in the top page only.
- `file://` pages, unless you allow file access for the extension in the browser.

## Review or revoke permissions

- **Chromium browsers:** open the extensions page, choose **Details** on Auric Artisan, and review **Site access** and **Permissions**. You can limit site access, but the page tools then work only on the sites you allow.
- **Firefox:** open `about:addons`, choose Auric Artisan, then the **Permissions** tab.

Revoking an optional permission turns the matching right-click actions back to **Allow** chips.

## Related pages

- [Privacy](../others/privacy.md)
- [Right-click settings](settings/right-click.md)
- The extension privacy policy: https://auricartisan.com/legal/extension-privacy/
