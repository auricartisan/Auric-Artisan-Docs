---
title: Auric Icons: Modern — Troubleshooting
description: Symptoms, causes and fixes for common problems with the Modern file icon theme and Icon Library.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Troubleshooting

## File icon theme

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| A setting change does not show in the Explorer. | VS Code caches icon themes until the window reloads. | Select **Reload Window** in the prompt, or run **Developer: Reload Window**. |
| No reload prompt appears. | The prompt only appears when Modern is the active file icon theme. | Activate the theme first with **Activate Icon Theme**. |
| "could not apply customisation — … The default icons remain active." | A value could not be applied, for example an invalid colour. | Check the value in Settings; folder colour must be `default` or a three- or six-digit hex colour. |
| A custom association shows a blank icon. | The value is not one of the theme's icon IDs. | Use an ID from the [reference](reference.md#icon-ids-for-associations). |
| A workspace setting does not seem to apply. | The extension's own commands write user-level settings; a workspace value may override them. | Check the workspace `settings.json` for `auricIcons.*` values. |
| The file icon theme picker lists two Modern entries. | Auric Artisan File Icons also contributes a Modern style (**Auric Artisan File Icons: Modern**) with the same theme ID. | Choose one extension to manage Modern and use its settings. See the note below. |
| The workspace detection offer never appears. | It only checks local folders, asks once per workspace, and does not ask when Modern is already active or `auricIcons.autoDetect` is off. | Run **Detect Auric Artisan Workspace**, or activate the theme directly. |

> **Note:** With both Auric Icons: Modern and Auric Artisan File Icons installed, use either `auricIcons.*` settings (this extension) or File Icon Studio (`auricFileIcons.*`) consistently. If icons look inconsistent, disable one of the two sources of the Modern theme. See [Modern and older Playful settings](../../auric-artisan-file-icons/docs/modern-and-legacy.md).

## Icon Library

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The **Auric Icons: Modern** Activity Bar view is missing. | Another extension hosts the shared library: Auric Artisan Icon Studio, or a sibling collection. | Use the host's view, or set `auricIconStudio.hostFamilyLibraries` to `false` if Icon Studio is the host. See [The merged Icon Studio](merged-icon-studio.md). |
| Modern commands are missing from the Command Palette. | Same as above: they hide while another extension hosts. | Use the host's commands; keybindings still work. |
| `Ctrl` + `Alt` + `I` does nothing. | The editor is not focused, another extension hosts the library, or the keys are bound elsewhere. | Focus a text editor and check **Keyboard Shortcuts**. |
| "Open a text editor before inserting an SVG." | No text editor was available. | Open a file, click into it, then insert again. |
| The inserted format is not what I expected. | Smart insert chose a format for the file's language. | Use **Copy Icon As…** for an explicit format, or turn off `auricIcons.library.smartInsert`. |
| Likes from the retired "Auric Artisan Drawing Icon" extension are missing. | Each extension keeps its own storage; history does not move between different extensions. | Like the icons again in Modern. |
| A command error mentions that another extension owns the same command. | The retired "Auric Artisan Drawing Icon" or "Auric Artisan Icons" extension is still installed. | Uninstall the retired extensions; Modern supersedes them. |
| The library says the icon catalog is not bundled. | The installed files are incomplete. | Reinstall the extension from the Marketplace. |

## Still stuck

Note your VS Code version, the extension version (0.12.1), which Auric icon extensions are installed, and the steps that reproduce the problem, then contact support at https://auricartisan.com/company/contact/.
