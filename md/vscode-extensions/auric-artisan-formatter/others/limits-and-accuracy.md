---
title: Auric Artisan Formatter — limits and accuracy
description: What Auric Artisan Formatter's safety gate guarantees, its known gaps in version 0.1.0, and its size and time limits.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Limits and accuracy

## What the safety gate guarantees

With the default settings, a result is written only if the output re-reads to the same significant tokens, keeps every comment and every string's content, and parses again. If any check fails, the original text is kept. The idempotency check (formatting twice gives the same bytes) is off by default because it doubles the work; the `verified` preset turns it on.

The gate protects meaning, not taste: a result can pass every check and still not be the layout you want. Use Formatter Studio to tune it.

## Known gaps in version 0.1.0

- **JSX and TSX** files containing JSX elements are formatted by the universal tier (indentation and spacing only), not pretty-printed.
- **Universal-tier languages** only change whitespace. Some only change spacing or trailing whitespace. See [Supported languages](../docs/supported-languages.md).
- **Format Every File in the Workspace** on a folder's context menu formats every pending file in the workspace, not only that folder.
- **The command line** ships inside the extension and is not a separate npm package.

## Limits

| Limit | Default | Setting |
| --- | --- | --- |
| Largest file formatted | 4096 KB (`0` removes the limit) | `auricFormatter.maxFileSizeKb` |
| Parse time before a parse is abandoned | 5000 ms (`0` waits indefinitely) | `auricFormatter.parseTimeoutMs` |
| Files in one workspace scan | 4000 | `auricFormatter.scanMaxFiles` |
| Formatter Studio preview | 200,000 characters | — |
| Open native previews | 24 | — |
| Formatting options | 391, in 17 categories | — |

## Deterministic output

The engine uses no clock, no randomness and no locale-dependent ordering, so the same input and configuration give the same output on every machine and in CI. Line width is measured in display columns, so wide characters such as CJK text and emoji break lines where a person would expect.

## What it is not

- It is not a linter: it changes layout, not code behaviour, and does not report style errors beyond "needs formatting".
- It is not a backup: the gate prevents corruption, but formatting many files is still a change you should commit or stash first.
