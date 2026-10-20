---
title: Auric Icons: Playful — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Icons: Playful.
product: VS Code extensions › Auric Icons: Playful
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The **Auric Icons: Playful** view is missing. | Auric Artisan Icon Studio, Modern or Drawn hosts the shared library, which already includes Playful. | Use the host's library and filter by **Library** › **Playful**, or set `auricIconStudio.hostFamilyLibraries` to `false` if Icon Studio is the host. |
| Playful commands are missing from the Command Palette. | Same reason. | Use the host's commands; keybindings still work. |
| `Ctrl` + `Alt` + `I` does nothing. | The editor is not focused, another extension hosts, or the keys are bound elsewhere. | Focus a text editor and check **Keyboard Shortcuts**. |
| "Open a text editor before inserting an SVG." | No text editor is available. | Open a file, click into it, insert again. |
| I chose Mono or Duotone and Playful cards look like Color. | Playful has no Mono or Duotone; it falls back to Color in a merged library. | Use Color, Outline, Filled or Small. |
| Auto shows Color in a CSS file. | Playful has no Mono variant, which Auto would use for stylesheets and data files. | Choose a variant explicitly if you prefer Outline or Filled. |
| I expected Playful Explorer file icons. | Those belong to Auric Artisan File Icons (the **Playful** Explorer style), a different set of artwork. | Install File Icons and choose **Playful** there. |
| The inserted format is not what I expected. | Smart insert chose a format for the file's language. | Use **Copy Icon As…**, or turn off `auricIconsPlayful.library.smartInsert`. |
| The library says the icon catalog is not bundled. | The installed files are incomplete. | Reinstall from the Marketplace. |

If the problem continues, note your VS Code version, the extension version (0.12.1), the other Auric extensions installed and the steps to reproduce, then contact support at https://auricartisan.com/company/contact/.
