---
title: Auric Artisan File System — rename, move and copy
description: Rename, move, copy and duplicate files one at a time or in batches, convert extensions, and review every change before it happens.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Rename, move and copy

These commands are in the **Edit & batch** group of the workspace panel and the **Auric Files** › **Edit and Batch** submenu. They need a trusted workspace. VS Code's own **Rename** (`F2`) and drag-and-drop in the Explorer keep working as usual; the Auric versions add collision planning, protection, confirmations and undo.

| Command | Use it to |
| --- | --- |
| **Rename…** | Rename the selected item |
| **Rename Current File** | Rename the file open in the editor |
| **Move…** / **Move Current File** | Move items, or the current file, to another folder |
| **Copy To…** | Copy items to another folder |
| **Duplicate** / **Duplicate Current File** | Make a copy beside the original |
| **Batch Rename…** | Rename many files by a rule, with a preview |
| **Batch Move…** | Move many items to one folder |
| **Convert Extension…** | Change the extension of many files |

**Rename…**, **Move…**, **Copy To…** and **Duplicate** act on the selection and run from the panel, the context menus or the shortcut deck; they are not listed in the Command Palette. The "Current File" versions act on the editor's file.

## Before anything changes

Every operation is planned first:

- **Protected paths.** Anything matching `auricFiles.safety.protectedPaths` cannot be renamed, moved or deleted. By default that covers `.git`, `node_modules`, `.env` files, `.pem` and `.key` files, and the npm, Yarn and pnpm lockfiles. A plan that touches one is blocked before any byte is written.
- **Collisions.** A target that already exists is a conflict and is reported. Nothing is overwritten silently.
- **Case-only renames** (`button.ts` to `Button.ts`) on a case-insensitive file system are applied as two renames, and the preview says so.
- **Git warnings.** Moving or deleting a file tracked by Git (`auricFiles.safety.warnOnGitTracked`) or with uncommitted edits (`auricFiles.safety.warnOnUncommittedChanges`) shows a warning first.
- **Bulk confirmation.** An operation touching at least `auricFiles.safety.confirmBulk` paths (default 5) asks first. Set it to `0` to be asked every time.
- **History.** The operation is recorded so **Undo Last File Operation** can reverse it.

## Rename one file

1. Right-click the file and choose **Auric Files** › **Edit and Batch** › **Rename Current File**, or run **Auric Files: Rename Current File** with the file open.
2. Type the new name.
3. The file is renamed; tags, groups and other Auric metadata follow it.

## Batch rename

1. Select the files in the Explorer (hold `Ctrl` or `Shift` while clicking).
2. Run **Auric Files: Batch Rename…**.
3. Answer **How should *N* files be renamed?**:

| Mode | What it does | You then enter |
| --- | --- | --- |
| **Find and replace** | Replace literal text | **Find**, then **Replace with** |
| **Regular expression** | Replace by pattern; use `$1`, `$2` for capture groups | **Find** (a regular expression), then **Replace with** |
| **Pattern** | Build each name from tokens | **Pattern**, for example `{parent}-{name}{ext}` |
| **Sequence** | Number the files | A pattern; the default is `{name}-{n}{ext}` |
| **Change case** | Change the letter case | A style: `kebab`, `camel`, `pascal`, `snake`, `upper`, `lower`, `title` |
| **Change extension** | Swap one extension for another | The extension to replace (blank for any), then the new one |

4. Review **Batch Rename — preview**: *N* files would change, with any problems counted. Each row shows the old name and, with an arrow, the new one; rows with a problem show a warning and the reason.
5. Choose **Apply** to rename, or press `Escape` to cancel.

With `auricFiles.safety.previewBeforeApply` on (the default), the preview is always shown and needs your approval.

### Pattern tokens

| Token | Replaced with |
| --- | --- |
| `{name}` | The file name without its extension (compound extensions such as `.test.ts` count as one) |
| `{ext}` | The extension, including the dot |
| `{n}` | A running number, starting at 1 |
| `{index}` | The file's position in the selection, starting at 0 |
| `{parent}` | The parent folder's name |
| `{date}` | Today's date as YYYY-MM-DD |
| `{rand}` | Six random letters and digits |

### Regular expressions

The preview updates as you type. A pattern that is too slow to preview stops the batch with **Pattern is too slow to preview; simplify it.** Patterns are limited to 512 characters.

## Move or copy

1. Select the items and run **Move…**, **Batch Move…** or **Copy To…** (or **Move Current File** for the editor's file).
2. **Choose the destination** from the folders in the workspace, or choose **Browse…** to pick a folder on disk.
3. Confirm if asked.

Moved items keep their tags, groups and other Auric metadata.

## Duplicate

**Duplicate** (or **Duplicate Current File**) makes a copy beside the original under a name that does not clash with an existing file.

## Convert extensions

1. Select the files and run **Auric Files: Convert Extension…**.
2. **Which extension should change?** Choose one of the extensions in the selection, or **Any extension**.
3. Type the **New extension**, for example `.ts`.
4. Review the preview and choose **Apply**.

Converting renames files only; it does not change their contents.

## Undo

Every rename, move, copy and duplicate made through Auric Files can be undone with **Auric Files: Undo Last File Operation**. See [History, undo and the workspace trash](history-and-workspace-trash.md).

After a batch rename, the Explorer shows the new names, and **Show Operation History** lists the rename as one operation.
