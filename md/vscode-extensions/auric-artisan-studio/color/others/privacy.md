---
title: Auric Color — Privacy
description: What Auric Color stores, which settings it changes, and when it uses the network.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Auric Color privacy

Auric Color works entirely on your machine. It sends no code, colours or telemetry anywhere and needs no account.

## What it changes or stores

| Where | What |
| --- | --- |
| Your user settings | `auricColor.appearance.accent`; the picker mode settings when you switch mode; and VS Code's `editor.colorDecorators`, which it turns off in Auric mode (see [Picker modes](../docs/picker-modes.md)) |
| Workspace settings | Values you save in Studio › Settings |
| VS Code's storage for the extension | Your recent colours (up to 12), dismissed suggestions, whether you answered the picker question, and which Studio sections you collapsed |
| Files you choose | Palette, shade and brand exports, through a save dialog |
| `.auric-artisan/` | Only when you build the knowledge database, or when Auric Color is the host and scans run in the background |

## When the network is used

Only when you open a link yourself, such as auricartisan.com from the Studio. The eyedropper reads the screen locally.

See the [Studio privacy page](../../others/privacy.md) for the full picture.
