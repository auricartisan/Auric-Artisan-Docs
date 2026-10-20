---
title: Auric Artisan File System — FAQ
description: Short answers to common questions about Auric Artisan File System.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# FAQ

## Does it replace the VS Code Explorer?

No. VS Code's Explorer stays as it is. Auric Files adds a companion section, a workspace panel, menus and commands around it.

## Does it change my files when I tag or group them?

No. Tags, groups, virtual folders, favourites, pins, highlights, filters and profiles are stored in VS Code's storage for the workspace. Only file operations (create, rename, move, copy, duplicate, convert, delete) change files, and **Toggle Native Explorer Exclusion** changes the `files.exclude` setting.

## Is anything uploaded?

No. Everything runs locally and no account is needed. Links to the Auric Artisan website and support open in your browser only when you choose them.

## Can I undo a batch rename?

Yes. **Undo Last File Operation** reverses the whole batch in one step.

## Where do deleted files go?

To `.auric/trash` in your workspace, unless you use **Delete Permanently** or turn off the workspace trash. Restore them with **Restore from Trash…** within the retention period (14 days by default).

## Should I commit `.auric/`?

The trash lives in `.auric/trash`, and templates you share can live in `.auric/templates`. You may want to commit shared templates and keep the trash out of version control by adding `.auric/trash/` to `.gitignore`.

## Do tags follow a file when I rename it?

Yes, when you rename or move it with Auric Files. Changes made outside Auric Files may leave organisation data pointing at the old path.

## Does Export Selected Items zip my files?

No. It writes a JSON manifest of paths and metadata, not the files' contents.

## Why is folder size shown as "Folder"?

Properties shows what the file system reports. A recursive disk-usage total is not calculated.

## Does it work over Remote SSH, in WSL or in virtual workspaces?

It runs next to the workspace files. In virtual workspaces browsing, scaffolding, renaming and moving work, but revealing in the operating system's file manager, content hashing and the native trash do not. What is available depends on the file system provider.

## Why do most shortcuts not work?

The full shortcut deck is off by default so it does not claim `Ctrl` + `Alt` combinations. Turn on `auricFiles.keyboard.enableDefaultShortcuts`.

## Is the interface available in Hindi?

Not at present; the interface is in English.

## Do I need the Auric icon themes?

No. The **Icon tools** section only works with the Auric Artisan File Icons Facet or Playful theme, which is an optional, separate extension.
