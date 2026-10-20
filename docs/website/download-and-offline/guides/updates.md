---
title: Download and offline — Updates
description: How new versions of the site reach your browser and installed app, and how to apply them.
product: Website › Download and offline
updated: 2026-09-25
---

# Updates

Auric Artisan updates itself from the website: there is no app store update. Each release has a version name, shown on the Download page as **PWA version** (for example `2026-09-24-pwa-303`).

## How you find out

When your browser has downloaded a newer version in the background, it waits for you. You may see:

- a prompt, **Update ready** — "Refresh to use the newest offline cache." — with **Refresh** and **Later**;
- on the Download page, an **Update app** button in the head, the **Update** check reading "Update is ready.", and the summary's **Update action** saying the same;
- in the right-click menu, a highlighted **Update available** row (see [Context menu](../../site-features/context-menu/README.md)).

## Apply an update

- Select **Refresh** on the prompt, or **Update app** on the Download page ("Applying update..."). The page reloads on the new version.
- Or press `Ctrl` + `Shift` + `U`, or choose **Update website** in the right-click menu, which checks for an update and applies it.

**Later** closes the prompt; the update is applied the next time all the site's tabs and app windows are closed and reopened, or when you choose to apply it.

## Check for an update

Open the Download page: it checks when it loads, and the **Update** check shows one of:

| State | Meaning |
|---|---|
| Checking for updates. | A check is running |
| Offline app is current. | You have the latest version |
| Update is ready. | A newer version is waiting |
| Applying update. | The update is being applied |
| Update check is not available. | The browser cannot check (for example, no service worker) |
| Update check failed. | The check could not reach the site |

## Your offline copy after an update

After an update, files are fetched fresh as you use them. To bring the whole offline copy up to date at once, select **Prepare offline version** again; the readiness checks show whether it is complete. In browsers with background sync, an offline copy you asked for before is refreshed in the background.

The Update Kit also reports and applies website updates; see [Kits](../../kits/README.md).
