---
title: Download and offline — Install the app
description: Install Auric Artisan as an app on each platform the Download page covers, and what installing changes.
product: Website › Download and offline
updated: 2026-09-25
---

# Install the app

The same app runs on Windows, macOS, Linux, ChromeOS, Android, iOS and iPadOS. What differs is how you install it: whether a browser offers an install button is the browser's decision. The Download page marks your current platform with "current".

## Using the Install app button

In browsers that offer installation to web pages (such as Chrome and Edge on desktop and Android), the Download page shows an **Install app** button.

1. Open https://auricartisan.com/download/.
2. Select **Install app**. The status reads "Opening the browser install prompt...".
3. Confirm in your browser's dialog.

| Result | Status line |
|---|---|
| Installed | "App install accepted. Finishing setup..." and a message "Auric Artisan installed" |
| You cancelled | "Install dismissed. You can still cache offline tools." |
| Browser cannot install | "Install prompt is not available in this browser." |

Once installed, the button reads **App installed** and is hidden, and the **Install** check reads "App is installed and running standalone." when you open the page in the app.

If there is no **Install app** button, use your browser's own install option below.

## Windows

Install from **Microsoft Edge** or **Google Chrome**:

- **Edge:** select the app icon in the address bar, or **Settings and more** (…) › **Apps** › **Install this site as an app**.
- **Chrome:** select the install icon in the address bar, or the menu (⋮) › **Cast, save and share** › **Install page as app** (wording varies by version).

The app appears in the Start menu and can be pinned to the taskbar. It supports local storage, files, the clipboard and graphics acceleration.

## macOS

- **Safari:** **File** › **Add to Dock**.
- **Chrome** or **Edge:** the install icon in the address bar, or the browser menu as on Windows.

The app appears in the Dock and Launchpad (Safari) or in the Applications folder (Chrome and Edge).

## Linux

Install from a Chromium-family browser (Chrome, Edge, Chromium, Brave) using the install icon in the address bar or the browser menu. Firefox on desktop does not install web apps, but offline use works in any browser with service worker support, Firefox included.

## ChromeOS

Use Chrome's install icon in the address bar, or the menu. The app appears in the launcher.

## Android

Install from **Chrome** or another compatible browser: select **Install app** on the Download page, or open the browser menu (⋮) and choose **Install app** or **Add to Home screen**. The icon appears on your home screen and in the app drawer.

## iOS and iPadOS

1. Open https://auricartisan.com/download/ in **Safari**.
2. Select **Share**, then **Add to Home Screen**.
3. Confirm the name and select **Add**.

Offline use and storage work within the limits Safari places on them on mobile devices; see [Limits and accuracy](../others/limits-and-accuracy.md).

## Other devices

Any modern browser with service workers, on a secure (https) connection, can run the app and cache pages for offline use, even where it cannot be installed.

## What installing changes

- Auric Artisan opens in its own window, without the browser's address bar, and appears among your apps.
- The app's name is **Auric Artisan** (short name **Auric**), with its own icon.
- Right-clicking or long-pressing the icon offers shortcuts to key pages (see [Installed app features](installed-app-features.md)).
- Links to the site open in the app where the system supports it.

Installing does not by itself download the whole site. Prepare the offline version as well: see [Prepare the offline version](prepare-offline.md).

Without the browser's toolbar, use the site's navigation dock for **Back**, **Forward** and **Reload** (see [Navigation dock](../../site-features/navigation-dock/README.md)).
