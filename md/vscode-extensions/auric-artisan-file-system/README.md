---
title: Auric Artisan File System — a file workspace for the VS Code Explorer
description: What Auric Artisan File System does, who it is for, how to install it and where to find every guide.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Auric Artisan File System

Auric Artisan File System adds a file workspace to the VS Code Explorer. It keeps VS Code's own Explorer, with its New File, New Folder, Rename and drag-and-drop, and adds the file work the Explorer does not do: creating whole project structures in one line, templates and framework presets, batch renaming with a preview, finding a file's test, style or story, tags, groups and profiles, a graphical **Properties** view, duplicate review, and a workspace trash you can restore from.

Its commands appear in the **Auric Files** section of the Explorer, in an editor-sized workspace panel, in an **Auric Files** submenu on Explorer and editor context menus, and in the Command Palette under **Auric Files**. There are 81 commands in seven groups: **Create**, **Inspect & navigate**, **Edit & batch**, **Organise**, **Find & filter**, **History & recovery** and **Workspace**.

Operations are guarded: paths are checked, protected files cannot be renamed, moved or deleted, collisions are planned before anything changes, bulk operations ask first, and every Auric operation is recorded so you can undo it. Everything runs locally; no account is needed.

## Who it is for

- Developers who create the same file patterns again and again: a component with its test, style and story.
- Anyone renaming or reorganising many files at once and wanting to see the result before it happens.
- People who work in large repositories and want tags, working groups and saved filters.
- Anyone who wants a safety net for deletes inside VS Code.

## Where to find it

- Marketplace ID: `auric-artisan.auric-artisan-file-system`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-file-system
- Install from a terminal:

  ```text
  code --install-extension auric-artisan.auric-artisan-file-system
  ```

- Requires VS Code 1.95 or newer. Version 0.1.0 at the time of writing. The interface is in English.

## Quick start

1. Install the extension and open a workspace folder.
2. In the Explorer, expand the **Auric Files** section, or run **Auric Files: Open File Workspace** for the larger editor panel.
3. Select a file in the Explorer or open one in the editor. The panel shows it as the **Selected resource**.
4. Type in **Find an action** (for example `rename` or `trash`), or open a group and choose an action.
5. Right-click a file in the Explorer and choose **File Properties** (or press `Alt` + `Enter` with the Explorer focused) to see its details.
6. Right-click and open the **Auric Files** submenu for grouped operations: **Create**, **Edit and Batch**, **Navigate and Paths**, **Organize**, **Safety and History** and **Sort**.
7. For a batch operation or a comparison, select several files in the Explorer first, then choose the action.
8. If something went wrong, run **Auric Files: Undo Last File Operation**.

## What you can do

- Create files and folders, nested paths, and whole structures with braces and ranges: `src/{Button,Card}/{index.ts,styles.css}`.
- Create from templates with variables, filters and conditions, or from ten framework presets: React, Vue, Angular, Svelte, Node.js, Python, Java, Go, Rust and Generic.
- Jump between a file and its test, style, story, component or documentation, and generate missing companions.
- Rename, move, copy, duplicate and convert extensions, one file or many, with a before-and-after preview.
- Compare two files, merge in VS Code's merge editor, and export a JSON manifest of a selection.
- Tag files, collect them into groups and virtual folders, mark favourites, pins and highlights, and save workspace profiles.
- Search with glob, regular expression or fuzzy matching, and filter by kind, tag, extension, path, size, date, flags and Git state.
- Find duplicate and empty files and move the ones you choose to the trash.
- Undo and redo Auric operations, review the history, and restore deleted items from the workspace trash.
- See a file's properties: name, path, type, size, dates, tags, groups, related files, permissions, Git status and history.

## In this folder

- [docs/](docs/README.md) — task guides and the full reference.
  - [Getting started](docs/getting-started.md)
  - [Create files and structures](docs/create-files-and-structures.md)
  - [Templates and generators](docs/templates-and-generators.md)
  - [Rename, move and copy](docs/rename-move-and-copy.md)
  - [Related files](docs/related-files.md)
  - [Properties, compare and export](docs/properties-compare-export.md)
  - [Tags, groups and profiles](docs/organise-tags-groups-profiles.md)
  - [Search, filters and duplicates](docs/search-filter-and-duplicates.md)
  - [History, undo and the workspace trash](docs/history-and-workspace-trash.md)
  - [Reference: commands, keys and settings](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Privacy](others/privacy.md)
  - [Related](others/related.md)
  - [Release notes](others/release-notes.md)
