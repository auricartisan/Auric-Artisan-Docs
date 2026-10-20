---
title: Status Kit — Reference
description: Every control, reading, filter and message in the Status Kit.
product: Website › Kits › Status Kit
updated: 2026-09-25
---

# Status Kit reference

## Launcher

| Control | What it does | Default |
|---|---|---|
| **Status** launcher (tick-in-circle icon) | Opens or closes the kit. Announces itself as **Open status kit** or **Close status kit** | Closed |
| Tooltip | "View the current page status and scan page status entries." | — |

There is no keyboard shortcut to open the Status Kit.

## Title bar

| Control | What it does | Values | Default |
|---|---|---|---|
| **Status Kit** title | Drag the title bar to move the kit | — | Bottom-left corner |
| **Focus mode** | Opens the kit again on the next page you load. Does not keep it open when another kit opens | On or off; remembered | Off |
| **Theme** | Switches the kit between light and dark | Light or dark; remembered | Follows the site |
| **Resize** | Normal (560 px wide) or expanded (up to 760 px wide) | Remembered | Normal |
| **Minimize** | Collapses the kit to its title bar | — | — |
| **Close** | Closes the kit ("Close Status Kit.") | — | — |

## This page card

| Element | What it shows |
|---|---|
| **This page** | Label |
| Status badge | The current page's status; tooltip "Current page status: [status]." Shows **Unknown** until worked out |
| Title link | The page's title; opens the page in a new tab |

## System status panel

| Control | What it does | Default |
|---|---|---|
| **System status** heading and chevron | Collapse or expand the panel | Expanded |
| **Online** / **Offline** pill | Your connection state | — |
| **Network**, **Hardware**, **Memory**, **Display**, **Runtime** tabs | Switch page | **Network** |

Readings, by tab:

| Tab | Readings |
|---|---|
| **Network** | **Connection**, **Speed**, **Latency**, **Data Saver** |
| **Hardware** | **Battery**, **Device memory**, **CPU threads** |
| **Memory** | **JS heap**, **Storage**, **Caches** |
| **Display** | **Resolution**, **Viewport**, **Pixel ratio**, **Color** |
| **Runtime** | **Frame rate**, **Page load**, **Service worker**, **App mode**, **Language**, **Time zone**, **Cookies** |

Readings refresh every 2 seconds while the kit is open. See [System status](system-status.md).

## Scanner

| Control | What it does |
|---|---|
| Path box (placeholder `https://auricartisan.com`) | The path or address to scan |
| **Scan** | Runs the scan (also `Enter` in the path box) |
| **Search pages...** | Filters results by title; appears after a scan |
| **Recent scans** | Your last 8 scans; select one to re-run it |
| Summary cards | **Pages**, **Tools**, **Stable**, **Beta**, **Issues** |
| Filter chips | **All**, one per status found, **Issues**; each with a count |
| Result count | **N pages** or **Showing N of M pages** |
| Target summary | For a page matching the path exactly: **URL**, **Category**, **Collection**, **Status** |
| Category groups | **Tools**, **Color Lab**, **Vision**, **Library**, **Company**, **Trust**, **Other**; collapsible and remembered |
| Result row | Thumbnail, title (tooltip shows the path), status badge; opens the page in a new tab |

## Statuses

**Stable**, **Beta**, **Alpha**, **Experimental**, **In development**, **Under testing**, **Maintenance**, **Research**, **Archived**, **Deprecated**, **Unknown**. **Issues** counts **Alpha**, **Deprecated** and **Archived**.

## Messages

| Message | When |
|---|---|
| **Scan a path for page statuses** — "Enter a URL or path (for example /tool/) and press Scan to list every page and its status." | Before a scan, or after scanning an empty box |
| **Scanning pages** with a count such as `12 / 48` | A scan is running |
| **No pages found** — "Nothing matched … Try a broader path like /tool/ or /library/." | No page starts with the path |
| **Couldn’t complete the scan** | The site map could not be read |
| **Nothing matches** | A filter or search hides every result |

## Keyboard

| Key | Where | What it does |
|---|---|---|
| `/` | Kit open, cursor not in a text box | Puts the cursor in the path box, or in **Search pages...** after a scan |
| `Enter` | Path box | Runs the scan |
| `Down arrow` | Path box or results search | Moves into the results |
| `Up arrow`, `Down arrow`, `Home`, `End` | Results | Move between the target summary, category headings and rows |
| `Enter` or `Space` | **System status** heading | Collapses or expands it |
| `Esc` | Kit open | Closes the kit |
