---
title: Search — Search the web
description: How to use the globe on the Auric Artisan search page to search Auric Artisan's own index of the web, with suggestions, spelling correction and paging.
product: Website › Search
updated: 2026-09-25
---

# Search the web

The globe button beside the search field switches from the site to the web. Web search uses Auric Artisan's own crawl of the web: an independent index, very much smaller than Google's or Bing's. Pages get into it when the crawler finds them by following links, and when site owners submit them through the [Search Console](search-console.md).

## Switch the globe on

1. Select the globe button beside the search field. Its tooltip reads **Web search**. The mode label beside the status line changes from **LOCAL** to **GLOBAL**.
2. If there is already a query in the field, it runs on the web straight away.
3. To go back to site search, select the globe again.

You can also switch from the no-results screen: **Search the web instead** turns the globe on and runs the same query.

## Search

1. Type your query. In web mode, results do not update as you type. Instead, a list suggests up to eight words from the web index's own vocabulary, most common first, marked **web**.
2. Press `Enter`, or choose a suggestion, to search.
3. The status line reads **Searching the web for** your query while it works.

## Read the results

Each result shows:

- The site's icon, or the first letter of its name on a coloured tile when it has no icon.
- The page title, with your words highlighted.
- The site name and its address.
- An excerpt with your words highlighted.
- Sometimes a tag such as **missing: gradient**, when the page does not contain one of your words.

Web results always open in a new tab.

The status line says how many results the index holds, for example **365 results from the crawled index for "github"**, and how long it took. It may add:

| Status line addition | What it means |
| --- | --- |
| **about** before the count | The count is an estimate. This happens with `site:` and `intitle:` filters. |
| **answered without** a word, **exact matches first** | No page had every word, so the search was relaxed. Pages with all your words, if any, come first. |
| **showing results for** a word; **search instead for** your word | Your query found nothing, so a corrected spelling was used. Select **search instead for** to see the results for your original spelling. |

## More results

Web results come 20 at a time. Under the list, **More results** shows how many are left, for example **More results 345 left**. Select it to add the next 20. The button disappears when there is nothing more.

## Operators

Web search understands phrases in quotes, `-word` exclusions, `site:` (or `host:`) and `intitle:`. See [Query syntax](query-syntax.md).

## When the index has nothing

If the crawled index has no results for your query, the page searches the web live instead. This takes longer. The status line then reads, for example, **12 global results from 4 sources, 15 crawled pages**. If that finds nothing too, it reads **No global results for** your query. If it fails, it reads **Global search failed for** your query, with the reason.

## What web mode does not do

The section tabs, sorting, answer cards and ranking panel belong to site search. They do not apply to web results.

## Your privacy in web mode

Web queries are sent to Auric Artisan's search service, unlike site search. When you open a web result, the page tells Auric Artisan the query, which result you chose and its position in the list. This helps ranking, and it gives site owners their click counts in the Search Console. Site icons are fetched through Auric Artisan, so other services are not told which sites appear in your results. See [Privacy](../others/privacy.md).
