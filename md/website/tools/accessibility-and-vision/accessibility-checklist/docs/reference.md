---
title: Accessibility Checklist — Reference
description: Every control, label, message and stored item of the Accessibility Checklist.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Accessibility Checklist reference

## Page

| Item | Detail |
| --- | --- |
| Address | https://auricartisan.com/resources/accessibility-checklist/ |
| Old addresses | `/accessibility-compliance/` and `/compliance` forward here |
| Menu entry | **Learn** › **Accessibility Compliance** ("WCAG checks & guidance") |
| Deep link to a check | `#check-` plus the ID, for example `#check-k2` |
| Masthead links | **Run the automated pass first →** (Analyzer), **Wire it into CI →** (API documentation) |

## Tabs and meter

| Control | What it does |
| --- | --- |
| **Checklist** | The Inspector: index and pane |
| **Export** | Counts, a preview of the Markdown, and the three export actions |
| **Reference** | WCAG levels and the law in 15 jurisdictions |
| Meter | "N passed · N flagged · N left … of 50", with a two-part bar. Always counts all 50. |
| Scope chip | Shown when a filter is on: the filter's name and how many rows are visible |

## Index

| Control | What it does |
| --- | --- |
| **All 50** | Show every check (default) |
| **Required** | Show Level A and AA checks (35) |
| **AAA** | Show Level AAA checks (2) |
| **Practice** | Show good-practice checks (13) |
| **Open only** | Hide checks marked Passed; combines with the filters above |
| Area header | Fold or unfold the area; shows decided out of total |
| Row | Select the check; shows state, title and tag |

## Pane

| Control | What it does |
| --- | --- |
| **All checks** | Back to the list (phone layout only) |
| Position | "N of 50", the check's place in the full list |
| **Previous check** / **Next check** | Move through the visible checks (`K` / `J`) |
| Chips | Criterion tag, **Required**, and **AUTO**, **PARTLY** or **BY HAND** |
| **Pass** | Mark as passed (`Space`); select again to clear |
| **Fail** | Mark as flagged (`F`); select again to clear |
| **N/A** | Mark as not applicable (`N`); select again to clear |
| **Attach screenshot** | Open the screenshot evidence dialog |
| **Evidence** | Thumbnails of attached screenshots, and an **Add** tile |
| Explanation | What it means, who it affects, how to test it, what the fix looks like, what usually breaks it, links |

## Screenshot evidence dialog

| Control | What it does | Default |
| --- | --- | --- |
| **Choose a file** | Pick one or more images | — |
| Drop or paste | Drop image files, or paste with `Ctrl` + `V` | — |
| Pen, Highlighter, Arrow, Box, Redact, Callout | Drawing tools (`P`, `H`, `A`, `B`, `R`, `C`) | Arrow |
| Colour | Red, Blue, Green, Black | Red |
| Line width | Fine, Medium, Broad | Medium |
| **Marks** list | Every mark on this screenshot, with a remove button each | — |
| Thumbnail strip | Switch screenshot, or add another | — |
| **Undo** | Remove the last mark | — |
| **Clear marks** | Remove every mark on this screenshot, without asking | — |
| **Remove** | Delete this screenshot; confirm with **Remove this one?** within four seconds | — |
| **Done** | Close the dialog (`Esc` does the same) | — |

## Export tab

| Control | What it does |
| --- | --- |
| **Export the report** | Opens the browser's print dialog with flagged and untouched checks |
| **Copy as Markdown** | Copies a Markdown report of all 50 checks to the clipboard |
| **Reset** | Clears every mark and screenshot at once, without asking |

## Messages

| Message | When |
| --- | --- |
| "Nothing matches these filters." | No check matches the active filters |
| "N screenshot(s) attached." | Screenshots were added |
| "Screenshot removed." | A screenshot was deleted |
| "Printing N finding(s)." | **Export the report** with flagged checks |
| "Nothing is flagged — printing the list as it stands." | **Export the report** with nothing flagged |
| "The findings are on your clipboard, as Markdown." | **Copy as Markdown** worked |
| "Could not reach the clipboard — the browser refused it." | **Copy as Markdown** failed |
| "Cleared — marks and screenshots." | After **Reset** |

## Stored in this browser

| Item | Kept |
| --- | --- |
| Your marks (Pass, Fail, N/A) for each check | Yes |
| Screenshots, their marks, and the marked-up copies | Yes |
| Filters, folded areas, the selected check | No (a `#check-` address selects a check) |
| Notes or reasons | Not available |

Nothing is sent to a server. See [Privacy](../others/privacy.md).

## Layout

| Width | Layout |
| --- | --- |
| 1080 px and wider | Index and pane side by side; the pane stays in view; the tab rail and meter stay under the header |
| Under 1080 px | Index only; a row opens the one-check view |
| 620 px and narrower | Key hints on the verdict buttons are hidden; **Attach screenshot** becomes an icon button |

Without JavaScript, the page shows the plain list of all 50 checks with their explanations, and no filters, meter or marking.
