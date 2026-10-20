---
title: Auric Artisan Theme — Save, share and export
description: Keep your customisation as named presets, move it between machines as JSON, and export a standalone VS Code colour theme file.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Save, share and export

Your customisation is small: the dials you changed plus any colour slot overrides. The extension gives you three ways to keep and move it.

| Method | Where it lives | Best for |
| --- | --- | --- |
| Preset | Inside the extension, on this machine | Switching between several set-ups quickly. |
| Customisation JSON | Clipboard or any text file | Moving a set-up to another machine or sharing it. |
| Theme file | A `.json` colour theme file | Using the result without this extension, or packaging it as your own theme. |

> **Important:** Edits apply live and there is no general undo history. Save a preset or export JSON before large experiments.

## Presets

### Save a preset

1. Open Theme Studio and select **Share** (or press `5`).
2. In the **Presets** card, type a name in **Name this preset…** (up to 64 characters).
3. Select **Save** or press `Enter`.

If you leave the name empty, the Studio shows "Give the preset a name first." Saving again with the same name updates that preset. Names that differ only by Hindi characters or punctuation are kept as separate presets.

You can also run **Auric Theme: Save Current as Preset…** from the Command Palette or the sidebar's **…** menu. It asks you to name the preset.

### Load or delete a preset

- In the **Saved** list, select **Load** beside a preset. Each entry shows the date and time it was saved.
- Select the bin icon beside a preset to delete it.
- From the Command Palette, run **Auric Theme: Load Preset…**. Each preset shows the theme it was saved on. If there are none, you see "Auric Theme: no saved presets yet."

Loading a preset replaces your current dials and the colour overrides of the active variant.

## Customisation JSON

The customisation is a small JSON document. It contains a format version, the theme it came from, your changed dials and your colour overrides. Default values are left out.

```json
{
  "$schema": "https://auricartisan.com/schema/theme-customization-1.json",
  "version": 1,
  "generator": "auric-artisan-theme",
  "name": "Auric Artisan — Obsidian Gold",
  "theme": "obsidian-gold",
  "knobs": {
    "accent.preset": "sapphire",
    "syntax.palette": "cool"
  },
  "overrides": {
    "syntax.string": "#A0D0B0"
  }
}
```

### Export from the Studio

1. On the **Share** tab, the **Export** card shows your current customisation as read-only JSON.
2. Select **Copy** to copy it, or **Refresh** to regenerate it after more changes.

### Copy from the Command Palette

Run **Auric Theme: Copy Customisation to Clipboard**. VS Code confirms with "Auric Theme: customisation copied to the clipboard."

### Import

1. On the **Share** tab, paste JSON into **Paste a customisation JSON here…** in the **Import** card.
2. Select **Import**. Select **Clear** to empty the box.

Or copy the JSON and run **Auric Theme: Apply Customisation from Clipboard**.

Importing replaces your dials and the overrides of the active variant. Export first if you want a way back. The import is checked first; you may see:

| Message | Meaning |
| --- | --- |
| Nothing to import — paste some JSON first. | The Import box is empty. |
| Auric Theme: the clipboard is empty. | The clipboard command found no text. |
| That is not valid JSON (…). | The text could not be read as JSON. |
| This looks like it came from "…", not Auric Artisan Theme. | The JSON was produced by another tool. |
| This customisation needs a newer version of the extension (format v…). | Update the extension, then import again. |
| That customisation is empty — no dials and no colours. | There is nothing to apply. |

## Export a standalone theme file

1. Make sure an Auric theme is active. Otherwise you see "Auric Theme: switch to an Auric Artisan theme first."
2. Run **Auric Theme: Export as Theme File…** from the Command Palette, or choose it from the sidebar's **…** menu.
3. A save dialog opens with a suggested name such as `obsidian-gold-custom-color-theme.json`. Choose a location and select **Export theme**.
4. VS Code confirms, for example "Auric Theme: exported obsidian-gold-custom-color-theme.json." If some pairs fail your contrast minimum, the message includes the number of contrast warnings.

The file is a complete VS Code colour theme built from your current palette. You can use it in a theme extension of your own. It does not update when you change the Studio later; export again after changes.

## Result

Your set-up is saved as a preset on this machine, available as portable JSON for other machines, and optionally exported as a standalone theme file.
