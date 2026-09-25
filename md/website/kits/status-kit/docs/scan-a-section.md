---
title: Status Kit — Scan a section of the site
description: List every page under a path with its status, then summarise, filter, search and repeat the scan.
product: Website › Kits › Status Kit
updated: 2026-09-25
---

# Scan a section of the site

The scanner lists every page of auricartisan.com whose address starts with a path you give, and shows each page's status.

## Run a scan

1. Open the Status Kit. The cursor is in the path box.
2. Type a path such as `/tool/`, `/library/` or `/company/`. You can also paste a full address such as `https://auricartisan.com/library/blog/`; only its path is used.
3. Press `Enter` or select **Scan**.

While the scan runs, the results area shows **Scanning pages** with a running count such as `12 / 48`. The kit reads the site map to find the pages, then fetches each page to read its title, so a large section takes a little while.

## Read the results

When the scan finishes you see, from top to bottom:

1. **Summary cards.**

   | Card | Counts |
   |---|---|
   | **Pages** | Every page found |
   | **Tools** | Pages in the tool categories (Tools, Color Lab and Vision) |
   | **Stable** | Pages with the Stable status |
   | **Beta** | Pages with the Beta status |
   | **Issues** | Pages that are Alpha, Deprecated or Archived |

2. **Filter chips.** **All**, one chip per status found, and **Issues** if any, each with a count. They appear only when the results contain more than one status or any issues.
3. **Result count**, for example **48 pages**, or **Showing 12 of 48 pages** when a filter or search is active.
4. **Target page.** If a page's address matches your path exactly (for example `/library/` itself), it appears first as an expanded summary with its **URL**, **Category**, **Collection** and **Status**.
5. **Category groups.** The other pages, grouped under collapsible headings with a count: **Tools**, **Color Lab**, **Vision**, **Library**, **Company**, **Trust** and **Other**. Each row shows a thumbnail, the page title and a status badge. Hover over a title to see its path.

Select a page row to open that page in a new tab.

## Filter and search the results

- Select a filter chip to show only pages with that status, or **Issues** for the problem statuses. Select **All** to clear it.
- Type in **Search pages...** (it appears after a scan) to show only pages whose title contains your text.

The two combine. If nothing matches, you see **Nothing matches** with either "No pages match" and your search, or "No pages have that status. Try a different filter."

## Collapse groups

Select a category heading to collapse or expand it. The kit remembers which categories you collapsed.

## Recent scans

After your first scan, a **Recent scans** section lists your last eight scans, newest first. Each shows the path you typed, "Scanned" with how long ago (for example **Scanned 5 minutes ago**), the number of pages, and the status of the target page. Select one to run it again.

## Which pages are included

- Pages come from the site map. If the site map cannot be read, the kit falls back to the pages listed in the Menu Kit.
- The home page (`/`) is never listed, even when you scan `/`.
- Individual colour pages, whose addresses start with `/color/`, are left out.
- Paths are matched from the start: `/tool/` finds `/tool/analyzer/` but `/analyzer/` finds nothing.

## Empty and error states

| Message | Meaning |
|---|---|
| **Scan a path for page statuses** | No scan yet. Enter a path such as `/tool/` and press **Scan** |
| **No pages found** — "Nothing matched" your path, "Try a broader path like /tool/ or /library/." | No page starts with that path |
| **Couldn’t complete the scan** | Something went wrong reading the site map. Check your connection and try again |

Selecting **Scan** with an empty box returns to the starting message.

## Related

- [Check a page's status](check-page-status.md)
- [Reference](reference.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
