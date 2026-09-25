---
title: Analyzer — Privacy
description: What the Analyzer keeps in your browser, what it sends to Auric Artisan's servers or third parties, and how to delete it.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Analyzer privacy

This page explains where your data goes when you use the Analyzer. For the site's full privacy policy, see the company and legal docs in [Company and legal](../../../../company-and-legal/README.md).

## What happens in your browser

When you audit a page on auricartisan.com and you are not signed in, the whole audit runs in your browser. The page is loaded into a hidden frame on your device, measured there, and nothing about the audit is sent anywhere.

Contrast, palette, media and SEO analysis run on your own device, whichever way the page was reached. When a page is rendered on Auric Artisan's servers, the accessibility rules run there, in the server's browser, because they need the page as it was laid out.

## What goes to Auric Artisan's servers

| When | What is sent | Why |
| --- | --- | --- |
| You are signed in and audit another website | The address you entered | The page is rendered on the server and the results come back to you |
| You run **Scan Site** | The address and the number of pages | The site is crawled and each page audited on the server |
| You use **Capture all devices** or the Device Lab captures screenshots | The address | Screenshots are rendered on the server |
| A run, scan or capture is metered | Your account and the token amount | Tokens and the monthly allowance are recorded against your account |
| You select **Keep in my account** in Compare | That version's full report | So you can open it on another device |

The audited page is fetched by Auric Artisan's servers, so the site you audit sees a visit from them, not from you.

## What goes to third parties

| When | Who | What |
| --- | --- | --- |
| You turn on **Public proxy** (off by default) | Third-party public CORS proxy services | The address being analysed, when your browser falls back to reading a page's HTML |
| You open a **How to meet this** link | The W3C website | A normal visit to that page |
| You select **Email** in Insights | Your own email app | A draft with the URL, score and headlines |

## What is kept in your browser

- Every run's full report, its versions, and the site's palette, in your library
- The history list, saved palettes and monitoring list in the **Workspace** section
- A copy of each audited page's HTML for up to 7 days, used only if a later run cannot reach the page
- Your preferences: mode, panel layouts, saved layouts, ticked checks, fix mode, **Public proxy**, network profile, issue statuses and custom rules
- Whether you dismissed the API hint

This data stays on this device and in this browser. It is not shared with other visitors.

## What share links contain

- The strip's **Share** link carries the audited address and its score.
- The **Share Link** in Report carries the address, the score and the issue count.
- The **Copy share link** in Insights carries the address.

Anyone who has the link can read these values. None of the links carries the full report or the scanned pages.

## Delete your data

| To delete | Do this |
| --- | --- |
| The Workspace history, saved palettes, notes and pinned findings | **Workspace** › **Clear All**, then **Clear workspace** |
| One saved project or all projects | Remove them in your library |
| A report kept in your account | **Compare**, choose the version, select **In your account ✓** to remove the account copy |
| Everything the Analyzer stored in this browser | Clear this site's data in your browser settings |
| Reports kept in your account, all at once | Deleting your account removes them |

Clearing site data cannot be undone: versions that are not kept in your account are lost.
