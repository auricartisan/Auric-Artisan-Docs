---
title: Auric Artisan Studio — Full Pack
description: What the Auric Artisan Studio Full Pack installs, who it is for, and how to get started with it.
product: VS Code extensions › Auric Artisan Studio › Full Pack
updated: 2026-09-25
---

# Auric Artisan Studio — Full Pack

The **Auric Artisan Studio — Full Pack** is a VS Code extension pack: an extension that contains no code of its own and exists only to install other extensions. Installing it installs the three Auric Artisan Studio extensions in one step: Auric Color, Auric Accessibility and Auric Code Health.

Each of the three stays a real, separate extension. You can update, disable or uninstall any of them from the Extensions view without affecting the others. When they are installed together, they cooperate as one Workstation: one sidebar, one Command Center and one Studio covering colour, accessibility and code health.

Like the rest of the Studio, everything runs locally, with no account, no telemetry and no paid tier. The pack does not install icon themes or icon libraries.

## Who it is for

- Anyone who wants the complete Studio without choosing extensions one by one.
- Teams that want everyone on the same set of tools; one pack ID to recommend in a workspace.

## Where to find it

- Marketplace ID: `auric-artisan.auric-artisan`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan
- Install from a terminal:

```text
code --install-extension auric-artisan.auric-artisan
```

- Version 0.1.0; requires VS Code 1.74 or newer.

## Quick start

1. Open the Extensions view (`Ctrl` + `Shift` + `X`) and search for **Auric Artisan Studio — Full Pack**.
2. Select **Install**. VS Code installs the pack and its three members.
3. Open a project folder.
4. Select the **Auric Accessibility** icon in the Activity Bar; it hosts the shared Workstation.
5. Select **Scan project** in the Overview and wait for the score.
6. Press `Ctrl` + `Alt` + `.` (`Cmd` + `Alt` + `.` on macOS) to open the Command Center.
7. Select **Studio** to open the Workstation Studio with the Home, Color, Check, Health and Brand spaces.

You now have colour hovers and pickers, contrast and WCAG diagnostics, code-health findings and a project score in one place.

## What you can do

- Install or update all three Studio extensions with one pack.
- Keep each member independently manageable: disable Auric Code Health for one workspace, uninstall Auric Color, or update one member on its own.
- Use the combined Workstation: one Overview, one Command Center, one Studio and one knowledge database for every installed capability.
- Recommend one ID to your team, for example in a workspace's `.vscode/extensions.json`.

For what each member does, see [Auric Color](../color/README.md), [Auric Accessibility](../accessibility/README.md) and [Auric Code Health](../code-health/README.md).

## In this folder

| Folder or file | What it covers |
| --- | --- |
| [docs/](docs/README.md) | Guides and reference for the pack. |
| [docs/getting-started.md](docs/getting-started.md) | Installing the pack and what happens next. |
| [docs/managing-members.md](docs/managing-members.md) | Enabling, disabling, updating and removing members. |
| [docs/reference.md](docs/reference.md) | The pack's manifest facts. |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Pack-specific problems. |
| [docs/faq.md](docs/faq.md) | Short answers. |
| [others/](others/README.md) | Glossary, related pages, release notes and privacy. |
| [others/glossary.md](others/glossary.md) | Terms used for the pack. |
| [others/related.md](others/related.md) | Related pages. |
| [others/release-notes.md](others/release-notes.md) | The pack's history. |
| [others/privacy.md](others/privacy.md) | Privacy for the pack. |

Back to the [Studio overview](../README.md).
