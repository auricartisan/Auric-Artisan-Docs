---
title: Status Kit — Troubleshooting
description: Fixes for Status Kit problems, such as empty readings, slow scans or a kit that closes on its own.
product: Website › Kits › Status Kit
updated: 2026-09-25
---

# Status Kit troubleshooting

For problems shared by every kit, see [Troubleshooting kits](../../docs/troubleshooting.md).

## Many readings show a dash (—)

**Why:** Your browser does not provide that information. Network speed, latency and data saver, battery, JS heap and device memory are available only in some browsers, mostly Chromium-based ones.

**What to do:** Nothing is wrong. Try another browser if you need those readings.

## The Status Kit closes when I open another kit

**Why:** The Status Kit always closes when another kit opens, even with Focus mode on.

**What to do:** Reopen it after using the other kit. Focus mode still reopens it on each new page.

## A scan takes a long time

**Why:** The kit fetches every page in the section to read its title. A broad path such as `/tool/` or `/library/` means many pages.

**What to do:** Scan a narrower path, such as `/library/blog/`. The running count shows how far the scan has got.

## "No pages found"

**Why:** No page's address starts with what you typed. Paths are matched from the start, and must be paths on auricartisan.com.

**What to do:** Start with a slash and a top-level folder, such as `/tool/`, `/library/`, `/company/` or `/legal/`.

## "Couldn’t complete the scan"

**Why:** The site map could not be read, usually because the connection dropped.

**What to do:** Check your connection and select **Scan** again.

## A page shows Beta although it looks finished

**Why:** Pages take the site's overall **Beta** status unless the site has given them their own.

**What to do:** Nothing; the status is the site's own assessment. See [Check a page's status](check-page-status.md).

## Ctrl + K opens a different search

**Why:** `Ctrl` + `K` opens the site-wide search, even while the Status Kit is open.

**What to do:** Press `/` to put the cursor in the path box or in **Search pages...**.

## The frame rate looks low

**Why:** The page is doing heavy work, your device is busy, or power saving is limiting it.

**What to do:** Close other heavy tabs or plug in your device, and watch the sparkline for changes.

## Storage is nearly full

**Why:** The **Storage** bar turns to a warning colour above 90% of the space your browser allows the site. Saved library items, notes and cached files all use it.

**What to do:** Export and delete library items you no longer need in the [Library Kit](../../library-kit/README.md), or clear cached site data in your browser.
