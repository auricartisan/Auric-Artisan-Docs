---
title: Menu Kit — Troubleshooting
description: Fixes for Menu Kit problems, such as a missing tab, a tool that does not appear, or a shortcut that does nothing.
product: Website › Kits › Menu Kit
updated: 2026-09-25
---

# Menu Kit troubleshooting

For problems shared by every kit, see [Troubleshooting kits](../../docs/troubleshooting.md).

## The Design tab is missing

**Why:** The site's tool visibility mode is **Basic**, which is the default. Basic mode hides the scientific tools, and the Design tab has nothing else to show.

**What to do:** Open the [Advanced Kit](../../advanced-kit/README.md) and choose **Advanced** or **Everything**.

## A tool I expect is not in the menu or the search results

**Why:** The tool visibility mode hides it, or you unticked it in **Custom** mode.

**What to do:** Choose **Everything** in the Advanced Kit, or tick the tool in **Custom** mode. If the tool still does not appear, it may not be in the Menu Kit's list; try **All Tools** in the Tools tab or the site-wide search (`Ctrl` + `K`).

## Ctrl + M does nothing

**Why:** Your browser or operating system uses that key combination first. On a Mac, `Cmd` + `M` minimises the window.

**What to do:** Open the Menu Kit from **Page utilities** > **Menu**.

## Ctrl + K opens a different search

**Why:** `Ctrl` + `K` opens the site-wide search, even while the Menu Kit is open.

**What to do:** Press `/` to put the cursor in the Menu Kit's own search box.

## The menu says "Menu unavailable"

**Why:** The list of pages could not be downloaded, usually because the connection dropped.

**What to do:** Check your connection and reload the page, then open the Menu Kit again.

## Most Used shows pages I have never opened

**Why:** Until you have opened pages from the Menu Kit, **Most Used** has no counts to go on and lists pages alphabetically.

**What to do:** Nothing; it fills with your own pages as you use the menu.

## A section is empty or missing

**Why:** You collapsed it earlier (the kit remembers), or every page in it is hidden by the tool visibility mode.

**What to do:** Select the section heading to expand it, or change the mode in the Advanced Kit.

## Selecting a result does nothing

**Why:** The result is the page you are already on. The kit closes without reloading it.

**What to do:** Choose another result, or use the **Reload page** quick action.

## The kit opens on every page

**Why:** Its **Focus mode** is on.

**What to do:** Select **Focus mode** so it is no longer gold, then close the kit.

## The status chip says Beta

**Why:** The chip shows the release status of the whole site, which is currently **Beta**. It is not a problem.

**What to do:** For the status of the page you are on, open the [Status Kit](../../status-kit/README.md).
