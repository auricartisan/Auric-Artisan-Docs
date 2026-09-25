---
title: Auric Accessibility — Project scans
description: Scan the whole project with Auric Accessibility, read the result, and keep the score up to date.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Project scans

A project scan reads every supported file in the workspace, grades it and saves the result, so you can see the whole project's state rather than just the open file.

## Run a scan

| How | What happens |
| --- | --- |
| **Scan project** on the Overview | Scans, reusing a fresh cache. After the first scan the button reads **Rescan** and forces a fresh read. |
| **Auric Artisan: Scan Project for Accessibility (Use Cache)** | Scans, reusing a fresh cache. Also the play button in the Project Issues title bar, and **Scan project** in the Command Center. |
| **Auric Artisan: Force Rescan Project and Refresh Cache** | Reads every file again and rewrites the cache. Also **Rescan project** in the Command Center, and **Rescan** in the Studio. |
| **Auric Artisan: Clear Workspace Scan Cache** | Deletes the cache; the score resets until the next scan. The message reads **Auric Artisan: cleared .auric-artisan scan cache.** |

A notification, **Auric Artisan: scanning project...**, shows progress and can be cancelled.

## Read the result

When the scan finishes, a message reports it:

```text
Accessibility 82/100 (B) — 12 contrast + 30 WCAG issue(s) across 214 files (scanned).
```

`(cached)` instead of `(scanned)` means the fresh cache was reused. The buttons are **Open Studio** (opens Home), **Show Issues** (focuses the Project Issues view) and **Force Rescan**. If no contrast pairs or markup were found, the message is **Auric Artisan: no color/background pairs found to evaluate.** After a forced rescan, the message is **Auric Artisan: refreshed scan cache for N file(s).**

The result then appears in:

- the status bar: `A11y 82 B`, with a database icon when it came from the cache; hover it for pass rates and the data source;
- the Overview's workspace card;
- the [Project Issues view](project-issues-view.md), with a badge counting all issues;
- the Studio's Home and Check spaces;
- the Command Center's **Findings** section.

## What the scan grades

- **Contrast:** every text and background pair the scanner can resolve, graded at your threshold (large text at 3:1), plus colour-vision risk and confusable hues.
- **WCAG:** every markup and CSS rule allowed by your audit profile.
- **Code health:** secrets, security, risky APIs, debug, task markers, merge markers and size, in every file. These appear in the Project Issues view and reports even without Auric Code Health; code-health underlines in the editor need Auric Code Health.
- **Branding:** pairs you marked as intentional are listed separately and left out of the score.

See [Scanning](../../docs/scanning.md) for which files are read, the cache, `.auricignore` and the file limit, and [Scores and grades](../../docs/scores-and-grades.md) for the formulas.

## Keep it current

- **As you type:** with `scan.live` on (the default), the score, the Project Issues view and an open Studio re-grade from your edits without a scan.
- **After file changes:** turn on `scan.autoScan` for a full background rescan after files change, and `scan.autoScanOnStartup` to refresh when the workspace opens.
- **After changing settings:** rescan after changing the contrast threshold or standard. Changing the audit profile makes the cache stale, so the next **Scan project** reads the workspace again.

## After a scan

- [The Project Issues view](project-issues-view.md) to browse findings.
- [The Check space: Findings and Preview](check-space.md) to filter findings and preview contrast repairs.
- [The remediation plan](../../docs/remediation-plan.md) for a prioritised backlog.
- [Exports and health records](../../docs/exports-and-records.md) to share results; the health record is written after every scan by default.
- [The CI gate](../../docs/ci-gate.md) to run the same scan on pull requests.
