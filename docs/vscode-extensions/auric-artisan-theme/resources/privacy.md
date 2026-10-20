---
title: Auric Artisan Theme — Privacy
description: What Auric Artisan Theme stores, where it stores it and what, if anything, uses the network.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Privacy

Auric Artisan Theme works entirely inside VS Code. It has no account, no telemetry and no runtime package dependencies, and it does not contact a server.

## What is stored and where

| Data | Where it is stored |
| --- | --- |
| Dial values and interface language | Your VS Code user settings, under `auricTheme.*`. |
| Theme-scoped colour customisations | Your VS Code user settings, in the colour, token and semantic-token customisation blocks for the Auric theme names. Unrelated blocks are left alone. An untouched set-up writes nothing. |
| Colour slot overrides (per variant) and presets | The extension's local storage in VS Code on this machine. |
| Studio view state (tab, scroll, open groups, searches) | The panel's own saved state in VS Code. |
| Recent colours in the picker | Memory only, for the current panel session. |

"Local" does not mean read-only: customising the theme writes to your user settings.

## What uses the network

Nothing, automatically. The links to auricartisan.com in the Studio and sidebar open your browser only when you select them.

## Clipboard and files

- The clipboard is read only when you run **Apply Customisation from Clipboard**, and written only when you copy.
- Files are written only when you run **Export as Theme File…** and choose a location.

## Security

The Studio and sidebar load only files packaged with the extension and use a restrictive content security policy. Imported JSON is validated before it is applied and is never executed.
