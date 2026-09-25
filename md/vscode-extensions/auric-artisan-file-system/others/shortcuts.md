---
title: Auric Artisan File System — keyboard shortcuts
description: Every keyboard shortcut Auric Artisan File System declares, the six that are always on and the optional deck.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Shortcuts

Auric Files declares 69 shortcuts. Six are always on while the Explorer has focus. The other 63 form the optional *deck*, which is off by default so the extension does not claim `Ctrl` + `Alt` combinations across VS Code. Turn the deck on with:

```json
{ "auricFiles.keyboard.enableDefaultShortcuts": true }
```

Deck shortcuts work when a folder is open; a few (such as **Rename Current File**) need an editor to be open. Every command is also available from menus and the Command Palette, and you can assign or change any shortcut in **Preferences: Open Keyboard Shortcuts** by searching for `auricFiles`.

Some commands have both a direct shortcut and a chord. A *chord* is two key presses in a row: the first combination, then a second key.

## Always on (Explorer focused)

| Windows and Linux | macOS | Command |
| --- | --- | --- |
| `Ctrl` + `N` | `Cmd` + `N` | **New File…** |
| `Ctrl` + `Shift` + `N` | `Cmd` + `Shift` + `N` | **New Folder…** |
| `Alt` + `Enter` | `Alt` + `Enter` | **File Properties** |
| `Ctrl` + `Shift` + `M` | `Cmd` + `Shift` + `M` | **Toggle File Metadata** |
| `Alt` + `S` | `Alt` + `S` | **Sort** |
| `Ctrl` + `Alt` + `B` | `Cmd` + `Alt` + `B` | **Batch Structure…** |

## Deck: direct shortcuts

| Windows and Linux | macOS | Command |
| --- | --- | --- |
| `Ctrl` + `Alt` + `Shift` + `D` | `Cmd` + `Alt` + `Shift` + `D` | **Compare Selected Files** |
| `Ctrl` + `Alt` + `E` | `Cmd` + `Alt` + `E` | **Focus VS Code Explorer** |
| `Ctrl` + `Alt` + `O` | `Cmd` + `Alt` + `O` | **Quick Open in Auric Files…** |
| `Ctrl` + `Alt` + `N` | `Cmd` + `Alt` + `N` | **New Sibling File** |
| `Ctrl` + `Alt` + `Shift` + `N` | `Cmd` + `Alt` + `Shift` + `N` | **Batch Create Folders…** |
| `Ctrl` + `Alt` + `D` | `Cmd` + `Alt` + `D` | **Duplicate Current File** |
| `Ctrl` + `Alt` + `Shift` + `R` | `Cmd` + `Alt` + `Shift` + `R` | **Rename Current File** |
| `Ctrl` + `Alt` + `Shift` + `M` | `Cmd` + `Alt` + `Shift` + `M` | **Move Current File** |
| `Ctrl` + `Alt` + `Shift` + `Backspace` | `Cmd` + `Alt` + `Shift` + `Backspace` | **Delete (Workspace Trash)** |
| `Ctrl` + `Alt` + `Shift` + `C` | `Cmd` + `Alt` + `Shift` + `C` | **Copy Relative Path** |
| `Ctrl` + `Alt` + `Shift` + `A` | `Cmd` + `Alt` + `Shift` + `A` | **Copy Absolute Path** |
| `Ctrl` + `Alt` + `R` | `Cmd` + `Alt` + `R` | **Go to Related File…** |
| `Ctrl` + `Alt` + `Z` | `Cmd` + `Alt` + `Z` | **Undo Last File Operation** |
| `Ctrl` + `Alt` + `Y` | `Cmd` + `Alt` + `Shift` + `Z` | **Redo File Operation** |
| `Ctrl` + `Alt` + `Shift` + `E` | `Cmd` + `Alt` + `Shift` + `E` | **Open File Workspace** |
| `Ctrl` + `Alt` + `Shift` + `F` | `Cmd` + `Alt` + `Shift` + `F` | **Batch Create Files…** |

## Deck: chords

Press `Ctrl` + `Alt` + `A` (`Cmd` + `Alt` + `A` on macOS), release, then press the second key.

