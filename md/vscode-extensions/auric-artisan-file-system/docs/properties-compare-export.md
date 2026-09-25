---
title: Auric Artisan File System — properties, compare and export
description: Inspect a file's properties, compare and merge files, copy paths, and export a JSON manifest of a selection.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Properties, compare and export

These commands are in the **Inspect & navigate** group of the workspace panel and the **Auric Files** › **Navigate and Paths** submenu.

## Properties

**Properties** shows the facts about a file or folder in one place: what the file system reports, plus what Auric Files knows about it. It reads metadata only, never the file's contents.

### Open it

- Right-click a file or folder in the Explorer and choose **File Properties** (the first entry in the menu).
- Press `Alt` + `Enter` with the Explorer focused.
- Run **Auric Files: File Properties**. If VS Code does not pass a selected file (some keyboard routes do not), a resource picker opens.
- In the workspace panel or the **Auric Files** sidebar, choose **02 Properties**.

Properties opens inside the existing workspace panel or sidebar rather than a new tab.

### What it shows

**General**

| Row | Meaning |
| --- | --- |
| **Name** | The file or folder name |
| **Full path** | The complete path (or URI for remote and virtual files) |
| **Type** | The extension in capitals (for example `TSX`), **Folder** or **Symbolic link** |
| **Size** | The reported size; folders show **Folder** (this is not a recursive disk-usage total) |
| **Created** | Creation time, where the file system records one; otherwise **Unavailable** |
| **Modified** | Last modification time |

**Organisation**

| Row | Meaning |
| --- | --- |
| **Tags** | Tags assigned to the item, or **None** |
| **Group / workspace** | Groups and virtual folders it belongs to |
| **Related files** | Up to six existing companions, such as its test or stylesheet. Before the index is built: **Not indexed yet** |

**Access & history**

| Row | Meaning |
| --- | --- |
| **Owner / creator** | **Not exposed by the VS Code file-system provider**; never guessed |
| **Permissions** | **Read-only** if the file system reports it, otherwise **No read-only flag reported**; plus **protected by Auric** for protected paths |
| **Git status** | The state from the last index, labelled as such, or **Unavailable** |
| **Version** | How many Auric operations touched the item and the latest one, or **No Auric operation history** |

### Buttons

- **Refresh** — re-read the file-system facts. (To update related files and Git state, refresh the workspace index with **Auric Files: Refresh**.)
- **Copy path** — copy the full path.
- **Edit tags…** — assign or remove tags.
- **Add to group…** — add the item to a group.

A resource outside the open workspace can be inspected, but file actions on it are blocked: **This resource is outside the workspace. Properties are available; choose an in-workspace resource to use file actions.**

## Compact hovers in the Explorer

Hovering an item in the Explorer shows a short summary: its name and size, and a reminder that Properties has the rest. Tagged, favourite, pinned, highlighted and hidden items say so in the hover.

Switch the summaries off and on with **Auric Files: Toggle File Metadata** (`Ctrl` + `Shift` + `M` with the Explorer focused). When off, the hover says **Metadata is hidden. Press Ctrl+Shift+M to show it.**

## Compare two files

1. Select exactly two files in the Explorer.
2. Run **Auric Files: Compare Selected Files** (`Ctrl` + `Alt` + `Shift` + `D` with the deck).
3. VS Code's diff editor opens with the first file on the left and the second on the right.

Selecting anything other than two files shows **Select exactly two files in VS Code Explorer to compare.**

## Merge files

1. Select two files, or three: a base file followed by two inputs.
2. Run **Auric Files: Merge Selected Files**.
3. VS Code's merge editor opens. With three files, the first is the base and the result; with two, the first file is both base and result.
4. Resolve the changes and save the merge editor. Nothing is written until you save.

This needs a trusted workspace. Some VS Code-based editors do not provide the merge editor; you then see **This VS Code-compatible editor does not expose the merge editor.**

## Copy paths and reveal

| Command | What it copies or does | Deck shortcut |
| --- | --- | --- |
| **Copy Relative Path** | The path from the workspace folder | `Ctrl` + `Alt` + `Shift` + `C` |
| **Copy Absolute Path** | The full path on disk | `Ctrl` + `Alt` + `Shift` + `A` |
| **Copy File URI** | The file's URI (`file:///…`) | `Ctrl` + `Alt` + `A`, then `U` |
| **Reveal in File Manager** | Shows the file in your operating system's file manager | `Ctrl` + `Alt` + `A`, then `V` |
| **Reveal in VS Code Explorer** | Selects the file in the Explorer | `Ctrl` + `Alt` + `A`, then `Shift` + `V` |

**Reveal in File Manager** is not available in virtual workspaces.

## Export a selection

**Export Selected Items…** saves a JSON *manifest*: a list describing the selected items and their metadata. It is not an archive of the files' contents.

1. Select files and folders in the Explorer.
2. Run **Auric Files: Export Selected Items…** (`Ctrl` + `Alt` + `A`, then `Shift` + `X` with the deck).
3. Choose where to save. The default name is `auric-selection.json`.

The manifest looks like this:

```json
{
  "format": "auric-artisan-selection",
  "version": 1,
  "workspace": "my-project",
  "exportedAt": "2026-09-25T10:00:00.000Z",
  "items": [
    {
      "name": "Button.tsx",
      "path": "src/components/Button.tsx",
      "uri": "file:///…/src/components/Button.tsx",
      "type": "file",
      "extension": ".tsx",
      "size": 1834,
      "created": "2026-09-20T08:12:00.000Z",
      "modified": "2026-09-24T16:40:00.000Z",
      "owner": null,
      "tags": ["UI"],
      "groups": ["Checkout"],
      "related": ["src/components/Button.test.tsx"],
      "versions": 2,
      "permissions": "writable",
      "gitStatus": "clean"
    }
  ]
}
```

`owner` is always `null` because the file system does not report it. Values that are not available are `null`.

When the export finishes, a message confirms how many items were exported and where.
