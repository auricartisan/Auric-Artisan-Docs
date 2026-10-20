---
title: Auric Artisan Emoji — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Artisan Emoji.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| No hover action on a shortcode. | The shortcode is incomplete or not in the catalog, or hovers are off. | Use a complete shortcode with both colons, such as `:rocket:`. Check VS Code's editor hover setting and `auricEmoji.hover.enabled`. |
| A hover no longer inserts. | The document changed, or the action was already used. | Keep the editor visible and writable, then hover again. |
| The Studio copied instead of inserting. | No writable editor was available, or your click action is Copy. | Open a writable editor and place the cursor, then return to the Studio. Check **Workspace overview** for the target, and `auricEmoji.clickAction`. |
| No suggestions after typing `:`. | Completions are off, or VS Code's suggestions are disabled for this language. | Turn on `auricEmoji.completions.enabled`. |
| Emoji look different or appear as boxes. | Emoji are drawn by your system's emoji font; older fonts lack newer emoji. | Update your operating system's emoji font, or choose an older emoji. |
| Extra spaces appear around inserted emoji. | `insertSpacing` is `auto` or `space`. | Set `auricEmoji.insertSpacing` to `none`. |
| A JavaScript escape breaks my JSON. | `\u{…}` code-point escapes are JavaScript syntax, not JSON. | Use the emoji character or a JSON-compatible escape. |
| Command titles are English although the Studio is Hindi. | Native VS Code labels follow VS Code's display language. | Run **Configure Display Language** if you want Hindi commands. |
| Remote or virtual file cannot be edited. | Editing depends on the file system provider and the document being writable. | Check that the file is writable; use Copy instead. |
| The **Emoji** status bar button is missing. | It is turned off. | Turn on `auricEmoji.statusBar.enabled`. |

If the problem continues, note your VS Code version, the extension version (0.2.0) and the steps to reproduce, then contact support at https://auricartisan.com/company/contact/.
