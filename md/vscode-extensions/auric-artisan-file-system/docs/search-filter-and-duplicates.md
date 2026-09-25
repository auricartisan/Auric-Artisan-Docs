---
title: Auric Artisan File System — search, filters and duplicates
description: Search the workspace index, build and save filters, sort and group files, and review duplicate and empty files.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Search, filters and duplicates

These commands are in the **Find & filter** group of the workspace panel. They work on the *workspace index*: a list of the workspace's files and folders that Auric Files builds the first time you need it and keeps up to date. Searching and filtering work in untrusted workspaces too.

## The workspace index

- It is built on demand, the first time a command needs it. The panel shows **Index builds when needed** until then, and **Workspace index ready** after.
- Folders in `auricFiles.explorer.excludePatterns` (by default `node_modules`, `.git`, `dist`, `out`, `.next`, `__pycache__`, `target` and `vendor`) and anything your `.gitignore` excludes (`auricFiles.explorer.respectGitignore`) are never indexed, searched, compared or batch-processed.
- One scan holds at most `auricFiles.explorer.maxNodes` entries (default 20,000). A larger workspace is marked as truncated, and counts say so.
- After the first scan, changes are followed automatically (`auricFiles.performance.watchWorkspace`). Run **Auric Files: Refresh** to rebuild it by hand.

## Search

1. Run **Auric Files: Search Files…**, or **Quick Open in Auric Files…** (`Ctrl` + `Alt` + `O` with the deck), which focuses the Explorer first.
2. Type part of a name or path. The title shows the default search mode.
3. Choose a file to open it.

The list holds up to `auricFiles.search.maxResults` files (default 2,000). With `auricFiles.explorer.showFileSize` on, each result shows its size.

## Filters

A *filter* narrows the indexed file list by several conditions at once.

### Build a filter

1. Run **Auric Files: Apply Filter…**.
2. If you have saved filters, start from **Current filter** or one of the **Saved filters**.
3. Answer each step. Every step is optional; press `Enter` to skip it.

| Step | What you enter |
| --- | --- |
| Search text | A glob, a regular expression or a fuzzy fragment |
| How should the text be matched? | `glob` wildcards (`src/**/*.tsx`), a `regex` regular expression, or `fuzzy` loose matching |
| Restrict to kinds | `file`, `folder`, `symlink` |
| Restrict to tags | Any of your tags |
| Extensions | Comma-separated, such as `.ts, .tsx, .vue` |
| Path globs | Include patterns, then `!exclude` patterns, such as `src/**, packages/**, !**/generated/**` |
| Size range | Bytes as `min..max`, either side may be blank, such as `1024..1048576` |
| Modified-date range | `YYYY-MM-DD..YYYY-MM-DD`, such as `2026-01-01..2026-12-31` |
| Flags | **Favorite**, **Pinned**, **Hidden**, **Highlighted**, **Empty files and folders only**, **Case-sensitive text** |
| Git states | `modified`, `added`, `deleted`, `untracked`, `ignored`, `conflict`, `clean` |

4. The results open as **Filtered Files — *summary of the filter***. Choose one to open it. If nothing matches: **No files match the selected filter.**

The default match mode is `auricFiles.search.defaultMode` (`glob`). Case is ignored unless you tick **Case-sensitive text** or turn on `auricFiles.search.caseSensitive`. Dot-files and hidden items are left out unless `auricFiles.explorer.showHiddenFiles` is on.

### Save and clear

- **Save Current Filter…** — type a **Name for this filter**. It then appears under **Saved filters** in **Apply Filter…**.
- **Clear Filter** — remove the active filter (**Filter cleared.**).

## Sorting

### VS Code's Explorer

Auric Files can set the sort order of VS Code's own Explorer. It writes the `explorer.sortOrder` setting, and its direction, for this workspace.

| Command | Effect |
| --- | --- |
| **Sort** (`Alt` + `S` with the Explorer focused) | Cycle between name, type and date modified |
| **Sort by Name** | Alphabetical |
| **Sort by Type** | By file type |
| **Sort by Date Modified** | By last change |
| **Sort Ascending** / **Sort Descending** | Direction |

The same commands are in the Explorer title bar's **Sort** menu and in **Auric Files** › **Sort**. VS Code's Explorer only supports these three orders.

### Auric's indexed lists

The indexed pickers can sort by more: `auricFiles.explorer.sort` is `name` (natural order, so `file10` follows `file9`), `path`, `type`, `size`, `modified`, `created`, `extension`, `status` (conflicts and changed Git files first) or `custom`. Add a tie-breaker with `auricFiles.explorer.secondarySort`, set directions with `auricFiles.explorer.sortDirection` and `auricFiles.explorer.secondarySortDirection`, and keep folders on top with `auricFiles.explorer.foldersFirst`.

## Grouping

**Group Indexed Files…** (in the panel's **Find & filter** group) chooses the headings for the indexed file list:

| Choice | Headings |
| --- | --- |
| **No grouping** | One sorted list |
| **Files and folders** | Files and folders separately |
| **Extension** | One heading per extension |
| **Parent folder** | One heading per containing folder |
| **Auric tag** | One heading per first tag; untagged items last |
| **Modified time** | Today, this week, this month and older |
| **Git status** | Changed, untracked, conflicted, clean and ignored |

The setting is `auricFiles.explorer.grouping`.

## Collapse and expand

**Collapse All** and **Expand All** fold or unfold VS Code's Explorer tree.

## Duplicate files

1. Run **Auric Files: Find Duplicate Files**. A progress notification shows the scan; you can cancel it.
2. The **Duplicate Files** list shows each group of matching files. In each group, the first file is kept and the other copies are ticked. Each row says why it matched and how much space the group would free.
3. Adjust the ticks and press `Enter`.
4. The ticked copies are moved to the workspace trash (with the usual confirmation), so you can restore them.

What counts as a duplicate depends on `auricFiles.search.duplicateStrategy`:

| Value | Meaning |
| --- | --- |
| `content` (default) | Same bytes. Files are grouped by size first, so files with a unique size are never read |
| `name` | The same file name in different folders |
| `size` | The same length; the fastest and loosest |

In a virtual workspace, content hashing is not available, and Auric Files falls back to comparing by size with a warning.

Nothing is deleted automatically: you choose every file.

## Empty files and folders

**Auric Files: Find Empty Files** lists empty files and folders, all ticked. Untick any to keep, press `Enter`, and the rest move to the workspace trash. If there are none: **Auric Files found no empty files or folders.**

After a filter, the results list shows only the files that meet every condition you set.
