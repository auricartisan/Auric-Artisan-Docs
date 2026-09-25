---
title: Analyzer — Scan a whole site
description: Audit several pages of one site in a single run, follow the live progress, and page through the per-page results.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Scan a whole site

A site scan finds the pages of a site from its links and sitemap, audits each one in a real browser on Auric Artisan's servers, and combines the results into one report with a page-by-page breakdown. Use it to find the shared components that fail on every page, or to check a set of pages before a release.

## Before you start

- You need to be **signed in**. Without an account the scan stops with "Sign in to scan a site. Analyzing this page still works without an account."
- Whole-site scanning is part of the **Artisan plan and above**. On other plans the scanner answers "Whole-site crawling is part of the Artisan plan and above."
- A site scan costs tokens. The pricing page describes it as one token per page analysed, so a 24-page crawl costs 24. The token sheet shows the exact quote, with a line for finding the pages and a line for the pages themselves. Tokens are held when the scan starts; you are charged for the pages that come back and refunded the rest.
- One run audits **up to 24 pages**.

## The site scan settings

Switch to **Advanced** and open **Site scan settings** under the strip.

| Setting | What it does | Values | Default |
| --- | --- | --- | --- |
| **Scan Site** | Starts the site scan for the address in the URL field | Button | — |
| **Robots** | Follow robots.txt rules while scanning | On or off | On |
| **Subdomains** | Include subdomains in the scan | On or off | Off |
| **Pages** | How many pages to audit, with a time estimate beside it | 1 to 24 | 10 |
| **Show** | How many detailed results to show per page of the results list | 25 or 50 | 25 |
| **Workers** | Concurrent scan workers: higher is faster, lower is gentler on the site | 1 to 20 | 3 |
| **Public proxy** | Fetch cross-origin pages through third-party public CORS proxies | On or off | Off |

**Pages** limits only how many pages are audited. It does not limit the site map: discovery still reads robots.txt and the whole sitemap tree, so the **Site Map** section covers the entire site however few pages you audit. The estimate beside the field, for example "≈ 23s", updates as you type.

With **Public proxy** on, the address being analysed is shared with those third-party services. It is off unless you turn it on.

> **Note:** On auricartisan.com the crawl runs on Auric Artisan's servers, and the scanner receives the address and the **Pages** number. In the current version the **Robots**, **Subdomains** and **Workers** settings do not change a site scan on the live site. **Public proxy** only affects single-page runs that fall back to reading a page's HTML in your browser.

## Run a site scan

1. Type the site's address in the URL field, for example `https://example.com/`.
2. Select **Advanced**, then open **Site scan settings**.
3. Set **Pages** to the number of pages you want audited, up to 24.
4. Check the token meter, or open the token sheet to see the quote.
5. Select **Scan Site**.
6. Follow the live console in the Overview panel (below).
7. When it ends, the live line reads "Scan complete: N pages scanned" and the report opens.

To stop part-way, select **Cancel** in the strip.

## The live console

While a site scan runs, the Overview panel shows a console headed **Live site audit**. The large title names the current phase, starting with "Discovering pages", then "Found N pages — auditing…". Below it, five folding groups count pages as they move:

| Group | What it lists |
| --- | --- |
| **In flight** | Pages being audited right now |
| **Completed pages** | Pages audited, with their score, title and issue count |
| **Failed pages** | Pages that could not be audited, and why |
| **Skipped** | Pages that were found but not audited |
| **Discovery & budget** | How pages were found and how the page budget was spent |

The progress rail's bar tracks the share of pages finished.

## Read the results

A site scan produces one combined report. Every section reads the combined result, and the Overview adds two cards:

- **Full-Site Scan** — counts of **Completed**, **Failed**, **Skipped** and **Found** pages (shown as "Found (sitemap)" when a sitemap was used).
- **Page-By-Page Breakdown** — one row per audited page, each with its overall score, accessibility, SEO, performance and security scores, issue count and its findings.

The breakdown list has its own controls:

| Control | What it does |
| --- | --- |
| Sort menu | **Lowest score** (default), **Highest score**, **Most issues**, **Title A-Z**, **URL A-Z**, **Scan order** |
| **25 / page**, **50 / page** | Rows per page of the list |
| **First**, **Prev**, **Next**, **Last** | Move through the list |
| **Expand visible**, **Collapse visible** | Open or close every row on screen |

A line above the list says which rows are showing, for example "Showing 1-25 of 24 pages". If full details for a page of rows are still loading, compact rows are shown meanwhile.

The **A11y+** panel adds an **A11y+ · Page-by-Page** card for the same pages, and the **Site Map** panel merges findings across pages under **Site-wide Findings (merged)**.

## How the combined score is worked out

- Each page is scored on its own, then the scores are combined into the site's result.
- For accessibility, each page's score leans on the in-depth audit of that page's rendered markup, and the combined accessibility score can only be lowered by it, never raised.
- A page the scanner could not reach is listed under **Failed pages** rather than scored.

## Pages the scanner cannot audit

The scanner runs in a real browser on Auric Artisan's servers. It cannot audit:

- pages behind a login, a bot challenge or a strict firewall. The page is reported as refused, with the HTTP status, and the advice to run the audit from a browser that is already on the page;
- private and local addresses such as `localhost`, `127.0.0.1`, `10.x.x.x`, `192.168.x.x`, `172.16.x.x` to `172.31.x.x` and `169.254.x.x`. These are refused with "That address is not reachable from the scanner.";
- anything other than `http` and `https` addresses ("Only http and https URLs can be scanned.").

## After the scan

The site scan is filed in your library as its own project, named "Audit · " followed by the host, separate from single-page audits of the same site. Re-scanning the same site adds a new version you can compare with the last one. See [Save, reopen and compare](save-reopen-and-compare.md).
