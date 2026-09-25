---
title: Auric Artisan File Icons — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Artisan File Icons.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The Explorer still uses another icon set. | Browsing a style in the Studio only previews it. | Select **Use … in Explorer**, or choose the theme in **Preferences: File Icon Theme**. |
| Colours or associations have not changed. | VS Code caches icon themes until a reload. | Accept the reload prompt, or run **Developer: Reload Window**. |
| Still no change after reloading. | Workspace or folder settings override user settings. | Check `.vscode/settings.json` for `auricFileIcons.*` values. |
| Duplicate Auric themes or actions. | The old standalone Playful extension is still installed, or Auric Icons: Modern also provides a Modern theme. | Disable the old Playful extension. See [Modern and older Playful settings](modern-and-legacy.md). |
| The **Auric File Icons** Explorer submenu has only **Open File Icon Studio**. | The other actions need an Auric file icon theme to be active. | Activate Facet, Playful or Modern. |
| No **Insert** action, or "No editor target". | No writable text editor is open. | Open and click into a writable file first; **Copy** works without one. |
| A token hover does not appear. | The token is incomplete, hovers are off, or VS Code's editor hovers are disabled. | Use a complete token copied from the inspector, and enable `auricFileIcons.hover.enabled` and editor hovers. |
| A hover action no longer inserts. | The document changed after the hover appeared. | Hover again for a fresh action. |
| An unexpected smart badge appears. | A built-in or custom rule matched. | Run **Explain Smart Icon Match**, then refresh or adjust smart settings. |
| Smart badges do not appear in a remote or virtual workspace. | The file system provider may not allow reading, or the folder is excluded. | Check `auricFileIcons.smart.exclusions` and the provider's support. |
| Exported code does not match my Explorer colours. | Code output always uses shipped artwork. | This is by design; recolour the code yourself if needed. |
| Import of a profile fails. | The clipboard is empty, too large, not JSON, or from an unknown source. | See the messages in [Profiles](profiles.md#export-and-import). |
| Old Playful profiles are missing after switching. | File Icons cannot read another extension's private storage. | Export profiles from the old extension first, then import them. |

## Diagnostics

Run **Auric Artisan File Icons: Show Icon Theme Diagnostics**. The report opens in the **Auric Artisan File Icons** output channel and omits filenames and file contents. Include it, with your VS Code version, the extension version, the active style and the steps to reproduce, when you contact support at https://auricartisan.com/company/contact/. Remove private information from screenshots.
