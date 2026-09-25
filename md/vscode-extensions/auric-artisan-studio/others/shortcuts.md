---
title: Auric Artisan Studio — Shortcuts
description: Every keyboard shortcut, Command Palette title and in-Studio key for Auric Artisan Studio.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Shortcuts

## Keyboard shortcuts

| Windows and Linux | macOS | Command | Extension |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `.` | `Cmd` + `Alt` + `.` | Workstation: Command Center | All three code extensions |
| `Ctrl` + `Alt` + `C` | `Cmd` + `Alt` + `C` | Pick / edit color (editor focused) | Auric Color |
| `Ctrl` + `Alt` + `A` | `Cmd` + `Alt` + `A` | Inspect Accessibility of Element (editor focused) | Auric Accessibility |

These VS Code shortcuts are useful with the Studio:

| Keys | What it does |
| --- | --- |
| `Ctrl` + `.` | Show quick fixes for the underline at the cursor |
| `Ctrl` + `Shift` + `P` | Open the Command Palette; type `Auric Artisan` to list every Studio command |
| `Ctrl` + `Shift` + `M` | Open the Problems panel |
| `Ctrl` + `Z` | Undo a fix, including a whole **Fix All Contrast Issues in File** |

## Command Palette titles

Every Studio command starts with `Auric Artisan:`.

| Title | Extension |
| --- | --- |
| Workstation: Command Center | All three |
| Open Color Studio | Auric Color |
| Open Accessibility Studio | Auric Accessibility |
| Open Code Health Studio | Auric Code Health |
| Open Rulebook & Knowledge Database | All three |
| Build Workspace Knowledge Database (JSON + Markdown) | All three |
| Open Unified Icon Studio | All three |
| Pick / edit color | Auric Color |
| Generate Accessible Palette | Auric Color |
| Check Contrast of Selection | Auric Color, Auric Accessibility |
| Fix All Contrast Issues in File | Auric Color |
| Choose Color Picker Mode | Auric Color |
| Disable native color picker (use Auric Artisan) | Auric Color |
| Restore native color picker (use VS Code's) | Auric Color |
| Refresh Contrast Diagnostics | Auric Color |
| Change Accent Color (Theme the Studio) | Auric Color |
| Mark Line as Intentional Branding (Toggle) | Auric Color, Auric Accessibility |
| Inspect Accessibility of Element | Auric Accessibility |
| Scan Project for Accessibility (Use Cache) | Auric Accessibility |
| Force Rescan Project and Refresh Cache | Auric Accessibility |
| Generate Agent-Ready Remediation Plan | Auric Accessibility, Auric Code Health |
| Clear Workspace Scan Cache | Auric Accessibility, Auric Code Health |
| Search Accessibility Issues | Auric Accessibility |
| Group Accessibility Issues (Type / File / Severity) | Auric Accessibility |
| Clear Accessibility Issue Search | Auric Accessibility |
| Generate Project Health Report (Color, A11y & Code Health) | Auric Code Health |
| Write Health Record (health.json + SARIF) | Auric Code Health |
| Open Workspace Data Folder | Auric Code Health |

## Keys inside the Studio

| Keys | Where | What it does |
| --- | --- | --- |
| Arrow keys, `Home`, `End` | Studio rail and tab rows | Move between spaces or tools |
| `/` | Findings and Health | Focus the search box |
| `Escape` | Studio | Close a picker, menu or tooltip, then clear the search |
| `Enter`, `Space` | Swatches, rows, tiles | Activate |
| Arrow keys, `Shift` + arrows, `Page Up`, `Page Down`, `Home`, `End` | Colour picker bars and spectrum | Adjust the colour |
| `Escape` | Colour picker | Close it |

See [Accessibility of the Studio](../docs/studio-accessibility.md) for more.

## Change a shortcut

1. Open **File › Preferences › Keyboard Shortcuts** (`Ctrl` + `K`, `Ctrl` + `S`).
2. Search for the command title, for example **Workstation: Command Center**.
3. Double-click the entry and press the new keys.

When several Studio extensions are installed, only the host's Command Center shortcut is active; the others are switched off automatically.
