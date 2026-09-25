---
title: Auric Artisan File System — glossary
description: Plain-language definitions of the terms used in the Auric Artisan File System documentation.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Glossary

**Barrel** — an index file that re-exports other modules, such as `index.ts`.

**Batch operation** — one action applied to many files at once, such as a batch rename.

**Brace expansion** — writing `{a,b}` or `{1..3}` in a path to produce several paths.

**Companion file** — a file that belongs with another: its test, stylesheet, story, documentation or types.

**Conflict** — a planned change whose target already exists.

**Deck** — the optional set of about 60 keyboard shortcuts turned on by `auricFiles.keyboard.enableDefaultShortcuts`.

**Filter** — a set of conditions (text, kind, tag, extension, path, size, date, flags, Git state) that narrows the indexed file list.

**Focus mode** — limiting Auric's indexed file lists to chosen paths.

**Framework preset** — a ready-made set of templates and relationships for one ecosystem, such as React or Go.

**Front matter** — the settings block between two `---` lines at the top of a template file.

**Generator** — a template defined in settings that can create companion files in the same step.

**Group** — a named set of files and folders from anywhere in the workspace. The panel calls creating one "Create Workspace from Selection".

**Guarded operation** — a file operation that is planned, checked against protected paths and collisions, confirmed when large, and recorded for undo.

**Operation history** — the list of Auric file operations you can undo and redo.

**Partial** — a template included inside another with `{{> id}}`.

**Profile** — a saved way of viewing the workspace: sort, grouping, filter, open folders, focus mode and hidden list.

**Properties** — the view that shows a file's facts and Auric organisation data.

**Protected path** — a path matching `auricFiles.safety.protectedPaths`, which no Auric operation may rename, move or delete.

**Relation rule** — a pattern linking a source file to its companions.

**Restricted Mode** — how VS Code runs an untrusted workspace; Auric Files then allows browsing and navigation but no file changes.

**Tag** — a named, coloured label you can put on files.

**Template** — a file pattern with a name and a body containing placeholders.

**Virtual folder** — a named collection of items that exists only as organisation data, not on disk.

**Workspace index** — Auric's list of the workspace's files and folders, used for search, filters, duplicates and related files.

**Workspace trash** — the `.auric/trash` folder where deleted items are kept so they can be restored.
