---
title: Auric Artisan File System — tags, groups and profiles
description: Organise files without moving them, with tags, groups, virtual folders, favourites, pins, highlights, Explorer exclusions, focus mode and workspace profiles.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Tags, groups and profiles

Auric Files lets you organise files by meaning rather than by folder. None of these tools moves or changes a file: they store labels about files. The labels follow a file when you rename or move it with Auric Files.

The commands are in the **Organise** group of the workspace panel and the **Auric Files** › **Organize** submenu.

## Where the organisation is stored

Tags, groups, virtual folders, flags, saved filters and profiles are kept in VS Code's storage for this workspace, on your machine. They are not written into your project, are not committed with it, and are not copied by Settings Sync. The one exception is **Toggle Native Explorer Exclusion**, which writes to the workspace's `files.exclude` setting.

## Tags

A *tag* is a named, coloured label you can put on any number of files.

### Create tags

1. Run **Auric Files: Manage Tags…**.
2. Choose **New tag…**.
3. Type the **Tag name**.
4. **Choose a colour**: gold, amber, orange, red, pink, purple, blue, teal, green or gray.

In **Manage Tags…** you can also choose an existing tag to **Rename** or **Delete** it.

### Tag files

1. Select files in the Explorer.
2. Run **Tag Files…** (`Ctrl` + `Alt` + `A`, then `G` with the deck), or choose **Edit tags…** in Properties.
3. Tick the tags to apply and untick any to remove. With no tags yet, the list says **No tags yet — create one from Manage Tags**.

A tagged file shows the first two letters of its first tag as a badge in the Explorer, and its hover names the tag. Filters can restrict results to tags; see [Search, filters and duplicates](search-filter-and-duplicates.md).

## Groups

A *group* is a named set of files and folders from anywhere in the workspace: a working set for a feature, a bug or a review.

- **Add to Group…** (`Ctrl` + `Alt` + `A`, then `K` with the deck) — add the selection to an existing group, or choose **New group…** and type a **Group name**.
- **Create Workspace from Selection** — create a group straight from the selection, named after the first item (with a number added if the name is taken). The message says **Created "*name*" with *N* linked items. Hover a member to see the workspace association.**
- **Manage Groups…** — choose a group, then **Rename**, **Delete** or **Open a member**.

Members of a group show a **W** badge in the Explorer, and Properties lists their groups.

## Virtual folders

A *virtual folder* gathers items under a name, and can sit inside another virtual folder, without moving anything on disk.

1. Run **New Virtual Folder…** from the panel's **Organise** group.
2. Type the **Folder name**.
3. Choose a parent: **(top level)** or an existing virtual folder.

Manage them in **Manage Groups…**, under **Virtual folders**.

## Favourites, pins, highlights and exclusions

| Command | Explorer badge | Deck shortcut |
| --- | --- | --- |
| **Toggle Favorite** | **★** | `Ctrl` + `Alt` + `A`, then `1` |
| **Toggle Pinned** | **P** | `Ctrl` + `Alt` + `A`, then `2` |
| **Toggle Native Explorer Exclusion** | **H** | `Ctrl` + `Alt` + `A`, then `3` |
| **Toggle Highlight** | **●** | `Ctrl` + `Alt` + `A`, then `4` |

Each toggles the flag on the selected items and reports, for example, **Added favorite on 3 items.**

**Toggle Native Explorer Exclusion** hides the item from VS Code's Explorer by adding it to the workspace's `files.exclude` setting (per folder in a multi-root workspace). Toggling again removes only the entries Auric Files added. To see hidden items again in Auric's own search and filters, turn on `auricFiles.explorer.showHiddenFiles`.

## Focus mode

*Focus mode* narrows Auric's indexed file lists to the paths you are working on.

1. Run **Auric Files: Toggle Focus Mode**.
2. **Focus Mode — choose paths**: pick the folders or files to focus on.
3. The indexed file list opens, limited to those paths: **Focused on *N* paths.**

Run the command again to switch it off (**Focus mode off.**). Focus mode affects Auric's lists; it does not change VS Code's own Explorer tree.

## Workspace profiles

A *profile* is a saved way of looking at the workspace: the sort, grouping, active filter, which folders are open, focus mode and the hidden list. It stores no file contents and no absolute paths, and switching profile never changes a file.

- **Save Workspace Profile…** — type a **Profile name**. **Saved the "*name*" profile.**
- **Switch Workspace Profile…** — choose a profile; the active one is marked **active**. With none saved: **No workspace profiles saved yet.**

## Remove organisation

- Remove a tag from files with **Tag Files…** (untick it), or delete the tag in **Manage Tags…**.
- Delete a group or virtual folder in **Manage Groups…**; the files themselves are untouched.
- Toggle a flag again to clear it.

When you tag or flag files, the Explorer badges update straight away, and Properties shows the tags and groups.
