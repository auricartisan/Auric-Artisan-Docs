---
title: Reference — all seventeen Auric Artisan extension IDs
description: Every Auric Artisan VS Code extension with its exact ID, minimum VS Code version, published version and Marketplace address, plus the install commands and flags.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Reference: extension IDs and requirements

## All seventeen extensions

Every extension is published by `auric-artisan` on the Visual Studio Marketplace and is free. "Minimum VS Code" is the lowest VS Code version the published package accepts. "Version" is the latest published version when this page was written (24 September 2026).

| Extension | Extension ID | Minimum VS Code | Version |
| --- | --- | --- | --- |
| Auric Artisan Studio — Full Pack | `auric-artisan.auric-artisan` | 1.74 | 0.1.0 |
| Auric Color — Picker, Palettes & Contrast | `auric-artisan.auric-color` | 1.74 | 0.1.0 |
| Auric Accessibility — WCAG 2.2 Linter | `auric-artisan.auric-a11y` | 1.74 | 0.1.0 |
| Auric Code Health — Secrets, TODOs & Risk | `auric-artisan.auric-codehealth` | 1.74 | 0.1.0 |
| Auric Artisan Theme | `auric-artisan.auric-artisan-theme` | 1.75 | 0.2.0 |
| Auric Artisan File Icons | `auric-artisan.auric-artisan-file-icon` | 1.85 | 0.1.1 |
| Auric Artisan Icon Pack | `auric-artisan.auric-artisan-icon-pack` | 1.85 | 0.1.0 |
| Auric Icons: Modern | `auric-artisan.auric-artisan-modern-icon` | 1.85 | 0.12.1 |
| Auric Icons: Drawn | `auric-artisan.auric-icons-drawn` | 1.85 | 0.12.1 |
| Auric Icons: Playful | `auric-artisan.auric-icons-playful` | 1.85 | 0.12.1 |
| Auric Artisan Emoji | `auric-artisan.auric-artisan-emoji` | 1.85 | 0.2.0 |
| Auric Artisan Icon Studio | `auric-artisan.auric-artisan-icon-studio` | 1.85 | 0.1.0 |
| Auric Artisan Icon Hub | `auric-artisan.auric-artisan-icon-lib` | 1.85 | 0.1.0 |
| Auric Artisan Live — Live Server & Preview | `auric-artisan.auric-artisan-live` | 1.95 | 0.2.1 |
| Auric Artisan File System | `auric-artisan.auric-artisan-file-system` | 1.95 | 0.1.0 |
| Auric Artisan Font Hub | `auric-artisan.auric-artisan-font-hub` | 1.85 | 0.1.0 |
| Auric Artisan Formatter | `auric-artisan.auric-artisan-formatter` | 1.74 | 0.1.0 |

### IDs that are easy to get wrong

- The Studio Full Pack is the bare `auric-artisan.auric-artisan`.
- Icon Hub's ID is `auric-artisan.auric-artisan-icon-lib`, not `…-icon-hub`.
- Auric Icons: Modern is `auric-artisan.auric-artisan-modern-icon`, while Drawn and Playful are `auric-artisan.auric-icons-drawn` and `auric-artisan.auric-icons-playful`.
- File Icons is `auric-artisan.auric-artisan-file-icon` (singular).
- Font Hub is `auric-artisan.auric-artisan-font-hub`. The older Font Library extension had a different ID.

## What each one is

