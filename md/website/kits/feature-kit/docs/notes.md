---
title: Feature Kit — Notes
description: Keep Markdown notes in the Feature Kit that save as you type, preview them, copy them and export them as .md files.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Keep notes

**Notes** is a scratchpad inside the Feature Kit. You can keep several notes, write them in Markdown, preview the formatting, and copy or export any note. Notes save automatically in your browser, so they are there the next time you open the kit on any page.

## Open Notes

Select the **Notes** card on the Feature Kit menu, or press `4` on the menu.

The first time, you see one note called **Scratchpad** containing a short example.

## The screen

- **Note tabs** along the top, one per note, named after the note's first line. A **+** button at the end adds a note.
- A toolbar with **Edit** and **Preview** on the left and **Copy**, **Export** and **Delete** on the right.
- The editor, or the preview when **Preview** is selected.
- A status line at the bottom: **Saving…** while you type, then **Saved ·** and the time.

## Write a note

1. Select the editor.
2. Type. The placeholder reminds you of the syntax: `# Title`, `**bold**`, `*italic*`, `` `code` ``, `- lists`, `- [ ] tasks`.
3. Stop typing for a moment. The status changes from **Saving…** to **Saved ·** and the time.

The note's tab takes its name from the first non-empty line, without any leading `#`, cut to 24 characters. An empty note is called **Untitled**.

## Add a note

Select **+** (**New note**). An empty note opens at the front of the tabs, in edit mode, with the cursor in the editor.

## Switch between notes

Select a note's tab.

## Preview the formatting

Select **Preview** to see the note formatted. Select **Edit** to go back to editing.

The preview understands this Markdown:

| You type | You get |
|---|---|
| `# Heading` to `#### Heading` | Headings, levels 1 to 4 |
| `**bold**` | Bold text |
| `*italic*` | Italic text |
| `` `code` `` | Inline code |
| A line of three backticks before and after | A code block |
| `- item` or `* item` | A bulleted list |
| `- [ ] task` and `- [x] task` | An open task and a done task, shown with empty and ticked boxes |
| `[label](https://example.com)` | A link that opens in a new tab (only links starting with `http:` or `https:`) |

Anything else shows as plain paragraphs. Any HTML you type is shown as text, not run.

## Copy a note

Select **Copy**. The status line reads **Copied** (or **Copy failed** if your browser blocked clipboard access). The raw Markdown is copied.

## Export a note

Select **Export**. Your browser downloads the note as a Markdown file named after the note's title, for example `Scratchpad.md`. Characters that are not letters, digits, hyphens or underscores in the title become hyphens in the file name.

## Delete a note

Select **Delete**. The note is removed at once, without a confirmation, and the first remaining note opens.

If it is your only note, **Delete** empties it instead and renames it **Untitled**.

> **Important:** Deleting cannot be undone. Export a note first if you might need it.

## Where notes are kept

Notes are saved in your browser for auricartisan.com. They are not sent anywhere and not linked to your account. They are lost if you clear the site's data in your browser, and they are not available in another browser or on another device. Export notes you want to keep.

## Related

- [Reference](reference.md)
- [Privacy](../others/privacy.md)
