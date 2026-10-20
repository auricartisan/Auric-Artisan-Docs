---
title: Auric Artisan File System — reference
description: Every Auric Artisan File System command grouped as the product groups them, every keyboard shortcut, menu and setting, with types, defaults and ranges.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Reference: commands, keys and settings

This page covers Auric Artisan File System 0.1.0: 81 commands, 69 keyboard shortcut declarations, one Explorer view and 48 settings. Commands appear in the Command Palette with the **Auric Files:** prefix.

## Commands

Commands are grouped as the workspace panel groups them. The **Keys** column gives Windows and Linux keys. **(Explorer)** keys work whenever the Explorer has focus. **(deck)** keys need `auricFiles.keyboard.enableDefaultShortcuts`. On macOS, `Cmd` replaces `Ctrl` in every shortcut, except **Redo File Operation**, which is `Cmd` + `Alt` + `Shift` + `Z`. "Then" means press the first combination, release, then press the second.

Commands marked "not in the Command Palette" act on a selection and run from the panel, context menus or shortcuts.

### Create

Files, folders and complete structures.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: New File…** | `auricFiles.newFile` | `Ctrl` + `N` (Explorer); `Ctrl` + `Alt` + `A`, then `Ctrl` + `N` (deck) | Create a file: choose the folder, type a name (a trailing / makes a folder), optionally pick a template |
| **Auric Files: New Folder…** | `auricFiles.newFolder` | `Ctrl` + `Shift` + `N` (Explorer); `Ctrl` + `Alt` + `A`, then `Ctrl` + `Shift` + `N` (deck) | Create a folder, including nested paths |
| **Auric Files: New File from Template…** | `auricFiles.newFromTemplate` | `Ctrl` + `Alt` + `A`, then `T` (deck) | Create a file from a built-in, workspace or global template, filling in its variables |
| **Auric Files: New from Framework Preset…** | `auricFiles.newFromPreset` | `Ctrl` + `Alt` + `A`, then `P` (deck) | Create files from a framework preset (React, Vue, Angular and more) or a custom generator |
| **Auric Files: New Sibling File** | `auricFiles.newSibling` | `Ctrl` + `Alt` + `N` (deck); `Ctrl` + `Alt` + `A`, then `N` (deck) | Create a file next to the selected file |
| **Auric Files: New Child File** | `auricFiles.newChild` | `Ctrl` + `Alt` + `A`, then `Shift` + `N` (deck) | Create a file inside the selected folder |
| **Auric Files: Create Related Files…** | `auricFiles.newRelated` | `Ctrl` + `Alt` + `A`, then `R` (deck) | Create companion files (test, style, story and so on) for the selected file |
| **Auric Files: Batch Structure…** | `auricFiles.batchCreate` | `Ctrl` + `Alt` + `B` (Explorer); `Ctrl` + `Alt` + `A`, then `B` (deck) | Type a whole structure of files and folders in one line; braces and ranges expand |
| **Auric Files: Batch Create Files…** | `auricFiles.batchCreateFiles` | `Ctrl` + `Alt` + `Shift` + `F` (deck); `Ctrl` + `Alt` + `A`, then `F` (deck) | Create many files at once from comma-separated paths with brace expansion |
| **Auric Files: Batch Create Folders…** | `auricFiles.batchCreateFolders` | `Ctrl` + `Alt` + `Shift` + `N` (deck); `Ctrl` + `Alt` + `A`, then `Shift` + `F` (deck) | Create many folders at once from comma-separated paths with brace expansion |

### Inspect & navigate

