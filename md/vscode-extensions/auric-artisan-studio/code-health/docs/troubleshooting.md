---
title: Auric Code Health — Troubleshooting
description: Symptoms, causes and fixes for Auric Code Health's findings, secrets, Studio and records.
product: VS Code extensions › Auric Artisan Studio › Auric Code Health
updated: 2026-09-25
---

# Auric Code Health troubleshooting

For problems shared by all Studio extensions (scans, the data folder, settings), see the [Studio troubleshooting page](../../docs/troubleshooting.md).

## Findings in the editor

### No code-health underlines appear

**Why:** One of these applies:

- `codeHealth.enabled` or `codeHealth.diagnostics` is off;
- the category is turned off (for example `codeHealth.todo`);
- VS Code does not recognise the file's language, or the file is larger than 1 MB;
- a suppression comment covers the line or file.

**What to do:** Check the settings under `auricCodeHealth.codeHealth`, and look for `auric-disable` comments.

### A TODO in my code is not reported

**Why:** In languages the Studio can lex, task markers count only inside comments, so a `TODO` inside a string or identifier is ignored on purpose. Lower-case markers need `@todo`, `todo:` or `fixme:`.

### console.log is not reported in a Python or Go file

**Why:** Debug signatures are limited to the languages where they are debug hooks: `console.log` in web languages, `breakpoint()` in Python, a `DEBUG`-prefixed `fmt.Print` in Go, and so on. Normal output such as `print` or `fmt.Println` is never reported.

### eval is reported with low confidence

**Why:** Its argument is a constant, so the risk is lower; the message ends **(constant argument — lower risk)**. A dynamic argument is reported with high confidence.

### innerHTML is not reported

**Why:** The assigned value is a constant string or passes through a sanitiser function, which is safe.

### A long line is not reported

**Why:** The line is 240 characters or fewer, or starts with a URL. Large files (over 800 lines) are reported only by project scans, not in the editor.

### "Unresolved merge-conflict marker" in Markdown

**Why:** A line starts with seven `<` or `>` characters. A lone `=======` heading underline is not reported.

**What to do:** Resolve the conflict, or suppress the line if the marker is intentional example text.

## Secrets

### A secret is reported that is a placeholder or test value

**Why:** The value does not look like a placeholder to the filters, for example a realistic-looking test token.

**What to do:** Add `auric-disable-line secret` (or the signature ID) in a comment on that line. If it is a real credential, rotate it.

### A real secret is not reported

**Why:** It does not match a provider shape, and its name does not end in a credential word, or its value looks like a placeholder or reference.

**What to do:** Add a pattern for your token format to `codeHealth.customSecretPatterns`. Auric Code Health is not a full secret scanner; use a dedicated tool where coverage matters.

### My custom pattern does nothing

**Why:** The regular expression is invalid (it is ignored silently), the matches look like placeholders, or you are running the command-line scanner, which does not read VS Code settings.

**What to do:** Test the expression, and remember the JSON string needs escaped backslashes.

### I cannot see which secret was found

**Why:** Secrets are always redacted; only their length is shown.

**What to do:** Use **Go to code**; the underline covers the secret's position.

## Studio, reports and records

### The Health space says "Code Health Studio" with a Scan button

**Why:** There is no scan result yet.

**What to do:** Select **Scan Code Health**.

### The status bar shows no Health score

**Why:** The status-bar item shows `Health` only when Auric Code Health is the only Studio extension; otherwise it shows the accessibility score (`A11y`). Before a scan it has no number.

**What to do:** Select **Report** on the Overview, or use the Studio's **Health** space.

### health.json was not updated after a scan

**Why:** `health.enabled` or `health.writeOnScan` is off, `health.formats` does not include `json`, or the scan was a live re-grade, which never writes files.

### A baseline suddenly reports old findings as new

**Why:** Lines moved (fingerprints include the line), or the baseline was written by an earlier detector version.

**What to do:** Regenerate the baseline. See [Health records](health-records.md#fingerprints-and-baselines).

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
