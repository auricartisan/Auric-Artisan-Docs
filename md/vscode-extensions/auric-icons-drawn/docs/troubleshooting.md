---
title: Auric Icons: Drawn — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Icons: Drawn.
product: VS Code extensions › Auric Icons: Drawn
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The **Auric Icons: Drawn** view is missing from the Activity Bar. | Auric Artisan Icon Studio or Auric Icons: Modern hosts the shared library, which already includes Drawn. | Use the host's library and filter by **Library** › **Drawn**, or set `auricIconStudio.hostFamilyLibraries` to `false` if Icon Studio is the host. |
| Drawn commands are missing from the Command Palette. | Same reason: they hide while another extension hosts. | Use the host's commands; keybindings still work. |
| `Ctrl` + `Alt` + `I` does nothing. | The editor is not focused, another extension hosts, or the keys are bound elsewhere. | Focus a text editor and check **Keyboard Shortcuts**. |
| "Open a text editor before inserting an SVG." | No text editor is available. | Open a file, click into it and insert again. |
| I cannot find Drawn icons in the Explorer file icon picker. | Drawn has no file icon theme. | Install Auric Icons: Modern or Auric Artisan File Icons for Explorer icons. |
| A card looks like Color after choosing Filled or Small. | Filled and Small are Playful variants; Drawn falls back to Color. | Choose Color, Mono, Outline or Duotone for Drawn icons. |
| The format inserted is not what I expected. | Smart insert chose a format for the file's language. | Use **Copy Icon As…**, or turn off `auricIconsDrawn.library.smartInsert`. |
| The library says the icon catalog is not bundled. | The installed files are incomplete. | Reinstall from the Marketplace. |

If the problem continues, note your VS Code version, the extension version (0.12.1), the other Auric extensions installed and the steps to reproduce, then contact support at https://auricartisan.com/company/contact/.