Properties, comparisons and companion files.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: File Properties** | `auricFiles.showMetadata` | `Alt` + `Enter` (Explorer) | Open Properties for the selected resource |
| **Auric Files: Quick Open in Auric Files…** | `auricFiles.quickOpen` | `Ctrl` + `Alt` + `O` (deck) | Focus the Explorer and search indexed files by name or path |
| **Auric Files: Compare Selected Files** | `auricFiles.compareSelected` | `Ctrl` + `Alt` + `Shift` + `D` (deck); `Ctrl` + `Alt` + `A`, then `Shift` + `C` (deck) | Open two selected files in VS Code's diff editor |
| **Auric Files: Merge Selected Files** | `auricFiles.mergeSelected` | `Ctrl` + `Alt` + `A`, then `Shift` + `G` (deck) | Open two files, or a base plus two inputs, in VS Code's merge editor |
| **Auric Files: Export Selected Items…** | `auricFiles.exportSelection` | `Ctrl` + `Alt` + `A`, then `Shift` + `X` (deck) | Save a JSON manifest of the selected items' paths and metadata |
| **Auric Files: Go to Related File…** | `auricFiles.goToRelated` | `Ctrl` + `Alt` + `R` (deck); `Ctrl` + `Alt` + `A`, then `O` (deck) | Pick and open any companion of the current file |
| **Auric Files: Open Matching Test** | `auricFiles.goToTest` | `Ctrl` + `Alt` + `A`, then `Q` (deck) | Open the current file's test |
| **Auric Files: Open Matching Style** | `auricFiles.goToStyle` | `Ctrl` + `Alt` + `A`, then `S` (deck) | Open the current file's stylesheet |
| **Auric Files: Open Matching Story** | `auricFiles.goToStory` | `Ctrl` + `Alt` + `A`, then `W` (deck) | Open the current file's story |
| **Auric Files: Open Matching Component** | `auricFiles.goToComponent` | `Ctrl` + `Alt` + `A`, then `I` (deck) | Open the component a test, style or story belongs to |
| **Auric Files: Open Matching Documentation** | `auricFiles.goToDocs` | `Ctrl` + `Alt` + `A`, then `Shift` + `D` (deck) | Open the current file's documentation |
| **Auric Files: Show Related File Group** | `auricFiles.showRelatedGroup` | — | List the file's related group, including missing companions; not in the Command Palette |
| **Auric Files: Generate Missing Companion Files** | `auricFiles.generateMissingRelated` | — | Create the companion files that do not exist yet |
| **Auric Files: Reveal in File Manager** | `auricFiles.revealInExplorer` | `Ctrl` + `Alt` + `A`, then `V` (deck) | Show the file in your operating system's file manager |
| **Auric Files: Reveal in VS Code Explorer** | `auricFiles.revealInVsCodeExplorer` | `Ctrl` + `Alt` + `A`, then `Shift` + `V` (deck) | Select the file in the VS Code Explorer |
| **Auric Files: Copy Relative Path** | `auricFiles.copyRelativePath` | `Ctrl` + `Alt` + `Shift` + `C` (deck); `Ctrl` + `Alt` + `A`, then `L` (deck) | Copy the workspace-relative path |
| **Auric Files: Copy Absolute Path** | `auricFiles.copyAbsolutePath` | `Ctrl` + `Alt` + `Shift` + `A` (deck); `Ctrl` + `Alt` + `A`, then `A` (deck) | Copy the full path |
| **Auric Files: Copy File URI** | `auricFiles.copyUri` | `Ctrl` + `Alt` + `A`, then `U` (deck) | Copy the file's URI |

### Edit & batch

Rename, duplicate and transform a selection.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: Rename…** | `auricFiles.rename` | — | Rename the selected item with collision checks and history; not in the Command Palette |
| **Auric Files: Move…** | `auricFiles.move` | — | Move the selected items to another folder; not in the Command Palette |
| **Auric Files: Copy To…** | `auricFiles.copyTo` | `Ctrl` + `Alt` + `A`, then `C` (deck) | Copy the selected items to another folder; not in the Command Palette |
| **Auric Files: Duplicate** | `auricFiles.duplicate` | — | Make a copy beside the original with a non-clashing name; not in the Command Palette |
| **Auric Files: Batch Rename…** | `auricFiles.batchRename` | `Ctrl` + `Alt` + `A`, then `Shift` + `R` (deck) | Rename many files by find and replace, regular expression, pattern, sequence, case or extension, with a preview |
| **Auric Files: Batch Move…** | `auricFiles.batchMove` | `Ctrl` + `Alt` + `A`, then `Shift` + `M` (deck) | Move many items to one folder, with collision planning |
| **Auric Files: Convert Extension…** | `auricFiles.convertExtension` | `Ctrl` + `Alt` + `A`, then `X` (deck) | Change the extension of the selected files, with a preview |

