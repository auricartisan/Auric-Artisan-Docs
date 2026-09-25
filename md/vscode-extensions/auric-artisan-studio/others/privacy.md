---
title: Auric Artisan Studio — Privacy
description: What Auric Artisan Studio does with your code and data, what it writes to disk, and when anything uses the network.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Privacy

Auric Artisan Studio analyses your code entirely on your machine.

## What never leaves your machine

- Your source code, colours, scan results, findings and reports.
- Telemetry: the extensions collect none.
- There is no account, sign-in, API key or licence server.

The extensions contain no network code. Their build is checked so that any code that could make a network request fails the build. The command-line scanner makes no network requests either.

## When the network is used

Only when you choose to open a link:

- **auricartisan.com**, from the Auric Artisan marks and links in the Overview, the Studio and hovers. The Studio's screens will only open links to that one site.
- **W3C documentation**, from **WCAG docs** and **Open WCAG Documentation** links on findings, and links inside knowledge-database entries to official sources.

These open in your browser. Installing or updating the extensions from the Marketplace is handled by VS Code.

## The remediation plan and "AI"

**Generate Agent-Ready Remediation Plan** calls no AI model and sends nothing anywhere. It writes a plan, including a prompt template, to your workspace. If you choose to give that prompt to a coding agent, that agent's own privacy terms apply.

## What is written to your disk

| Where | What | When |
| --- | --- | --- |
| `.auric-artisan/` in your workspace | Scan cache, settings copy, health record, SARIF, history, reports, remediation plan, knowledge database and overrides, a README and a `.gitignore` | When you scan, generate outputs or save Studio settings; see [The .auric-artisan folder](../docs/scanning.md#the-auric-artisan-folder) |
| Your VS Code user settings | The accent colour; colour picker mode switches; `editor.colorDecorators` when Auric Color manages VS Code's colour decorators | When you change them |
| Your workspace's VS Code settings | Values saved from Studio › Settings | When you select **Save settings** |
| VS Code's storage for the extension | Recent colours, dismissed suggestions, the Project Issues grouping, which Studio sections you left open, whether you answered the colour picker prompt, and small colour icons for the Project Issues view | As you use the Studio |
| Files you choose | Palette, shade, brand and Markdown exports | When you export through a save dialog |

To stop the Studio writing to your workspace, turn off **Store workspace data locally** (`data.enabled`). To remove everything, delete the `.auric-artisan` folder and uninstall the extensions.

## Secrets

Code Health never stores a detected secret. The secret's text is replaced by a note such as `[redacted secret; 40 characters]` everywhere it could appear: diagnostics, the Studio, reports, `health.json`, SARIF, the history, the scan cache and remediation tasks. See [Secrets and redaction](../code-health/docs/secrets-and-redaction.md).

## Sharing reports

Reports and records are ordinary files. They contain file paths, line numbers, colour values and messages from your project, but never secret values. Review them before sharing outside your team.

## Related

- [Limits and accuracy](limits-and-accuracy.md)
- [FAQ](../docs/faq.md)