| Windows and Linux | macOS | Command |
| --- | --- | --- |
| `Ctrl` + `Alt` + `A`, then `N` | `Cmd` + `Alt` + `A`, then `N` | **New Sibling File** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `N` | `Cmd` + `Alt` + `A`, then `Shift` + `N` | **New Child File** |
| `Ctrl` + `Alt` + `A`, then `F` | `Cmd` + `Alt` + `A`, then `F` | **Batch Create Files…** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `F` | `Cmd` + `Alt` + `A`, then `Shift` + `F` | **Batch Create Folders…** |
| `Ctrl` + `Alt` + `A`, then `B` | `Cmd` + `Alt` + `A`, then `B` | **Batch Structure…** |
| `Ctrl` + `Alt` + `A`, then `Ctrl` + `N` | `Cmd` + `Alt` + `A`, then `Cmd` + `N` | **New File…** |
| `Ctrl` + `Alt` + `A`, then `Ctrl` + `Shift` + `N` | `Cmd` + `Alt` + `A`, then `Cmd` + `Shift` + `N` | **New Folder…** |
| `Ctrl` + `Alt` + `A`, then `T` | `Cmd` + `Alt` + `A`, then `T` | **New File from Template…** |
| `Ctrl` + `Alt` + `A`, then `P` | `Cmd` + `Alt` + `A`, then `P` | **New from Framework Preset…** |
| `Ctrl` + `Alt` + `A`, then `R` | `Cmd` + `Alt` + `A`, then `R` | **Create Related Files…** |
| `Ctrl` + `Alt` + `A`, then `E` | `Cmd` + `Alt` + `A`, then `E` | **Rename Current File** |
| `Ctrl` + `Alt` + `A`, then `D` | `Cmd` + `Alt` + `A`, then `D` | **Duplicate Current File** |
| `Ctrl` + `Alt` + `A`, then `M` | `Cmd` + `Alt` + `A`, then `M` | **Move Current File** |
| `Ctrl` + `Alt` + `A`, then `C` | `Cmd` + `Alt` + `A`, then `C` | **Copy To…** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `R` | `Cmd` + `Alt` + `A`, then `Shift` + `R` | **Batch Rename…** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `M` | `Cmd` + `Alt` + `A`, then `Shift` + `M` | **Batch Move…** |
| `Ctrl` + `Alt` + `A`, then `X` | `Cmd` + `Alt` + `A`, then `X` | **Convert Extension…** |
| `Ctrl` + `Alt` + `A`, then `Backspace` | `Cmd` + `Alt` + `A`, then `Backspace` | **Delete (Workspace Trash)** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `Backspace` | `Cmd` + `Alt` + `A`, then `Shift` + `Backspace` | **Delete Permanently** |
| `Ctrl` + `Alt` + `A`, then `O` | `Cmd` + `Alt` + `A`, then `O` | **Go to Related File…** |
| `Ctrl` + `Alt` + `A`, then `V` | `Cmd` + `Alt` + `A`, then `V` | **Reveal in File Manager** |
| `Ctrl` + `Alt` + `A`, then `L` | `Cmd` + `Alt` + `A`, then `L` | **Copy Relative Path** |
| `Ctrl` + `Alt` + `A`, then `A` | `Cmd` + `Alt` + `A`, then `A` | **Copy Absolute Path** |
| `Ctrl` + `Alt` + `A`, then `U` | `Cmd` + `Alt` + `A`, then `U` | **Copy File URI** |
| `Ctrl` + `Alt` + `A`, then `G` | `Cmd` + `Alt` + `A`, then `G` | **Tag Files…** |
| `Ctrl` + `Alt` + `A`, then `K` | `Cmd` + `Alt` + `A`, then `K` | **Add to Group…** |
| `Ctrl` + `Alt` + `A`, then `1` | `Cmd` + `Alt` + `A`, then `1` | **Toggle Favorite** |
| `Ctrl` + `Alt` + `A`, then `2` | `Cmd` + `Alt` + `A`, then `2` | **Toggle Pinned** |
| `Ctrl` + `Alt` + `A`, then `3` | `Cmd` + `Alt` + `A`, then `3` | **Toggle Native Explorer Exclusion** |
| `Ctrl` + `Alt` + `A`, then `4` | `Cmd` + `Alt` + `A`, then `4` | **Toggle Highlight** |
| `Ctrl` + `Alt` + `A`, then `Q` | `Cmd` + `Alt` + `A`, then `Q` | **Open Matching Test** |
| `Ctrl` + `Alt` + `A`, then `S` | `Cmd` + `Alt` + `A`, then `S` | **Open Matching Style** |
| `Ctrl` + `Alt` + `A`, then `W` | `Cmd` + `Alt` + `A`, then `W` | **Open Matching Story** |
| `Ctrl` + `Alt` + `A`, then `I` | `Cmd` + `Alt` + `A`, then `I` | **Open Matching Component** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `D` | `Cmd` + `Alt` + `A`, then `Shift` + `D` | **Open Matching Documentation** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `V` | `Cmd` + `Alt` + `A`, then `Shift` + `V` | **Reveal in VS Code Explorer** |
| `Ctrl` + `Alt` + `A`, then `Z` | `Cmd` + `Alt` + `A`, then `Z` | **Undo Last File Operation** |
| `Ctrl` + `Alt` + `A`, then `Y` | `Cmd` + `Alt` + `A`, then `Y` | **Redo File Operation** |
| `Ctrl` + `Alt` + `A`, then `H` | `Cmd` + `Alt` + `A`, then `H` | **Show Operation History** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `T` | `Cmd` + `Alt` + `A`, then `Shift` + `T` | **Open Workspace Trash** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `U` | `Cmd` + `Alt` + `A`, then `Shift` + `U` | **Restore from Trash…** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `Delete` | `Cmd` + `Alt` + `A`, then `Shift` + `Delete` | **Empty Workspace Trash** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `C` | `Cmd` + `Alt` + `A`, then `Shift` + `C` | **Compare Selected Files** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `G` | `Cmd` + `Alt` + `A`, then `Shift` + `G` | **Merge Selected Files** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `X` | `Cmd` + `Alt` + `A`, then `Shift` + `X` | **Export Selected Items…** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `E` | `Cmd` + `Alt` + `A`, then `Shift` + `E` | **Open File Workspace** |
| `Ctrl` + `Alt` + `A`, then `Shift` + `S` | `Cmd` + `Alt` + `A`, then `Shift` + `S` | **Open Settings** |

## In the workspace panel

| Keys | What they do |
| --- | --- |
| `Escape` in **Find an action** | Clear the search |
| `Tab`, `Enter`, `Space` | Move between and use buttons and group headings |
| Mouse wheel, arrow keys | Scroll the panel |

## Native VS Code keys that still apply

`F2` renames in the Explorer with VS Code's own rename, and drag-and-drop moves files as usual. These native actions are not recorded in Auric's operation history.
