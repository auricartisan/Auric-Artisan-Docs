---
title: Update Kit — Update the website
description: What happens, step by step, when you select Update now or run Update website, and what is and is not affected.
product: Website › Kits › Update Kit
updated: 2026-09-25
---

# Update the website

## Start an update

Use any of:

- **Update now** on the **Update available** notice;
- **Update website** (or **Update available**) in the right-click menu;
- `Ctrl` + `Shift` + `U`.

The command always refreshes, even if you are already on the newest release. In that case the notice may show briefly with the line **Refreshing website cache...**.

## What happens

1. **Check.** The site reads its newest release number. When run from the right-click menu or the keyboard, the message **Checking for updates…** appears.
2. **Clear cached files.** The site deletes the copies of its files that your browser keeps for this site (the caches used for speed and offline use). The message **Updating website...** appears.
3. **Refresh the offline helper.** The site asks its service worker, the background part that makes offline use possible, to check for a new version of itself.
4. **Re-download current files.** The files the current page uses (its scripts, styles, images and data, up to 180 files) are downloaded again, bypassing the browser's cache.
5. **Record the version.** The site notes that you are now on the newest release.
6. **Reload.** The message **Update ready. Reloading...** appears and the page reloads. For a moment the address carries `?auric-update=` and the version; it is removed once the page has loaded.

If something goes wrong, the message reads **Update failed. Try again.** and the right-click entry changes to **Retry update**.

## What is not affected

- Your library items, notes, calculator history and kit preferences.
- Your site settings and theme.
- Whether you are signed in.

These are kept in your browser's storage, which the update does not clear.

## What to expect afterwards

- The page you were on reloads with the new release. Unsaved work in that page's tools is lost, so save first.
- Other pages refresh their files as you visit them.
- Offline copies of pages are rebuilt as you browse, so if you rely on offline use, visit the pages you need again while online.
- The **Update available** notice stays away until the next release.

## Put the notice away without updating

Select **x** (**Hide update notice**). You can keep working on the old release. The notice returns on the next page load, and the right-click menu keeps showing **Update available** until you update.

## Related

- [Reference](reference.md)
- [Troubleshooting](troubleshooting.md)
- [Download and offline use](../../../download-and-offline/README.md)
