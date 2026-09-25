---
title: Browser extension — Install
description: Which browsers the extension supports and how to install it on each one, from a store or from a ZIP package.
product: Browser extension › Install
updated: 2026-09-25
---

# Install the extension

The Auric Artisan extension is one product with two store listings: the Chrome Web Store, which serves every Chromium-based browser, and Firefox Add-ons. Installing from a store is one click, survives restarts and updates itself. The product page, https://auricartisan.com/extension, also offers the packages as ZIP files, for anyone who prefers to load the extension from a folder they can read first.

## Supported browsers

| Browser | Support | Install from |
|---|---|---|
| Google Chrome | Full, with the side panel | [Chrome Web Store](chrome-and-chromium.md) |
| Brave, Vivaldi | Full, with the side panel | [Chrome Web Store](chrome-and-chromium.md) |
| Arc | Installs from the Chrome listing | [Chrome Web Store](chrome-and-chromium.md) |
| Microsoft Edge | Full, with the side panel | [Chrome Web Store or the Edge ZIP](edge.md) |
| Opera | Full, with the side panel | [Chrome Web Store or the Opera ZIP](opera.md) |
| Firefox 115 and later | Full, with the sidebar. The screen eyedropper is not available. | [Firefox Add-ons](firefox.md) |
| Safari on macOS | Not published. You can convert the Chromium package yourself. There is no side panel. | [Convert with Xcode](safari.md) |

The extension is built on Manifest V3, the current extension format in Chromium browsers and Firefox. The Chrome, Edge and Opera ZIPs are identical copies of the same Chromium package, named for their stores. The Firefox package is a separate build.

## What the browser asks when you install

Every browser shows a permission prompt before it installs the extension. It says that Auric Artisan can read and change your data on all websites. That is the host access the tools need to work on whatever page you use them on. A small script loads on each page and waits until you start a tool, and every feature that changes a page is off until you turn it on. [Permissions](../permissions.md) explains each permission.

## Files in this folder

| Page | What it covers |
|---|---|
| [Chrome and Chromium browsers](chrome-and-chromium.md) | Chrome, Brave, Vivaldi and Arc from the Chrome Web Store |
| [Microsoft Edge](edge.md) | Edge from the Chrome Web Store, or from the Edge ZIP |
| [Opera](opera.md) | Opera from the Chrome Web Store, or from the Opera ZIP |
| [Firefox](firefox.md) | Firefox from Firefox Add-ons, and the temporary add-on route |
| [Safari](safari.md) | Converting the Chromium package with Xcode on macOS |
| [Load from a ZIP](load-from-a-zip.md) | Loading an unpacked copy in any Chromium browser or Firefox |
| [Update and remove](update-and-remove.md) | Keeping the extension current, reloading a ZIP copy, and uninstalling |
