---
title: Auric Artisan Studio — Getting started
description: Install the Studio, run your first project scan, and learn where every view, hover and status-bar item lives.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Getting started

This guide installs Auric Artisan Studio, runs a first scan and tours every place the Studio shows information. It assumes the Full Pack, which installs Auric Color, Auric Accessibility and Auric Code Health together. If you install only one extension, the same screens appear with only that extension's parts; the differences are listed in [Choose what to install](choosing-an-install.md).

## Before you start

- You need Visual Studio Code 1.74 or newer.
- Open a folder or a multi-root workspace. Several features (the scan cache, reports, the remediation plan and the knowledge database) write to a `.auric-artisan` folder inside your workspace, so they need a folder to be open.
- No account, sign-in, API key or network connection is needed. Everything runs on your machine.

## Install

1. Open the Extensions view with `Ctrl` + `Shift` + `X`.
2. Search for `auric-artisan.auric-artisan` (the Full Pack) and select **Install**. VS Code installs the pack and its three members: Auric Color, Auric Accessibility and Auric Code Health.
3. Alternatively, run this in a terminal:

```text
code --install-extension auric-artisan.auric-artisan
```

The extensions start automatically once VS Code has finished loading. There is nothing to configure before the first use.

## Your first scan

1. Open a project folder that contains stylesheets, templates or components.
2. Select the Auric icon in the Activity Bar. When all three extensions are installed, the sidebar is titled **Auric Accessibility** and shows three views: **Overview**, **Project Issues** and a collapsed **Color Picker**.
3. In the **Overview**, select **Scan project**. A notification titled **Auric Artisan: scanning project...** shows progress and has a **Cancel** button.
4. When the scan finishes, a message reports the result, for example `Accessibility 82/100 (B) — 12 contrast + 30 WCAG issue(s) across 214 files (scanned).` It offers **Open Studio**, **Show Issues** and **Force Rescan**.
5. The Overview's score ring now shows the overall score and grade, and the rows beside it show the accessibility, contrast and code-health results.

The scan result is saved in `.auric-artisan/scan-cache.json`. Next time you open the workspace, the Studio loads it instead of reading every file again, as long as it is less than 24 hours old (you can change this; see [Scanning](scanning.md)).

## A tour of the screens

### The Activity Bar views

| View | What it shows |
| --- | --- |
| **Overview** | The Studio's home in the sidebar: the workspace score, the file you are editing, up to three suggestions, recent colours and buttons for the Studio, the Rulebook, the Icon Studio and the fix plan. See [The Overview view](overview-view.md). |
| **Project Issues** | Every finding from the last scan as a tree, grouped by type, file or severity, with search. Provided by Auric Accessibility. See [The Project Issues view](../accessibility/docs/project-issues-view.md). |
| **Color Picker** | A docked colour picker, collapsed by default. Provided by Auric Color. See [The colour pickers](../color/docs/color-picker.md). |

### The status bar

Two items appear at the right of the status bar:

- **The score item**, for example `A11y 82 B`. A database icon after it means the score came from the saved scan cache. Its background turns to the theme's warning colour below 90 and to the error colour below 70. Hover it for the pass rate of contrast pairs, the data source and a warning if a file limit cut the scan short. Select it to open the Studio.
- **Auric: N in this file** appears only when the active file has contrast or accessibility findings. Hover it for the breakdown; select it to open the Project Issues view (or, without Auric Accessibility, the Contrast Studio).

When Auric Code Health is installed on its own, the score item reads `Health` instead of `A11y` and shows the code-health score.

### In the editor

- **Underlines.** Auric findings are marked with a violet wavy underline and a mark in the overview ruler at the right edge of the editor. They also appear in the **Problems** panel with the source `auric-artisan`.
- **Issue hovers.** Hover an underlined finding for a card that leads with what is wrong and how urgent it is, then shows the evidence, a before-and-after of the fix, and actions such as **Apply fix**, **Go to code**, **WCAG docs**, **Ignore here** and **Copy reference**.
- **Colour hovers.** Hover any colour literal, such as `#1d4ed8` or `oklch(0.6 0.15 250)`, for its values, contrast on white and black, a colour-vision preview and an inline picker. See [Hover and swatches](../color/docs/hover-and-swatches.md).
- **Inspect.** Hover an element or CSS rule (when you are not over a colour or a finding) for its accessible name and role, the colours that apply and a before-and-after preview. See [Inspect](../accessibility/docs/inspect.md).
- **Quick fixes.** Put the cursor on an underline and press `Ctrl` + `.` to see fixes such as **Fix contrast → #767676 (4.54:1)** or **Ignore this WCAG 1.1.1 finding here**.
- **Swatches.** A small coloured square appears before every colour literal. Clicking a literal opens the inline picker.

### The Studio

Select **Studio** in the Overview, or the status-bar score, to open the Studio in an editor tab titled **Auric Artisan — Workstation Studio**. A rail on the left lists its spaces:

| Space | Tools inside |
| --- | --- |
| **Home** | The workspace score, files to fix first, graphs, suggestions, the CI gate command and the project palette. |
| **Color** | **Palette**, **Shades** and **Vision**. |
| **Check** | **Findings**, **Contrast** (the Contrast Studio) and **Preview**. |
| **Health** | The code-health score, categories and findings. |
| **Brand** | A brand accessibility audit on real text. |
| **Settings** | Appearance and the settings for installed capabilities. |

The **Rulebook** and **Icons** buttons at the foot of the rail open the knowledge database and the Icon Studio. See [The Studio](studio.md).

### The Command Center

Press `Ctrl` + `Alt` + `.` (`Cmd` + `Alt` + `.` on macOS) anywhere to open **Auric Artisan — Command Center**, a searchable list with **Suggested**, **Actions**, **Recent colors**, **Findings** and **Artifacts** sections. See [The Command Center](command-center.md).

## Your first fix

1. Open a stylesheet with a violet underline under a colour value.
2. Hover the underline. The card leads with the verdict, for example `2.32 : 1 — fails WCAG AA for normal text`, and shows the nearest passing colour of the same hue.
3. Select the gold **Apply fix** button. The value is replaced in one edit you can undo with `Ctrl` + `Z`.
4. If the colour comes from a CSS custom property defined in the same file, the button reads **Apply to --token-name** instead and changes the definition, so every use follows.

The underline disappears and the status-bar count drops. To fix every failing pair in the file at once, run **Auric Artisan: Fix All Contrast Issues in File**; it shows a preview of every change and asks before applying.

## Where to go next

- [The Overview view](overview-view.md) and [The Studio](studio.md) for the full screen reference.
- [Scanning](scanning.md) to control what is scanned and when.
- [Auric Color](../color/README.md), [Auric Accessibility](../accessibility/README.md) and [Auric Code Health](../code-health/README.md) for each extension's features.
- [Exports and health records](exports-and-records.md) and [The CI gate](ci-gate.md) to share results and gate pull requests.