### Organise

Tags, groups and personal workspace views.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: Tag Files…** | `auricFiles.tagFiles` | `Ctrl` + `Alt` + `A`, then `G` (deck) | Assign or remove tags on the selected items; not in the Command Palette |
| **Auric Files: Manage Tags…** | `auricFiles.manageTags` | — | Create, rename or delete tags |
| **Auric Files: Add to Group…** | `auricFiles.addToCollection` | `Ctrl` + `Alt` + `A`, then `K` (deck) | Add the selected items to a group, or create a new one; not in the Command Palette |
| **Auric Files: Create Workspace from Selection** | `auricFiles.createWorkspace` | — | Create a group (virtual workspace) from the current selection |
| **Auric Files: Manage Groups…** | `auricFiles.manageCollections` | — | Rename, delete or open members of groups and virtual folders |
| **Auric Files: New Virtual Folder…** | `auricFiles.newVirtualFolder` | — | Create a virtual folder that gathers items without moving them; not in the Command Palette |
| **Auric Files: Toggle Favorite** | `auricFiles.toggleFavorite` | `Ctrl` + `Alt` + `A`, then `1` (deck) | Mark or unmark as a favourite (★ in the Explorer); not in the Command Palette |
| **Auric Files: Toggle Pinned** | `auricFiles.togglePinned` | `Ctrl` + `Alt` + `A`, then `2` (deck) | Pin or unpin (P in the Explorer); not in the Command Palette |
| **Auric Files: Toggle Native Explorer Exclusion** | `auricFiles.toggleHidden` | `Ctrl` + `Alt` + `A`, then `3` (deck) | Add or remove the item from VS Code's files.exclude for this workspace; not in the Command Palette |
| **Auric Files: Toggle Highlight** | `auricFiles.toggleHighlight` | `Ctrl` + `Alt` + `A`, then `4` (deck) | Highlight or unhighlight (● in the Explorer); not in the Command Palette |
| **Auric Files: Toggle Focus Mode** | `auricFiles.toggleFocusMode` | — | Limit Auric's indexed file lists to chosen paths, or switch focus mode off |
| **Auric Files: Switch Workspace Profile…** | `auricFiles.switchProfile` | — | Apply a saved workspace profile |
| **Auric Files: Save Workspace Profile…** | `auricFiles.saveProfile` | — | Save the current view preferences as a named profile |

### Find & filter

Search, duplicates and a quieter Explorer.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: Search Files…** | `auricFiles.search` | — | Search indexed files by name or path and open one |
| **Auric Files: Apply Filter…** | `auricFiles.applyFilter` | — | Build a filter from text, kinds, tags, extensions, globs, size, dates, flags and Git state |
| **Auric Files: Save Current Filter…** | `auricFiles.saveFilter` | — | Save the current filter under a name |
| **Auric Files: Clear Filter** | `auricFiles.clearFilter` | — | Remove the active filter |
| **Auric Files: Find Duplicate Files** | `auricFiles.findDuplicates` | — | Find duplicate files and choose copies to move to the workspace trash |
| **Auric Files: Find Empty Files** | `auricFiles.findEmptyFiles` | — | Find empty files and folders and choose which to move to the workspace trash |
| **Auric Files: Sort** | `auricFiles.setSort` | `Alt` + `S` (Explorer) | Cycle the native Explorer sort between name, type and date modified |
| **Auric Files: Sort by Name** | `auricFiles.sortName` | — | Sort the native Explorer by name |
| **Auric Files: Sort by Type** | `auricFiles.sortType` | — | Sort the native Explorer by type |
| **Auric Files: Sort by Date Modified** | `auricFiles.sortModified` | — | Sort the native Explorer by date modified |
| **Auric Files: Sort Ascending** | `auricFiles.sortAscending` | — | Sort the native Explorer ascending |
| **Auric Files: Sort Descending** | `auricFiles.sortDescending` | — | Sort the native Explorer descending |
| **Auric Files: Group Indexed Files…** | `auricFiles.setGrouping` | — | Choose the headings used by the indexed file list; not in the Command Palette |
| **Auric Files: Collapse All** | `auricFiles.collapseAll` | — | Collapse every folder in the Explorer |
| **Auric Files: Expand All** | `auricFiles.expandAll` | — | Expand the Explorer tree |

