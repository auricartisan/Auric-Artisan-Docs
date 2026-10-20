---
title: Auric Artisan Emoji — Insert from the editor
description: Insert emoji without opening the Studio, using Quick Insert, shortcode completions, code hovers, shortcode replacement and the recent and favorite pickers.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Insert from the editor

## Quick Insert

1. Place the cursor (or several cursors) in a text file.
2. Press `Ctrl` + `Alt` + `J` (`Cmd` + `Alt` + `J`), run **Auric Artisan Emoji: Quick Insert Emoji**, or right-click › **Quick Insert Emoji**.
3. Search names, shortcodes, categories or Unicode, and choose an emoji.

Quick Insert uses your preferred skin tone and spacing.

## Shortcode completions

Type `:` followed by part of a name. Suggestions appear:

```text
:spa      → sparkles     :sparkles:
:rock     → rocket       :rocket:
:thinking → thinking face :thinking_face:
```

Accept a suggestion to insert the emoji. Turn completions off with `auricEmoji.completions.enabled`.

## Hover over a shortcode

1. Write a complete shortcode with both colons, such as `:rocket:` or `:waving_hand:`.
2. Hover over it. The hover shows a preview.
3. Choose **Insert emoji**, **JavaScript** or **HTML**.

```js
// Before: hover over :rocket: inside the string
const launch = ":rocket:";

// After choosing Insert emoji
const launch = "(the rocket emoji character)";
```

- Only the hovered shortcode is replaced, in one undo step. Quotes, other cursors and surrounding code are untouched, and no whitespace is added.
- The emoji uses the skin tone shown in the preview.
- If the document changes before you click, hover again for a fresh action. An action cannot be reused after it has inserted.
- Unlike Studio insertion, a failed hover edit does not fall back to the clipboard.
- Needs VS Code's editor hovers and `auricEmoji.hover.enabled` to be on.

## Replace several shortcodes

1. Select text containing shortcodes. With no selection, the current line is used.
2. Run **Auric Artisan Emoji: Replace Emoji Shortcodes in Selection**, or right-click › **Replace Emoji Shortcodes in Selection** (shown when text is selected).

```text
Before: Ready to ship :rocket: :sparkles:
After:  Ready to ship (rocket emoji) (sparkles emoji)
```

Unknown tokens are left unchanged. If none are recognised, you see "No recognized :emoji_shortcodes: were found." Without an editor you see "Open a text editor before replacing emoji shortcodes."

## Recent, favorite and last emoji

| Command | What it does |
| --- | --- |
| **Insert Recent Emoji** | Pick from your recent emoji and insert. |
| **Insert Favorite Emoji** | Pick from your favorites and insert. |
| **Copy Last Emoji Again** | Copy the last emoji you used. If none, "Use an emoji first, then Copy Last Emoji Again." |

If a list is empty you see "…: no saved emoji yet."

## Spacing

`auricEmoji.insertSpacing` controls editor insertion:

| Value | Behaviour |
| --- | --- |
| `auto` (default) | Adds a space only when adjacent text would touch the emoji. |
| `space` | Appends one space. |
| `none` | Inserts only the emoji, for exact string contents. |

Hover replacement leaves surrounding whitespace unchanged whatever this setting says.

## Result

You can add emoji anywhere you type without leaving the editor.
