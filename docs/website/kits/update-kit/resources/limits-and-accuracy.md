---
title: Update Kit — Limits and accuracy
description: What an update refreshes, what it leaves alone, and when the notice appears.
product: Website › Kits › Update Kit
updated: 2026-09-25
---

# Update Kit limits

## When the notice appears

- The site compares the newest release it can find with the release recorded the last time you updated in this browser. The notice appears only when they differ.
- On a first visit the current release is recorded silently, so you will not see a notice until the following release.
- If the release information cannot be reached, for example offline, no notice is shown.
- The check runs once per page load.

## What an update refreshes

- All of the site's caches in your browser are deleted.
- The service worker is asked to update itself; it is not removed.
- Up to 180 files used by the current page are downloaded again. Files used only by other pages refresh when you visit those pages.
- The page reloads.

## What it does not do

- It does not clear site storage: library items, notes, calculator history, settings and your sign-in are kept.
- It does not update browser extensions, VS Code extensions or the browser itself.
- It does not change anything on the server; it only refreshes your browser's copy of the site.
- It cannot bypass a network or company proxy that serves old copies.