### History & recovery

Review operations and recover workspace trash.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: Undo Last File Operation** | `auricFiles.undo` | `Ctrl` + `Alt` + `Z` (deck); `Ctrl` + `Alt` + `A`, then `Z` (deck) | Undo the last Auric file operation |
| **Auric Files: Redo File Operation** | `auricFiles.redo` | `Ctrl` + `Alt` + `Y` (deck); `Ctrl` + `Alt` + `A`, then `Y` (deck) | Redo an undone Auric file operation |
| **Auric Files: Show Operation History** | `auricFiles.showHistory` | `Ctrl` + `Alt` + `A`, then `H` (deck) | List recent Auric operations and undo back to one |
| **Auric Files: Open Workspace Trash** | `auricFiles.openTrash` | `Ctrl` + `Alt` + `A`, then `Shift` + `T` (deck) | Browse the workspace trash; restore an entry or empty it |
| **Auric Files: Restore from Trash…** | `auricFiles.restoreFromTrash` | `Ctrl` + `Alt` + `A`, then `Shift` + `U` (deck) | Restore an entry from the workspace trash to its original place |
| **Auric Files: Delete (Workspace Trash)** | `auricFiles.delete` | `Ctrl` + `Alt` + `Shift` + `Backspace` (deck); `Ctrl` + `Alt` + `A`, then `Backspace` (deck) | Move the selected items to the workspace trash; not in the Command Palette |
| **Auric Files: Delete Permanently** | `auricFiles.deletePermanent` | `Ctrl` + `Alt` + `A`, then `Shift` + `Backspace` (deck) | Delete the selected items permanently, after confirmation; not in the Command Palette |
| **Auric Files: Empty Workspace Trash** | `auricFiles.emptyTrash` | `Ctrl` + `Alt` + `A`, then `Shift` + `Delete` (deck) | Permanently delete everything in the workspace trash |

### Workspace

Native Explorer and extension preferences.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: Focus VS Code Explorer** | `auricFiles.focus` | `Ctrl` + `Alt` + `E` (deck) | Focus the native VS Code Explorer |
| **Auric Files: Refresh** | `auricFiles.refresh` | — | Rebuild the workspace index |
| **Auric Files: Open Settings** | `auricFiles.openSettings` | `Ctrl` + `Alt` + `A`, then `Shift` + `S` (deck) | Open the Settings editor filtered to Auric Files |
| **Auric Files: Show Log** | `auricFiles.showLog` | — | Show the Auric Artisan File System output channel |

### Editor and global commands

