---
title: Auric Artisan Studio — The Overview view
description: Every card, row and button in the Overview sidebar view, in its accessibility, colour and code-health layouts.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# The Overview view

The **Overview** is the first view in the Studio's Activity Bar container. It is a compact home that shows how the workspace is doing, what is wrong in the file you are editing, and what to do next. Its layout depends on which extension hosts it:

| Layout | Used when the host is | What it centres on |
| --- | --- | --- |
| Accessibility dashboard | Auric Accessibility (alone or in a Workstation) | The workspace score and one row per installed capability |
| Colour workbench | Auric Color (alone, or hosting Code Health) | The file you are editing, swatches and colour tools |
| Code-health report | Auric Code Health (alone) | The code-health score and its seven categories |

Every layout opens with the **Auric Studio** heading (a link to https://auricartisan.com) and an **Open the Studio** button at the top right, and ends with a footer that shows `Ctrl Alt .` **Command Center** (`⌘ ⌥ .` on macOS).

The Overview follows **one gold action per view**: the most useful action is drawn in gold, everything else in the theme's plain button style. When the open file has contrast pairs that can be fixed automatically, **Fix N in this file** is gold; otherwise the workspace card's main button is.

## The accessibility dashboard

### Workspace card

- **Workspace** heading with your workspace's name, and how long ago it was scanned, for example `scanned 3 days ago` or `not scanned yet`. The age refreshes every minute.
- **Score ring.** The overall score out of 100 and its grade, for example `82` and `grade B`. Before the first scan it reads `—` and `no scan`.
- **Accessibility** row: the overall score, its grade and the number of WCAG issues, or `Run a scan to grade` before the first scan.
- **Contrast issues** row: the number of text pairs below target, followed by colour-vision and branding counts when there are any.
- **Code health** row (only when Auric Code Health is installed): the code-health score and number of findings.
- **Scan project** button. After the first scan it reads **Rescan** and forces a fresh read of the workspace.
- **Report** (only with Auric Code Health): runs **Generate Project Health Report**.
- **SARIF** (only with Auric Code Health): runs **Write Health Record (health.json + SARIF)**.

All rows update as you type, from the live re-grade described in [Scanning](scanning.md). You do not need to press a button to see the effect of an edit.

### This file

The **This file** card shows the file in the active editor:

- Its workspace-relative name and a count, for example `3 issues`, or `clean`.
- Up to four findings, worst first. Contrast rows lead with the ratio, for example `2.32:1 #999999 on #FFFFFF`; other rows name their kind (`WCAG`, `APCA`, `code health`, `color vision`). Each row shows its line number; select a row to jump to that line.
- **Fix N in this file**: recolours every automatically fixable contrast pair in the file (needs Auric Color). It runs **Fix All Contrast Issues in File**, which previews the changes and asks first.
- **Contrast Studio**: opens the file's first failing pair in the [Contrast Studio](contrast-studio.md), linked to its location.

A file with no findings shows **No findings in this file.** When no editor is open, the card is hidden.

### Suggested

Up to three cards from the deterministic suggestion engine, each with a priority pill (**Critical**, **High**, **Workflow** or **Tip**), a title that states what was detected, a one-line reason, and one or two buttons. Select **✕** to dismiss a suggestion for good. The six rules are listed in [The Command Center](command-center.md#the-suggestion-rules). The strip is hidden when there is nothing to suggest.

### Recent colors

Shown when Auric Color is installed and you have applied at least one colour. It lists up to 12 recently applied colours; select a swatch to copy its value. **Picker** opens the colour picker.

### Navigation

| Button | What it opens |
| --- | --- |
| **Studio** | The Studio tab. |
| **Rulebook** | The rulebook and knowledge database search. |
| **Icon Studio** | The combined Auric icon library, if an icon provider is installed. |
| **Fix plan** | Generates the agent-ready remediation plan. |

The footer reads **Runs on this machine**.

## The colour workbench

Used when Auric Color is the host: on its own, or with Auric Code Health but without Auric Accessibility. It has no project score. (With that pair, open the Studio's **Health** space for the code-health score.)

- **This file** card, as above. **Fix N in this file** is the gold action when the file has fixable pairs.
- **Suggested**: only the file-level suggestion **N fixable contrast pairs in this file**, when it applies.
- **Brand palette**: a fixed row of nine swatches. Select one to copy it (**click to copy**).
- **Recent colors**: up to 12 recently applied colours, with a **Picker** link. Before you pick anything it says **Pick a color and it lands here.**
- **Open the color picker** (gold unless the file has fixable pairs): runs **Pick / edit color**.
- Navigation: **Contrast**, **Palette**, **Shades**, **Vision** (each opens that Studio tool), **Rulebook** and **Icon Studio**.
- Footer: **Hover a color literal to edit it in place**, or **Native decorator mode — VS Code's picker owns the hover** when you have switched to VS Code's own picker.

## The code-health report

Used by Auric Code Health on its own.

- Workspace card with a **Code health** ring and row. Before the first report the row reads **Run a health report to grade this repo**.
- Seven category chips with counts: **Secrets**, **Security**, **Risky APIs**, **Debug**, **TODOs**, **Conflicts** and **Large files**. Chips with a count of zero are shown in a muted style.
- **Report** (gold): runs **Generate Project Health Report**, which scans (or reuses a fresh cache) and writes the report.
- **health.json + SARIF**: runs **Write Health Record**.
- **This file** and **Suggested**, as above.
- Navigation: **Studio**, **Rulebook**, **Icon Studio** and **Fix plan**.

## Keyboard and screen readers

Every control is a real button. Score changes and new suggestions are announced through a polite live region, for example `Score 82 of 100, 42 findings`. See [Accessibility of the Studio](studio-accessibility.md).
