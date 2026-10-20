---
title: Download and offline — Installed app features
description: App shortcuts, opening files with the app, sharing to it, and how links behave once Auric Artisan is installed.
product: Website › Download and offline
updated: 2026-09-25
---

# Installed app features

These work once Auric Artisan is installed, in systems and browsers that support them (mostly Chromium-based browsers such as Chrome and Edge, and Android).

## App shortcuts

Right-click the app's icon on the taskbar or dock, or long-press it on Android, for shortcuts:

| Shortcut | Opens |
|---|---|
| **Palette Library** | Saved and generated palettes |
| **Gradient Library** | Gradient collections |
| **Basic Tools** | The core colour tool workspace |
| **Workspace** | Saved local palettes, gradients, assets and exports |
| **Analyzer** | The website analyzer |
| **Browser PWA** | The Download page's offline controls |

## Open files with the app

The installed app can be chosen to open these file types, for example from your file manager's **Open with** menu:

| Type | Extensions |
|---|---|
| JSON | `.json` |
| CSS | `.css` |
| CSV | `.csv` |
| Text and Markdown | `.txt`, `.md` |
| Images | `.png`, `.jpg`, `.jpeg`, `.svg` |

The files open in your Workspace. A message reads "1 file ready" (or the number of files). Text files up to 500 KB and images up to 2 MB are read straight away; larger files are passed on to open later. If a file cannot be read, the message is "Could not open file".

## Share to the app

On systems with a share menu (such as Android), you can share a link or text to **Auric Artisan**. It opens in your Workspace with what you shared.

## Links

- Links to auricartisan.com can open in the installed app, and an already-open app window is reused.
- The app registers two link types, `web+auric:` and `web+palette:`, which open the Workspace and the Palette Library, where the browser supports them.

## Standalone window

The app opens without the browser's toolbar. Use the site's navigation dock for **Back**, **Forward** and **Reload**, and **Copy link** to share the page you are on.
