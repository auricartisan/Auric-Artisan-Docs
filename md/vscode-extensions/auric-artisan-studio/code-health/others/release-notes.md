---
title: Auric Code Health — Release notes
description: Auric Code Health's version history, taken from the Studio changelog.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Auric Code Health release notes

Auric Code Health shares one version number and one changelog with the other Studio extensions. This page lists the entries that concern code health. The complete history is in the [Studio release notes](../../others/release-notes.md).

## Unreleased

Listed under **Unreleased** in the changelog, as upcoming entries for the next numbered release (detector 1.2.0):

- Accuracy measured on a labelled set, including a held-out set: precision 1.00 in every category; recall 1.00 except secrets, 0.96 (up from 0.53).
- Secret detection now covers JSON, PHP, typed and Go assignments, prefixed names such as `MYSQL_PASSWORD`, unquoted `.env`, YAML and INI values, OpenAI `sk-proj-` keys, Google keys ending in `-`, and Azure and ADO.NET connection strings.
- False positives removed: placeholders such as `CHANGE_ME`, `{{API_KEY}}`, `$VAR` and SOPS `ENC[…]`; translation labels, autocomplete tokens and key-file paths; `redis.eval` and `model.eval()`; tagged SQL templates; phone masks read as `XXX` markers; Markdown underlines read as merge markers.
- One credential is one finding.
- Secret bytes no longer leak through task-marker messages or security evidence into SARIF or `health.json`.
- Calls whose arguments cannot be read are reported at medium confidence instead of being passed.
- A mention of `auric-disable-file` in prose or a string no longer silences a whole file.
- Task markers, `debugger` and breakpoints are recognised only where they belong in each language.
- The underline covers the finding's real span.
- Worst-case inputs scan in 5–30 ms.
- Findings are fingerprinted by detector 1.2.0, so a baseline written by 1.1.0 may list some findings as new once.
- **Generate Project Health Report** also writes a printable `project-health.html`, with **Open in Browser**.

## 0.1.0 — Initial Studio release

- Checks for exposed secrets, injection risks, unsafe APIs, merge markers, debug code, task markers, oversized files and maintainability problems.
- Secret evidence redacted before it reaches diagnostics, reports or the Studio.
- Project health records, JSON and SARIF 2.1.0 output, stable fingerprints, baselines, trend history and an offline command-line scanner.
- A versioned local knowledge base covering rules, policies, glossary entries, sources and remediation guidance.
