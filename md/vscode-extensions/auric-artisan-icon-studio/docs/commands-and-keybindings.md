---
title: Auric Artisan Icon Studio — Commands and keybindings
description: Use Icon Studio from the Command Palette and keyboard, including Quick Pick insertion and a fixed icon bound to a key.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Commands and keybindings

You can use Icon Studio without opening its panel. Open the Command Palette (`Ctrl` + `Shift` + `P`) and type "Auric Icon Studio".

## Search everything and choose an action

1. Run **Auric Icon Studio: Search All Icons…** (also the search icon in the sidebar title bar).
2. A Quick Pick opens. With an empty search and recommendations on, it starts with **Recommended for this file**, then **All icons**. Each row shows the icon, its collection, category and tags.
3. Type to search. Up to 200 results are listed.
4. Choose an icon, then choose an action:
   - **Smart Insert (matches this file)**
   - **Insert**
   - **Copy**
   - **Copy As…**
   - **Save as SVG…** (SVG artwork only)
   - **Toggle Like**

## Smart insert with one shortcut

1. Place the cursor in a text editor.
2. Press `Ctrl` + `Alt` + `I` (`Cmd` + `Alt` + `I` on macOS), or run **Auric Icon Studio: Smart Insert Icon (matches active language)**. It is also on the editor's right-click menu.
3. Choose an icon. It is inserted in the format that suits the file.

## Insert from Recent or Likes

- Press `Ctrl` + `Alt` + `R` (`Cmd` + `Alt` + `R` on macOS) or run **Insert from Recent**.
- Run **Insert from Likes** (also the heart icon in the sidebar title bar).

Both run the action set in `auricIconStudio.clickAction`: **insert** (default), **copy**, or **insert and copy**. If the list is empty, you see "Icon Studio: no recent icons yet." or a prompt to like an icon first.

## Other commands

| Command | What it does |
| --- | --- |
| **Open Icon Studio** | Opens the editor-tab Studio beside your editor. |
| **Copy Icon As…** | Choose an icon, then a format, and copy. |
| **Save Icon as SVG…** | Choose an SVG icon and save it through a dialog. |
| **Clear Likes, Recents and Learned Recommendations** | After confirmation (**Clear**), resets Icon Studio's personalisation. |

Keyboard shortcuts need editor focus. When you have chosen to keep the separate Auric collection libraries, Icon Studio's shortcuts step aside for theirs (see [Work with the Auric collection extensions](auric-collections.md)).

## Insert a specific icon from a keybinding

The command `auricIconStudio.insertIcon` inserts one icon by its catalog ID. It is hidden from the Command Palette and meant for keybindings and macros.

1. Open **Preferences: Open Keyboard Shortcuts (JSON)**.
2. Add an entry such as:

```json
{
  "key": "ctrl+alt+shift+r",
  "command": "auricIconStudio.insertIcon",
  "args": {
    "id": "tabler-rocket",
    "format": "jsx"
  }
}
```

| Argument | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | The catalog ID. You can also pass the ID as a plain string instead of an object. |
| `variant` | No | A style ID for that collection, such as `outline`. |
| `format` | No | An output format ID. If omitted, smart insert rules apply. |

Format IDs: `raw`, `jsx`, `jsxComponent`, `js`, `img`, `markdown`, `css`, `dataUri`, `name` (SVG artwork); `html`, `jsx`, `jsxComponent`, `js`, `css`, `name` (Material); `emoji`, `shortcode`, `unicode`, `html` (emoji).

To find an icon's ID, copy it with **As…** › **Icon ID** rather than guessing. An unknown ID shows "Icon Studio: unknown icon id …".

## Result

You can search, insert, copy and save icons entirely from the keyboard, and bind a favourite icon to its own shortcut.
