---
title: Search — Query syntax
description: The operators the Auric Artisan search page understands — phrases, exclusions and field filters — for site search and for web search.
product: Website › Search
updated: 2026-09-25
---

# Query syntax

Plain words are enough for most searches. The operators below narrow a search when you need to. The line under the search field shows how your query was read, with a chip for each filter, phrase, word and exclusion, so you can check that an operator was understood.

## Site search operators

| Operator | Example | What it does |
| --- | --- | --- |
| Words | `oklch gradient` | Finds pages that contain the words; pages with more of them, and with the words close together, rank higher. |
| `"…"` | `"colour blindness"` | Only pages where the words appear together, in that order. |
| `-word` | `palette -tailwind` | Leaves out pages that contain the word. The word must be at least two characters. |
| `type:` | `type:learn contrast` | Only one kind of page. See the list below. |
| `tag:` | `tag:oklch` | Only pages with a tag containing the value. |
| `title:` | `title:gamut` | Only pages whose title contains the value. |
| `desc:` or `description:` | `desc:printing` | Only pages whose description or text contains the value. |
| `path:` | `path:/library/learn/` | Only pages whose address contains the value. |
| `category:` | `category:legal` | Only pages whose category contains the value. Categories mostly match the `type:` values below. |
| A hex code | `#d3af37` | Shows the colour answer card. See [Instant answers](instant-answers.md). |
| Two hex codes | `#d3af37 #0d0d0d` | Shows the contrast-pair card. |

You can combine operators, for example `type:learn "colour blindness" -quiz`.

### Filter values with spaces

Put the value in quotes after the colon: `title:"contrast ratio"`.

### A filter on its own

A filter works without any words. `type:changelog` lists changelog pages, and `tag:oklch` lists everything tagged OKLCH.

### Values for type:

`type:` must match exactly. The main values are:

| Value | Pages |
| --- | --- |
| `learn` | Learn articles |
| `documentation` | Documentation guides |
| `tool` | Tool pages |
| `library` | Library pages |
| `blog` | Blog posts |
| `changelog` | Changelog pages |
| `company` | Company pages |
| `legal` | Legal pages |
| `portfolio` | Portfolios in the Portfolio Index |

The section tabs are often quicker than `type:`. See [Search this site](search-this-site.md).

## Web search operators

When the globe is on, the web index understands:

| Operator | Example | What it does |
| --- | --- | --- |
| Words | `color contrast` | Finds pages with the words. Pages with every word are shown before pages missing one. |
| `"…"` | `"design tokens"` | The words together, in that order. |
| `-word` | `gradient -css` | Leaves out pages with the word. |
| `site:` | `site:w3.org contrast` | Only pages on that site and its subdomains. `host:` does the same. |
| `intitle:` | `intitle:palette` | Only pages whose title contains the value. |

The site-search operators `type:`, `tag:`, `title:`, `desc:`, `path:` and `category:` do not apply to web search, and the answer cards appear only in site search.

## Tips

- If a query with operators finds nothing, the **Worth trying** list names the operator most likely to be the cause.
- Hex codes work with or without `#`, in three-digit or six-digit form: `#abc`, `abc`, `#aabbcc` or `aabbcc`.
- A word of three or six letters made only from the letters a to f, such as `bad` or `facade`, is read as a hex code too. Put it in quotes to search for the word itself.
