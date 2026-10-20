---
title: Browser extension — Safari
description: Auric Artisan is not published for Safari; how to convert the Chromium package yourself on macOS, and what to expect.
product: Browser extension › Install
updated: 2026-09-25
---

# Safari

Auric Artisan is not published for Safari, and there is no Safari listing. Safari takes web extensions through an Xcode project rather than a ZIP, so you can build a copy yourself on a Mac from the Chromium package. This route is for people comfortable with Apple's developer tools.

## What you need

- A Mac with Xcode installed.
- The Chromium package from https://auricartisan.com/extension (its name starts with `auric-suite-chrome-`).

## Convert and run it

1. Unzip the Chromium package.
2. Open Terminal and run Apple's converter against the unzipped folder. Replace the folder name with the one you unzipped:

   ```bash
   xcrun safari-web-extension-converter ./auric-suite-chrome-1.0.2
   ```

3. The converter creates an Xcode project. Open it, then build and run it.
4. In Safari, enable the extension in Safari's extension settings.

The product page has a **Copy command** button that copies the converter command for the package version it offers.

## What to expect

- **There is no side panel.** Safari has no equivalent of the Chromium side panel or the Firefox sidebar, so the workspace is available only as the popup.
- **The build is yours.** Auric Artisan does not build, test or support a Safari version. Features that rely on Chromium or Firefox interfaces may not work.
- **Updates are manual.** To update, convert the newer package and build again.

If you need the full feature set, use a Chromium browser or Firefox. See [Install](README.md).
