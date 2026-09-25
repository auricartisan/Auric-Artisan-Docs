---
title: FAQ — installing and setting up Auric Artisan extensions
description: Short answers to common questions about installing, updating and configuring the Auric Artisan VS Code extensions.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# FAQ

## Do I have to install all seventeen extensions?

No. Each extension works on its own. Two packs install a set in one step: the Icon Pack (Modern, Drawn, Playful and Emoji) and the Studio Full Pack (Color, Accessibility and Code Health).

## Are the extensions free?

Yes. Every Auric Artisan extension is listed as free on the Marketplace, and none needs an Auric Artisan account. Each has its own licence; read it on the extension's Marketplace page before redistributing anything.

## Which VS Code version do I need?

It depends on the extension, from 1.74 up to 1.95. The [reference](reference.md) lists each one. If you keep VS Code up to date, all seventeen work.

## Do they work in Cursor, Windsurf or VSCodium?

Yes, in forks that keep VS Code's extension, colour theme and icon theme interfaces. Those editors usually search Open VSX, where the Auric extensions are not published, so you install from a VSIX file. See [Cursor, Windsurf, VSCodium and other editors](forks-and-other-editors.md).

## How do I install the same set on every machine?

Turn on VS Code Settings Sync, or run the `code --install-extension` lines from [Install from the command line](install-from-command-line.md) on each machine. For a project, list the IDs in `.vscode/extensions.json` so VS Code recommends them to everyone.

## Do the extensions update themselves?

In VS Code, yes, unless you turn automatic updates off. In an editor that cannot reach the Marketplace, you install each new VSIX yourself.

## How do I go back to an earlier version?

In the Extensions view, right-click the extension and choose **Install Specific Version…**, or run `code --install-extension <id>@<version>`. Then turn off automatic updates for that extension.

## Can I share my settings with my team?

Yes, for settings with window or resource scope: commit them in `.vscode/settings.json`. Live, Formatter and File System also read project files you can commit. Settings with application scope stay personal. See [Settings, sync and workspace trust](settings-and-sync.md).

## Can I use the extensions in Hindi?

Auric Artisan Live, Theme and Emoji include Hindi. See [Use an extension in Hindi](display-language-hindi.md).

## Do the extensions send data anywhere?

Most work entirely on your machine. Font Hub and Icon Hub use the network to fetch their catalogues and assets, and Live runs a local server that other devices on your network can reach if you allow it. See [Privacy](../others/privacy.md).

## What happens to my files if I uninstall?

Files you created stay. Uninstalling removes the extension's code, not your project files, your settings or any workspace trash. See [Update, disable and uninstall](update-disable-uninstall.md).

## Where do I report a bug?

Use https://auricartisan.com/company/contact/ and include the details listed in [Get support](get-support.md).