Commands outside the workspace groups.

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Files: Rename Current File** | `auricFiles.renameCurrent` | `Ctrl` + `Alt` + `Shift` + `R` (deck); `Ctrl` + `Alt` + `A`, then `E` (deck) | Rename the file open in the editor |
| **Auric Files: Move Current File** | `auricFiles.moveCurrent` | `Ctrl` + `Alt` + `Shift` + `M` (deck); `Ctrl` + `Alt` + `A`, then `M` (deck) | Move the file open in the editor |
| **Auric Files: Duplicate Current File** | `auricFiles.duplicateCurrent` | `Ctrl` + `Alt` + `D` (deck); `Ctrl` + `Alt` + `A`, then `D` (deck) | Duplicate the file open in the editor |
| **Auric Files: Toggle File Metadata** | `auricFiles.toggleMetadata` | `Ctrl` + `Shift` + `M` (Explorer) | Switch the compact Explorer hover summaries on or off |
| **Auric Files: Open File Workspace** | `auricFiles.openMenu` | `Ctrl` + `Alt` + `Shift` + `E` (deck); `Ctrl` + `Alt` + `A`, then `Shift` + `E` (deck) | Open the Auric Files workspace in an editor tab |
| **Auric Files: Quick Actions…** | `auricFiles.quickActions` | — | Open a keyboard-first list of file-system actions |

## Where commands appear

- Explorer title bar: **Batch Structure…**, the **Sort** menu, **Open File Workspace**; **…** menu: **Quick Actions…**
- Explorer context menu: **File Properties** at the top; the **Auric Files** submenu
- Editor and editor tab context menus: The **Auric Files** submenu (not for untitled files)
- **Auric Files** submenu: **File Properties**, **Create**, **Edit and Batch**, **Navigate and Paths**, **Organize**, **Safety and History**, **Sort**, **Open File Workspace**, **Open Settings**
- **Create**: **New File…**, **New Folder…**, **New Sibling File** (files) or **New Child File** (folders), **Batch Create Files…**, **Batch Create Folders…**, **Batch Structure…**, **New File from Template…**, **New from Framework Preset…**, **Create Related Files…** (files)
- **Edit and Batch**: **Rename Current File**, **Duplicate**, **Move Current File**, **Copy To…**, **Batch Rename…**, **Batch Move…**, **Convert Extension…**
- **Navigate and Paths**: **File Properties**, **Compare Selected Files**, **Merge Selected Files**, **Export Selected Items…**, **Go to Related File…**, **Open Matching Test**, **Style**, **Story**, **Component** and **Documentation**, **Reveal in VS Code Explorer**, **Reveal in File Manager**, **Copy Relative Path**, **Copy Absolute Path**, **Copy File URI**
- **Organize**: **Create Workspace from Selection**, **Tag Files…**, **Add to Group…**, **Toggle Favorite**, **Toggle Pinned**, **Toggle Native Explorer Exclusion**, **Toggle Highlight**
- **Safety and History**: **Delete (Workspace Trash)**, **Delete Permanently**, **Undo Last File Operation**, **Redo File Operation**, **Show Operation History**, **Open Workspace Trash**, **Restore from Trash…**, **Empty Workspace Trash**
- **Sort**: **Sort by Name**, **Sort by Type**, **Sort by Date Modified**, **Sort Ascending**, **Sort Descending**
- **Auric Files** view title: **Open File Workspace**

## Views and panels

| Surface | Where | Contents |
| --- | --- | --- |
| **Auric Files** | A section of the Explorer | The compact workspace: summary, selection, **01 Actions**, **02 Properties** |
| **Auric Files** panel | An editor tab | The same workspace at full size |

Output channel: **Auric Artisan File System**.

## Explorer badges

| Badge | Meaning |
| --- | --- |
| **●** | Highlighted |
| **★** | Favourite |
| **P** | Pinned |
| **H** | Hidden (excluded from the native Explorer) |
| Two letters | The first two letters of the item's first tag |
| **W** | A member of a group |

When an item has several marks, the first in this list is shown.

## Settings

All 48 settings, grouped by area. They can be set in user or workspace settings.

