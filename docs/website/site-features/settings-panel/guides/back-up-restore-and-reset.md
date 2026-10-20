---
title: Settings panel — Back up, restore and reset
description: Export your settings to a file, import them on another browser, restore one section, reset everything, and use the panel's right-click menu.
product: Website › Site features › Settings panel
updated: 2026-09-25
---

# Back up, restore and reset

Your settings live in this browser only. Clearing the browser's site data, using a private window or switching to another browser starts you from the defaults. A settings file lets you carry them across.

## Export your settings

1. Open the panel (`Ctrl` + `,`).
2. Select **Export** in the footer.
3. Your browser downloads a file named `auric-settings.json`. A message confirms "Settings exported".

The file contains every setting in the panel, including your saved colours. It is plain JSON (see [Reference](reference.md#the-settings-file) for its fields). It contains no account details.

## Import settings from a file

1. Open the panel on the browser you want to set up.
2. Select **Import** in the footer.
3. Choose an `auric-settings.json` file (any `.json` file is accepted for selection).
4. The settings apply at once, including the theme. A message confirms "Settings imported".

What happens to the file's contents:

- Only settings the panel knows are read. Anything else in the file is ignored.
- A setting missing from the file is set to its default.
- A value that is not allowed (for example a text size that does not exist) is replaced by that setting's default.
- If the file is not valid JSON, nothing changes and the message reads "That file isn't valid settings". If the file cannot be read, the message reads "Couldn't read that file".

You can import the same file again later; the panel accepts a repeat of the same file.

## Restore one section

Every section except Shortcuts ends with **Restore section defaults**. It resets only that section's settings. For example, in Comfort it turns every switch back to its default and leaves your accent colour alone. A message names the section, for example "Clock restored to defaults".

| Section | What its restore resets |
|---|---|
| Appearance | Accent, theme and text size (not language, not saved colours) |
| Comfort | Reading mode, reduce motion, reduce transparency, boost contrast, underline links, custom cursor, eye-rest reminders and interval, screen saver and delay |
| Highlights | Live demo chips, welcome bar, announcement bar, quick links bar, clock strip, hero notice |
| Clock | 24-hour time, show seconds, show date, timezone, date format |
| Tooltips | Show tooltips, detailed tooltips, advanced tooltips |
| Ads | Show ads, ad density, ads in panels & search |

## Reset everything

1. Select **Reset all** in the footer.
2. A confirmation covers the panel: "Reset **all** settings to their defaults? Your accent, theme, comfort and clock preferences will be cleared."
3. Select **Reset all** to confirm, or **Cancel** (or press `Esc`, or click outside the card) to keep your settings.

After a reset, a message confirms "All settings reset to defaults". Your **saved colours are kept**, because they are a palette you built rather than a preference. Remove them one by one with the X on each swatch if you want them gone.

> **Tip:** Export your settings before a reset if you might want them back.

## Use the panel's right-click menu

Right-clicking inside the Settings panel opens a small menu of its own instead of the site's page menu.

- The heading shows the name of the setting you right-clicked, or **Settings** if you right-clicked elsewhere in the panel.
- **This setting** (only when you right-clicked a switch row): **Turn on** or **Turn off**.
- **Panel**: **Export**, **Import**, **Reset section** and **Reset all**. **Reset section** is unavailable in the Shortcuts section, which has nothing to reset. **Reset all** still asks for confirmation.

Press `Esc`, click elsewhere, scroll or resize the window to close the menu. `Esc` closes only the menu, not the panel.
