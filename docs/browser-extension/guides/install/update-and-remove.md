---
title: Browser extension — Update and remove
description: How Auric Artisan updates, how to update a copy loaded from a ZIP, how to keep your data across a reinstall, and how to uninstall.
product: Browser extension › Install
updated: 2026-09-25
---

# Update and remove

## Updating

| How you installed | How it updates |
|---|---|
| Chrome Web Store (Chrome, Brave, Vivaldi, Arc, Edge, Opera) | Automatically. The store reviews each version before it ships. |
| Firefox Add-ons | Automatically, signed by Mozilla |
| ZIP, loaded unpacked in a Chromium browser | Manually: see below |
| ZIP, temporary add-on in Firefox | Load the newer package after each restart |
| Safari conversion | Convert and build the newer package |

### Update a copy loaded from a ZIP

1. Download the newer package from https://auricartisan.com/extension.
2. Replace the contents of the folder you loaded with the newly unzipped files. Keep the same folder location.
3. Open the browser's extensions page (`chrome://extensions`, `edge://extensions` or `opera://extensions`).
4. Choose the reload button on the Auric Artisan card.
5. Reload any tabs that were open before the update, so the page tools use the new version.

To check your version, look at the Auric Artisan card on the extensions page.

## Keep your data across a reinstall

Your settings, colour history, library and snippets live in the browser's extension storage. Removing the extension deletes them. Before you remove it, or before moving to another browser or computer:

1. Open **Settings** › **Data**.
2. Choose **Download a backup**. A file named `auric-artisan-backup-` followed by the date is saved.
3. After reinstalling, open **Settings** › **Data** › **Restore from a file** and choose that file.

See [Data settings](../settings/data.md) and [Back up and move your data](../workflows/back-up-and-move-your-data.md).

## Remove the extension

1. Open the browser's extensions page, or right-click the toolbar icon.
2. Choose **Remove** (in Firefox, **Remove Extension**).
3. Confirm.

Removing the extension deletes everything it stored in your browser. Nothing else is left behind: the extension never writes to websites' storage.

## Turn off parts instead of removing

If one feature is in the way, you can switch it off without uninstalling:

- the website pickers: Settings › Pickers › **Auric pickers on websites**;
- the custom right-click menu: Settings › Right-click › **Custom right-click menu**;
- the entries in the browser's own right-click menu: Settings › Right-click › **Items in the browser's menu**;
- a single site: add it to the **Never on** list in Settings › Pickers or Settings › Right-click.
