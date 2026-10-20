---
title: Offline use
description: Install the Auric Artisan website as an app and prepare it to keep working without a network connection.
product: Getting started
updated: 2026-09-25
---

# Offline use

The Auric Artisan website can be installed as a web app (a PWA — a website your browser can install and keep in its own cache) and prepared to work without a connection. You do this once while you are online. The page for it is **The app** under **Get Auric** in the header, at https://auricartisan.com/download/.

## Prepare the website for offline use

1. While you are online, open https://auricartisan.com/download/.
2. Optional: if your browser offers it, select **Install app** to add Auric Artisan to your apps or home screen. Whether the button appears is your browser's decision.
3. Under **How much to keep**, leave **Auto** selected unless the device is short of storage. The profiles are:

   | Profile | Keeps | Suits |
   | --- | --- | --- |
   | **Auto** | Chooses for you from the device's memory, storage headroom and connection | Almost everyone |
   | **Lite** | The app shell and the core tools, and little else | Phones, tight storage, metered connections |
   | **Balanced** | Shell, core tools and the libraries you actually open | A laptop you also use for other things |
   | **Full** | The widest cache the profile allows | A desktop that will be offline for a while |

4. Select **Prepare offline version**, or **Download full offline** for the widest cache. The cache fills in the background and you can keep working.
5. Under **Is this browser ready**, select **Check readiness**. Six checks report on the shell, the full cache, persistent storage, local capabilities, install and update state.
6. Grant persistent storage if your browser asks. Without it, the browser may clear the cache when the device runs short of space.

The result: cached libraries and tools open straight from the browser when you are offline, and palettes and exports you make stay on the device.

## What works offline, and what does not

| Works offline once cached | Needs a connection |
| --- | --- |
| Cached tools that run in your browser | Signing in, the dashboard and account changes |
| Cached libraries, palettes and datasets | Buying a plan or credits |
| Your saved work in My Library | Analysing a live web page, and any token-based server run |
| Settings, theme and language | The REST API |
| | Publishing a portfolio, sending a contact message |

## Keep it up to date

The download page shows **Update app** when a newer version is available. The same page offers **Audit cache**, **Repair cache** and **Reset cache** if something looks out of date or broken.

## Where it runs

The download page lists Windows, macOS, Linux, ChromeOS, Android, iOS and iPadOS. On iPhone and iPad, install with **Add to Home Screen** from Safari; mobile Safari limits how much it caches.

## Related

- [Download and offline](../website/download-and-offline/README.md), the full guide to the download page
- [Troubleshooting](../help/troubleshooting.md#offline-and-the-installed-app)
- The browser extension works fully offline by design: [Browser extension](../browser-extension/README.md)
