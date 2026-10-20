---
title: Auric Accessibility — The Project Issues view
description: Browse, group, search and act on every finding from the last scan in the Project Issues tree view.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# The Project Issues view

**Project Issues** is a tree view in the **Auric Accessibility** sidebar. It lists every finding from the last scan (or the live re-grade), so you can work through a project without opening files one by one.

## Before a scan

The view shows two rows: **Run a project scan** (*WCAG, contrast, CVD*) and **Open Auric Artisan Studio**. Select either.

## The title bar

| Button | Command |
| --- | --- |
| Search | **Search Accessibility Issues**: filter the tree |
| Tree | **Group Accessibility Issues (Type / File / Severity)** |
| Play | **Scan Project for Accessibility (Use Cache)** |
| Studio | **Open Accessibility Studio** |
| Collapse All | Collapses every group |
| **…** menu | **Generate Agent-Ready Remediation Plan** |

The Activity Bar icon shows a **badge** with the total number of issues (WCAG, contrast, colour-vision risk and code health), and the view's description reads, for example, `WCAG 2.2 · score 82`.

## The summary row

The first row reads **Project accessibility: 82/100 B** with the number of files scanned and a small score ring. Select it to open the Studio's Home. Hover it for a table of the score, audit profile, files scanned, WCAG issues, contrast failures, colour-vision risks, branding (when any), counts by level (A, AA, AAA) and by WCAG version, and links to **Open full scan report**, **Group by…** and **Search issues**.

## Group the tree

Run **Group Accessibility Issues** (or the tree button) and choose:

| Option | Groups |
| --- | --- |
| **By type** (default) | **WCAG issues**, **Contrast failures**, **CVD risk**, **Branding** (only when present, marked **excluded from score**), **Code health**, **Confusable colors** |
| **By file** | One group per file, busiest first, described as `N issues - worst serious`; rows sorted by line |
| **By severity** | **Critical**, **Serious**, **Moderate**, **Minor**, and **Branding (N) — excluded from score** |

Your choice is remembered. In type mode each group shows its count; groups list up to 500 rows (800 for code health). File groups show up to 200 rows, and severity groups up to 300.

## Rows

| Row type | Label | Description | Icon |
| --- | --- | --- | --- |
| WCAG | `1.1.1 Non-text Content` | `critical - src/index.html:12` | Impact icon: error, warning, info or circle |
| Contrast failure | `#999999 on #FFFFFF` | `2.85:1 - src/app.css:40` | A small sample of the pair |
| Colour-vision risk | `#hex on #hex` | Ratio `->` CVD ratio, and location | A sample of the pair |
| Code health | The message | Category and location | Category icon |
| Branding | `#D3AF37 on #FFFFFF` | Kind, ratio and location | A sample of the pair |
| Confusable colors | `#hex <-> #hex` | `DeltaE 24 -> 6 (deuteranopia)` | A sample of the pair |

Select a row to open the file at that line. Hover a row for the full issue card: the problem, priority, before-and-after and fix, as in the editor. Code-health rows show the category, message, evidence (redacted for secrets), location and fix.

### Row actions

| Button | Shown on | What it does |
| --- | --- | --- |
| **Open WCAG Documentation** | WCAG rows | Opens the W3C *Understanding* page for the criterion |
| **Open Issue in Contrast Studio** | Contrast and colour-vision rows | Opens the pair in the Contrast Studio, linked to its line |

These two commands are not in the Command Palette; use them from the row.

## Search

1. Run **Search Accessibility Issues** (or the search button).
2. Type any text: part of a message, a criterion number, an impact, a file path or a colour, for example `label`, `auth/settings`, `#777777` or `serious`.
3. The tree shows only matching rows, with counts such as `WCAG issues (3/40)`, and every group opens. A **Filtered by "label"** row appears at the top; select it (or run **Clear Accessibility Issue Search**) to clear the filter.

The search is a case-insensitive text match on each row's details.

## Related

- [Project scans](project-scans.md)
- [The Check space: Findings and Preview](check-space.md)
- [Reference](reference.md)
