---
title: Search — Read the console reports
description: What the Overview, Performance, Coverage, Pages and Links sections of the Auric Artisan Search Console show, and how to inspect a single address.
product: Website › Search
updated: 2026-09-25
---

# Read the console reports

These sections show data for the site chosen in the console header, once it is verified. Dated figures follow the period chosen at the top: **7d**, **28d** or **90d**. Each figure is compared with the same length of time just before it.

## What counts as an impression and a click

- An **impression** is counted when a page from your site appears in a result on Auric Artisan's web search.
- A **click** is counted when a searcher opens that result.
- **Position** is where the result appeared in the list; lower is better.

Figures start counting the first time your site appears in a result.

## Overview

The console opens on the Overview. It leads with what you can fix.

- **Four cards**: **Indexed pages**, with the share of known addresses; **Impressions** ("times you appeared"); **Clicks** ("times someone came"); **Average position** ("lower is better"). Each has a small trend line and the change against the previous period. In your first period the card says **first period** instead.
- **In the index** and **Not in the index**: the two counts, a bar that splits them, and how many of the addresses outside the index are yours to fix. The line below gives the total number of addresses the crawler has met on the site.
- **Why pages are not indexed**: every reason the crawler recorded, most common first. Reasons you can act on are listed first, marked **Yours**, each with its fix and a **Show them** button that opens **Pages** filtered to those addresses. The rest follow under **Nothing to do about these**. **Open coverage** goes to the full Coverage section.
- **Crawl log**: what the crawler did, newest first. Similar outcomes from the same pass are grouped, for example **12 pages — Indexed**. Select a group to see its addresses, grouped by folder.

## Performance

**Performance** lists every search that put your site in front of somebody.

- **Four figures** at the top: **Impressions**, **Clicks**, **Click-through** (clicks as a share of impressions) and **Average position**, each with the change against the previous period.
- **A chart** of impressions and clicks per day, with the peak of each. When there are only a few days with any impressions, the chart shows those days as columns instead, and a note says how many quiet days came before.
- **Choose how to group the table**: **By search**, **By page**, **By day**, **By country** or **By device**.
- **The table**: the search, page, day, country or device; **Impressions**, with a bar; **Clicks**; **CTR**; and **Position**. A dash means there were no clicks to calculate from.
- **By name or by topic**: grouped by search, a bar splits impressions between people who **were already looking for you by name** and people who **found you for something they wanted**. A search counts as "by name" when it contains your domain's name.

If nothing has been recorded yet, the page says **No impressions recorded yet. They start counting the first time this site appears in a result.**

## Coverage

**Coverage** covers every address the crawler knows about on your site and, for those not indexed, why not.

At the top, three totals add up to every address outside the index:

| Total | Meaning |
| --- | --- |
| **On its way** | Fetched and kept. Searchable after the next index build. |
| **Needs you** | Only you can change these. |
| **Nothing to do** | Real, counted, and working as intended. |

Below them:

- A heading such as **3 pages need you**, or **Nothing needs you**.
- One row per reason you can act on, with what it means and **To fix:**. Select the page count on a row to open **Pages** filtered to those addresses.
- A folded list of the reasons with nothing to do, for example **40 with nothing to do about them**. Open it to read each one.
- **Crawl activity, 28 days**: a bar for each day, the total fetched, the peak day, and a chip for each HTTP status code the site answered with, with a count.
- **Sitemaps**: the sitemaps the crawler has read, and how many addresses were queued from them.

Every reason is listed, with its meaning and fix, under **Coverage reasons** in the [Reference](reference.md).

## Pages

**Pages** lists every address on the site that the crawler has an opinion about.

- **Find a path** filters the list as you type. Try a folder such as `/blog/`, a word, or `.xml`.
- The chips **Everything**, **Indexed**, **Waiting**, **Excluded** and **Errored** filter by state, each with its count. **Waiting** covers addresses discovered or crawled but not yet in the index.
- **By folder** groups addresses by the folder they sit in, largest first. Each folder shows a bar of its states, its count and how many are **to fix**. Select a folder to open it. **Flat list** shows every address in one list.
- Each address shows its state, when it was last crawled, and its canonical address when that differs. Select the address to open it in a new tab.
- On a large site, a note says the list shows the most recently crawled addresses only.

### Inspect an address

Select **Inspect** on any row. A panel opens over the list:

- **A verdict** in words: the state, what it means, and **To fix:** or **Note:**.
- **Last crawl**: the HTTP **Status**, **Canonical**, **First seen**, **Last indexed**, the **Indexed title**, the page's **Static rank** out of 255, and, if it is queued, where it came from, its priority, attempts and any **Last error**.
- **Live now**: select **Fetch the page now** to fetch the page as it is at this moment. The panel shows the **Outcome** (status and time), any redirect, the canonical address, the robots meta tag and X-Robots-Tag header, **Still noindex** if the live page still asks not to be indexed, and **Title has changed** if the title differs from the indexed one.
- **Searches it appears for**: each search with impressions and position, or **No impressions for this page yet.**

At the bottom, **Ask for a crawl** queues the address; the panel says **Queued. Crawled within a day.** **Test live** fetches the live page again. Close the panel with the close button, by selecting outside it, or with `Escape`.

## Links

**Links** is meant to show who links to you and how the crawler walks your site: **Sites linking to you**, **Your most-linked pages**, **Pages nothing links to** and **Links that go nowhere**. These are **Not collected yet**, so the section stays empty rather than showing numbers nobody measured.

What it shows today is the site's rank, out of 255. Rank is worked out from links between sites. It is how much weight a page on your site carries when the search is choosing between two equally good matches.
