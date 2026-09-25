---
title: Browser extension — Install on Microsoft Edge
description: Install Auric Artisan in Microsoft Edge from the Chrome Web Store listing, or load the Edge package from a ZIP.
product: Browser extension › Install
updated: 2026-09-25
---

# Install on Microsoft Edge

Edge is a Chromium browser, so it installs the Chrome Web Store listing directly and gets every feature, including the side panel. The product page also offers an Edge-named ZIP, which is an identical copy of the Chromium package.

## Install from the Chrome Web Store

1. In Edge, open https://chromewebstore.google.com/detail/auric-artisan/bpmkaljljnlmbjfbmkbbbgiinlbpcocp
2. If Edge asks whether to allow extensions from other stores, allow it. Edge asks this once, the first time you install from the Chrome Web Store.
3. Choose the store's add button, then confirm the permission prompt.
4. Open the extensions menu on Edge's toolbar and show **Auric Artisan** on the toolbar.
5. Open a normal web page and click the icon, or press `Alt` + `Shift` + `A`.

You should see the popup with **Home** selected and the first-run tour on top.

## Install from the Edge ZIP instead

1. Download the Edge package from https://auricartisan.com/extension. Its name starts with `auric-suite-edge-`.
2. Unzip it into a folder you will keep. Edge loads the extension from that folder every time it starts.
3. Open `edge://extensions`.
4. Turn on **Developer mode**.
5. Choose **Load unpacked** and select the unzipped folder, the one with `manifest.json` at its top level.

A copy loaded this way does not update itself. See [Update and remove](update-and-remove.md).

## Side panel and shortcuts

- **Open the side panel** in the popup's header docks the workspace in Edge's side panel. See [Side panel](../surfaces/side-panel.md).
- The default shortcuts are the same as in Chrome. Change them on `edge://extensions/shortcuts`. Settings › Shortcuts › **Change them in the browser** opens the shortcuts page.

## Related pages

- [Load from a ZIP](load-from-a-zip.md)
- [Permissions](../permissions.md)
- [Troubleshooting](../troubleshooting.md)
