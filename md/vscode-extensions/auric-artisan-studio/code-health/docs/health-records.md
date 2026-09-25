---
title: Auric Code Health — Health records
description: Write health.json, SARIF 2.1.0 and a trend history for CI, understand how code-health findings are recorded and fingerprinted, and gate on new issues with a baseline.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Health records

Auric Code Health writes the project's findings to machine-readable files, so CI systems, dashboards and code-scanning tools can use them. The records cover every source the Studio scans: accessibility, contrast, colour vision, branding and code health.

## The three files

| File | Format | Purpose |
| --- | --- | --- |
| `health.json` | JSON | A versioned record of scores, a summary and every issue, each with a stable fingerprint |
| `health.sarif` | SARIF 2.1.0 | The same issues for GitHub code scanning and other SARIF tools |
| `health-history.json` | JSON | One entry per recorded scan, for tracking scores over time |

They are written to `.auric-artisan/` in your workspace. The full formats are described in [Exports and health records](../../docs/exports-and-records.md#the-health-record).

## When they are written

- **Auric Artisan: Write Health Record (health.json + SARIF)**, **SARIF** or **health.json + SARIF** on the Overview, the button of the same name in the Health space, and **Write health.json + SARIF** in the Home space's CI gate card. The record opens when it is written, and a message offers **Open SARIF** and **Open Data Folder**.
- Automatically after every project scan, when `health.writeOnScan` is on (the default).
- Never during live re-grades while you type.

## Settings

| Setting | Default | Effect |
| --- | --- | --- |
| `auricCodeHealth.health.enabled` | `true` | Maintain the record at all |
| `auricCodeHealth.health.writeOnScan` | `true` | Rewrite it after each project scan |
| `auricCodeHealth.health.formats` | `["json","sarif","history"]` | Which files to write |
| `auricCodeHealth.health.fileName` | `health.json` | Name of the JSON file; SARIF and history names follow it |
| `auricCodeHealth.health.maxIssues` | `5000` | Most issues recorded, worst first (100–100000) |
| `auricCodeHealth.health.historyLimit` | `200` | Most history entries kept (10–5000) |

## How code-health findings are recorded

Each code-health issue in `health.json` has:

- `source`: `code-health`;
- `ruleId`: the signature, for example `ch-sec-tls-python`, and `category`: `security`;
- `severity`: merge markers `high`; secrets, security and risky APIs `medium`; debug `low`; task markers and oversized `info`;
- `confidence`, `detectorVersion` (1.2.0) and `knowledgeRuleId` (the rule's entry in the knowledge database);
- `file`, `line`, `col`, `message` and `fix`;
- `match`: the evidence, which for secrets is only the redaction note; `evidenceType` (the kind of secret) and `redacted: true` for secrets.

In SARIF, each signature is a rule with its category, detector version and confidence as properties; results for secrets carry `evidenceRedacted`. Levels are `error` for high, `warning` for medium and `note` for low and info.

The `summary.codeHealthByCategory` object counts findings per category, and `scores.codeHealth` holds the code-health score.

## Fingerprints and baselines

Every issue has an 8-character `id` fingerprint built from its source, signature, file, line and a key detail. For secrets, the key detail is the signature and column, never the secret. Fingerprints let a CI gate compare two runs:

1. Save the current state as a baseline once.
2. On each pull request, compare with it and fail only if there are new fingerprints.

Use the command-line scanner for this; see [The CI gate](../../docs/ci-gate.md). A finding that moves to another line gets a new fingerprint.

> **Note:** Code-health findings are fingerprinted with the detector version that produced them. A baseline written by an earlier detector (1.1.0) may list some existing findings as new once. Regenerate the baseline after updating.

## Git information

When the workspace has a `.git` folder, the record includes the current branch and commit, read directly from the folder (no Git command is run). SARIF includes them as version-control provenance, so code scanning can link results to the commit.

## Related

- [Exports and health records](../../docs/exports-and-records.md)
- [The CI gate](../../docs/ci-gate.md)
- [Secrets and redaction](secrets-and-redaction.md)
