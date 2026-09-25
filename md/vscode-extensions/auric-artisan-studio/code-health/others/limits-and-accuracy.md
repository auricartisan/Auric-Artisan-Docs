---
title: Auric Code Health — Limits and accuracy
description: What Auric Code Health's checks can and cannot find, and how their accuracy was measured.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Auric Code Health limits and accuracy

## What it is

A high-signal heuristic linter that reads the text of the files in your workspace. It favours precision: it reports the common, high-confidence cases and tells a constant from a dynamic value.

## Measured accuracy

On a labelled set of examples used in development, including a held-out set, precision is 1.00 in every category (no false positives), and recall is 1.00 in every category except secrets, where 96% of the planted secrets were found.

## What it does not do

- It does not build a syntax tree or trace data flow between functions, so it cannot tell whether a dynamic value is actually user-controlled.
- It does not scan Git history, so a secret removed from the current files but still in history is not found.
- It does not check whether a credential is live.
- It is not a full static application security testing tool or a dedicated secret scanner.

## Behaviour to know

- Secrets are found everywhere, including comments; other categories ignore comments and, where it matters, strings.
- Signatures run only in the languages where they apply; see [Categories and signatures](../docs/categories-and-signatures.md).
- A file reports at most 300 findings.
- Lines over 240 characters are reported, except lines that start with a URL. Files over 800 lines are reported by project scans and the command-line scanner only.
- Files over 1 MB are skipped in the editor and in project scans (1.5 MB for the command-line scanner).
- Worst-case inputs, such as a 200 KB minified line or a 5,000-line file, are checked in milliseconds.

For scanning and scoring limits shared with the other extensions, see the [Studio limits and accuracy page](../../others/limits-and-accuracy.md).
