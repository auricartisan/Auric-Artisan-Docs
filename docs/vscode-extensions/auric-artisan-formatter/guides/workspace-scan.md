---
title: Auric Artisan Formatter — scan the workspace
description: See how many files would change before formatting a repository, review them in the Workspace tab, format them explicitly, or check without writing.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Scan the workspace

Adopting a formatter on an existing codebase is mostly a question of trust. Format on save quietly rewrites the first file you open; formatting the whole workspace rewrites thousands at once. The workspace scan is a third option: it formats every supported file **in memory**, tells you what would change, and writes nothing.

## What the scan does

A few seconds after the window opens (`auricFormatter.scanOnStartup`, on by default), the formatter:

- reads every supported file in the workspace and formats it in memory;
- records whether each file would change, and how many lines it would gain and lose;
- notes files that fail to parse, are skipped, or trip the safety gate.

Nothing is written to disk; your working tree and `git status` stay as they were.

The scan also follows your work: saved and unsaved edits, external changes and created or deleted files update the results, and new files trigger a short, delayed rescan. Changing the preset or saving a configuration file re-runs the scan, because they change what "already formatted" means.

## Where the results appear

- **The status bar** shows ***N* unformatted** with a warning background. The tooltip says ***N* of *M* files would change if formatted. Nothing has been written — click to review them.** When everything is formatted, it shows **Auric** with a double tick.
- **The Workspace tab** of Formatter Studio lists every file.
- **Check Formatting Without Writing (CI Mode)** puts the same result in the Problems panel.

## Run a scan on demand

**Auric Formatter: Scan the Workspace Without Writing** runs the scan now, even if the startup scan is off. Afterwards:

- if files would change: ***N* of *M* files would change. Nothing has been written.** with **Review them** and **Format them all**;
- otherwise: **all *M* files are already formatted.**

## The Workspace tab

Open it with **Show Files That Need Formatting** (`Ctrl` + `Alt` + `Shift` + `U`), the status bar item, or **02 Workspace** in Studio.

| Control | Options |
| --- | --- |
| Which files to show | **Needs formatting** (files whose bytes would change), **Every scanned file**, **Already formatted**, **Errors and skips** (parse failures, safety reverts, skipped files) |
| Sort order | **Largest change first** (what a review will notice), **Path** (alphabetical, grouped by folder), **Language**, **File size** (biggest first) |
| **Filter by path…** | Type part of a path |
| **Rescan** / **Stop** | Format every file in memory again, or stop a running scan |
| Tick boxes and **Select every listed file** | Choose files |
| **Format selected** | Write the ticked files |
| **Format all files** | Write every file that needs formatting |
| A row's diff button | Open that file with a preview of what would change |
| A row's write button | Write this one file |

Each row shows the path, language, tier and the lines added and removed.

## Taking the change

All three ways are explicit:

1. **Format all files** writes every pending file at once.
2. Tick rows, then **Format selected**, to take a folder at a time so each commit stays reviewable.
3. The diff button on a row lets you read the change for one file first.

Writing more than one file asks **Format *N* files?** first, while `auricFormatter.confirmBeforeFormattingAll` is on. Each file is re-read and re-formatted at the moment it is written, so a file you edited since the scan is never overwritten with a stale result; a file open with unsaved changes is written through the editor. Batch formatting saves the files, unlike a single-document **Apply**, which leaves the file unsaved.

The result is reported as **formatted *N* files**, or with a count of failures and **Show log**.

## Check without writing (CI mode)

**Auric Formatter: Check Formatting Without Writing (CI Mode)** runs a fresh scan and adds a Problems entry for every file that is not formatted (**This file is not formatted (*N* lines added, *M* removed). Run Auric Formatter to fix it.**) or could not be formatted. It then reports ***N* of *M* files need formatting. See Problems.** For the same check in a CI pipeline, use the command line: see [Command line and CI](command-line.md).

## Scan settings

| Setting | Default | Effect |
| --- | --- | --- |
| `auricFormatter.scanOnStartup` | `true` | Scan when the window opens |
| `auricFormatter.scanExclude` | empty (built-in list) | Globs the scan skips. Empty uses `node_modules`, `.git`, `dist`, `build`, `out`, `coverage`, `vendor`, `target`, `.next`, `.venv`, minified files and source maps |
| `auricFormatter.scanMaxFiles` | 4000 | Stop after this many files, so a very large monorepo is bounded |
| `auricFormatter.confirmBeforeFormattingAll` | `true` | Ask before writing more than one file |

Files larger than `auricFormatter.maxFileSizeKb` are skipped before they are read. In a multi-root workspace, each file is identified with its folder name.

The scan is not an unlimited index: exclusions, the file-size limit and `scanMaxFiles` always apply.

When you format selected files, the Workspace tab removes them from **Needs formatting**, and the status bar count goes down.
