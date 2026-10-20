---
title: Auric Artisan File System — privacy
description: What Auric Artisan File System keeps on your machine and what, if anything, uses the network.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Privacy

## Everything runs locally

- File operations, the index, search, filters, duplicate review and Properties all run on your machine (or next to the workspace, in a remote setup).
- No Auric Artisan account is needed.
- Properties reads file-system metadata only, never file contents. Duplicate review reads contents only to compare files by hash when the `content` strategy is used, and only for files that share a size.

## Where data is kept

| Data | Where |
| --- | --- |
| Tags, groups, virtual folders, flags, saved filters, profiles, operation history | VS Code's storage for this workspace, on your machine. Not written into the project and not copied by Settings Sync |
| Workspace trash | `.auric/trash/` inside the workspace folder |
| Native Explorer exclusions | The workspace's `files.exclude` setting |
| Explorer sort order | The workspace's `explorer.sortOrder` setting |
| Selection manifests | Wherever you save them |

## Logging

The **Auric Artisan File System** output channel logs paths relative to the workspace and never writes file contents. `auricFiles.logLevel` controls how much is written (default `warn`).

## Network

The extension's own features do not use the network. The workspace panel loads its scripts and styles from the extension itself. Opening the auricartisan.com link, support links or Marketplace images uses your browser and the network.
