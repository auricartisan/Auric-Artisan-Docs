---
title: Use Auric Artisan extensions in Cursor, Windsurf, VSCodium and other editors
description: Install the Auric Artisan VS Code extensions in editors built on VS Code that use a different extension gallery.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Cursor, Windsurf, VSCodium and other editors

Several editors are built from the VS Code source code. People call them *forks*. Cursor, Windsurf and VSCodium are common examples. They run most VS Code extensions, but many of them search a different extension gallery, usually Open VSX, instead of the Visual Studio Marketplace.

The Auric Artisan extensions are published only on the Visual Studio Marketplace. They are not on Open VSX, so a search inside one of these editors may find nothing. The extensions still work in forks that keep VS Code's extension, colour theme and icon theme interfaces; you install them from a VSIX file.

## Install in a fork

1. **Find the VS Code version your editor is based on.** Open the editor's **About** dialog. Most forks show a VS Code version there. Compare it with the extension's minimum in the [reference](reference.md).
2. **Download the VSIX** of the extension you want from the Marketplace, as described in [Install from a VSIX file](install-from-vsix.md). If you want a pack, download each member instead; see [The two extension packs](extension-packs.md).
3. **Install it** in the editor:
   - Command Palette › **Extensions: Install from VSIX…**, or
   - the Extensions view's **…** menu › **Install from VSIX…**, or
   - the editor's own command-line launcher, if it has one, with `--install-extension <file>.vsix`. Cursor installs a `cursor` launcher, Windsurf a `windsurf` launcher and VSCodium a `codium` launcher; the flags are the same as VS Code's.
4. **Reload** the window if asked, then check the Command Palette for the extension's commands.

## Keeping extensions up to date in a fork

An editor that cannot reach the Visual Studio Marketplace cannot tell when a new version is published. To update:

1. Check the extension's page on the Marketplace or its release notes (each extension's folder in these docs has release notes).
2. Download the new version's VSIX.
3. Install it over the old one. The new version replaces the old one.

## What to expect

- **Themes and icon themes** work in forks that keep VS Code's colour theme and file icon theme support.
- **Webview panels** (for example Formatter Studio, the Font Hub studio or the Auric Live control panel) depend on the fork supporting VS Code webviews. Most do.
- **Minimum version.** If the fork's VS Code base is older than the extension's minimum, installation fails with a compatibility message. Use an older version of the extension, if one exists for your base version, or update the editor.
- **Keyboard shortcuts.** A fork may already use a shortcut that an Auric extension declares, for example `Ctrl` + `K` combinations or `Ctrl` + `Alt` combinations. Check **Preferences: Open Keyboard Shortcuts** for conflicts and rebind as needed.

## Support

Auric Artisan describes the extensions as working in forks that preserve the VS Code interfaces they use; each fork is not separately certified. If something behaves differently in a fork than in VS Code, report it with the editor's name and version. See [Get support](get-support.md).

When the install succeeds, the extension is listed as installed in the editor's Extensions view and its commands appear in the Command Palette.
