---
title: Changelog — Getting started
description: Use the changelog page to find a release, search every change, filter by type and by what was touched, and link to a release.
product: Website › Library › Changelog
updated: 2026-09-25
---

# Getting started

## The page

Open https://auricartisan.com/library/changelog/.

- **Changelog**, with the line "Every release, what was in it, and what it touched. The search reads the changes themselves, not just the headings — so 'when did overage arrive?' is a question this page can answer."
- A facts line: **11 releases · v0.9.0 → v0.9.11 · 12 August 2026 — the latest**.
- A search box, **Search every change — overage, recorder, dark mode…**, with a clear button.
- Type buttons: **All**, **Releases**, **Patches**.
- A count, for example **11 of 11 releases**, and **Expand all**.
- The timeline: one entry per release, newest first. The newest is open when the page loads.

## A release entry

The header shows the version (for example **v0.9.10**), a type badge (**release**, **patch**, or another label such as **Changelog**) and the date. Under it, a summary sentence — shortened while the entry is closed, in full when it is open.

Select the header to open or close the entry. Open, it shows:

| Part | What it contains |
| --- | --- |
| **What changed** | The list of changes. |
| Notes | Extra notes, where the release has them. |
| **Touched** | Tags for the parts of the platform the release touched, such as `analyzer` or `pricing`. |
| **Read the full release note** | A link to the release's own page. |

## Search

1. Type a word or phrase. The timeline keeps only releases whose title, summary, changes or notes contain it.
2. Matches are marked where they appear.
3. Select the × in the box to clear the search.

## Filter by type

- **Releases** — feature releases.
- **Patches** — fix and clean-up releases.
- **All** — everything.

## Filter by what was touched

In an open release, select a tag under **Touched**. The timeline shows only releases that touched the same part, and a button appears beside the count, **touching** and the tag's name. Select that button, or the tag again, to stop filtering.

**Clear filters** appears whenever a search, type or tag is active; it resets all three. If nothing matches, the page says **No release matches that.** with its own **Clear filters** button.

## Open everything

**Expand all** opens every release currently shown; it then reads **Collapse all**.

## Link to a release

Add `#` and the version to the page's address, for example https://auricartisan.com/library/changelog/#0.9.11 (a leading `v` also works). The page opens that release and scrolls to it.

## Follow releases

Add https://auricartisan.com/library/changelog/rss.xml to your news reader.

If the page cannot load the timeline, it says **The changelog could not be loaded.** with a link, **Read it as a feed instead**, and a plain list of **All releases** still links to every release note.
