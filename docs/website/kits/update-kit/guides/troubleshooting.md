---
title: Update Kit — Troubleshooting
description: Fixes for update problems, such as a notice that keeps returning, an update that fails, or a page that still looks old.
product: Website › Kits › Update Kit
updated: 2026-09-25
---

# Update Kit troubleshooting

## The notice keeps coming back

**Why:** **x** only hides the notice for the current page. It returns on every page load until you update.

**What to do:** Select **Update now**.

## "Update failed. Try again."

**Why:** The update could not finish, usually because the connection dropped while files were re-downloading, or the browser refused access to its storage.

**What to do:** Check your connection and run **Update website** again. If it keeps failing, allow site storage for auricartisan.com in your browser settings.

## The page still looks old after updating

**Why:** Some pages you have not visited since the update still use older cached files until you open them, and some browsers keep their own short-term copies.

**What to do:** Open the page and run **Update website** there, or reload it with your browser's hard-reload shortcut.

## No notice appears, but I know there is a new release

**Why:** The notice appears only when the release number has changed since you last updated in this browser. On your first visit the site records the current release silently. If the release information cannot be reached, nothing is shown.

**What to do:** Run **Update website** from the right-click menu or with `Ctrl` + `Shift` + `U`; it refreshes regardless.

## Ctrl + Shift + U does nothing, or types a character

**Why:** Some systems use `Ctrl` + `Shift` + `U` to enter special characters, and take the key press first.

**What to do:** Use the right-click menu's **Update website** instead.

## The right-click menu does not show Update website

**Why:** You may have switched the site's right-click menu off in favour of the browser's, or you are on a shared public portfolio page, where the entry is not offered.

**What to do:** Hold `Shift` while right-clicking to get the site's menu when the browser's menu is set as default, or use `Ctrl` + `Shift` + `U`. See [Site features](../../../site-features/README.md).

## I lost work when the page reloaded

**Why:** Updating reloads the page, which discards unsaved work in the page's tools.

**What to do:** Save to the library, or export, before updating. Items already saved are not affected by the update.
