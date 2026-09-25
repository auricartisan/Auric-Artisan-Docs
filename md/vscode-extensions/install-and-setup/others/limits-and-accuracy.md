---
title: Compatibility and limits of the Auric Artisan VS Code extensions
description: What the Auric Artisan extensions need from your editor and environment, and the boundaries to know before you install.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Compatibility and limits

## Editor versions

- The extensions need VS Code 1.74 or newer; some need 1.85 or 1.95. The [reference](../docs/reference.md) gives each minimum.
- A newer VS Code is always fine. The minimum is a floor, not a range.

## Editors other than VS Code

- The extensions are published only on the Visual Studio Marketplace. They are not on Open VSX.
- They work in forks that preserve VS Code's extension, colour theme and icon theme interfaces. Each fork is not separately certified.
- In a fork that cannot reach the Marketplace, updates and pack members must be installed by hand from VSIX files.
- The extensions are for desktop VS Code and compatible editors. They are not browser extensions.

## Where extensions run

VS Code can run an extension on your computer (the "UI" side) or next to the files (the "workspace" side, for example on a remote server over SSH or in a container).

- Font Hub, Icon Hub, Icon Studio, File Icons and Emoji can run on either side.
- Live, File System and Formatter run next to the workspace files.

## Remote and virtual workspaces

- **Auric Artisan Live** needs a real file system and a local port. It does not support virtual workspaces.
- **Auric Artisan File System** supports virtual workspaces with limits: no revealing in the operating system's file manager, no content hashing for duplicate detection and no native trash there. Remote file providers expose different capabilities.
- **Auric Artisan Formatter**, **Font Hub**, **Theme**, **File Icons**, **Emoji**, **Icon Studio** and **Icon Hub** declare support for virtual workspaces.

## Workspace trust

Live, File System and Formatter limit themselves in an untrusted folder. See [Settings, sync and workspace trust](../docs/settings-and-sync.md).

## Languages

- Auric Artisan Live, Theme and Emoji include Hindi. The other extensions use English.
- Even in Hindi, some technical text stays in English, and served web pages are never translated.

## Settings Sync

- Settings Sync carries user settings and the list of installed extensions.
- It does not carry workspace settings, project files or data an extension keeps in its own storage (favourites, recents, tags, history and similar).

## Versions in these pages

Version numbers in the reference were correct when written (24 September 2026). The Marketplace page and the **Version History** tab always show the current state.
