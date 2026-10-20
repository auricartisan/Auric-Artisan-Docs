---
title: Auric Artisan Icon Studio — Privacy
description: What Icon Studio stores, where, and confirmation that it makes no network requests.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Privacy

Icon Studio is offline by design. The catalog, SVG artwork and Material preview fonts ship with the extension. It makes no network requests, has no account and collects no telemetry.

## What is stored

| Data | Where |
| --- | --- |
| Likes (up to 500), recent icons (up to 60) and learned preferences for tags and categories | VS Code's extension storage on this machine. |
| Search text, filters and current view | The panel's saved state in VS Code. |
| Settings | Your VS Code settings under `auricIconStudio.*`. |

## What Icon Studio reads

To rank recommendations and choose smart-insert formats, it reads the language, file name and up to about 60 lines around the cursor of the file you are editing. This stays in memory and is not stored or sent anywhere.

## What Icon Studio writes

- Inserting changes the editor content at your cursors or selections.
- Copying writes to your clipboard.
- Saving an SVG writes a file only through a save dialog you confirm.

Review what you insert or export, especially with multiple cursors or a selection.

## Clear your data

Run **Auric Icon Studio: Clear Likes, Recents and Learned Recommendations** and confirm with **Clear**.
