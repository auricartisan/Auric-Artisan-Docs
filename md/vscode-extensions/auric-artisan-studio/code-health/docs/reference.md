---
title: Auric Code Health — Reference
description: Every command, keybinding, setting and view Auric Code Health contributes.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Auric Code Health reference

Facts for Auric Code Health 0.1.0 (`auric-artisan.auric-codehealth`). It needs VS Code 1.74 or newer and starts when VS Code finishes loading. Categories: Linters, Other.

## Keybindings

| Keys (Windows, Linux) | Keys (macOS) | Command | Active when |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `.` | `Cmd` + `Alt` + `.` | Workstation: Command Center | Auric Code Health is not suppressed by a Workstation host |

## Commands

All titles appear in the Command Palette after `Auric Artisan:`.

| Title | Command ID | What it does |
| --- | --- | --- |
| Open Code Health Studio | `auricCodeHealth.openStudio` | Opens the Studio on Health, or the Workstation host's Studio |
| Workstation: Command Center | `auricCodeHealth.commandCenter` | Opens the Command Center list |
| Open Rulebook & Knowledge Database | `auricCodeHealth.openKnowledgeBase` | Searches signatures, categories, policies, articles and sources |
| Build Workspace Knowledge Database (JSON + Markdown) | `auricCodeHealth.writeKnowledgeDatabase` | Writes `knowledge.json`, `rulebook.md` and an overrides template |
| Open Unified Icon Studio | `auricCodeHealth.openIconStudio` | Opens the combined Auric icon library |
| Generate Agent-Ready Remediation Plan | `auricCodeHealth.generateAiPlan` | Writes the local remediation plan |
| Generate Project Health Report (Color, A11y & Code Health) | `auricCodeHealth.projectHealthReport` | Writes `project-health.md`, `.json` and `.html` |
| Write Health Record (health.json + SARIF) | `auricCodeHealth.writeHealthReport` | Writes `health.json`, SARIF and history |
| Clear Workspace Scan Cache | `auricCodeHealth.clearScanCache` | Deletes `scan-cache.json` |
| Open Workspace Data Folder | `auricCodeHealth.openDataFolder` | Shows `.auric-artisan` in your file manager, creating it if needed |

## Views

| View | ID | Notes |
| --- | --- | --- |
| Overview | `auricCodeHealthHome` | In the **Auric Code Health** Activity Bar container; hidden while another Studio extension hosts |

Auric Code Health adds no editor right-click entries.

## Settings

