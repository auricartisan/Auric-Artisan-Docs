---
title: Browser extension — Findings
description: One list of everything the tools found — accessibility, contrast and inspection problems — ordered by severity, with actions for each.
product: Browser extension › Check
updated: 2026-09-25
---

# Findings

Findings (All Findings) pools the problems the extension found in this session into one list, most serious first. It fills from three sources:

| Source | Label | What it adds |
|---|---|---|
| The accessibility audit | `a11y` | Every rule failure and warning from the last audit |
| The contrast scan | `color` | Every failing or borderline piece of text from the last audit |
| The element inspector | `inspect` | The inspected element's text contrast, when it fails |

Until you run an audit, the list reads "No findings yet. Run a page audit to fill this in."

## Read the list

Three counts sit at the top: **Failing**, **Warnings** and **Total**. The Findings chip in the Check space shows the number of open failures and warnings.

Findings are ordered with failures before warnings, then by impact: critical, serious, moderate and minor. Each finding shows:

- its source label;
- its title, such as "Form field has no label" or "Contrast 3.12:1";
- a message naming the element and the problem, such as `"Sign up" needs 4.5:1`;
- the element's CSS selector;
- action buttons.

## Actions

| Button | Appears on | What it does |
|---|---|---|
| **Show on page** | All | Outlines the page's contrast problems for 15 seconds (for an inspected element, highlights that element) |
| **Copy selector** | All | Copies the element's CSS selector |
| **Inspect** | Accessibility findings | Opens Code › Inspect |
| **Check contrast** | Contrast and inspection findings | Loads the colour pair into Contrast |

## Keeping findings

Findings live only while the popup or side panel stays open. Closing the popup clears them. To keep a record, use **Export JSON** in [Audit](audit.md) before you close it.

## Related pages

- [Audit](audit.md)
- [Audit rules](audit-rules.md)
- [Element inspector](../surfaces/inspector.md)
