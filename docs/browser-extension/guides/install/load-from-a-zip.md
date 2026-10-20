---
title: Browser extension — Load from a ZIP
description: Load an unpacked copy of Auric Artisan from the ZIP packages on the product page, in a Chromium browser or in Firefox.
product: Browser extension › Install
updated: 2026-09-25
---

# Load from a ZIP

The store listings are the easiest way to install and keep the extension current. The product page, https://auricartisan.com/extension, also offers the same packages as ZIP files. An unpacked extension is a folder of plain files you can read before you trust it. Browsers do not let a website open their internal extension pages, so you copy those addresses into the address bar yourself.

## The packages

| Package | File name starts with | Use it in |
|---|---|---|
| Chromium | `auric-suite-chrome-` | Chrome, Brave, Vivaldi, Arc and any Chromium browser |
| Edge | `auric-suite-edge-` | Edge (identical to the Chromium package) |
| Opera | `auric-suite-opera-` | Opera (identical to the Chromium package) |
| Firefox | `auric-suite-firefox-` | Firefox 115 and later |

The Chrome, Edge and Opera files are byte-for-byte the same package, named for their stores. Take any one of them for any Chromium browser. The Firefox package is a different build.

## Chromium browsers

1. **Download and unzip.** Unzip the package into a folder you will keep. The browser loads the extension from that folder every time it starts, so do not leave it in a Downloads folder you clear out.
2. **Open the extensions page.** Paste `chrome://extensions` into the address bar (in Edge, `edge://extensions`; in Opera, `opera://extensions`).
3. **Turn on Developer mode.**
4. **Load it.** Choose **Load unpacked** and select the unzipped folder, the one with `manifest.json` at its top level.
5. **Pin it.** Pin Auric Artisan to the toolbar, then click the icon or press `Alt` + `Shift` + `A`.

The extension appears in the list with its version. It works exactly like a store install, except that it does not update itself.

## Firefox

1. **Download and unzip** the Firefox package.
2. **Open the debugging page.** Paste `about:debugging#/runtime/this-firefox` into the address bar.
3. **Load it.** Choose **Load Temporary Add-on** and select the `manifest.json` file inside the unzipped folder.
4. Open a web page and click the icon, or press `Alt` + `Shift` + `A`.

> **Important:** A temporary add-on lasts only until you quit Firefox. Firefox keeps only signed add-ons across restarts, which is Firefox's rule rather than a limit of this extension. For a permanent install, use [Firefox Add-ons](firefox.md).

## After loading

- Allow file access if you want page tools on `file://` pages (Chromium: **Details** › **Allow access to file URLs**).
- Your settings and data live in the browser profile, not in the folder. Removing the extension removes them; see [Update and remove](update-and-remove.md).
