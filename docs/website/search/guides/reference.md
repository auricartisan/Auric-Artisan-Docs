---
title: Search — Reference
description: Every control, operator, status line, message and limit on the Auric Artisan search page and in the Search Console.
product: Website › Search
updated: 2026-09-25
---

# Search reference

## Search page controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Search field | Takes your query. Results start at two characters. | Any text | Empty |
| Clear button | Empties the field and returns to the start screen. Appears once you type. | — | Hidden |
| Globe button (**Web search**) | Switches between site search and web search. | On, off | Off |
| Mode label | Shows which index you are searching. | **LOCAL**, **GLOBAL** | **LOCAL** |
| Suggestions list | Pages and tags that match what you typed (site search), or words from the web index (web search). | Up to 8 | — |
| Section tabs | Filter site-search results by kind of page, with a count on each. | **All**, **Tools**, **Learn**, **Docs**, **Blog**, **Portfolios**, **Pages** | **All** |
| **Tools** menu | Opens sorting and ranking options. | — | Closed |
| **Sort by** | Orders site-search results. Shown with two or more results. | **Relevance**, **Newest**, **A–Z** | **Relevance** |
| **Ranking** | Shows the field weights and tuning values. | — | — |
| **Show the score on every result** | Adds a score bar, number and matched fields to each result. Remembered in this browser. | On, off | Off |
| Query chips | Show how the query was read: filters, colours, phrases, words, exclusions and related words (dashed). | — | — |
| **did you mean** | Runs the corrected query. | — | — |
| **More results** | Loads the next 20 web results, with how many are left. | — | — |
| **Search the web instead** | On the no-results screen: turns the globe on and runs the query. | — | — |
| **Recent** chips | Run a recent search again. | Up to 6 | — |
| **Clear** (recent) | Empties the recent searches list. | — | — |

## Section tabs

| Tab | Contents | Result label |
| --- | --- | --- |
| **Tools** | Tool pages and Collections | **Tool** |
| **Learn** | Learn articles | **Learn** |
| **Docs** | Documentation and changelog | **Docs** |
| **Blog** | Blog posts | **Blog** |
| **Portfolios** | Portfolio Index entries and the index page | **Portfolio** |
| **Pages** | Everything else, including the colour libraries | **Page** |

## Field weights

| Field | Weight |
| --- | --- |
| Title | ×6 |
| Tags | ×4 |
| Description | ×3 |
| Category | ×2 |
| URL | ×1.5 |
| Content | ×1 |
| k1 / b | 1.2 / 0.4 |

## Operators

| Operator | Site search | Web search |
| --- | --- | --- |
| `"a phrase"` | Yes | Yes |
| `-word` | Yes | Yes |
| `type:` | Yes | No |
| `tag:` | Yes | No |
| `title:` | Yes | No |
| `desc:`, `description:` | Yes | No |
| `path:` | Yes | No |
| `category:` | Yes | No |
| `site:`, `host:` | No | Yes |
| `intitle:` | No | Yes |
| Hex code or two hex codes | Answer card | No |

Details and examples: [Query syntax](query-syntax.md).

## Start screen

| Element | What it does |
| --- | --- |
| Privacy line | **Indexed on this device — nothing you type leaves the browser** |
| **Paste a hex** card | Runs the query `#D3AF37`. |
| **Give it two** card | Runs the query `#D3AF37 #0D0D0D`. |
| **Narrow by section** card | Runs `type:learn contrast` and shows its first two results and count. |
| Section ribbon | The largest sections with their page counts, each linking to its section; and the total **pages in the index**. |
| **More ways to ask** | Puts `type:learn`, `"a phrase"`, `-word` or `tag:oklch` in the field. |
| **Put your site in it** | Opens the Search Console. |

## Answer cards

| Card | Appears when | Buttons |
| --- | --- | --- |
| **Colour** | The query holds one hex code. | **Check it against a background**, **Palettes with it** |
| **Contrast pair** | The query holds two or more hex codes. | **Open the checker**, **Swap them** |
| **Tool** | The whole query is `contrast`, `contrast checker`, `palette`, `gradient`, `image picker` or `analyzer`. | **Open the tool** |

Grades and thresholds: [Instant answers](instant-answers.md).

## Status lines

| Status line | When |
| --- | --- |
| **Index ready — N items indexed in N ms** | The page has loaded its index. |
| **Search index is empty. Try refreshing the page.** | The index did not load. |
| **About N results (N ms)** | Site-search results. Adds **in** a section when a tab is chosen. |
| **No results for** your query | Nothing matched in site search. |
| **All N shown** | Every site-search result is on screen. |
| **Searching the web for** your query | Web search is running. |
| **N results from the crawled index for** your query | Web results from the index. |
| **about N results** | The web count is an estimate. |
| **answered without** a word, **exact matches first** | The web search was relaxed. |
| **showing results for** a word; **search instead for** your word | The web search corrected your spelling. |
| **N global results from N sources** | Live web results, used when the index had none. |
| **No global results for** your query | The live web search found nothing. |
| **Global search failed for** your query | The live web search failed. |

## Page address parameters

| Parameter | What it does | Example |
| --- | --- | --- |
| `q` | Runs a site search for the value. | `/search/?q=oklch` |
| `scope` | Opens a section tab: `all`, `tools`, `learn`, `docs`, `blog`, `portfolios` or `pages`. | `/search/?q=oklch&scope=learn` |

## Limits

| Item | Limit |
| --- | --- |
| Shortest query | 2 characters |
| Site-search results listed | Up to 100 |
| First site-search page | 20 results, then 12 more at a time |
| Web results per page | 20 |
| Suggestions | Up to 8 |
| Recent searches | 6 |