### Explorer, sorting and indexing

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.explorer.sort` | string | `name` | `name`, `path`, `type`, `size`, `modified`, `created`, `extension`, `status`, `custom` | Primary order for Auric's indexed pickers. Orders VS Code supports are also applied to its Explorer. |
| `auricFiles.explorer.sortDirection` | string | `asc` | `asc`, `desc` | Direction the chosen sort runs in — ascending puts A, the smallest and the oldest first. |
| `auricFiles.explorer.secondarySort` | string | `none` | `none`, `name`, `path`, `type`, `size`, `modified`, `created`, `extension`, `status`, `custom` | Optional second sort key used when two entries have the same primary value. |
| `auricFiles.explorer.secondarySortDirection` | string | `asc` | `asc`, `desc` | Direction for the secondary sort key. |
| `auricFiles.explorer.grouping` | string | `none` | `none`, `type`, `extension`, `folder`, `tag`, `modified`, `status` | Headings used by Auric's indexed grouped-file picker. |
| `auricFiles.explorer.foldersFirst` | boolean | `true` |  | Keep directories above files no matter which sort is active. |
| `auricFiles.explorer.showHiddenFiles` | boolean | `false` |  | Include dot-files and metadata-hidden entries in Auric search and filter results. |
| `auricFiles.explorer.showFileSize` | boolean | `false` |  | Show a size beside each file in Auric's file lists. Costs one file check per entry on large trees. |
| `auricFiles.explorer.showGitStatus` | boolean | `true` |  | Read Git state for filtering and Git-aware safety warnings. |
| `auricFiles.explorer.previewOnSingleClick` | boolean | `true` |  | Open a single click in a reusable preview tab. Off, a double click is needed to open anything. |
| `auricFiles.explorer.maxNodes` | number | `20000` | 500–200000 | Most entries held in one scan. Reaching it stops the scan and marks the index as truncated. |
| `auricFiles.explorer.excludePatterns` | array | see "Long default values" |  | Globs skipped while scanning. Matches are never indexed, searched, compared or batch-processed. |
| `auricFiles.explorer.respectGitignore` | boolean | `true` |  | Read the workspace .gitignore and skip whatever it excludes, on top of the patterns above. |

### Creating files

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.create.defaultTemplate` | string | empty |  | Template id applied by New File when you do not pick one. Leave empty to create a blank file. |
| `auricFiles.create.openAfterCreate` | boolean | `true` |  | Open a new file in the editor, with the cursor at the template's cursor marker. |
| `auricFiles.create.createIntermediateDirs` | boolean | `true` |  | Create missing folders in a path such as `src/lib/util/index.ts` instead of refusing. |
| `auricFiles.create.expandBraces` | boolean | `true` |  | Treat braces and ranges as several targets, so `src/{Button,Card}/index.ts` makes two files. |
| `auricFiles.create.preset` | string | `auto` | `auto`, `react`, `vue`, `angular`, `svelte`, `node`, `python`, `java`, `go`, `rust`, `generic` | Which framework's templates and relation rules are offered. `auto` picks from the workspace's files. |
| `auricFiles.create.componentStyleLanguage` | string | `css` | `css`, `scss`, `less`, `styled`, `module-css`, `module-scss` | Stylesheet flavour for a component's companion style file, and the extension relation rules look for. |
| `auricFiles.create.testFramework` | string | `auto` | `auto`, `jest`, `vitest`, `mocha`, `node`, `pytest`, `junit`, `gotest`, `cargo` | Test style and imports for generated test files. `auto` reads the workspace's dependencies and scripts. |
| `auricFiles.create.indent` | string | `space2` | `space2`, `space4`, `tab` | Indentation written into generated file bodies. |
| `auricFiles.create.generatorProfiles` | array | `[]` |  | Custom generators shown beside the framework presets. Each can create any number of companion files. |

