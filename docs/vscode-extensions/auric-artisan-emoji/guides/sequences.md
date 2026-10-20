---
title: Auric Artisan Emoji — Compose a sequence
description: Collect up to 50 emoji in Emoji Studio and insert or copy them together.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Compose a sequence

A **sequence** is a short list of emoji you collect and then insert or copy in one go, for example rocket, sparkles and party popper.

## Build a sequence

Use any of these:

- Focus an emoji and press `Space`.
- `Shift`-click an emoji's preview.
- In the full Studio, turn on **Compose**. The switch shows "Composing · {count}", and selecting emoji adds them.

The **Sequence** tray appears with the count and the emoji. Cards show "In the sequence {n}×". A sequence holds up to 50 emoji, repeats included; beyond that you see "A sequence holds up to 50 emoji."

## Edit it

- `Backspace` (outside text boxes) removes the last emoji.
- Select an emoji in the tray to remove it.
- `Escape` clears the sequence (after closing any open panel), or select **Clear**.

## Use it

| Button | Result |
| --- | --- |
| **Insert sequence** | Inserts the emoji characters at your cursors. "Inserted {n} emoji: …" |
| **Copy sequence** | Copies in your copy format. "Copied {n} emoji: …" |

When copying, shortcodes, Unicode labels and CSS escapes are separated by spaces; emoji, HTML entities and JavaScript escapes are joined directly. If no editor is active, **Insert sequence** copies instead.

The sequence is restored if the Studio reloads, and changing the interface language keeps it.

## Result

Your collected emoji are in your file or on your clipboard in one step.
