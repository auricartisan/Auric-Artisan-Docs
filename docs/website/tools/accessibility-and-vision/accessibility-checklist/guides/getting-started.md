---
title: Accessibility Checklist — Getting started
description: Open the Accessibility Checklist, learn the screen, and mark your first check.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Getting started with the Accessibility Checklist

## Open it

Go to https://auricartisan.com/resources/accessibility-checklist/, or open the **Learn** menu in the site header and select **Accessibility Compliance**. No account is needed.

## The screen, top to bottom

### Masthead

The kicker "Auric Artisan · Accessibility", the title **The accessibility checklist**, and a line: "Fifty checks across the whole of WCAG 2.2, each one explained: what it means, who it affects, how to test it, and what the fix looks like in code."

A note under it says: "The analyzer decides 11 of these outright and narrows 23 more. The rest needs a person, which is what the explanations are for." Two links follow:

- **Run the automated pass first →** opens the [Analyzer](../../analyzer/README.md).
- **Wire it into CI →** opens the public API documentation.

### Tab rail and meter

Three tabs: **Checklist**, **Export** and **Reference**. With a tab focused, `Left` and `Right` move between tabs (wrapping round), and `Home` and `End` jump to the first or last.

Beside the tabs is the **meter**: "0 passed · 0 flagged · 50 left", a two-colour bar (passed and flagged), and "of 50". The meter always counts all 50 checks, whatever filter is on. When a filter is on, a small chip beside it names the filter and how many rows it shows, for example "REQUIRED · 35".

On wide screens the tab rail and meter stay pinned under the site header as you scroll.

### The Checklist tab: the Inspector

On screens at least 1080 pixels wide, the Checklist tab is two columns:

- **The index**, on the left: filter buttons, then nine numbered areas, each with a header showing how many of its checks you have decided (for example "0 / 6"), then one row per check. Each row shows a state symbol, the check title and its tag (for example "A 1.3.1" or "PRACTICE"). Required checks show their tag in gold.
- **The pane**, on the right: the selected check in full. It stays in view while the index scrolls.

The first check is selected when you arrive, unless the address names another one.

On narrower screens you see the index only. Tapping a row opens that check full-screen, with an **All checks** button to go back. See [Work through the checklist](work-through-the-checklist.md).

### What the pane shows

From top to bottom:

1. A bar with the check's position ("3 of 50") and **Previous check** and **Next check** buttons.
2. The area, for example "01 Semantics & structure".
3. The check title.
4. Chips: the criterion tag, **Required** for Level A and AA checks, and **AUTO**, **PARTLY** or **BY HAND** with a sentence saying how much the Analyzer can decide.
5. A one-sentence summary of the check.
6. The verdict buttons: **Pass**, **Fail**, **N/A** and **Attach screenshot**.
7. **Evidence**, once you have attached screenshots.
8. The explanation: **What it means**, **Who it affects**, **How to test it**, **What the fix looks like** (on most checks), **Usually breaks when**, and links such as "Understanding 1.3.1" to the W3C.

## Mark your first check

1. Make sure the first check, "Landmarks wrap every region of the page", is selected in the pane.
2. Open the page you are testing in another tab.
3. Follow **How to test it**. For this check, you run a short snippet in the browser console and look for exactly one `main` landmark and a label on every repeated `nav`.
4. Back in the checklist, select **Pass** if the page meets it, **Fail** if it does not, or **N/A** if it does not apply.
5. Look at the index row: its symbol changes, and the meter updates.
6. Select **Next check** (or press `J` with focus in the list or pane) to move on.

The result: your mark is saved in this browser straight away. Close the tab and come back later, and it is still there.

## Next steps

- [Work through the checklist](work-through-the-checklist.md) for filters, keys and the phone layout.
- [Attach evidence](attach-evidence.md) to back up a failure with an annotated screenshot.
- [Export your results](export-your-results.md) when you are done.