### Safety, trash and history

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.safety.confirmDelete` | boolean | `true` |  | Ask before anything is deleted, listing what goes and where it lands. |
| `auricFiles.safety.confirmBulk` | number | `5` | 0–no maximum | Ask for confirmation once an operation touches this many paths. `0` asks every time. |
| `auricFiles.safety.useWorkspaceTrash` | boolean | `true` |  | Move deleted items to `.auric/trash` in the workspace so they can be restored. |
| `auricFiles.safety.trashRetentionDays` | number | `14` | 1–365 | How long a trashed entry survives before it is purged automatically. |
| `auricFiles.safety.trashMaxBytes` | number | `268435456` | 0–no maximum | Size limit for the workspace trash in bytes (256 MiB). The oldest entries are purged first. |
| `auricFiles.safety.protectedPaths` | array | see "Long default values" |  | Globs no Auric operation may rename, move or delete. A plan touching one is blocked before any change. |
| `auricFiles.safety.warnOnGitTracked` | boolean | `true` |  | Warn when a file about to be deleted or moved is tracked by Git. |
| `auricFiles.safety.warnOnUncommittedChanges` | boolean | `true` |  | Warn when a file about to be deleted or moved has uncommitted edits. |
| `auricFiles.safety.previewBeforeApply` | boolean | `true` |  | Show the full before-and-after list of a batch rename or move, with conflicts, and require approval. |
| `auricFiles.safety.historyLimit` | number | `200` | 10–2000 | How many past operations stay undoable. Older entries drop off the end of the stack. |

### Related files

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.related.enabled` | boolean | `true` |  | Resolve companions for the active file: test, style, story, component, docs and types. |
| `auricFiles.related.rules` | array | `[]` |  | Extra file relationships for conventions the built-in presets do not know. |
| `auricFiles.related.testDirectories` | array | `["__tests__","tests","test","spec"]` |  | Folder names searched when tests live in a separate folder rather than beside each file. |
| `auricFiles.related.storyExtensions` | array | see "Long default values" |  | Suffixes recognised as a component's story file, in the order they are tried. |

### Templates

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.templates.directories` | array | `[".auric/templates",".vscode/templates"]` |  | Workspace folders scanned for templates. A workspace template replaces a built-in one with the same id. |
| `auricFiles.templates.global` | array | `[]` |  | Absolute folders of templates shared across every workspace, for conventions you carry between projects. |
| `auricFiles.templates.variables` | object | `{}` |  | Values available in every template, such as an author or licence header. Prompted values win. |

### Search and duplicates

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.search.defaultMode` | string | `glob` | `glob`, `regex`, `fuzzy` | How a filter's search text is read: `glob` wildcards, `regex` regular expression, or `fuzzy` matching. |
| `auricFiles.search.caseSensitive` | boolean | `false` |  | Match letter case exactly. Off, a search for button also finds Button.tsx. |
| `auricFiles.search.maxResults` | number | `2000` | 50–50000 | Matches kept by one search before it stops and reports a partial result. |
| `auricFiles.search.duplicateStrategy` | string | `content` | `content`, `name`, `size` | What counts as a duplicate: `content` (same bytes), `name` (same file name) or `size` (same length). |

### Performance

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.performance.watchWorkspace` | boolean | `true` |  | After the first indexed command, follow file changes and update the index. Turn off on slow network shares. |
| `auricFiles.performance.scanConcurrency` | number | `8` | 1–64 | Folders read at once while indexing. Raise on a fast local disk, lower on a remote file system. |
| `auricFiles.performance.debounceMs` | number | `120` | 0–2000 | Quiet period after the last file change before the index updates. |

### Keyboard and logging

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFiles.keyboard.enableDefaultShortcuts` | boolean | `false` |  | Turn on the full shortcut deck of `Ctrl` + `Alt` (`Cmd` + `Alt`) combinations. Off by default. |
| `auricFiles.logLevel` | string | `warn` | `off`, `error`, `warn`, `info`, `debug` | Detail written to the output channel. Paths are logged workspace-relative; file contents never. |

### Long default values

`auricFiles.explorer.excludePatterns`:

```json
["**/node_modules/**", "**/.git/**", "**/dist/**", "**/out/**", "**/.next/**", "**/__pycache__/**", "**/target/**", "**/vendor/**"]
```

`auricFiles.safety.protectedPaths`:

