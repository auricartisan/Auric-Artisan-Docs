---
title: Auric Artisan File System — history, undo and the workspace trash
description: Undo and redo Auric file operations, review the history, delete safely into the workspace trash, restore items and control the safety settings.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# History, undo and the workspace trash

These commands are in the **History & recovery** group of the workspace panel and the **Auric Files** › **Safety and History** submenu.

## Undo and redo

Every operation Auric Files performs (create, rename, move, copy, duplicate, delete, convert) is recorded as one step, however many files it touched.

| Command | What it does | Deck shortcut |
| --- | --- | --- |
| **Undo Last File Operation** | Reverse the most recent Auric operation | `Ctrl` + `Alt` + `Z` |
| **Redo File Operation** | Redo the last undone operation | `Ctrl` + `Alt` + `Y` (macOS `Cmd` + `Alt` + `Shift` + `Z`) |
| **Show Operation History** | List recent operations; choose one to undo back to it | `Ctrl` + `Alt` + `A`, then `H` |

When it works you see **Undid *operation*.** or **Redid *operation*.** If an undo cannot be completed, both the undo and redo lists stay as they were rather than pretending.

- The history keeps the last `auricFiles.safety.historyLimit` operations (default 200, range 10–2000).
- It is saved in VS Code's storage for the workspace, so it survives a restart.
- It records **Auric** operations only. Edits you make in the editor, VS Code's own Explorer actions (rename with `F2`, drag-and-drop) and changes made by other tools are not in it, and it does not keep old copies of file contents. Keep using version control and backups.

With no history yet: **No file operations have been recorded yet.**

## Delete into the workspace trash

The *workspace trash* is a folder inside your workspace, `.auric/trash`, where Auric Files moves deleted items so you can restore them.

1. Select items and run **Delete (Workspace Trash)** from the panel, the context menu or the deck (`Ctrl` + `Alt` + `Shift` + `Backspace`).
2. Confirm **Move *N* items to the workspace trash?**. The dialog lists what goes and says you can **Restore from the Trash surface or with Undo**.
3. The items move to `.auric/trash`.

Each deleted item is kept in its own folder in `.auric/trash`, with a small record of where it came from, so the trash can always be rebuilt even if its index file is lost.

### Delete permanently

**Delete Permanently** (`Ctrl` + `Alt` + `A`, then `Shift` + `Backspace` with the deck) asks **Permanently delete *N* items?** with **This cannot be undone.** and removes the items without using the workspace trash. If you turn off `auricFiles.safety.useWorkspaceTrash`, every delete is permanent.

**Delete (Workspace Trash)** and **Delete Permanently** act on the selection and are not listed in the Command Palette.

## Browse and restore

- **Open Workspace Trash** lists every entry by its original name. Choose one to restore it, or choose **Empty Workspace Trash…** at the end of the list. If the trash is empty: **The workspace trash is empty.**
- **Restore from Trash…** restores a chosen entry to its original place. If something already exists there, it is restored under a free name instead of overwriting. The message says **Restored *path*.**

## Empty the trash

**Empty Workspace Trash** asks **Permanently delete *N* items from the workspace trash?**, shows how much space will be freed and says **This cannot be undone.** Choose **Empty Trash** to confirm.

The trash also cleans itself:

| Setting | Default | What it does |
| --- | --- | --- |
| `auricFiles.safety.useWorkspaceTrash` | `true` | Use the workspace trash for deletes |
| `auricFiles.safety.trashRetentionDays` | 14 (1–365) | Days an entry is kept before it is purged automatically |
| `auricFiles.safety.trashMaxBytes` | 268435456 (256 MiB) | Size limit; the oldest entries are purged when a delete would exceed it |

A single item larger than the whole trash limit is refused with an explanation rather than half-stored.

The workspace trash is left out of Auric's index, search and duplicate review. You may want to add `.auric/` to your `.gitignore`. In virtual workspaces the operating system's trash is not available.

## Safety settings

| Setting | Default | What it does |
| --- | --- | --- |
| `auricFiles.safety.confirmDelete` | `true` | Ask before anything is deleted, listing what goes and where |
| `auricFiles.safety.confirmBulk` | 5 | Ask once an operation touches this many paths; `0` asks every time |
| `auricFiles.safety.protectedPaths` | see below | Globs no Auric operation may rename, move or delete |
| `auricFiles.safety.warnOnGitTracked` | `true` | Warn when moving or deleting a file Git tracks |
| `auricFiles.safety.warnOnUncommittedChanges` | `true` | Warn when moving or deleting a file with uncommitted edits |
| `auricFiles.safety.previewBeforeApply` | `true` | Show and require approval of a batch rename or move preview |
| `auricFiles.safety.historyLimit` | 200 | Operations kept for undo |

Default protected paths:

```json
[
  "**/.git/**", "**/node_modules/**", "**/.env", "**/.env.*",
  "**/*.pem", "**/*.key", "**/package-lock.json", "**/yarn.lock", "**/pnpm-lock.yaml"
]
```

A plan that touches a protected path is blocked before any change is made. The safety settings are workspace configuration: in an untrusted workspace they come only from your user settings, and file-changing operations are disabled until you trust the folder.

After deleting into the workspace trash, **Open Workspace Trash** lists the item, and restoring it puts it back where it was.
