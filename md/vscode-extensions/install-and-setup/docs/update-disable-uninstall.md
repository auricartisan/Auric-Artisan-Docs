---
title: Update, disable and uninstall Auric Artisan extensions
description: Keep Auric Artisan extensions up to date, install a specific version, switch an extension off, or remove it.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Update, disable and uninstall

These controls are part of VS Code itself and work the same way for every Auric Artisan extension.

## Updates

VS Code checks the Marketplace for new versions and, by default, updates installed extensions automatically.

- **See pending updates.** In the Extensions view, an extension with an update available shows an **Update** button. The view's **…** menu has **Check for Extension Updates**.
- **Control automatic updates.** The VS Code setting `extensions.autoUpdate` decides whether updates install on their own. You can also switch auto-update on or off for one extension: right-click it in the Extensions view and choose **Auto Update** (the exact wording depends on your VS Code version).
- **Read what changed.** The **Changelog** tab on an extension's page shows its release notes. Each extension's folder in these docs has a user-facing release-notes page.

### Install a specific version

Use this to stay on a version you know, or to go back after an update.

1. In the Extensions view, right-click the extension (or use the gear on its page).
2. Choose **Install Specific Version…**.
3. Pick the version from the list.
4. Reload the window if asked.

From a terminal:

```text
code --install-extension auric-artisan.auric-artisan-live@0.2.0
```

After installing an older version, turn off automatic updates for that extension, or VS Code will update it again.

## Disable

Disabling keeps the extension installed but stops it running. Its settings are kept.

1. In the Extensions view, select the extension.
2. Select **Disable**, or open the drop-down next to it and choose **Disable (Workspace)** to switch it off only for the folder you have open.

A disabled extension contributes no commands, views, themes or icon themes until you select **Enable** again.

Two situations where disabling matters:

- **Moving from the old Font Library to Font Hub.** Font Hub replaces an earlier extension called Font Library, which has a different ID. Disable or uninstall the old one before enabling Font Hub, otherwise you see duplicate commands and views.
- **Keeping part of a pack.** Disable any pack member you do not use. See [The two extension packs](extension-packs.md).

## Uninstall

1. In the Extensions view, select the extension.
2. Select **Uninstall**.
3. Reload the window if VS Code asks.

From a terminal:

```text
code --uninstall-extension auric-artisan.auric-artisan-live
```

### What uninstalling leaves behind

Uninstalling removes the extension's code. Some things it created stay where they are, because they belong to you or to VS Code:

- **Your settings.** Values you set, such as `auricLive.port`, stay in your `settings.json` files. VS Code shows them as unknown settings; you can delete them.
- **Files in your project.** Files you created with an extension stay. For example: `auric.live.json`, `.auricignore-live` and the `.auric-live/` session folder from Auric Artisan Live; `.auric/templates/` and the `.auric/trash/` workspace trash from Auric Artisan File System; `.auricformatrc` and `.auricformatignore` from Auric Artisan Formatter. Before uninstalling File System, restore anything you still need from its workspace trash.
- **Workspace settings an extension wrote for you.** For example, **Auric Formatter: Toggle Format on Save** writes `editor.defaultFormatter` and `editor.formatOnSave`, and File System's sort and exclusion commands write `explorer.sortOrder` and `files.exclude`. Review your workspace settings after removing those extensions.
- **Extension storage.** Favourites, recents and similar per-extension data live in VS Code's extension storage, which VS Code manages.

When you have finished, the extension no longer appears under **Installed**, and its commands are gone from the Command Palette.
