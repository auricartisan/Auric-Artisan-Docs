---
title: Auric Artisan Emoji — Reference
description: Every command, keybinding, setting, key, view, category, format and message in Auric Artisan Emoji 0.2.0.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Auric Artisan Emoji reference

This reference describes version 0.2.0 as published on the Visual Studio Marketplace.

## Commands

Category in the Command Palette: **Auric Artisan Emoji**.

| Command | ID | What it does |
| --- | --- | --- |
| Open Emoji Studio | `auricEmoji.openStudio` | Opens the full Studio in an editor tab. |
| Quick Insert Emoji | `auricEmoji.quickPick` | Searchable Quick Pick; inserts the chosen emoji. |
| Insert Recent Emoji | `auricEmoji.insertRecent` | Quick Pick of recent emoji. |
| Insert Favorite Emoji | `auricEmoji.insertFavorite` | Quick Pick of favorites. |
| Copy Last Emoji Again | `auricEmoji.copyLast` | Copies the last emoji used. |
| Replace Emoji Shortcodes in Selection | `auricEmoji.replaceShortcodes` | Replaces known `:shortcodes:` in the selection or current line. |
| Clear Emoji History | `auricEmoji.clearHistory` | Clears recents and last-emoji recall; keeps favorites. |
| Focus Emoji Search | `auricEmoji.focusSearch` | Focuses the Studio search box. |
| Choose Interface Language… | `auricEmoji.chooseInterfaceLanguage` | Auto, English or Hindi for the Studio. |

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command |
| --- | --- | --- |
| `Ctrl` + `Alt` + `E` | `Cmd` + `Alt` + `E` | Open Emoji Studio |
| `Ctrl` + `Alt` + `J` | `Cmd` + `Alt` + `J` | Quick Insert Emoji |

Both work anywhere in VS Code.

### Keys inside Emoji Studio

| Key | Action |
| --- | --- |
| `/` or `Ctrl` + `K` (`Cmd` + `K`) | Focus search |
| Arrow keys on a preview | Move through the grid |
| `Enter` on a preview | Click action |
| `Shift` + `Enter` on a preview | Copy |
| `Space` on a preview | Add to the sequence |
| `Backspace` outside text boxes | Remove the last sequence item |
| `F` on a preview | Toggle favorite |
| `I` on a preview | Open or close the inspector |
| `Escape` | Close the open panel, or clear the sequence |
| `?` | Open the keyboard map |

## Settings

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricEmoji.interfaceLanguage` | string | `auto`, `en`, `hi` | `auto` | Emoji Studio language. |
| `auricEmoji.clickAction` | string | `insert`, `copy`, `insertAndCopy` | `insert` | Primary action when an emoji is chosen. |
| `auricEmoji.insertSpacing` | string | `none`, `space`, `auto` | `auto` | Spacing added on editor insertion. |
| `auricEmoji.copyFormat` | string | `emoji`, `shortcode`, `unicode`, `html`, `javascript`, `css` | `emoji` | Format used by copy actions. |
| `auricEmoji.preferredSkinTone` | string | `none`, `medium`, `light`, `mediumLight`, `mediumDark`, `dark` | `none` | Default tone; `none` is standard yellow. |
| `auricEmoji.gridDensity` | string | `compact`, `comfortable`, `showcase` | `comfortable` | Card density. |
| `auricEmoji.showNames` | boolean | `true`, `false` | `true` | Show names on cards when space allows. |
| `auricEmoji.closeStudioAfterInsert` | boolean | `true`, `false` | `false` | Close the full Studio after inserting. |
| `auricEmoji.maxRecents` | integer | 8 to 200 | 48 | Recent emoji kept. |
| `auricEmoji.hover.enabled` | boolean | `true`, `false` | `true` | Preview and insert actions on `:shortcode:` hovers. |
| `auricEmoji.completions.enabled` | boolean | `true`, `false` | `true` | Completions after typing `:`. |
| `auricEmoji.statusBar.enabled` | boolean | `true`, `false` | `true` | The **Emoji** status bar button. |

## Views and menus

| Place | Contents |
| --- | --- |
| Activity Bar | **Auric Emoji** container with the **Emoji Studio** view. |
| View title bar | **Open Emoji Studio**, **Focus Emoji Search**; **…** menu: **Choose Interface Language…**. |
| Editor right-click | **Quick Insert Emoji**; **Replace Emoji Shortcodes in Selection** (with a selection). |
| Status bar | **Emoji** (smiley icon), tooltip "Open Auric Emoji Studio". |
| Editor tab | **Emoji Studio**, beside the active editor. |

## Studio controls

| Control | Options |
| --- | --- |
| Tabs | **01 Library**, **02 For you**, **03 Favorites**, **04 Recent** |
| Category | **All**, Smileys & Emotion, People & Body, Animals & Nature, Food & Drink, Travel & Places, Activities, Objects, Symbols, Flags |
| Skin tone | Yellow, Light, Medium light, Medium, Medium dark, Dark |
| Quick filter | All, Curated, Skin tone, Newest |
| Density | Compact, Comfortable, Showcase |
| Layout | Grid, List |
| Compose | On or off |
| Card | Insert, Copy, … (inspector), heart |
| Sequence tray | **Copy sequence**, **Insert sequence**, **Clear** |
| Inspector | Tones, **Make {tone} my default**, **Copy as** ledger, **Make {format} my copy format**, **Insert**, **Copy**, **Favorite**, **Also try** |
| Workspace overview | **Quick insert**, **Replace shortcodes**, **Keyboard map →**, **Insert {emoji} again**, **Clear history** |
| Footer | **Keyboard map**, **Settings** |

## Catalog

| Item | Value |
| --- | --- |
| Emoji | 1,914 |
| Categories | 9 |
| Tone-capable entries | 330 |
| Sequence length | Up to 50 |

## Messages you may see

| Message | Meaning |
| --- | --- |
| No editor was active, so … was copied. | Studio insertion fell back to the clipboard. |
| … copied because no writable editor was active. | A command's insertion fell back to the clipboard. |
| …: no saved emoji yet. | The recent or favorite list is empty. |
| Use an emoji first, then Copy Last Emoji Again. | Nothing to copy yet. |
| Open a text editor before replacing emoji shortcodes. | No editor for shortcode replacement. |
| No recognized :emoji_shortcodes: were found. | Nothing to replace. |
| A sequence holds up to 50 emoji. | The sequence is full. |
| Recent emoji cleared. | History was cleared. |
