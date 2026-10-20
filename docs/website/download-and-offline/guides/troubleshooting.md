---
title: Download and offline — Troubleshooting
description: Fixes for common problems installing Auric Artisan, preparing it offline and keeping it up to date.
product: Website › Download and offline
updated: 2026-09-25
---

# Troubleshooting the app and offline use

## There is no Install app button

**Why:** the button appears only in browsers that let pages offer installation, such as Chrome and Edge. Safari and Firefox do not; the site is already installed; or the browser has decided not to offer it yet.

**What to do:** use your browser's own install option (see [Install the app](install-the-app.md)). On iPhone and iPad, use Safari's **Share** › **Add to Home Screen**. You can still prepare the offline version without installing.

## "Install prompt is not available in this browser."

**Why:** the browser did not offer installation to the page, or you dismissed it recently.

**What to do:** use the browser menu to install, or try later.

## "PWA runtime is still loading."

**Why:** the offline system starts after the page finishes loading.

**What to do:** wait a few seconds; if it does not clear, reload the page.

## "Offline download could not start yet."

**Why:** the browser has not finished setting up the site's offline system, or service workers are blocked (for example in some private windows or by an extension).

**What to do:** reload the page and try again. Use a normal window, and make sure the site is not blocked from storing data.

## The download finished with failed files

**Why:** some files could not be fetched, usually because of a brief network problem.

**What to do:** select **Repair cache** while online.

## Persistent storage stays "best-effort"

**Why:** the browser decides whether to grant it. Some grant it only to installed apps or sites you use often.

**What to do:** install the app, keep using the site, and check again. Until then, keep some free space on the device so the browser has no reason to clear the offline copy.

## A page says "You are offline"

**Why:** that page was not stored before the connection dropped.

**What to do:** open one of the pages listed under **Saved on this device**, or select **Try again** when you are back online. Next time, prepare a larger profile.

## The site seems out of date

**Why:** an update is waiting, or your offline copy predates a release.

**What to do:** select **Refresh** on the **Update ready** prompt, **Update app** on the Download page, or press `Ctrl` + `Shift` + `U`. Then prepare the offline version again.

## Storage is nearly full

**What to do:** choose **Lite** or **Balanced**, select **Reset cache** and prepare again, or free space on the device.

## iPhone or iPad cleared the offline copy

**Why:** mobile Safari limits storage for websites and may clear it for sites that have not been used for a while.

**What to do:** add the site to your Home Screen, open it regularly, and prepare the offline version again when needed.
