---
title: Auric Artisan File Icons — Privacy
description: What Auric Artisan File Icons reads, stores and writes, and confirmation that it has no telemetry.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Privacy

- **No account or telemetry.** The extension does not automatically contact a server, run shell commands or execute workspace code. Website links open only when you select them.
- **Bounded inspection.** Smart detection reads up to 250 direct folder entries and text files up to 64 KiB by default, caches results for 15 seconds, and skips excluded, binary, oversized and unavailable files.
- **Remote-aware access.** Inspection goes through VS Code's file system interface, which covers local, remote and virtual resources. What can be read or written depends on the provider.
- **Explicit edits.** Code is inserted only after your action, and hover actions check that the document has not changed.

## What is stored

| Data | Where |
| --- | --- |
| Appearance settings | Your VS Code settings under `auricFileIcons.*` (user level when set from the Studio). |
| Associations from the Explorer, smart style choices and scan results | The workspace settings. |
| Saved profiles | VS Code's extension storage on this machine. |
| Rebuilt theme files after customisation | Inside the extension's own folder; the shipped artwork is not modified. |

## Diagnostics

**Show Icon Theme Diagnostics** writes counts and settings to a local output channel. It omits filenames and file contents and sends nothing anywhere.