## Search Console: layout

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| Site switcher | Chooses the site every section shows. Appears with two or more sites. | Your sites | The site needing attention, else the first |
| Period | Sets the period for every dated figure. | **7d**, **28d**, **90d** | **28d** |
| Header line | Last crawl and queue, for example **Crawled 3 hours ago • 42 queued for the next pass**. | — | — |
| Side rail | Opens a section. Arrow keys, `Home` and `End` move between sections. | **Overview**, **Performance**, **Coverage**, **Pages**, **Links**, **Submit**, **Your sites**, **Portfolios** | **Overview** |

## Search Console: verification

| Method | Label | What to add | Notes |
| --- | --- | --- | --- |
| **File on the site** | Quickest | A text file at `/auric-site-verification-TOKEN.txt` containing the token | Easiest on a static site. |
| **Meta tag** | No deploy | `<meta name="auric-site-verification" content="TOKEN">` in the home page head | Removing it later un-verifies the site. |
| **DNS TXT record** | Strongest | A TXT record with the value shown | Covers every subdomain; can take an hour to appear. |

**Check now** tries all three. The report for each shows ✓ or ✕, where it looked, the detail, **expected** and **found instead**.

## Search Console: Performance

| Control or figure | Meaning |
| --- | --- |
| **Impressions** | Times your site appeared in a web-search result. |
| **Clicks** | Times someone opened it. |
| **Click-through**, **CTR** | Clicks divided by impressions. |
| **Average position**, **Position** | Where it appeared in the list; lower is better. |
| **By search**, **By page**, **By day**, **By country**, **By device** | How the table is grouped. Default **By search**. |
| Change badges | Percentage change against the previous period, or **no change**. |
| Name or topic bar | Impressions from searches for your name against searches for a topic. **By search** only. |

## Search Console: Coverage totals

| Total | Meaning |
| --- | --- |
| **On its way** | Fetched and kept. Searchable after the next index build. |
| **Needs you** | Only you can change these. |
| **Nothing to do** | Real, counted, and working as intended. |

## Coverage reasons

| Label | Yours to fix | Meaning | What to do |
| --- | --- | --- | --- |
| **Indexed** | — | Fetched, kept and searchable. | Nothing. |
| **Discovered, not yet crawled** | No | Known and queued; crawling is paced per site. | Nothing, or submit it to move it up. |
| **Crawled, waiting for the next index build** | No | Fetched and kept; searchable after the next build. | Nothing. |
| **Blocked by robots.txt** | Yes | Your robots.txt tells crawlers not to fetch it. | Allow the path in robots.txt. |
| **Excluded by noindex** | Yes | The page asks not to be indexed. | Remove the noindex tag or header. |
| **Too little content** | Yes | Almost no text once navigation is stripped. | Serve real text; the crawler does not run JavaScript. |
| **Not found** | Yes | The server answered 404, but something links to it. | Restore, redirect or remove the links. |
| **Timed out** | Yes | The server did not answer in time. | Speed up the page; it is retried. |
| **Could not be fetched** | Yes | The request failed. It is retried. | Check the page is reachable from outside your network. |
| **Duplicate of another page** | No | Near-identical to an indexed page. | Nothing, or set `rel=canonical`. |
| **Redirected** | No | Forwards elsewhere; the destination is indexed. | Nothing, unless the destination is wrong. |
| **A sitemap, read for its links** | No | A sitemap; its addresses were queued. | Nothing. |
| **Not a web page** | No | Not HTML, such as a PDF or image. | Nothing, unless you expected a page. |

## Search Console: Pages

| Control | What it does | Default |
| --- | --- | --- |
| **Find a path** | Filters addresses as you type. | Empty |
| State chips | **Everything**, **Indexed**, **Waiting**, **Excluded**, **Errored**, with counts. | **Everything** |
| **By folder**, **Flat list** | Groups addresses by folder, or lists them. | **By folder** |
| **Inspect** | Opens the inspection panel for one address. | — |

## Search Console: inspection

| Field or button | Meaning |
| --- | --- |
| Verdict | The state in words, with **To fix:** or **Note:**. |
| **Status** | The HTTP status at the last crawl. |
| **Canonical** | The canonical address the page gave. |
| **First seen**, **Last indexed** | When the crawler first met it, and when it last entered the index. |
| **Indexed title** | The title held in the index. |
| **Static rank** | The page's weight, out of 255. |
| **In the queue**, **Last error** | Where a queued address came from, its priority and attempts, and its last error. |
| **Fetch the page now**, **Test live** | Fetch the live page and show **Outcome**, **Redirects to**, **Canonical**, **Robots meta** and **X-Robots-Tag**. |
| **Still noindex** | The live page still asks not to be indexed. |
| **Title has changed** | The live title differs from the indexed one. |
| **Searches it appears for** | Searches, impressions and position for this address. |
| **Ask for a crawl** | Queues the address. |

## Search Console: Submit

| Item | Meaning |
| --- | --- |
| **Add a page or a sitemap** | The address to crawl. **Submit** or `Enter` sends it. |
| Queue sources | **from your sitemaps**, **you asked for**, **sitemaps to re-read**, **found by following links**, **due a re-crawl** |
| Sitemap tags | **You added**, **Detected**, **Found while crawling** |

## Search Console: messages

| Message | Meaning |
| --- | --- |
| **Sign in to use the Search Console.** | You are signed out. |
| **Type a domain or a URL prefix first.** | **Add** was selected with an empty field. |
| **You have already added that property.** | The site is already on your account. |
| **A property is a domain like example.com or a URL prefix like https://example.com/docs/.** | The value was not a valid domain. |
| **Verify a property first.** | The section needs a verified site. |
| **Which URL?** | **Submit** was selected with an empty field. |
| **The search service did not answer.** | The console could not reach its service. Try again later. |
