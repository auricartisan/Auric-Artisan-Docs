---
title: Search — FAQ
description: Short answers to common questions about the Auric Artisan search page, web search and the Search Console.
product: Website › Search
updated: 2026-09-25
---

# Search FAQ

## Does the site search send what I type anywhere?

No. Site search runs in your browser against an index the page downloads once. The start screen says so: **Indexed on this device — nothing you type leaves the browser**. Web search is different; see below.

## Does web search send my query?

Yes. With the globe on, your query goes to Auric Artisan's search service. When you open a web result, the query, the result and its position are reported too. See [Privacy](../others/privacy.md).

## Is web search the same as Google?

No. It is Auric Artisan's own independent crawl of the web, much smaller than Google's or Bing's.

## Do I need an account to search?

No. Only the Search Console needs an account.

## Can I link to a search?

Yes. Copy the page address after searching. It includes `?q=` and, for a section tab, `&scope=`.

## Why does a hex code show a card instead of results?

A colour is usually the answer to a colour query. The card shows the colour and its contrast. The results for the hex code, if any, follow below it.

## Which colour comes first in a pair?

The text colour first, then the background: `#d3af37 #0d0d0d` is gold text on near-black. The ratio is the same either way; the sample text changes. **Swap them** reverses the pair.

## Why does #777777 on white fail AA?

Its ratio is 4.48:1, just under the 4.5:1 that AA needs for body text. The card uses the exact ratio, not a rounded one.

## Why did a page about swatches appear when I searched for palettes?

Related words count at reduced weight. The line under the field shows them dashed. See [Understand the ranking](understand-the-ranking.md).

## Is the Search Console free?

Yes, for any site you own.

## Does the Search Console affect my Google ranking?

No. It changes only what Auric Artisan's own index knows about your site.

## How long until a submitted page is searchable?

A page asked for from the inspection panel is crawled within a day. After crawling it waits for the next index build before it becomes searchable.

## How do I stop the crawler?

Disallow it in your robots.txt, in a group for `AuricBot` or for all crawlers (`*`). See [Request a crawl](request-a-crawl.md).

## If I remove my site from the console, does it leave the index?

No. Its pages stay in the index. Removing it takes the site off your console and deletes its search history.

## How many sites can I add?

There is no limit.

## Can I list my portfolio from the console?

Yes, in the **Portfolios** section. See [List your portfolio](../../portfolio/docs/list-your-portfolio.md).