Auric Code Health has 28 settings. Search `auricCodeHealth` in **File › Preferences › Settings**. The data, scan, code-health and health settings are shared across installed Studio extensions; see [Shared settings](../../docs/reference.md#shared-settings).

### Appearance

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricCodeHealth.appearance.accent` | string | `gold` | The Studio's accent: a preset ID or a hex colour. See [Appearance](../../docs/appearance.md). |

### Code health

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricCodeHealth.codeHealth.enabled` | boolean | `true` | Runs the code-health checks at all |
| `auricCodeHealth.codeHealth.diagnostics` | boolean | `true` | Shows findings in the editor and Problems panel; when off, only in scans, the Studio and reports |
| `auricCodeHealth.codeHealth.todo` | boolean | `true` | Task markers: TODO, FIXME, HACK, XXX, BUG, OPTIMIZE, REFACTOR, DEPRECATED |
| `auricCodeHealth.codeHealth.debug` | boolean | `true` | Debug leftovers such as `console.log`, `debugger`, `dbg!`, `var_dump`, `breakpoint()`, `NSLog` |
| `auricCodeHealth.codeHealth.secret` | boolean | `true` | Possible hardcoded secrets |
| `auricCodeHealth.codeHealth.conflict` | boolean | `true` | Merge-conflict markers |
| `auricCodeHealth.codeHealth.risk` | boolean | `true` | Risky APIs such as `eval()`, `new Function()`, `innerHTML =`, `document.write()` |
| `auricCodeHealth.codeHealth.security` | boolean | `true` | Security footguns: TLS bypass, weak hashing, unsafe deserialization, XSS sinks, CORS, injection |
| `auricCodeHealth.codeHealth.customSecretPatterns` | array of strings | `[]` | Extra regular expressions reported as possible secrets (medium confidence) |
| `auricCodeHealth.codeHealth.size` | boolean | `true` | Very long lines and large files |

### Health record

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricCodeHealth.health.enabled` | boolean | `true` | Maintains `health.json`, SARIF and history |
| `auricCodeHealth.health.writeOnScan` | boolean | `true` | Rewrites the record after each project scan |
| `auricCodeHealth.health.formats` | array: `json`, `sarif`, `history` | all three | Which files to write |
| `auricCodeHealth.health.fileName` | string | `health.json` | JSON file name; SARIF and history names follow it |
| `auricCodeHealth.health.maxIssues` | number, 100–100000 | `5000` | Most issues recorded, worst first |
| `auricCodeHealth.health.historyLimit` | number, 10–5000 | `200` | Most history entries kept |

### Data folder

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricCodeHealth.data.enabled` | boolean | `true` | Creates and uses the `.auric-artisan` folder |
| `auricCodeHealth.data.folderName` | string | `.auric-artisan` | The folder's name, relative to the workspace |

### Scanning

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricCodeHealth.scan.cache.enabled` | boolean | `true` | Reuses the scan cache |
| `auricCodeHealth.scan.cache.maxAgeMinutes` | number, 0 or more | `1440` | Maximum cache age; `0` keeps it until a forced or automatic scan |
| `auricCodeHealth.scan.live` | boolean | `true` | Re-grades the project as you type, from memory |
| `auricCodeHealth.scan.liveDelayMs` | number, 200–5000 | `700` | Wait after the last keystroke before a live re-grade |
| `auricCodeHealth.scan.autoScan` | boolean | `false` | Rescans from disk after file changes |
| `auricCodeHealth.scan.autoScanOnStartup` | boolean | `false` | With auto scan on, also rescans soon after the workspace opens |
| `auricCodeHealth.scan.autoScanDelayMs` | number, 250–60000 | `1800` | Wait after a file change before an automatic scan |
| `auricCodeHealth.scan.maxFiles` | number | `4000` | Most files one scan reads |
| `auricCodeHealth.scan.exclude` | glob | see below | Paths to skip |

The default of `scan.exclude` is `**/{node_modules,dist,build,out,.git,vendor,coverage,.auric-artisan}/**`.

## Diagnostics codes

| Code | Category |
| --- | --- |
| `code-health:secret` | Possible secrets |
| `code-health:security` | Security risks |
| `code-health:conflict` | Merge markers |
| `code-health:risk` | Risky APIs |
| `code-health:debug` | Debug leftovers |
| `code-health:todo` | Task markers |
| `code-health:size` | Oversized |

## Quick fixes

| Quick fix | What it inserts |
| --- | --- |
| **Ignore this secret finding here** (category varies) | `auric-disable-next-line <category>` on the line above |
| **Ignore all secret findings in this file** (category varies) | `auric-disable-file <category>` at the top |

## Studio spaces

On its own: **Health** and **Settings** (Appearance, Project data, Scan engine, Scope).

## Files it writes

`.auric-artisan/` `scan-cache.json`, `settings.json`, `health.json`, `health.sarif`, `health-history.json`, `project-health.md`, `.json` and `.html`, `ai-remediation-plan.md` and `.json`, and the knowledge files. See [The .auric-artisan folder](../../docs/scanning.md#the-auric-artisan-folder).

## Command-line scanner

The `auric-artisan` scanner ships inside the extension at `bin/auric-artisan.js`. See [The CI gate](../../docs/ci-gate.md).

## Related

- [Categories and signatures](categories-and-signatures.md)
- [Studio reference](../../docs/reference.md)
- [Shortcuts](../others/shortcuts.md)
