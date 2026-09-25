---
title: Auric Artisan Studio — Reference
description: Every command, keybinding, view, menu entry, setting, theme colour and workspace file contributed by the four Studio extensions, in one place.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Reference

This page lists everything the Studio extensions add to VS Code, across all four extensions. Each extension's own reference page describes its commands and settings in more detail:

- [Auric Color reference](../color/docs/reference.md)
- [Auric Accessibility reference](../accessibility/docs/reference.md)
- [Auric Code Health reference](../code-health/docs/reference.md)
- [Full Pack reference](../full-pack/docs/reference.md)

The facts on this page are for version 0.1.0.

## Extensions

| Display name | ID | Settings prefix | Categories |
| --- | --- | --- | --- |
| Auric Color — Picker, Palettes & Contrast | `auric-artisan.auric-color` | `auricColor.` | Visualization, Programming Languages, Other |
| Auric Accessibility — WCAG 2.2 Linter | `auric-artisan.auric-a11y` | `auricA11y.` | Linters, Programming Languages, Other |
| Auric Code Health — Secrets, TODOs & Risk | `auric-artisan.auric-codehealth` | `auricCodeHealth.` | Linters, Other |
| Auric Artisan Studio — Full Pack | `auric-artisan.auric-artisan` | none | Extension Packs, Linters, Visualization, Other |

All need VS Code 1.74 or newer. The three code extensions start when VS Code finishes loading.

## Keybindings

| Keys (Windows, Linux) | Keys (macOS) | Command | Extensions | Active when |
| --- | --- | --- | --- | --- |
| `Ctrl` + `Alt` + `.` | `Cmd` + `Alt` + `.` | Workstation: Command Center | All three | The extension is not suppressed by a Workstation host |
| `Ctrl` + `Alt` + `C` | `Cmd` + `Alt` + `C` | Pick / edit color | Auric Color | The editor has focus |
| `Ctrl` + `Alt` + `A` | `Cmd` + `Alt` + `A` | Inspect Accessibility of Element | Auric Accessibility | The editor has focus |

To rebind them, open **File › Preferences › Keyboard Shortcuts** and search for the command title.

## Commands

Every command appears in the Command Palette under the **Auric Artisan** category, so its full palette title starts with `Auric Artisan:`. The command ID's prefix depends on the extension: `auricColor.`, `auricA11y.` or `auricCodeHealth.`.

