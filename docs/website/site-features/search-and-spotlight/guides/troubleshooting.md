---
title: Search and Spotlight — Troubleshooting
description: Fixes for common problems with Spotlight search.
product: Website › Site features › Search and Spotlight
updated: 2026-09-25
---

# Troubleshooting Spotlight

## `Ctrl` + `K` opens my browser's address bar or search

**Why:** Spotlight loads a moment after the page. A shortcut pressed before that goes to the browser.

**What to do:** wait for the page to finish loading, or select **Search** in the header.

## The list says "Search engine is loading…"

**Why:** the first time you open Spotlight on a page, it builds its search index in the background.

**What to do:** wait a moment and keep typing; results appear once the index is ready. On a slow connection this takes longer.

## A page I know exists does not appear

**Possible causes and fixes:**

- A scope tab is hiding it. Select **All**, or **Show all N results** under **Try instead**.
- You typed only one character. Type at least two.
- Only 8 results are listed. Select **View all results for "…"** for the full list.
- A `-word` in your query excluded it, or a quoted phrase is too strict. Remove it.

## Web search says "Global search is unavailable right now"

**Why:** the Web tab needs a network connection and the site's web search service.

**What to do:** check your connection and try again later, or search the site with **All**.

## Typing a colour does not show a colour answer

**Why:** only six-digit hex codes with a `#`, and nothing else in the box, are read as a colour. `#fff`, `rebeccapurple` or `rgb(...)` are searched as text.

**What to do:** type the full six-digit form, for example `#ffffff`. For other formats, use the Contrast Checker or the colour tools.

## A command is missing

**Why:** commands appear only when the page has the control they drive.

**What to do:** go to a page that has it, or use the control directly, for example the header's theme button.

## Recent searches are gone

**Why:** they are kept in this browser and are lost if you clear site data, use a private window, or select **Clear**.
