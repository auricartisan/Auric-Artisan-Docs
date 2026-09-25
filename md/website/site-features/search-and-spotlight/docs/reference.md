---
title: Search and Spotlight — Reference
description: Every Spotlight control, key, launcher, command, query mode and message.
product: Website › Site features › Search and Spotlight
updated: 2026-09-25
---

# Spotlight reference

## Ways to open

| Method | Result |
|---|---|
| `Ctrl` + `K` / `Cmd` + `K` | Opens Spotlight, or closes it if open |
| Header **Search** button | Opens Spotlight |
| Drawer **Search tools, colours and pages** | Opens Spotlight |
| Right-click › **Site** › **Search the site** | Opens Spotlight |

## Controls

| Control | What it does |
|---|---|
| Search box | Type a query; results update as you type |
| Mode chip | Shows **Colour**, **Contrast pair**, **Command** or the field filter in use |
| `ESC` hint | Reminder that `Esc` clears, then closes |
| **Clear search** (X) | Empties the box and shows the launchers |
| Scope tabs | **All**, **Pages**, **Tools**, **Docs**, **Learn**, **Web** |
| Results list | Up to 8 results, commands, launchers or recent searches |
| Preview pane | Details of the highlighted result, or the colour answer |
| **Recent** › **Clear** | Deletes your recent searches |
| Footer count | Results and time, command count, or "colour" / "contrast pair" |
| Dimmed page | Click to close |

## Keys

| Keys | What they do |
|---|---|
| `Up` / `Down` | Move through the list |
| `Enter` | Open or run the highlighted row |
| `Ctrl` + `Enter` / `Cmd` + `Enter` | Open the highlighted result in a new tab |
| `Tab` / `Shift` + `Tab` | Next or previous scope tab |
| `Esc` | Clear the box; if already empty, close |

## Query modes

| Query | Mode | Minimum |
|---|---|---|
| Words | Search | 2 characters |
| `#rrggbb` alone | Colour | — |
| `#rrggbb #rrggbb` | Contrast pair (first = text, second = background) | — |
| `>…` | Command | — |
| `title:`, `desc:`, `tag:`, `path:`, `type:`, `category:` | Field filter | — |
| `"phrase"` | Exact phrase | — |
| `-word` | Exclude word | — |

## Colour answer fields

| Field | Meaning |
|---|---|
| Swatch and OKLCH | The colour and its OKLCH value |
| **Hex** | Hex code |
| **RGB** | RGB value |
| **On black** | WCAG contrast ratio against `#000000` |
| **On white** | WCAG contrast ratio against `#FFFFFF` |
| **Check it against a background** | Opens the Contrast Checker with this colour |

## Contrast pair fields

| Field | Meaning |
|---|---|
| Two "Aa" swatches | Each colour drawn on the other |
| Ratio | WCAG contrast ratio |
| **AA body** | Pass at 4.5:1 or more |
| **AAA body** | Pass at 7.0:1 or more |
| **AA large** | Pass at 3.0:1 or more |
| **Open in the checker** | Opens the Contrast Checker with both colours |

## Commands

| Command | Available when |
|---|---|
| **Toggle light and dark** | The page has the header theme button |
| **Open the page guide** | The page has the guide button |
| **Open the library** | The page has the library button |
| **Open settings** | The page has Settings |
| **Switch language** | The page has the language button |
| **Open the full search page** | Always |
| **Install the app** | Always |

## Launchers (empty box)

| Scope | Launchers and addresses |
|---|---|
| All | Full Search `/search/`, Collections `/collections/`, URL Analyzer `/tool/analyzer/`, Color Science Lab `/tool/color-science-lab/` |
| All (continued) | Documentation `/library/documentation/`, Learn Color `/library/learn/`, Vision Simulations `/tool/vision-simulation/` |
| All (continued) | Install the PWA `/download/`, Install Extension `/extension` |
| Pages | Home, Collections, About, Pricing, FAQ, Contact, Security |
| Tools | URL Analyzer, Color Science Lab, Vision Simulations, ASCII, Ishihara Plates, General Tools |
| Docs | Documentation Home, Changelog |
| Learn | Learn Color, Blog |

## Messages

| Message | When |
|---|---|
| Search engine is loading… | The index is still being prepared |
| No results for "…" (in Scope) | Nothing matched |
| Show all N results | Matches exist outside the chosen scope |
| Search the web for "…" | Offered when nothing matched on the site |
| Open full search page / View all results for "…" | Hands the query to the search page |
| Searching trusted sources… | A web search is running |
| Global search is unavailable right now | The web search service could not be reached |
| No trusted web results for "…" | The web search found nothing |
| Type at least 2 characters to search trusted sources across the web. | The Web tab with an empty box |
| No command matches that on this page. | Command mode found nothing |
| Nothing in the index mentions this colour by name — the answer is on the right. | Colour mode with no matching pages |
