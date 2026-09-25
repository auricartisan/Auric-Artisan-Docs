---
title: Auric Accessibility — Privacy
description: What Auric Accessibility stores and writes, and when it uses the network.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Auric Accessibility privacy

Auric Accessibility analyses your code on your machine. It sends no code, results or telemetry anywhere and needs no account.

## What it writes

| Where | What |
| --- | --- |
| `.auric-artisan/` in your workspace | The scan cache, a settings copy, the health record, SARIF and history after scans, the remediation plan, and the knowledge files you build |
| Your settings | The accent colour (user settings) and values you save in Studio › Settings (workspace settings) |
| VS Code's storage for the extension | The Project Issues grouping, dismissed suggestions, collapsed Studio sections, and small colour icons for tree rows |
| Files you choose | The WCAG and accessibility Markdown exports |

## When the network is used

Only when you open a link yourself: **WCAG docs** and **Open WCAG Documentation** open the W3C's *Understanding* pages in your browser, and Auric Artisan marks open auricartisan.com.

See the [Studio privacy page](../../others/privacy.md) for details.
