---
title: Auric Artisan File System — limits and accuracy
description: What Auric Artisan File System reports and how precisely, its built-in limits, and what it deliberately does not do.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Limits and accuracy

## What Properties can report

Properties shows what the file system reports through VS Code, and labels anything it cannot know.

| Detail | Accuracy |
| --- | --- |
| Name, path, type | Exact |
| Size | As reported. Folders show **Folder**; a recursive disk-usage total is not calculated |
| Created | Only where the file system records a creation time; otherwise **Unavailable** |
| Modified | As reported |
| Owner / creator | Not available through VS Code; never guessed |
| Permissions | Only the read-only flag. Its absence does not prove you can write the file. Full access-control lists are not available |
| Git status | From the last index, and labelled so; refresh the index to update it |
| Related files | Found through the index; before it is built, shown as not indexed |
| Version | Counts Auric operations only |

## Built-in limits

| Limit | Default | Setting |
| --- | --- | --- |
| Entries per index scan | 20,000 (500–200,000) | `auricFiles.explorer.maxNodes` |
| Matches per search | 2,000 (50–50,000) | `auricFiles.search.maxResults` |
| Paths from one brace expression | 1,000 | — |
| Paths in one batch creation | 2,000 | — |
| Operations kept for undo | 200 (10–2,000) | `auricFiles.safety.historyLimit` |
| Workspace trash size | 256 MiB | `auricFiles.safety.trashMaxBytes` |
| Workspace trash retention | 14 days (1–365) | `auricFiles.safety.trashRetentionDays` |
| Folders read at once while indexing | 8 (1–64) | `auricFiles.performance.scanConcurrency` |
| Regular expression length in batch rename | 512 characters | — |

When the index reaches its limit, it stops and marks itself as truncated, and counts say so, rather than stalling VS Code.

## Deliberate boundaries

- The **Auric Files** sidebar is a companion, not a second file tree. VS Code owns the Explorer's rows, sorting and drag-and-drop.
- VS Code's Explorer supports sorting by name, type and date modified only. Auric's other sort and grouping options apply to its own indexed lists.
- The operation history records Auric operations only. It does not record editor edits or native Explorer actions, and it does not keep old copies of file contents.
- Duplicate review never deletes by itself; you choose every file.
- Selection export is a JSON manifest, not an archive of file contents.
- Template expressions are substitution only; templates cannot run code.
- File-changing operations require a trusted workspace.
- Remote and virtual file systems offer different capabilities. In virtual workspaces, revealing in the operating system's file manager, content hashing and the native trash are unavailable.
- The interface is in English.
- The icon tools only work with the Auric Artisan File Icons Facet or Playful theme. Icon menu entries added by those themes are managed by that extension.

## Keeping your work safe

Protected paths, confirmations, previews, history and the workspace trash are safeguards, not a backup. Keep using version control and normal backups.
