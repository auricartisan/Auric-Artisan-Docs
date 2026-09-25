---
title: Auric Code Health — FAQ
description: Short answers about Auric Code Health.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Auric Code Health FAQ

### Which languages does it check?

More than 40: JavaScript, TypeScript, Python, Go, Rust, Java, C#, C and C++, Kotlin, Swift, Ruby, PHP, shell, SQL, YAML, TOML, JSON, Markdown, HTML, CSS and many more. Some signatures apply only where they make sense; see [Categories and signatures](categories-and-signatures.md).

### Is it a replacement for a secret scanner or SAST tool?

No. It is a fast, high-signal heuristic linter for the files in your workspace. It does not scan Git history, verify credentials or trace data flow. Use dedicated tools where compliance requires them.

### Will it ever show or store my secrets?

No. Every secret is replaced by `[redacted secret; N characters]` everywhere it could appear. See [Secrets and redaction](secrets-and-redaction.md).

### How is the code-health score calculated?

Each finding costs points by category (secrets 14, security 12, merge markers 10, risky APIs 4, debug 2, oversized 0.5, task markers 0.25), scaled by confidence and divided by the number of files. See [Scores and grades](../../docs/scores-and-grades.md#the-code-health-score).

### Does the code-health score affect the accessibility score?

No. They are separate. The overall score in the status bar and Overview combines contrast and accessibility only.

### Can I turn off TODO findings?

Yes: set `auricCodeHealth.codeHealth.todo` to `false`. Every category has its own switch.

### Can I silence one finding?

Yes: **Ignore here** in the hover, the **Ignore this … finding here** quick fix, or an `auric-disable-next-line <category>` comment. The comment must be a real comment; mentioning it in a string does nothing.

### Why does the project health report mention accessibility and colour?

The report covers everything the Studio scans. Its command is provided by Auric Code Health, but the scan always includes contrast and WCAG checks.

### How do I use it in CI?

Run the bundled `auric-artisan` command-line scanner with a baseline and upload the SARIF. See [The CI gate](../../docs/ci-gate.md).

### Does it need the internet?

No. See [Privacy](../others/privacy.md).
