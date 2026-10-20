---
title: Auric Artisan Studio — The CI gate
description: Run the bundled auric-artisan command-line scanner, freeze a baseline, fail pull requests only on new issues, and upload SARIF to code scanning.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# The CI gate

The Studio extensions include a command-line scanner, `auric-artisan`, that runs the same colour, accessibility and code-health engine as the editor, without VS Code and without any network access. Use it to fail a pull request when it introduces new problems, and to send findings to your code-scanning dashboard as SARIF.

**CI** (continuous integration) is the automated build and test run on every pull request. A **baseline** is a saved record of the findings a project already has, so a gate can fail only on findings that are new.

## Get the scanner

The scanner is the file `bin/auric-artisan.js` inside each installed Studio extension (Auric Color, Auric Accessibility and Auric Code Health). It is not published as a separate npm package. It needs Node.js; the GitHub Actions example below uses Node 20.

VS Code installs extensions in the `extensions` folder of your user profile's `.vscode` folder, in a folder named after the extension and its version, for example:

```text
~/.vscode/extensions/auric-artisan.auric-codehealth-0.1.0/bin/auric-artisan.js
```

On Windows this is `%USERPROFILE%\.vscode\extensions\auric-artisan.auric-codehealth-0.1.0\bin\auric-artisan.js`.

Run it with Node:

```text
node ~/.vscode/extensions/auric-artisan.auric-codehealth-0.1.0/bin/auric-artisan.js scan .
```

The examples on this page write `auric-artisan` for short. To make that work, create a shell alias or a small script on your path that runs the file with Node. The Studio's **Home › CI gate** card shows the same short form.

> **Important:** The Auric Artisan Free Use Licence 2.0 allows you to install and run the extensions on machines you own or control, but does not allow you to redistribute their files, including publishing them to a public repository. Do not commit the scanner's files to a public repository. In CI, download the extension from the Visual Studio Marketplace during the job, as shown below.

## Usage

```text
auric-artisan scan [dir] [options]
```

`dir` is the folder to scan; it defaults to the current folder.

| Option | What it does |
| --- | --- |
| `--json <file>` | Write the `health.json` record to a file |
| `--sarif <file>` | Write SARIF 2.1.0 to a file, for GitHub code scanning |
| `--baseline <file>` | Compare with a saved record and report only new issues |
| `--write-baseline <file>` | Save the current record as a baseline, then exit |
| `--fail-on <severity>` | Exit with code 1 if any issue is at or above `high`, `medium` or `low` (`critical` and `info` also work) |
| `--max-new <n>` | Exit with code 1 if there are more than `n` new issues; needs `--baseline` |
| `--min-score <n>` | Exit with code 1 if the overall score is below `n` (0–100) |
| `--profile <profile>` | WCAG profile: `2.0`, `2.1`, `2.2` (default) or `3.0-draft` |
| `--threshold <ratio>` | WCAG contrast ratio target (default 4.5) |
| `--no-code-health` | Skip the code-health checks |
| `--max-files <n>` | Most files to scan (default 20000) |
| `--quiet` | Do not print the console summary |
| `--version` | Print the version |
| `--help` | Print the usage |

With `--baseline`, `--fail-on` counts only new issues.

### Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Passed, or no policy was set |
| `1` | A policy failed (`--fail-on`, `--max-new` or `--min-score`) |
| `2` | A usage or runtime error: no command, an unknown command, a missing folder, no scannable files, or a baseline that cannot be read |

Running the scanner with no command, or with `--help` alone, prints the usage and exits with code 2. `auric-artisan help` exits with 0.

## What it scans

