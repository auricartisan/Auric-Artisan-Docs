---
title: Status Kit — Check a page's status
description: Read the status of the page you are on in the Status Kit, and what each status label means.
product: Website › Kits › Status Kit
updated: 2026-09-25
---

# Check a page's status

Every page on Auric Artisan has a status that says how finished it is. The Status Kit's **This page** card shows it for the page you are on.

## Read the This page card

1. Open the Status Kit (**Page utilities** > **Status**).
2. Look at the **This page** card at the top.

The card shows:

- the label **This page**;
- a coloured status badge, for example **Beta**. Its tooltip reads "Current page status: Beta.";
- the page's title as a link. Selecting it opens the same page in a new tab.

Until the status has been worked out, the badge reads **Unknown** for a moment.

## What each status means

The kit can show the labels below. The site does not publish formal definitions for them; they carry their usual software meanings.

| Status | Meaning |
|---|---|
| **Stable** | Finished and expected to keep working as it does now |
| **Beta** | Complete and usable, still being refined. Most of the site is Beta, matching the site's overall status |
| **Alpha** | Early; expect gaps and changes |
| **Experimental** | A trial feature that may change a lot or be withdrawn |
| **In development** | Being built |
| **Under testing** | Being tested before a wider release |
| **Maintenance** | Temporarily limited while it is being worked on |
| **Research** | A research tool; results are exploratory |
| **Archived** | Kept for reference, no longer developed |
| **Deprecated** | Being retired; use its replacement |
| **Unknown** | No status could be found |

The scanner counts **Alpha**, **Deprecated** and **Archived** pages as **Issues**.

## How a page gets its status

The site keeps one central list of statuses. A page takes the status of the closest entry that covers it: an entry for that exact page wins, then an entry for the folder it sits in. Pages with no closer entry take the status of the whole site, which is **Beta**.

At the time of writing:

- the Vision Simulation lab is **Experimental**;
- the changelog, the timeline, blog and documentation articles, the About, Accessibility and FAQ pages, the legal pages and the Collections page are **Stable**;
- everything else, including the home page and the tools, is **Beta**.

These assignments change as the site develops; the kit always shows the current one.

## The site status versus a page status

The Menu Kit shows a status chip for the whole site. The Status Kit shows the status of individual pages. They often agree, because most pages share the site's **Beta** status.

## Related

- [Scan a section of the site](scan-a-section.md)
- [Reference](reference.md)
