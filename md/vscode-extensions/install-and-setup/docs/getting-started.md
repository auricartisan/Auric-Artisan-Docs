---
title: Install an Auric Artisan extension from the Extensions view
description: Find the right Auric Artisan extension in VS Code, install it, and confirm that it is working.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Install an extension from the Extensions view

The Extensions view is the panel inside VS Code where you search the Visual Studio Marketplace and install, update and manage extensions. This is the simplest way to install any Auric Artisan extension, and it needs a network connection to the Marketplace.

## Before you start

- **Check your VS Code version.** Open **Help** › **About** (on macOS, **Code** › **About Visual Studio Code**). Each extension states the lowest version it runs on. The lowest version across the family is 1.74; Auric Artisan Live and Auric Artisan File System need 1.95. The [reference](reference.md) lists every extension.
- **Open a folder if the extension works on a project.** Auric Artisan Live, File System and Formatter act on the folder you have open. The icon, theme and library extensions work without one.

## Install

1. Open the Extensions view: select the Extensions icon in the Activity Bar, or press `Ctrl` + `Shift` + `X`.
2. In the search box, type the extension ID with the `@id:` prefix. For example:

   ```text
   @id:auric-artisan.auric-artisan-live
   ```

   The `@id:` prefix returns exactly one extension. You can also type a name such as `Auric Artisan` and browse the results.
3. Remove any other filter from the search box, such as `@installed` or `@disabled`. A leftover filter hides extensions you have not installed yet.
4. Select the result. Check that the publisher shown under the name is **Auric Artisan** and that the identifier on the page matches the ID you searched for.
5. Select **Install**.
6. If VS Code shows a trust prompt for the publisher, read it and confirm.

When installation finishes, the **Install** button changes to **Disable** and **Uninstall** (or a settings gear), and the extension is active. Most Auric Artisan extensions do not need a restart.

## Check it worked

- **Command Palette.** Press `Ctrl` + `Shift` + `P` and type the extension's command prefix. Each extension groups its commands under a prefix, shown in the table below.
- **Activity Bar or Explorer.** Some extensions add their own icon to the Activity Bar (for example **Auric Live** and **Auric Font Hub**) or a section to the Explorer (for example **Auric Files** and **Auric Formatter**).
- **Features tab.** On the extension's page in the Extensions view, the **Features** tab lists every command, setting and keyboard shortcut the extension contributes.

| Extension | Command Palette prefix | Settings prefix |
| --- | --- | --- |
| Auric Artisan Live | `Auric Live` | `auricLive.` |
| Auric Artisan File System | `Auric Files` | `auricFiles.` |
| Auric Artisan Font Hub | `Auric Artisan Font Hub` (and `Auric Font Hub` for **Show Logs**) | `auricFontLib.` |
| Auric Artisan Formatter | `Auric Formatter` | `auricFormatter.` |
| Auric Artisan Theme | `Auric Theme` | `auricTheme.` |
| Auric Artisan File Icons | `Auric Artisan File Icons` | `auricFileIcons.` |
| Auric Icons: Modern | `Auric Icons: Modern` | `auricIcons.` |
| Auric Icons: Drawn | `Auric Icons: Drawn` | `auricIconsDrawn.` |
| Auric Icons: Playful | `Auric Icons: Playful` | `auricIconsPlayful.` |
| Auric Artisan Emoji | `Auric Artisan Emoji` | `auricEmoji.` |
| Auric Artisan Icon Studio | `Auric Icon Studio` | `auricIconStudio.` |
| Auric Artisan Icon Hub | `Auric Icon Hub` | `auricIconLib.` |
| Auric Color | `Auric Artisan` | `auricColor.` |
| Auric Accessibility | `Auric Artisan` | `auricA11y.` |
| Auric Code Health | `Auric Artisan` | `auricCodeHealth.` |

The two packs, Auric Artisan Icon Pack and Auric Artisan Studio — Full Pack, add no commands or settings of their own. See [The two extension packs](extension-packs.md).

## Install several at once

- Install a pack to get a set in one step. See [The two extension packs](extension-packs.md).
- Run several `code --install-extension` lines in a terminal. See [Install from the command line](install-from-command-line.md).
- Add the IDs to your repository's `.vscode/extensions.json` so VS Code recommends them to everyone who opens the project. See [Settings, sync and workspace trust](settings-and-sync.md).

## Next steps

- Configure the extension: [Settings, sync and workspace trust](settings-and-sync.md).
- Use it in Hindi, where supported: [Use an extension in Hindi](display-language-hindi.md).
- Learn the extension itself: open its folder from [Related extensions and pages](../others/related.md).

You should now see the extension listed under **Installed** in the Extensions view, and its commands in the Command Palette.
