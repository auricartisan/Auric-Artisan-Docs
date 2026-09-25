---
title: Full Pack — Reference
description: The Auric Artisan Studio Full Pack's ID, members, version, requirements and Marketplace metadata.
product: VS Code extensions › Auric Artisan Studio › Full Pack
updated: 2026-09-25
---

# Full Pack reference

| Property | Value |
| --- | --- |
| Display name | Auric Artisan Studio — Full Pack |
| Extension ID | `auric-artisan.auric-artisan` |
| Publisher | `auric-artisan` (Auric Artisan) |
| Version | 0.1.0 |
| VS Code required | 1.74 or newer |
| Categories | Extension Packs, Linters, Visualization, Other |
| Keywords | color, accessibility, a11y, wcag, contrast, code health, extension pack |
| Licence | Auric Artisan Free Use Licence 2.0 |
| Website | https://auricartisan.com |
| Marketplace | https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan |

## Members

| Order | Extension | ID |
| --- | --- | --- |
| 1 | Auric Color — Picker, Palettes & Contrast | `auric-artisan.auric-color` |
| 2 | Auric Accessibility — WCAG 2.2 Linter | `auric-artisan.auric-a11y` |
| 3 | Auric Code Health — Secrets, TODOs & Risk | `auric-artisan.auric-codehealth` |

## What the pack contributes

Nothing beyond its members: no commands, keybindings, views, settings or files. Every command, shortcut and setting you get comes from a member. See the [Studio reference](../../docs/reference.md).

## Marketplace description

"The complete Auric Artisan Studio in one install: colour picking and palettes, 70-rule WCAG 2.2 accessibility linting, local rulebooks and team knowledge, and language-agnostic code-health scanning. Installs the three focused Studio extensions, which you can enable or disable independently."

The accessibility engine in the current package runs 72 rules; see [the rule catalogue](../../accessibility/docs/rules.md).

## Commands

| Command | Result |
| --- | --- |
| `code --install-extension auric-artisan.auric-artisan` | Installs the pack and its members |
| `code --uninstall-extension auric-artisan.auric-artisan` | Uninstalls the pack |
| `code --list-extensions` | Lists installed extensions, including the members |
