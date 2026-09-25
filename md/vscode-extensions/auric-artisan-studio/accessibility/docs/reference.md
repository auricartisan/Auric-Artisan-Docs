---
title: Auric Accessibility — Reference
description: Every command, keybinding, setting, view, menu entry and theme colour Auric Accessibility contributes.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Auric Accessibility reference

Facts for Auric Accessibility 0.1.0 (`auric-artisan.auric-a11y`). It needs VS Code 1.74 or newer and starts when VS Code finishes loading. Categories: Linters, Programming Languages, Other.

## Keybindings

| Keys (Windows, Linux) | Keys (macOS) | Command | Active when |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `.` | `Cmd` + `Alt` + `.` | Workstation: Command Center | Auric Accessibility is not suppressed (it is always the host when installed) |
| `Ctrl` + `Alt` + `A` | `Cmd` + `Alt` + `A` | Inspect Accessibility of Element | The editor has focus |

## Commands

All titles appear in the Command Palette after `Auric Artisan:`, except the two marked row action.

| Title | Command ID | What it does |
| --- | --- | --- |
| Open Accessibility Studio | `auricA11y.openStudio` | Opens the Studio on Home |
| Workstation: Command Center | `auricA11y.commandCenter` | Opens the Command Center list |
| Open Rulebook & Knowledge Database | `auricA11y.openKnowledgeBase` | Searches rules, WCAG criteria, manual checks, policies and articles |
| Build Workspace Knowledge Database (JSON + Markdown) | `auricA11y.writeKnowledgeDatabase` | Writes `knowledge.json`, `rulebook.md` and an overrides template |
| Open Unified Icon Studio | `auricA11y.openIconStudio` | Opens the combined Auric icon library |
| Scan Project for Accessibility (Use Cache) | `auricA11y.scanProject` | Scans the project, reusing a fresh cache |
| Force Rescan Project and Refresh Cache | `auricA11y.rescanProject` | Re-reads the project and rewrites the cache |
| Generate Agent-Ready Remediation Plan | `auricA11y.generateAiPlan` | Writes the local remediation plan |
| Clear Workspace Scan Cache | `auricA11y.clearScanCache` | Deletes `scan-cache.json` |
| Search Accessibility Issues | `auricA11y.searchIssues` | Filters the Project Issues view |
| Group Accessibility Issues (Type / File / Severity) | `auricA11y.groupIssues` | Groups the Project Issues view |
| Open WCAG Documentation | `auricA11y.openIssueDocs` | Row action: opens the criterion's Understanding page |
| Open Issue in Contrast Studio | `auricA11y.openIssueInStudio` | Row action: opens a contrast or colour-vision finding in the Contrast Studio |
| Clear Accessibility Issue Search | `auricA11y.clearIssueSearch` | Removes the Project Issues filter |
| Check Contrast of Selection | `auricA11y.checkContrast` | Opens the Contrast Studio with the selected colour as text |
| Inspect Accessibility of Element | `auricA11y.inspectAccessibility` | Shows the Inspect card at the cursor |
| Mark Line as Intentional Branding (Toggle) | `auricA11y.markBranding` | Adds or removes `auric-brand-line` on the current lines |

## Views

| View | ID | Notes |
| --- | --- | --- |
| Overview | `auricA11yHome` | In the **Auric Accessibility** Activity Bar container; the accessibility dashboard |
| Project Issues | `auricA11yIssues` | The findings tree, with a badge |
| Color Picker | `auricA11yPickerView` | Only when Auric Color is installed; collapsed by default |

## Menus

| Menu | Entries |
| --- | --- |
| Editor right-click | **Inspect Accessibility of Element** (Inspect languages); **Check Contrast of Selection** (with a selection); **Mark Line as Intentional Branding (Toggle)** (Inspect languages and Markdown) |
| Project Issues title bar | **Search**, **Group**, **Scan**, **Open Accessibility Studio**, **Collapse All**; **Generate Agent-Ready Remediation Plan** in **…** |
| Project Issues rows | **Open WCAG Documentation** (WCAG rows); **Open Issue in Contrast Studio** (contrast and colour-vision rows) |

Inspect languages: HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JavaScript, TypeScript, JSX, TSX, CSS, SCSS, Less, Sass, PostCSS and Stylus.

## Settings

