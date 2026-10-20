---
title: Auric Icons: Playful — Privacy
description: What Auric Icons: Playful stores, where, and confirmation that it makes no network requests.
product: VS Code extensions › Auric Icons: Playful
updated: 2026-09-25
---

# Privacy

Auric Icons: Playful runs entirely inside VS Code. It has no telemetry, no account and no network access at runtime.

| Data | Where |
| --- | --- |
| Settings | Your VS Code settings under `auricIconsPlayful.library.*`. |
| Likes (up to 500), recent icons (up to 60), learned preferences, dismissed tips | VS Code's extension storage on this machine. |
| Search, filters, variant and preview surface | The view's saved state in VS Code. |

For recommendations and smart insert, the extension reads the language, file name and up to about 60 lines around the cursor of the active editor. This stays in memory and is never stored or sent.

Inserting changes your editor content, copying writes to the clipboard, and saving writes a file only where you choose in a save dialog.
