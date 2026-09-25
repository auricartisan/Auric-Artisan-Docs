---
title: Auric Code Health — Getting started
description: Install Auric Code Health, read your first finding, grade the repository and write your first CI record.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Getting started with Auric Code Health

## Install

1. Open the Extensions view (`Ctrl` + `Shift` + `X`).
2. Search for `auric-artisan.auric-codehealth` and select **Install**. Or run `code --install-extension auric-artisan.auric-codehealth`.

It starts when VS Code finishes loading. You need VS Code 1.74 or newer. All seven categories are on by default.

## Your first finding

1. Open any source file, in any of the 40+ supported languages.
2. Findings are underlined and listed in the Problems panel with the source `auric-artisan` and a code such as `code-health:debug`. For example:

```text
Leftover debug statement (console.).  —  Remove before committing, or route through a real logger.
```

3. Hover the underline. The card shows the signature's title (for example **Console debug output**), a severity pill, the category (for example **Debug leftovers**), the confidence, a priority, the location, requirement tags such as `CWE-798` or `OWASP-A05:2025` where they apply, the line of code, the fix, and actions: **Go to code**, **Rule details**, **Ignore here** and **Copy reference**. The footer shows the signature ID and detector version, such as `ch-debug-console v1.2.0`.
4. Press `Ctrl` + `.` for **Ignore this debug finding here** (inserts `auric-disable-next-line debug` above) or **Ignore all debug findings in this file**.

Secret findings never show the secret itself; the evidence reads, for example, `[redacted secret; 40 characters]`. See [Secrets and redaction](secrets-and-redaction.md).

## Grade the repository

1. Select the **Auric Code Health** icon in the Activity Bar. The **Overview** shows a **Code health** ring (empty until the first grade) and seven chips: **Secrets**, **Security**, **Risky APIs**, **Debug**, **TODOs**, **Conflicts** and **Large files**.
2. Select **Report**. The Studio scans the workspace (or reuses a fresh cache) and writes the project health report to `.auric-artisan`.
3. The ring shows the code-health score and grade, and each chip its count. The status bar shows, for example, `Health 88 B`.
4. In the message that appears, select **Open in Browser** to read the printable report.

See [Scores and grades](../../docs/scores-and-grades.md#the-code-health-score) for how the score is calculated.

## Explore the findings

Run **Auric Artisan: Open Code Health Studio** (or **Studio** on the Overview, or the status-bar item). The **Health** space shows the score, the seven categories as filters, confidence filters, a search box and every finding. See [The Code Health Studio](code-health-studio.md).

## Write the CI records

Select **health.json + SARIF** on the Overview, or run **Auric Artisan: Write Health Record (health.json + SARIF)**. The Studio writes `health.json`, `health.sarif` and `health-history.json` to `.auric-artisan` and opens `health.json`. See [Health records](health-records.md) and [The CI gate](../../docs/ci-gate.md).

## Where Auric Code Health appears

| Place | What you get |
| --- | --- |
| Editor | Code-health underlines, hovers and ignore quick fixes |
| Activity Bar, **Auric Code Health** | **Overview** (the code-health layout) |
| Status bar | `Health` and the score, when it is the only Studio extension |
| Studio (**Open Code Health Studio**) | **Health** and **Settings** |
| Command Center (`Ctrl` + `Alt` + `.`) | Project health report, health record, data folder, remediation plan, worst findings, written files |

## With the other Studio extensions

When Auric Accessibility or Auric Color is installed, one of them hosts the Workstation. Auric Code Health hides its own views, adds its **Health** space, **Report**, **SARIF** and the CI gate card to the host, and keeps publishing code-health underlines. See [The Workstation](../../docs/workstation.md).

## Next steps

- [Categories and signatures](categories-and-signatures.md)
- [Secrets and redaction](secrets-and-redaction.md)
- [The remediation plan](../../docs/remediation-plan.md)
