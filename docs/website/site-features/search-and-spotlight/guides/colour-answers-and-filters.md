---
title: Search and Spotlight — Colour answers and filters
description: Get instant colour and contrast answers in Spotlight, and use field filters, quoted phrases and exclusions.
product: Website › Site features › Search and Spotlight
updated: 2026-09-25
---

# Colour answers and filters

Spotlight reads what you type and, for some kinds of query, answers directly. A small **mode chip** at the start of the search box says how it read your query.

| You type | Chip | What Spotlight does |
|---|---|---|
| Ordinary words | none | Searches the site |
| One hex colour, such as `#2f5eaa` | **Colour** | Shows the colour's values in the preview |
| Two hex colours, such as `#ffffff #2f5eaa` | **Contrast pair** | Judges the pair against WCAG in the preview |
| `>` followed by anything | **Command** | Lists commands (see [Commands](commands.md)) |
| A field filter such as `title:gamut` | **title:gamut** | Searches only that field |

## Read a colour

1. Open Spotlight and type a colour as `#` and six hex digits, for example `#2f5eaa`, with nothing else.
2. The chip reads **Colour**. The preview pane shows:
   - a swatch of the colour with its OKLCH value;
   - **Hex**, **RGB**, **On black** and **On white** (the WCAG contrast ratio of the colour against black and against white);
   - a link, **Check it against a background**, which opens the Contrast Checker with this colour.
3. The list shows **Pages that mention it** (up to three pages whose text contains that hex code), or the note "Nothing in the index mentions this colour by name — the answer is on the right."

## Check a colour pair

1. Type two hex colours, for example `#ffffff #2f5eaa`. The first is treated as the text colour and the second as the background.
2. The chip reads **Contrast pair**. The preview pane shows:
   - two swatches with "Aa" drawn in each colour on the other;
   - the contrast ratio;
   - three verdicts: **AA body** (pass or fail at 4.5), **AAA body** (7.0) and **AA large** (3.0);
   - **Open in the checker**, which opens the Contrast Checker with both colours.

Only six-digit hex codes with a `#` are recognised. Three-digit codes, colour names and other formats are searched as text.

## Field filters

Start the query with a field name and a colon to search one part of each page:

| Filter | Searches |
|---|---|
| `title:` | Page titles |
| `desc:` | Page descriptions |
| `tag:` | Page tags |
| `path:` | Page addresses, for example `path:/tool/` |
| `type:` | The kind of content |
| `category:` | The page category |

Put a phrase in quotes after the colon to match it exactly, for example `title:"colour vision"`. The chip shows the filter you used.

## Phrases and exclusions

- Put words in double quotes to require that exact phrase: `"contrast ratio"`.
- Put a minus sign before a word to leave out pages that contain it: `palette -gradient`.

These work in the full search page too.
