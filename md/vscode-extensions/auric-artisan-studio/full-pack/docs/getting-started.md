---
title: Full Pack — Getting started
description: Install the Auric Artisan Studio Full Pack, check what it installed, and find the Workstation it creates.
product: VS Code extensions › Auric Artisan Studio › Full Pack
updated: 2026-09-25
---

# Getting started with the Full Pack

## Install

1. Open the Extensions view with `Ctrl` + `Shift` + `X`.
2. Search for `auric-artisan.auric-artisan`, or **Auric Artisan Studio — Full Pack**.
3. Select **Install**.

Or run:

```text
code --install-extension auric-artisan.auric-artisan
```

You need VS Code 1.74 or newer.

## What gets installed

| Extension | ID | What it adds |
| --- | --- | --- |
| Auric Color — Picker, Palettes & Contrast | `auric-artisan.auric-color` | Colour hovers, swatches and pickers in 40+ languages, contrast diagnostics, palettes, shades, colour vision and the brand audit |
| Auric Accessibility — WCAG 2.2 Linter | `auric-artisan.auric-a11y` | 70+ WCAG rules, Inspect, project scans, the Project Issues view and the remediation plan |
| Auric Code Health — Secrets, TODOs & Risk | `auric-artisan.auric-codehealth` | Secrets, security, risky APIs, debug leftovers, task markers, merge markers and size checks; health records, SARIF and reports |

The pack itself adds no commands, views or settings.

To check what was installed, open the Extensions view and look under **Installed**, or open the pack's page in the Extensions view: VS Code lists the extensions it includes.

## What you see afterwards

The three extensions start once VS Code has finished loading, and form one Workstation hosted by Auric Accessibility:

- **Activity Bar:** one Auric icon, **Auric Accessibility**, with the **Overview**, **Project Issues** and a collapsed **Color Picker** view. Auric Color's and Auric Code Health's own views are hidden.
- **Overview:** the workspace card with **Accessibility**, **Contrast issues** and **Code health** rows, **Scan project**, **Report** and **SARIF**.
- **Status bar:** the score item and, when the open file has findings, **Auric: N in this file**.
- **Studio:** titled **Auric Artisan — Workstation Studio**, with the Home, Color, Check, Health and Brand spaces and Settings.
- **Command Center:** `Ctrl` + `Alt` + `.` lists actions for all three capabilities.

See [Getting started](../../docs/getting-started.md) for a full tour, and [The Workstation](../../docs/workstation.md) for how the three combine.

## Recommend the pack to your team

To prompt everyone who opens a repository to install the pack, add it to the workspace's `.vscode/extensions.json`:

```json
{
  "recommendations": ["auric-artisan.auric-artisan"]
}
```

VS Code then suggests the pack when a teammate opens the folder.

## Next steps

- [Manage the pack's members](managing-members.md)
- [Choose what to install](../../docs/choosing-an-install.md), if you decide you need only one member.
