---
title: Update Kit — Reference
description: Every control, state and message of the Update Kit's notice and command.
product: Website › Kits › Update Kit
updated: 2026-09-25
---

# Update Kit reference

## Update notice

| Element | What it shows or does |
|---|---|
| Title | **Update available** followed by the version, such as **Update available v0.9.11** |
| Message | For example **New update found: 0.9.11**, or **Refreshing website cache...** during a forced refresh |
| **Update now** | Starts the update |
| **x** (**Hide update notice**) | Hides the notice until the next page load |

Position: centred at the top of the page; across the top on screens 520 px wide or narrower. The notice follows the site's light or dark theme and is announced politely to screen readers.

## Right-click menu entry

| State | Label | Hint on the right |
|---|---|---|
| Up to date or unknown | **Update website** | **Ctrl+⇧+U** |
| Update available | **Update available** and the version | **Ready** |
| Updating | **Updating website** | **…** |
| Failed | **Retry update** | **Error** |

When an update is available or running, the entry also appears as a banner at the top of the right-click menu, in a group named **Website update**. The entry is not offered on shared public portfolio pages.

## Keyboard

| Shortcut | What it does |
|---|---|
| `Ctrl` + `Shift` + `U` | Runs **Update website** on any page |

## Messages

| Message | When |
|---|---|
| **Checking for updates…** | You started an update from the right-click menu or keyboard |
| **Updating website...** | Caches are being cleared and files re-downloaded |
| **Update ready. Reloading...** | The update finished; the page reloads |
| **Update failed. Try again.** | Something went wrong |

## When the site checks

| Situation | Result |
|---|---|
| First visit in this browser | The current release is recorded; nothing is shown |
| Same release as last recorded | Nothing is shown |
| Newer release than last recorded | The notice appears |
| Release information unreachable (for example offline) | Nothing is shown |

The check runs once per page load, shortly after the page becomes ready.

## What an update clears and keeps

| Clears or refreshes | Keeps |
|---|---|
| The site's cached files in your browser | Library items, notes, calculator history |
| The service worker's copy of itself (asked to update) | Settings, theme and kit preferences |
| Up to 180 files used by the current page, re-downloaded | Your signed-in session |
