---
title: Auric Icons: Modern — Privacy
description: What Auric Icons: Modern stores, where, and confirmation that it makes no network requests.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Privacy

Auric Icons: Modern runs entirely inside VS Code. It has no telemetry, no account and no network access at runtime.

## What is stored

| Data | Where |
| --- | --- |
| Theme and library settings | Your VS Code settings under `auricIcons.*`. |
| A rebuilt copy of the theme when you customise it | Inside the extension's own installation folder. The original artwork is never changed. |
| Likes (up to 500), recent icons (up to 60), learned preferences and dismissed guide tips | VS Code's extension storage on this machine. |
| "Don't ask again" for workspace detection | VS Code's storage for that workspace. |
| Library search, filters, variant and preview surface | The view's saved state in VS Code. |

## What the extension reads

- To offer the theme in Auric Artisan workspaces, it checks whether `.auric-artisan` or `.auricignore` exists at the top of each local workspace folder. It does not read their contents or walk your folders.
- For recommendations and smart insert, it reads the language, file name and up to about 60 lines around the cursor in the active editor. This stays in memory.

## What the extension writes

- Inserting changes your editor content. Copying writes to the clipboard. Saving writes a file only where you choose in a save dialog.
- Its own commands update your user settings.