| Extension | In one line |
| --- | --- |
| Studio — Full Pack | Installs Auric Color, Auric Accessibility and Auric Code Health together |
| Auric Color | Inline colour picker, swatches and hover readouts, WCAG and APCA contrast, palettes and OKLCH scales |
| Auric Accessibility | Accessibility linting against WCAG 2.0, 2.1 and 2.2 for HTML, JSX, Vue, Svelte, Astro, PHP and CSS |
| Auric Code Health | Scans for hardcoded secrets, TODO and FIXME markers, debug leftovers, risky APIs and oversized files |
| Theme | Colour themes with Theme Studio for customising them |
| File Icons | Facet, Playful and Modern file and folder icon themes for the Explorer |
| Icon Pack | Installs Auric Icons: Modern, Drawn and Playful and Auric Artisan Emoji together |
| Auric Icons: Modern | A file and folder icon theme plus an SVG icon library |
| Auric Icons: Drawn | A hand-drawn style SVG icon library |
| Auric Icons: Playful | An emoji-style SVG icon library in colour, outline, filled and small variants |
| Emoji | Emoji Studio for finding and inserting emoji, with English and Hindi |
| Icon Studio | One offline studio for every Auric icon collection, emoji and seven open-source icon sets |
| Icon Hub | Search open-source icons across seven collections, customise SVG and export sprites or ZIPs |
| Live | Local development server with live reload, preview, HTTPS, API proxy and mocks, and request inspection |
| File System | A file workspace in the Explorer: batch rename, templates, related files, tags, Properties and workspace trash |
| Font Hub | Discover and compare fonts, add them from the Auric font CDN, and export self-hosting kits |
| Formatter | Code formatter with native diff previews, Formatter Studio, workspace scans and a command-line check |

## Pack membership

| Pack | Members |
| --- | --- |
| `auric-artisan.auric-artisan-icon-pack` | `auric-artisan.auric-artisan-modern-icon`, `auric-artisan.auric-icons-playful`, `auric-artisan.auric-artisan-emoji`, `auric-artisan.auric-icons-drawn` |
| `auric-artisan.auric-artisan` | `auric-artisan.auric-color`, `auric-artisan.auric-a11y`, `auric-artisan.auric-codehealth` |

## Addresses

| What | Address pattern |
| --- | --- |
| Marketplace page | `https://marketplace.visualstudio.com/items?itemName=<extension ID>` |
| VSIX download | `https://marketplace.visualstudio.com/_apis/public/gallery/publishers/auric-artisan/vsextensions/<name>/<version>/vspackage` |
| Auric Artisan VS Code page | https://auricartisan.com/vscode/ |
| Support | https://auricartisan.com/company/contact/ |

In the VSIX address, `<name>` is the part of the ID after `auric-artisan.`.

## Command-line flags

| Command | What it does |
| --- | --- |
| `code --install-extension <id>` | Install the latest version |
| `code --install-extension <id>@<version>` | Install a specific version |
| `code --install-extension <id> --force` | Update to the latest version without a prompt |
| `code --install-extension <file>.vsix` | Install from a VSIX file |
| `code --uninstall-extension <id>` | Remove an extension |
| `code --list-extensions --show-versions` | List installed extensions with versions |
| `code --profile "<name>" --install-extension <id>` | Install into a named VS Code profile |

## VS Code commands used in these guides

| Command | What it does |
| --- | --- |
| **Extensions: Install from VSIX…** | Install an extension from a `.vsix` file |
| **Extensions: Check for Extension Updates** | Look for newer versions now |
| **Developer: Reload Window** | Reload the window after installing or updating |
| **Configure Display Language** | Change VS Code's own display language |
| **Workspaces: Manage Workspace Trust** | Trust or restrict the open folder |
| **Preferences: Open User Settings (JSON)** | Edit user settings as JSON |
| **Preferences: Open Workspace Settings (JSON)** | Edit workspace settings as JSON |
| **Preferences: Open Keyboard Shortcuts** | Review and change shortcuts |
| **Shell Command: Install 'code' command in PATH** | macOS: make the `code` launcher available in terminals |

## Settings that control installation

These are VS Code settings, not Auric settings.

| Setting | What it does |
| --- | --- |
| `extensions.autoUpdate` | Whether VS Code installs extension updates automatically |
| `extensions.autoCheckUpdates` | Whether VS Code checks for updates automatically |
| `settingsSync.ignoredExtensions` | Extension IDs that Settings Sync should not install or remove on other machines |
| `settingsSync.ignoredSettings` | Setting IDs that Settings Sync should not copy |
