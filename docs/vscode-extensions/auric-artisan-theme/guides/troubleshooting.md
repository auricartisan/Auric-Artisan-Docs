---
title: Auric Artisan Theme — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Artisan Theme and Theme Studio.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| Dials and colour changes have no effect. | A non-Auric colour theme is active. Customisations are scoped to the Auric theme names. | Run **Auric Theme: Switch Variant…** and pick an Auric theme. |
| A message says "customisations apply to the Auric Artisan themes. Pick one first." | Same as above. | Select **Choose theme** in the message. |
| The status bar item is missing. | It only shows while an Auric theme is active. | Switch to an Auric theme. |
| My colour override is not exactly the colour I typed. | The contrast guard adjusted it to meet your minimum contrast. | Lower **Minimum contrast** or turn off **Enforce contrast** in the Accessibility dials. Check the Audit tab afterwards. |
| Overrides disappeared after switching theme. | Colour overrides are stored per variant. | Switch back to the variant where you made them, or save a preset and load it on the new variant. |
| A warning keeps saying colour pairs no longer meet the minimum. | **Audit on apply** reports failures after each change. | Fix the failing pairs (see the Audit tab), or turn off **Audit on apply**. |
| "Auric Theme: could not save auricTheme.…" | VS Code could not write your user settings, often because `settings.json` has a syntax error or is read-only. | Open **Preferences: Open User Settings (JSON)**, fix any error, then try again. |
| Import fails with "That is not valid JSON". | The pasted text is incomplete or not JSON. | Copy the whole block again, including the braces. |
| Import says the customisation "came from" another tool. | The JSON was not produced by Auric Artisan Theme. | Only import files exported by this extension. |
| Import says a newer version is needed. | The JSON uses a newer format. | Update the extension. |
| The sidebar's **Export** button seems to do nothing. | It prepares customisation JSON for the Studio's Share tab; it does not open a save dialog. | Use **Export as Theme File…** from the sidebar's **…** menu, or **Copy Customisation to Clipboard**. |
| Italics look slanted and blurry. | Your editor font has no true italic, so it is synthesised. | Set **Italics** to **Off**, or run **Auric Theme: Toggle Italics**. |
| Whitespace marks setting has no visible effect. | Marks only show when VS Code draws whitespace. | Turn on `editor.renderWhitespace`. |
| Title bar dial has no visible effect. | The title bar colour only applies with VS Code's custom title bar style. | Set `window.titleBarStyle` to `custom`. |
| A preset I saved in an older version is missing. | In versions before 0.2.0, presets with distinct Hindi or punctuation-only names could overwrite each other. | This was fixed in 0.2.0, but presets already overwritten cannot be recovered. |
| Recent colours in the picker are gone. | Recent colours last only for the current panel session. | Note important colours as presets or overrides. |
| The Preview tab does not look like my editor. | Preview is an illustrative specimen of the palette, not a full editor. | Look at a real file to judge the result; edits are already live. |
| The Studio shows a banner listing problems. | The theme engine reported something it could not apply. | Read the listed problem; resetting the affected dial or slot usually clears it. |
| Hindi labels do not appear in the Command Palette. | Command titles follow VS Code's display language, not the Studio switch. | Run **Configure Display Language** and choose Hindi, or keep the Studio switch for the panels only. |

## Start again from the shipped theme

1. Run **Auric Theme: Reset Everything** and confirm with **Reset**, or
2. In Theme Studio, select **Reset all**, then **Reset everything?** within four seconds.

This clears every dial and the active variant's colour overrides. Presets are not deleted.

## Still stuck

Collect your VS Code version, the extension version (0.2.0), the active theme and the steps that reproduce the problem, then contact support at https://auricartisan.com/company/contact/.
