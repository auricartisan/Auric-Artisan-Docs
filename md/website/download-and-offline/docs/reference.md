---
title: Download and offline — Reference
description: Every control, check, metric, profile, app property and message of the Download page and offline system.
product: Website › Download and offline
updated: 2026-09-25
---

# Download and offline reference

Page: https://auricartisan.com/download/

## Head actions

| Control | Shown | Action |
|---|---|---|
| **Install app** | When the browser offers installation | Opens the browser's install dialog |
| **Update app** | When an update is waiting | Applies the update and reloads |
| **Prepare offline version** | Always | Downloads the profile in effect |
| **Download full offline** | Always | Downloads the Full profile |
| **Open in browser** | Always | Opens the homepage |
| Status line and progress bar | Always | What is happening now |

## Readiness section

| Control | Action |
|---|---|
| Badge | Checking, Preparing, Shell ready, Offline ready |
| Checks | Shell, Full cache, Persistent storage, Local capabilities, Install, Update |
| **Check readiness** | Refreshes the checks |
| **Audit cache** | Compares the store with the profile |
| **Repair cache** | Fetches missing files of the profile |
| **Reset cache** | Deletes the offline store and rebuilds the shell |

## Metrics section

Cache entries, Storage used, Local CPU, Graphics, Offline profile, Cache target, Missing assets, PWA version; **Browser capabilities** (Ready or Limited): Service worker, Cache API, Persistent storage, IndexedDB, File access, Clipboard, Share, Camera input, EyeDropper, Workers, Graphics, Offline privacy; **Check local hardware**.

## Profile section

| Control | Values | Default |
|---|---|---|
| Profile | **Auto**, **Lite**, **Balanced**, **Full** | Auto |
| **Limit background cache work on low-power hardware** | On, off | Off |
| Summary | Selected, Effective profile, Install action, Update action | — |
| **Configure profile** | Scrolls to the profile section | — |

| Profile | Keeps |
|---|---|
| Lite | App shell (main pages, styles, scripts, offline page) |
| Balanced | Shell, library data, core tools and colour libraries |
| Full | Every file listed for offline use |
| Any, in Hindi | Plus the Hindi text (about 11 MB) |

## The installed app

| Property | Value |
|---|---|
| Name / short name | Auric Artisan / Auric |
| Display | Standalone window (falls back to minimal or browser display) |
| Start page | The homepage |
| Shortcuts | Palette Library, Gradient Library, Basic Tools, Workspace, Analyzer, Browser PWA |
| Opens files | `.json`, `.css`, `.csv`, `.txt`, `.md`, `.png`, `.jpg`, `.jpeg`, `.svg` |
| Share target | Links and text shared to the app open in the Workspace |
| Link types | `web+auric:`, `web+palette:` |
| Categories | Design, education, productivity, utilities |

## Messages

| Message | When |
|---|---|
| Ready to prepare the offline version in this browser. | The page has loaded |
| Checking offline readiness... | Checks are running |
| Browser PWA is active. Prepare offline version to cache the full toolset. | Shell stored, profile not complete |
| Offline version is prepared for this browser. | Profile complete |
| Downloading the NAME offline profile into this browser... | Prepare started |
| Downloading the full offline app into this browser... | Download full offline started |
| Full profile selected. Downloading the full offline cache... | Full chosen in Profile |
| Preparing offline version: A/B checked, C cached, D failed. | During a download |
| NAME offline download finished: A/B assets ready. | Download finished |
| Offline version ready with N cached assets. | Background download finished |
| Offline download could not start yet. Check service worker readiness and try again. | The offline system was not ready |
| Updated offline hardware profile. / Updated hardware limit setting. | Profile or switch changed |
| Cache audit passed. Offline profile is complete. | Audit found nothing missing |
| Cache audit found missing assets. Repair cache can retry them. | Audit found gaps |
| Cache repair finished: A/B assets ready. | Repair finished |
| PWA caches reset. Shell cache rebuilt. | Reset finished |
| Offline now. Cached Auric Artisan tools remain available in this browser. | Connection lost while on the page |
| Back online. Checking browser PWA status... | Connection returned |
| PWA runtime is still loading. Refresh the page if this does not clear. | The page's offline controls are not ready |
| Saving for offline — N% / Full offline app ready | Site-wide progress messages |
| Offline mode / Back online | Site-wide connection messages |
| Update ready — Refresh to use the newest offline cache. | An update is waiting |
