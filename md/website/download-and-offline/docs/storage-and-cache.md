---
title: Download and offline — Storage and cache
description: Read the readiness checks and live metrics, and audit, repair or reset the offline copy.
product: Website › Download and offline
updated: 2026-09-25
---

# Storage and cache

The Download page reads its figures from your browser itself: the offline store, the storage estimate and the browser's capabilities. Open it on the device you care about.

## Readiness checks

Select **Check readiness** to refresh them.

| Check | Possible states |
|---|---|
| **Shell** | "Service worker shell is preparing." / "Service worker shell is ready for cached navigation." |
| **Full cache** | "Full offline cache is not warmed yet." / "Run prepare offline version to warm every core route." / "Offline cache has warmed this device profile." |
| **Persistent storage** | "Persistent storage is active for this browser." / "Storage is best-effort until the browser grants persistence." |
| **Local capabilities** | The number of CPU threads available for local work |
| **Install** | Checking / available / not offered by this browser yet / installed and running standalone / accepted / dismissed / could not be opened |
| **Update** | See [Updates](updates.md) |

The badge sums it up: **Checking**, **Preparing**, **Shell ready** (the core is stored) or **Offline ready** (your profile is complete).

## Live metrics

| Metric | What it shows |
|---|---|
| **Cache entries** | How many files are stored |
| **Storage used** | Space used by the site, and the browser's quota for it (persistent or best effort) |
| **Local CPU** | Processor threads, and approximate device memory where reported |
| **Graphics** | WebGL 2, WebGL 1 or Canvas, and the graphics processor where reported |
| **Offline profile** | The profile in effect, for example "Auto selected Full for this device." |
| **Cache target** | How many files the profile holds |
| **Missing assets** | Files of the profile not yet stored (after an audit) |
| **PWA version** | The version of the site in your browser |

**Browser capabilities** lists each feature as **Ready** or **Limited**: Service worker, Cache API, Persistent storage, IndexedDB, File access, Clipboard, Share, Camera input, EyeDropper, Workers, Graphics and Offline privacy (a secure connection). Select **Check local hardware** to refresh them.

## Audit the offline copy

Select **Audit cache**. The site compares your store with the profile ("Auditing Balanced cache coverage...") and reports:

- "Cache audit passed. Offline profile is complete." with **Missing assets** at 0; or
- "Cache audit found missing assets. Repair cache can retry them." with the count and the first missing file.

## Repair it

Select **Repair cache**. The site fetches any missing files of the profile ("Repairing the Balanced cache profile..."), then reports "Cache repair finished: A/B assets ready." and re-runs the audit. You need to be online.

## Reset it

Select **Reset cache** to delete the site's offline store and rebuild the app shell: "Resetting browser PWA caches and rebuilding the shell..." then "PWA caches reset. Shell cache rebuilt." Use it if the offline copy seems out of date or damaged. Prepare the offline version again afterwards.

Reset cache does not delete your library, settings or recordings, which are kept separately in your browser.

## How much space it takes

Storage depends on your profile. Lite is small; Balanced and Full can take from tens to more than a hundred megabytes. **Storage used** shows the real figure on your device.