```json
["**/.git/**", "**/node_modules/**", "**/.env", "**/.env.*", "**/*.pem", "**/*.key", "**/package-lock.json", "**/yarn.lock", "**/pnpm-lock.yaml"]
```

`auricFiles.related.storyExtensions`:

```json
[".stories.tsx", ".stories.jsx", ".stories.ts", ".stories.js", ".stories.svelte", ".stories.mdx"]
```

### Enumerated values explained

| Setting | Value | Meaning |
| --- | --- | --- |
| `auricFiles.explorer.sort` | `name` | Alphabetical, natural order, so `file10` follows `file9` |
| `auricFiles.explorer.sort` | `path` | By the full workspace-relative path |
| `auricFiles.explorer.sort` | `type` | Folders, files and links in that order, then by name |
| `auricFiles.explorer.sort` | `size` | Largest first when descending; folders keep name order |
| `auricFiles.explorer.sort` | `modified` | Most recently written first when descending |
| `auricFiles.explorer.sort` | `created` | Creation time, where recorded |
| `auricFiles.explorer.sort` | `extension` | By extension, then by name |
| `auricFiles.explorer.sort` | `status` | Conflicts and changed Git files first, then clean and ignored |
| `auricFiles.explorer.sort` | `custom` | A stored custom rank; unranked items follow by name |
| `auricFiles.explorer.grouping` | `none` | One continuous list |
| `auricFiles.explorer.grouping` | `type` | Folders, files and links under separate headings |
| `auricFiles.explorer.grouping` | `extension` | One heading per extension |
| `auricFiles.explorer.grouping` | `folder` | One heading per parent folder |
| `auricFiles.explorer.grouping` | `tag` | One heading per tag; untagged last |
| `auricFiles.explorer.grouping` | `modified` | Today, this week, this month and older |
| `auricFiles.explorer.grouping` | `status` | Changed, untracked, conflicted, clean and ignored |
| `auricFiles.search.defaultMode` | `glob` | Wildcards over the path |
| `auricFiles.search.defaultMode` | `regex` | A regular expression tested against the path |
| `auricFiles.search.defaultMode` | `fuzzy` | Loose matching ranking the closest paths first |
| `auricFiles.search.duplicateStrategy` | `content` | Same bytes; files are bucketed by size first |
| `auricFiles.search.duplicateStrategy` | `name` | Same file name in different folders |
| `auricFiles.search.duplicateStrategy` | `size` | Same length; fastest and loosest |
| `auricFiles.logLevel` | `off`, `error`, `warn`, `info`, `debug` | Nothing, failures, skips too, one line per operation, per-step detail |

### Settings restricted in untrusted workspaces

Workspace values of these settings are ignored until you trust the folder: `auricFiles.safety.confirmDelete`, `auricFiles.safety.confirmBulk`, `auricFiles.safety.useWorkspaceTrash`, `auricFiles.safety.protectedPaths`, `auricFiles.safety.warnOnGitTracked`, `auricFiles.safety.warnOnUncommittedChanges`, `auricFiles.safety.previewBeforeApply`, `auricFiles.related.rules`, `auricFiles.templates.directories`, `auricFiles.templates.global` and `auricFiles.templates.variables`.

## Files and settings Auric Files writes

| What | Where | Written by |
| --- | --- | --- |
| Workspace trash | `.auric/trash/` in the workspace folder, with `index.json` | **Delete (Workspace Trash)** |
| Workspace templates | `.auric/templates/`, `.vscode/templates/` (read, not written) | You |
| Selection manifest | Where you choose; default `auric-selection.json` | **Export Selected Items…** |
| `files.exclude` | Workspace or folder settings | **Toggle Native Explorer Exclusion** |
| `explorer.sortOrder` and its direction | Workspace settings | The **Sort** commands |
| Tags, groups, virtual folders, flags, filters, profiles, history | VS Code's storage for this workspace | The **Organise**, **Find & filter** and history commands |