- Files with any extension the editor scan reads (see [Scanning](scanning.md#what-is-read)), plus `.xhtml`, `.svg` (as XML) and `.tf` (Terraform, code health only). A file named `.env` is read too.
- It skips folders named `node_modules`, `.git`, `.hg`, `.svn`, `dist`, `build`, `out`, `.next`, `.nuxt`, `.svelte-kit`, `coverage`, `vendor`, `.auric-artisan`, `.cache`, `__pycache__`, `.venv`, `venv`, `.idea` and `.vscode-test`, and every folder whose name starts with a dot.
- It reads the `.auricignore` file at the root of the scanned folder.
- It skips files larger than 1.5 MB.
- When `--max-files` stops the scan early, it prints `⚠ Scanned N of M+ files (capped — raise --max-files).` so a partial scan is never mistaken for a clean one.

The scanner does not read your VS Code settings. It uses its own options: contrast target 4.5 unless you pass `--threshold`, profile 2.2 unless you pass `--profile`, all code-health categories and no custom secret patterns. It always grades rules that set only a text colour against the page background, as the editor does with `contrast.checkPageBackground` on.

## Console output

Without `--quiet`, the scanner prints a summary:

```text
Auric Artisan — scanned 4 files
  score 72/100  C   a11y 3  contrast 2  cvd 0  code-health 3
  1 critical  4 high  1 medium  1 low  1 info   (8 total)
  1 new  0 fixed  7 pre-existing (vs baseline)

  high   contrast  src/a.css:3
         #AAAAAA|#FFFFFF

✗ FAILED: 1 new issue(s) > --max-new 0
```

It lists up to 50 issues, worst first (only the new ones when you compare with a baseline), then `… and N more`. When every policy passes, it prints `✓ PASSED policy checks.`

## Adopt it on an existing codebase

A project that already has findings would fail a strict gate immediately. Freeze the current findings once, then fail only on new ones.

**Step 1.** Create the baseline and commit it:

```text
auric-artisan scan . --write-baseline .auric/baseline.json
```

The scanner prints `Wrote baseline (N issues) → .auric/baseline.json`. Keep the baseline in a folder whose name starts with a dot, such as `.auric/`, so the scanner does not read the baseline itself as a source file.

**Step 2.** In CI, compare every run with the baseline:

```text
auric-artisan scan . --baseline .auric/baseline.json --max-new 0 --sarif auric.sarif
```

**Step 3.** When you fix old findings, regenerate the baseline so they cannot quietly return.

Issues are matched by fingerprint, which includes the line number. A finding that moves to another line counts as new once; regenerate the baseline after large refactors. See [Fingerprints](exports-and-records.md#fingerprints).

> **Note:** Code-health findings are fingerprinted by detector version 1.2.0 in the current package. A baseline written by an earlier detector may list some existing code-health findings as new once; regenerate it.

## GitHub Actions

This workflow downloads Auric Code Health from the Marketplace during the job, scans the pull request, uploads SARIF to GitHub code scanning and fails the check when a new issue appears.

```yaml
name: Auric Artisan
on: [pull_request]
jobs:
  audit:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Download Auric Code Health from the Marketplace
        run: |
          curl -sSL --compressed -o auric.vsix \
            "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/auric-artisan/vsextensions/auric-codehealth/0.1.0/vspackage"
          unzip -q auric.vsix -d "$RUNNER_TEMP/auric"
      - name: Scan
        run: >
          node "$RUNNER_TEMP/auric/extension/bin/auric-artisan.js" scan .
          --baseline .auric/baseline.json --max-new 0
          --sarif auric.sarif --min-score 70
      - if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: auric.sarif
```

- The package is a ZIP file; `--compressed` is needed because the Marketplace sends it compressed.
- Replace `0.1.0` with the version you want. Pinning a version keeps results reproducible.
- `security-events: write` lets the job upload SARIF. Findings then appear in the repository's Security tab and inline on the pull request's diff.

## Pre-commit hook

On your own machine, where the extension is installed, a Git pre-commit hook can block commits with high-severity issues:

```text
auric-artisan scan src --fail-on high --quiet
```

## Same engine, same findings

The scanner, project scans in the editor and live diagnostics share one engine, so the same file with the same settings produces the same findings and fingerprints everywhere. Differences come only from settings: the editor uses your VS Code settings, the scanner uses its options.

## Related

- [Exports and health records](exports-and-records.md) for the `health.json` and SARIF formats.
- [Scanning](scanning.md) and `.auricignore`.
- [Scores and grades](scores-and-grades.md) for `--min-score`.