| Palette title (after `Auric Artisan:`) | ID suffix | Color | A11y | Code Health |
| --- | --- | --- | --- | --- |
| Workstation: Command Center | `commandCenter` | yes | yes | yes |
| Open Color Studio | `openStudio` | yes | | |
| Open Accessibility Studio | `openStudio` | | yes | |
| Open Code Health Studio | `openStudio` | | | yes |
| Open Rulebook & Knowledge Database | `openKnowledgeBase` | yes | yes | yes |
| Build Workspace Knowledge Database (JSON + Markdown) | `writeKnowledgeDatabase` | yes | yes | yes |
| Open Unified Icon Studio | `openIconStudio` | yes | yes | yes |
| Pick / edit color | `pickColor` | yes | | |
| Generate Accessible Palette | `generatePalette` | yes | | |
| Check Contrast of Selection | `checkContrast` | yes | yes | |
| Fix All Contrast Issues in File | `fixAllContrast` | yes | | |
| Choose Color Picker Mode | `chooseColorPickerMode` | yes | | |
| Disable native color picker (use Auric Artisan) | `disableNativeColorPicker` | yes | | |
| Restore native color picker (use VS Code's) | `restoreNativeColorPicker` | yes | | |
| Refresh Contrast Diagnostics | `refreshDiagnostics` | yes | | |
| Change Accent Color (Theme the Studio) | `chooseAccent` | yes | | |
| Mark Line as Intentional Branding (Toggle) | `markBranding` | yes | yes | |
| Inspect Accessibility of Element | `inspectAccessibility` | | yes | |
| Scan Project for Accessibility (Use Cache) | `scanProject` | | yes | |
| Force Rescan Project and Refresh Cache | `rescanProject` | | yes | |
| Generate Agent-Ready Remediation Plan | `generateAiPlan` | | yes | yes |
| Clear Workspace Scan Cache | `clearScanCache` | | yes | yes |
| Search Accessibility Issues | `searchIssues` | | yes | |
| Group Accessibility Issues (Type / File / Severity) | `groupIssues` | | yes | |
| Clear Accessibility Issue Search | `clearIssueSearch` | | yes | |
| Open WCAG Documentation | `openIssueDocs` | | row action only | |
| Open Issue in Contrast Studio | `openIssueInStudio` | | row action only | |
| Generate Project Health Report (Color, A11y & Code Health) | `projectHealthReport` | | | yes |
| Write Health Record (health.json + SARIF) | `writeHealthReport` | | | yes |
| Open Workspace Data Folder | `openDataFolder` | | | yes |

Auric Color contributes 15 commands, Auric Accessibility 17 and Auric Code Health 10. **Open WCAG Documentation** and **Open Issue in Contrast Studio** are hidden from the Command Palette; they appear as buttons on rows of the Project Issues view.

What each command does:

| Command | What it does |
| --- | --- |
| Workstation: Command Center | Opens the Command Center list. See [The Command Center](command-center.md). |
| Open … Studio | Opens the Studio tab, or the Workstation host's Studio. See [The Studio](studio.md). |
| Open Rulebook & Knowledge Database | Searches the local knowledge database. |
| Build Workspace Knowledge Database (JSON + Markdown) | Writes `knowledge.json`, `rulebook.md` and an overrides template. |
| Open Unified Icon Studio | Opens the combined Auric icon library. |
| Pick / edit color | Opens the colour picker on the colour under the cursor, or inserts a new colour. |
| Generate Accessible Palette | Opens Studio › Color › Palette seeded with the selected colour. |
| Check Contrast of Selection | Opens the Contrast Studio with the selected colour as the text colour. |
| Fix All Contrast Issues in File | Previews and applies a fix for every failing pair in the file, as one undoable edit. |
| Choose Color Picker Mode | Chooses between the Auric picker and VS Code's native picker. |
| Disable native color picker (use Auric Artisan) | Switches to the Auric picker and turns VS Code's colour decorators off. |
| Restore native color picker (use VS Code's) | Hands colour picking back to VS Code's native picker. |
| Refresh Contrast Diagnostics | Re-checks every open file. |
| Change Accent Color (Theme the Studio) | Picks the Studio's accent colour. |
| Mark Line as Intentional Branding (Toggle) | Adds or removes an `auric-brand-line` comment on the current lines. |
| Inspect Accessibility of Element | Shows the Inspect card for the element or CSS rule at the cursor. |
| Scan Project for Accessibility (Use Cache) | Scans the workspace, reusing a fresh cache. |
| Force Rescan Project and Refresh Cache | Scans the workspace from disk and rewrites the cache. |
| Generate Agent-Ready Remediation Plan | Writes the local, deterministic remediation plan. |
| Clear Workspace Scan Cache | Deletes `scan-cache.json`. |
| Search Accessibility Issues | Filters the Project Issues view by text. |
| Group Accessibility Issues (Type / File / Severity) | Changes how the Project Issues view is grouped. |
| Clear Accessibility Issue Search | Removes the Project Issues filter. |
| Open WCAG Documentation | Opens the W3C Understanding page for a finding's success criterion. |
| Open Issue in Contrast Studio | Opens a contrast or colour-vision finding in the Contrast Studio, linked to its line. |
| Generate Project Health Report (Color, A11y & Code Health) | Writes the Markdown, JSON and HTML project health report. |
| Write Health Record (health.json + SARIF) | Writes `health.json`, SARIF and history. |
| Open Workspace Data Folder | Shows the `.auric-artisan` folder in your file manager. |

## Views

| View | View ID | Extension | Notes |
| --- | --- | --- | --- |
| Overview | `auricColorHome` | Auric Color | Activity Bar container **Auric Color** |
| Color Picker | `auricColorPickerView` | Auric Color | Collapsed by default |
| Overview | `auricA11yHome` | Auric Accessibility | Activity Bar container **Auric Accessibility** |
| Project Issues | `auricA11yIssues` | Auric Accessibility | Tree view with a badge count |
| Color Picker | `auricA11yPickerView` | Auric Accessibility | Shown only when Auric Color is installed; collapsed by default |
| Overview | `auricCodeHealthHome` | Auric Code Health | Activity Bar container **Auric Code Health** |

Views of a suppressed extension are hidden while another extension hosts the Workstation. VS Code also creates a focus command for each view, for example `auricA11yIssues.focus`, which you can bind to a key.

## Menus

### Editor right-click menu

| Entry | Extension | Shown when |
| --- | --- | --- |
| Inspect Accessibility of Element | Auric Accessibility | HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JS, TS, JSX, TSX and CSS-family files |
| Pick / edit color | Auric Color | Always |
| Generate Accessible Palette | Auric Color | Text is selected |
| Check Contrast of Selection | Auric Color, Auric Accessibility | Text is selected |
| Choose Color Picker Mode | Auric Color | Always |
| Mark Line as Intentional Branding (Toggle) | Auric Color, Auric Accessibility | The Inspect languages above, plus Markdown |

### Project Issues view title bar

**Search Accessibility Issues**, **Group Accessibility Issues**, **Scan Project for Accessibility**, **Open Accessibility Studio** and **Collapse All**, with **Generate Agent-Ready Remediation Plan** in the **…** menu.

### Project Issues rows

**Open WCAG Documentation** on WCAG rows; **Open Issue in Contrast Studio** on contrast and colour-vision rows.

## Settings

The table lists each setting's key after its prefix, and which extensions declare it. Give the full key in `settings.json`, for example `auricA11y.contrast.threshold`.

| Key | Type | Default | Color | A11y | Code Health |
| --- | --- | --- | --- | --- | --- |
| `appearance.accent` | string | `gold` | yes | yes | yes |
| `hover.enabled` | boolean | `true` | yes | | |
| `colorPicker.mode` | `auric` or `decorators` | `auric` | yes | | |
| `colorPicker.nativeHoverPicker` | boolean | `false` | yes | | |
| `colorPicker.swatches` | boolean | `true` | yes | | |
| `colorPicker.clickAction` | `inlinePicker`, `fullEditor`, `off` | `inlinePicker` | yes | | |
| `colorPicker.autoOpen` | boolean | `false` | yes | | |
| `colorPicker.inlineSwatches` | boolean | `false` | yes | | |
| `inspect.enabled` | boolean | `true` | | yes | |
| `inspect.onHover` | boolean | `true` | | yes | |
| `contrast.enabled` | boolean | `true` | yes | yes | |
| `contrast.standard` | `wcag2`, `apca`, `both` | `wcag2` | yes | yes | |
| `contrast.threshold` | number, 1–21 | `4.5` | yes | yes | |
| `contrast.apcaThreshold` | number, 15–106 | `60` | yes | yes | |
| `contrast.severity` | `error`, `warning`, `information`, `hint` | `warning` | yes | yes | |
| `contrast.flagCvdRisk` | boolean | `true` | yes | yes | |
| `contrast.checkPageBackground` | boolean | `true` | yes | yes | |
| `branding.enabled` | boolean | `true` | yes | yes | |
| `a11y.enabled` | boolean | `true` | | yes | |
| `a11y.profile` | `2.0`, `2.1`, `2.2`, `3.0-draft` | `2.2` | | yes | |
| `codeHealth.enabled` | boolean | `true` | | | yes |
| `codeHealth.diagnostics` | boolean | `true` | | | yes |
| `codeHealth.todo` | boolean | `true` | | | yes |
| `codeHealth.debug` | boolean | `true` | | | yes |
| `codeHealth.secret` | boolean | `true` | | | yes |
| `codeHealth.conflict` | boolean | `true` | | | yes |
| `codeHealth.risk` | boolean | `true` | | | yes |
| `codeHealth.security` | boolean | `true` | | | yes |
| `codeHealth.customSecretPatterns` | array of strings | `[]` | | | yes |
| `codeHealth.size` | boolean | `true` | | | yes |
| `health.enabled` | boolean | `true` | | | yes |
| `health.writeOnScan` | boolean | `true` | | | yes |
| `health.formats` | array of `json`, `sarif`, `history` | all three | | | yes |
| `health.fileName` | string | `health.json` | | | yes |
| `health.maxIssues` | number, 100–100000 | `5000` | | | yes |
| `health.historyLimit` | number, 10–5000 | `200` | | | yes |
| `data.enabled` | boolean | `true` | | yes | yes |
| `data.folderName` | string | `.auric-artisan` | | yes | yes |
| `scan.cache.enabled` | boolean | `true` | | yes | yes |
| `scan.cache.maxAgeMinutes` | number, 0 or more | `1440` | | yes | yes |
| `scan.live` | boolean | `true` | | yes | yes |
| `scan.liveDelayMs` | number, 200–5000 | `700` | | yes | yes |
| `scan.autoScan` | boolean | `false` | | yes | yes |
| `scan.autoScanOnStartup` | boolean | `false` | | yes | yes |
| `scan.autoScanDelayMs` | number, 250–60000 | `1800` | | yes | yes |
| `scan.maxFiles` | number | `4000` | | yes | yes |
| `scan.exclude` | glob string | see below | | yes | yes |

The default of `scan.exclude` is `**/{node_modules,dist,build,out,.git,vendor,coverage,.auric-artisan}/**`. The default of `health.formats` is `["json","sarif","history"]`.

Auric Color declares 16 settings, Auric Accessibility 24 and Auric Code Health 28.

### Shared settings

The installed extensions share one `.auric-artisan` folder, so settings that shape it must mean the same thing to every extension. For these keys, each extension reads the first value it finds set (in any scope: user, workspace or folder), looking first under `auricCodeHealth.`, then `auricA11y.`, then `auricColor.`:

- `data.enabled`, `data.folderName`
- `scan.cache.enabled`, `scan.cache.maxAgeMinutes`, `scan.autoScan`, `scan.autoScanOnStartup`, `scan.autoScanDelayMs`, `scan.maxFiles`, `scan.exclude`, `scan.live`
- every `codeHealth.` key
- `health.formats`, `health.fileName`, `health.historyLimit`, `health.writeOnScan`

The simplest approach is to set each of these once, under one prefix. The Studio's **Settings** space writes a shared key to wherever its current value is set, so its edits always take effect.

The other settings are read by the extension that owns the feature: colour picker and hover settings by Auric Color; Inspect and profile settings by Auric Accessibility; contrast settings by Auric Accessibility when it is installed, otherwise by Auric Color; and the accent by the extension that hosts the Studio.

In a multi-root workspace, scan and data settings can be set per workspace folder; the accent is always stored in your user settings.

## Theme colours

Both Auric Color and Auric Accessibility contribute four colours for the Branding group. Override them in `workbench.colorCustomizations`, for example `"auricA11y.branding.icon": "#FF4FA0"`.

| Colour ID suffix | Used for | Dark | Light | High contrast | High contrast light |
| --- | --- | --- | --- | --- | --- |
| `branding.foreground` | Foreground of Branding findings | `#F06595` | `#C2255C` | `#FF80AB` | `#A61E4D` |
| `branding.background` | Soft wash behind Branding rows and badges | `#F0659522` | `#C2255C1A` | transparent | transparent |
| `branding.border` | Border or underline for Branding findings | `#F0659580` | `#C2255C80` | `#FF80AB` | `#A61E4D` |
| `branding.icon` | Icon tint of the Branding group in the Issues view | `#F06595` | `#C2255C` | `#FF80AB` | `#A61E4D` |

The full IDs are `auricColor.branding.foreground` and so on, and `auricA11y.branding.foreground` and so on.

## Status-bar items

| Item | Shown | Select to |
| --- | --- | --- |
| Score, for example `A11y 82 B` (or `Health 90 A` for Auric Code Health alone) | Always, by one extension | Open the Studio |
| **Auric: N in this file** | When the active file has contrast or accessibility findings | Open the Project Issues view, or the Contrast Studio without Auric Accessibility |

## Diagnostics

All findings in the Problems panel have the source `auric-artisan`.

| Finding | Problems severity | Code shown |
| --- | --- | --- |
| Low contrast | `contrast.severity` (warning by default); information when the background was assumed | `low-contrast` |
| Low APCA contrast | Same as low contrast | `apca-low` |
| Colour-vision risk | Hint | `cvd-risk` |
| Branding | Information | `branding:contrast`, `branding:apca` or `branding:cvd` |
| WCAG, critical or serious | Warning | `WCAG 1.1.1` (linked to the Understanding page) |
| WCAG, moderate | Information | Same |
| WCAG, minor, and best-practice hints | Hint | Same |
| Code health | By category: merge markers error; secrets, security and risky APIs warning; debug information; task markers and oversized hint | `code-health:secret` and so on |

## Workspace files

See [The .auric-artisan folder](scanning.md#the-auric-artisan-folder) for every file the Studio writes, and [Exports and health records](exports-and-records.md) for their formats.

## Command-line scanner

See [The CI gate](ci-gate.md) for every option and exit code of `auric-artisan`.