Auric Accessibility has 24 settings. Search `auricA11y` in **File › Preferences › Settings**. Many can also be changed in Studio › Settings.

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricA11y.appearance.accent` | string | `gold` | The Studio's accent: a preset ID or a hex colour. Stored in user settings. See [Appearance](../../docs/appearance.md). |
| `auricA11y.inspect.enabled` | boolean | `true` | Turns Inspect (hover card and command) on or off. |
| `auricA11y.inspect.onHover` | boolean | `true` | Shows the Inspect card automatically on hover; when off, only through the command. |
| `auricA11y.contrast.enabled` | boolean | `true` | Flags text and background pairs below the target. |
| `auricA11y.contrast.standard` | `wcag2`, `apca`, `both` | `wcag2` | The contrast model. |
| `auricA11y.contrast.apcaThreshold` | number, 15–106 | `60` | Minimum APCA Lc when APCA is used. |
| `auricA11y.contrast.threshold` | number, 1–21 | `4.5` | Minimum WCAG 2.x ratio. |
| `auricA11y.contrast.severity` | `error`, `warning`, `information`, `hint` | `warning` | Problems severity for failing contrast. |
| `auricA11y.contrast.flagCvdRisk` | boolean | `true` | Adds colour-vision risk hints. |
| `auricA11y.contrast.checkPageBackground` | boolean | `true` | Grades colour-only rules against the page background, as softer hints. |
| `auricA11y.a11y.enabled` | boolean | `true` | Turns WCAG diagnostics in the editor on or off. |
| `auricA11y.a11y.profile` | `2.0`, `2.1`, `2.2`, `3.0-draft` | `2.2` | The audit profile. Rescan after changing it. |
| `auricA11y.branding.enabled` | boolean | `true` | Honours `auric-brand-…` marks in the editor. |
| `auricA11y.data.enabled` | boolean | `true` | Creates and uses the `.auric-artisan` folder. Shared. |
| `auricA11y.data.folderName` | string | `.auric-artisan` | The data folder's name, relative to the workspace. Shared. |
| `auricA11y.scan.cache.enabled` | boolean | `true` | Reuses the scan cache instead of rescanning. Shared. |
| `auricA11y.scan.cache.maxAgeMinutes` | number, 0 or more | `1440` | Maximum cache age; `0` keeps it until a forced or automatic scan. Shared. |
| `auricA11y.scan.live` | boolean | `true` | Re-grades the project as you type, from memory. |
| `auricA11y.scan.liveDelayMs` | number, 200–5000 | `700` | Wait after the last keystroke before a live re-grade. |
| `auricA11y.scan.autoScan` | boolean | `false` | Rescans from disk after file changes. Shared. |
| `auricA11y.scan.autoScanOnStartup` | boolean | `false` | With auto scan on, also rescans soon after the workspace opens. Shared. |
| `auricA11y.scan.autoScanDelayMs` | number, 250–60000 | `1800` | Wait after a file change before an automatic scan. Shared. |
| `auricA11y.scan.maxFiles` | number | `4000` | Most files one scan reads. Shared. |
| `auricA11y.scan.exclude` | glob | see below | Paths to skip in scans. Shared. |

The default of `scan.exclude` is `**/{node_modules,dist,build,out,.git,vendor,coverage,.auric-artisan}/**`. "Shared" means the value is read suite-wide when other Studio extensions are installed; see [Shared settings](../../docs/reference.md#shared-settings).

## Theme colours

| Colour ID | Dark | Light | High contrast | High contrast light |
| --- | --- | --- | --- | --- |
| `auricA11y.branding.foreground` | `#F06595` | `#C2255C` | `#FF80AB` | `#A61E4D` |
| `auricA11y.branding.background` | `#F0659522` | `#C2255C1A` | transparent | transparent |
| `auricA11y.branding.border` | `#F0659580` | `#C2255C80` | `#FF80AB` | `#A61E4D` |
| `auricA11y.branding.icon` | `#F06595` | `#C2255C` | `#FF80AB` | `#A61E4D` |

`auricA11y.branding.icon` colours the Branding group in the Project Issues view.

## Studio spaces

On its own: **Home**, **Check** (Findings, Contrast, Preview) and **Settings** (Appearance, Project data, Scan engine, Scope, Accessibility audit, Contrast). As a Workstation host, it adds the spaces of the other installed extensions.

## Diagnostics codes

| Code | Meaning |
| --- | --- |
| `WCAG 1.1.1` and so on | A WCAG rule finding, linked to the criterion |
| `low-contrast`, `apca-low`, `cvd-risk` | Contrast findings |
| `branding:contrast`, `branding:apca`, `branding:cvd` | Classified as branding |

## Files it writes

`.auric-artisan/scan-cache.json`, `settings.json`, the health record (`health.json`, `health.sarif`, `health-history.json`) after scans, `ai-remediation-plan.md` and `.json`, and the knowledge files. See [The .auric-artisan folder](../../docs/scanning.md#the-auric-artisan-folder).

## Related

- [Rules](rules.md)
- [Studio reference](../../docs/reference.md)
- [Shortcuts](../others/shortcuts.md)
