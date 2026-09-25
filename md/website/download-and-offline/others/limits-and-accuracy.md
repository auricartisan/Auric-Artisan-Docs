---
title: Download and offline — Limits and accuracy
description: Platform limits, storage limits, and what the Download page's figures do and do not tell you.
product: Website › Download and offline
updated: 2026-09-25
---

# Download and offline limits and accuracy

## Platform limits

- **Installing** depends on the browser. Chrome and Edge offer it on desktop and Android; Safari offers Add to Home Screen on iPhone and iPad and Add to Dock on macOS; Firefox on desktop does not install web apps.
- **Offline use** needs a browser with service workers and a secure (https) connection. It does not work in browsers or modes that block service workers or site storage.
- **Mobile Safari** limits how much a website may store and may clear it if the site is not used for a while.
- **App shortcuts, file opening, sharing to the app and link types** work only where the system and browser support them, mostly Chromium-based browsers and Android.
- **Background sync**, which finishes interrupted downloads, is available only in some browsers.

## Storage

- The browser sets the site's quota. The **Storage used** figure shows use and quota as the browser reports them.
- Without persistent storage, the browser may clear the offline copy when the device is short of space.
- **Reset cache** clears only the offline copy. Your library, settings and recordings are separate.

## What the figures mean

- **Cache entries** counts stored files; it includes pages you visited as well as prepared files.
- **Cache target** is the number of files in the profile for the current release; it changes between releases.
- **Local CPU**, **device memory** and **Graphics** are what the browser chooses to report. Some browsers report less, or round the figures, for privacy.
- **Offline ready** means every file of your profile is stored, as of the last check. It does not mean that features needing a server work offline.
- Auto's choice is based on the reported figures and connection type at the moment you prepare.

## What offline cannot do

Signing in, account data, live website audits, web search, installing and updating need a connection. See [What works offline](../docs/what-works-offline.md).
