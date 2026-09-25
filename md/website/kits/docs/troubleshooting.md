---
title: Kits — Troubleshooting
description: Fixes for problems that affect every kit, such as a missing launcher, a kit that keeps reopening, or a panel stuck in the wrong place.
product: Website › Kits
updated: 2026-09-25
---

# Troubleshooting kits

This page covers problems that affect all kits. Each kit also has its own troubleshooting page for problems inside that kit.

## The Page utilities button is missing

**Why:** The bar is added by the site's scripts after the page has loaded. It does not appear if JavaScript is blocked, if a content blocker removes the site's scripts, or while the page is still loading on a slow connection.

**What to do:**

1. Wait a few seconds after the page appears. The button is added once the page is ready.
2. Check that JavaScript is allowed for auricartisan.com.
3. Pause content-blocking extensions for the site and reload.

## A launcher is dimmed and does nothing

**Why:** The kit is still loading. A launcher is dimmed, with a busy pointer, from the moment you select it until the kit has loaded. It ignores further clicks during that time.

**What to do:** Wait for the kit to open. If the launcher stays dimmed for a long time, or returns to normal without opening anything, the kit could not load, usually because the connection dropped. Reload the page and try again.

## A kit opens by itself on every page

**Why:** Its **Focus mode** is on. The Menu, Advanced, Status and Library Kits keep Focus mode on after you close them, and open again on the next page you load.

**What to do:** Open the kit, select **Focus mode** (the target icon) so it is no longer gold, then close the kit. In the Library Kit, open **Panel options** and turn off **Keep open**.

## Opening one kit closes another

**Why:** This is expected. Opening a kit closes any other open kit unless that kit's Focus mode is on.

**What to do:** Turn on Focus mode in the kit you want to keep. The Status Kit is the exception: it always closes when another kit opens, whatever its Focus mode setting.

## The page goes dark behind the Feature Kit

**Why:** With Focus mode off, the Feature Kit dims the page behind it and keeps `Tab` inside the kit. Clicking the dimmed page closes the kit.

**What to do:** Turn on Focus mode in the Feature Kit if you want to use the page while the kit is open. The dimming goes away.

## A kit is off to one side, or I cannot find it

**Why:** Kits remember where you dragged them, as a proportion of the window. On a much smaller window the saved position can look odd, although a kit never goes outside the window.

**What to do:**

- Drag the kit by its title bar to where you want it.
- In the Library Kit, open **Panel options** and select **Reset position**.
- If a kit is minimised, look for its title bar alone (or, for the Feature Kit, a small round icon) and select it to restore the kit.

## A kit is light on a dark page, or dark on a light page

**Why:** You have used the kit's own **Theme** button. From then on the kit keeps its own light or dark setting and no longer follows the site theme.

**What to do:** Select the kit's **Theme** button to switch it to the mode you want. There is no button that makes a kit follow the site again; clearing this site's stored data in your browser does that, but also clears your other kit preferences.

## A keyboard shortcut does nothing

**Why:** Some shortcuts are also used by browsers or operating systems, which can take the key press first. For example, on a Mac `Cmd` + `M` minimises the browser window, and some desktop environments use `Ctrl` + `Shift` + `U` to type special characters.

**What to do:** Open the kit from the page utilities bar instead. See [Keyboard shortcuts](../others/shortcuts.md) for every shortcut.

## Ctrl + K opens the site search instead of the kit's search

**Why:** `Ctrl` + `K` opens the site-wide search on every page, even while the Menu Kit or the Status Kit is open.

**What to do:** Press `/` instead. While the Menu Kit is open, `/` puts the cursor in its search box. While the Status Kit is open, `/` puts the cursor in its path box, or in its results search after a scan.

## Esc closed more than one kit

**Why:** With Focus mode, several kits can be open at once, and `Esc` is heard by every open kit.

**What to do:** Use each kit's **Close** button when you want to close only one of them.

## My kit settings are not remembered

**Why:** Kits keep their preferences in your browser's storage. In a private window, or when the browser blocks site storage, nothing is kept after you close the page. Clearing this site's data also removes them.

**What to do:** Use a normal window and allow site storage for auricartisan.com. The kits still work without storage; they simply start fresh each time.

## The launcher bar covers the bottom of the page on a phone

**Why:** The open bar takes two rows at the bottom of the screen.

**What to do:** The page gains extra space at the bottom while the bar is open, so you can scroll the last content above it. Select **Close** or press anywhere on the page to fold the bar back into its round button.

## Still stuck

See the kit's own troubleshooting page, or [Help](../../../help/README.md) for how to contact support.

- [Feature Kit troubleshooting](../feature-kit/docs/troubleshooting.md)
- [Menu Kit troubleshooting](../menu-kit/docs/troubleshooting.md)
- [Advanced Kit troubleshooting](../advanced-kit/docs/troubleshooting.md)
- [Status Kit troubleshooting](../status-kit/docs/troubleshooting.md)
- [Library Kit troubleshooting](../library-kit/docs/troubleshooting.md)
- [Update Kit troubleshooting](../update-kit/docs/troubleshooting.md)
