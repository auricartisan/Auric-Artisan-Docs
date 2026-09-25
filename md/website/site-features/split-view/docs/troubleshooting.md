---
title: Split view — Troubleshooting
description: Fixes for common split view problems.
product: Website › Site features › Split view
updated: 2026-09-25
---

# Troubleshooting split view

## `Ctrl` + `Shift` + `D` does nothing, or bookmarks the page

**Why:** in some browsers `Ctrl` + `Shift` + `D` also means "bookmark all tabs". Split view claims the shortcut once the page has loaded; pressed too early, the browser may act on it instead.

**What to do:** wait for the page to finish loading, or use **Open split view** in the navigation dock.

## An outside website shows as a blank pane

**Why:** many websites do not allow themselves to be shown inside another page. External pages that do load are not controlled by split view, so the pane's theme, zoom and history buttons may not affect them.

**What to do:** use **Open in new tab** from the pane's More menu.

## A pane is slow or the page stutters

**Why:** two full pages are running at once.

**What to do:** let eco mode switch on, close heavy tools in one pane, or use a smaller viewport. The performance chip shows what is happening.

## Closing split view took me to a different page

**Why:** you loaded another page in the live pane. Closing follows the live pane.

**What to do:** use your browser's Back button to return.

## The Theme control shows Auto but the pane is not following my theme

**Why:** switching a pane back to **Auto** reloads it. If the reload has not finished, wait a moment.

## Compare shows everything in colour

**Why:** the two pages differ everywhere, for example because they are scrolled to different places or use different themes on purpose.

**What to do:** load the same page in both panes (**Mirror**), then change one thing, such as the theme, to see just that difference.

## A shared split opened as a normal page

**Why:** the link lost the part after `#split=`, for example because an app shortened it.

**What to do:** copy the full address again from the address bar.
