---
title: Auric Artisan Studio — Scanning
description: How project scans, live re-grading and background scans work, what is read, how the cache and .auricignore behave, and what the .auric-artisan folder contains.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Scanning

The Studio checks your code in three ways. Knowing which is which explains when numbers change and when files are written.

| Kind | What it covers | When it runs | Writes files? |
| --- | --- | --- | --- |
| **Live diagnostics** | The files open in editors | As you type, about 300 ms after you stop | No |
| **Live re-grade** | The whole project score, from files held in memory | As you type, after `scan.liveDelayMs` (700 ms by default) | No |
| **Project scan** | Every matching file in the workspace | When you ask, or automatically if you turn on auto scan | Yes: the scan cache, and health records if enabled |

## Live diagnostics

Underlines, hovers and Problems entries for open files update as you type. They are always on and do not depend on any scan setting. What is checked depends on the installed extensions and their switches: `contrast.enabled`, `a11y.enabled`, `codeHealth.enabled` and `codeHealth.diagnostics`. Files larger than 1 MB are not analysed in the editor.

## Project scans

A project scan reads the workspace, grades it and saves the result.

### Start a scan

| How | Uses a fresh cache? |
| --- | --- |
| **Scan project** on the Overview, or **Auric Artisan: Scan Project for Accessibility (Use Cache)** | Yes |
| **Rescan** on the Overview or Studio, **Force rescan** in Studio Settings, or **Auric Artisan: Force Rescan Project and Refresh Cache** | No, always re-reads |
| **Scan Code Health** or **Rescan** in the Studio's Health space | No |
| **Generate Project Health Report**, **Write Health Record**, **Generate Agent-Ready Remediation Plan** | Yes; they scan first if there is no fresh cache |

A scan started from a command shows a progress notification, **Auric Artisan: scanning project...**, with a **Cancel** button. If a scan fails, you see an error and your previous results are left untouched.

### What a scan produces

- The overall score and grade, the contrast and accessibility sub-scores, and the code-health score. See [Scores and grades](scores-and-grades.md).
- Every contrast pair the scanner could resolve, the failing pairs, and pairs at colour-vision risk.
- WCAG findings from markup and CSS files, under the audit profile you chose.
- Code-health findings from every supported file.
- Branding classifications, the project palette (every colour and how often it appears), a harmony analysis and pairs of hues that become confusable under colour-vision deficiency.
- A ranked list of files to fix first and up to six recommendations.

The result appears in the Overview, the status bar, the Project Issues view, the Studio and the Command Center.

### What is read

The scan reads files with these extensions. Stylesheets, markup and script files get the contrast and WCAG checks; every file gets the code-health checks.

| Group | Extensions |
| --- | --- |
| Stylesheets | `.css` `.scss` `.sass` `.less` `.styl` `.stylus` `.pcss` `.postcss` |
| Markup and components | `.html` `.htm` `.vue` `.svelte` `.astro` `.php` `.xml` `.md` `.markdown` |
| Scripts and data | `.js` `.cjs` `.mjs` `.jsx` `.ts` `.mts` `.cts` `.tsx` `.json` `.jsonc` `.json5` |
| Python, Go, Rust, Java, C# | `.py` `.pyw` `.pyi` `.go` `.rs` `.java` `.cs` |
| C, C++, Objective-C | `.c` `.h` `.cpp` `.cc` `.cxx` `.hpp` `.hh` `.m` `.mm` |
| Kotlin, Swift, Dart, Ruby, Lua, R, Julia | `.kt` `.kts` `.swift` `.dart` `.rb` `.lua` `.r` `.jl` |
| Scala, Groovy, Perl, Haskell | `.scala` `.groovy` `.gradle` `.pl` `.pm` `.hs` |
| Elixir, Erlang, Clojure, F#, Visual Basic | `.ex` `.exs` `.erl` `.clj` `.cljs` `.fs` `.fsx` `.vb` |
| Shell and query | `.sh` `.bash` `.zsh` `.ps1` `.psm1` `.coffee` `.sol` `.graphql` `.gql` `.sql` |
| Config and templates | `.yaml` `.yml` `.toml` `.ini` `.cfg` `.conf` `.properties` `.env` `.hbs` `.handlebars` `.pug` `.jade` `.ejs` `.twig` `.razor` |

It skips:

- anything matched by `scan.exclude` (by default `**/{node_modules,dist,build,out,.git,vendor,coverage,.auric-artisan}/**`);
- anything matched by a `.auricignore` file (below);
- the `.auric-artisan` data folder;
- files larger than 1 MB, and files that cannot be read.

If no matching files are found, the scan falls back to the stylesheets and markup files that are open in editors.

> **Note:** A file named exactly `.env` (with nothing before the dot) is not read by the in-editor project scan, although files such as `production.env` are. The command-line scanner reads both.

### The file limit

`scan.maxFiles` (default 4000) caps how many files one scan reads. When the cap cuts a scan short, the status-bar tooltip says so, for example `⚠ Scanned 4000 of 5230 files (capped at 4000 …)`, and the Command Center suggests **Scanned X of Y files**. Raise the limit in Studio › Settings › **Scope**, or narrow the scan with `scan.exclude` or `.auricignore`.

## The scan cache

Each completed scan is saved to `.auric-artisan/scan-cache.json`. The next **Scan project** reuses it instead of reading every file again, as long as it is fresh.

- **Freshness.** `scan.cache.maxAgeMinutes` (default 1440, which is 24 hours). A value of `0` keeps the cache until you force a rescan or an automatic scan refreshes it.
- **At startup** the Studio loads a fresh cache so the score is there straight away. The status-bar score shows a database icon when it came from the cache.
- **Audit profile.** If you change the WCAG audit profile, Auric Accessibility treats a cache made under another profile as stale and scans again.
- **Turning it off.** Clear **Use cached scan data** in Studio Settings (`scan.cache.enabled`), and every scan reads the workspace.
- **Clearing it.** Run **Auric Artisan: Clear Workspace Scan Cache**, or **Clear cache** in Studio Settings. The file is deleted and the score resets until the next scan.

## Live re-grade

With `scan.live` on (the default), the project score, the Project Issues view and an open Studio keep up with your edits without a scan. The Studio keeps the files from the last scan in memory and swaps in the text of the file you are editing. It never reads the disk on a keystroke and never writes the cache.

- The first edit after VS Code starts reads the workspace once to warm up.
- Only files that were part of the scan are re-graded. New or ignored files are skipped until the next scan.
- Very large workspaces, over 1,500 files or about 12 MB of text, are not re-graded live. Run a scan, or turn on automatic scans, to refresh them.
- `scan.liveDelayMs` sets how long the Studio waits after your last keystroke (200–5000 ms, default 700).

When several Studio extensions are installed, the one that owns the status-bar score runs the live re-grade. The others re-grade only while their own Studio tab is open.

## Automatic background scans

With `scan.autoScan` on (off by default), the Studio runs a full scan, and rewrites the cache, after files are created, changed, deleted or saved. It waits `scan.autoScanDelayMs` (default 1800 ms, range 250–60000) after the last change. With `scan.autoScanOnStartup` also on, it scans shortly after the workspace opens. When a background scan finishes, the status bar briefly shows **Auric Artisan cache updated**. Background scans never interrupt you with errors.

When several Studio extensions are installed, only the one that owns the status-bar score runs automatic scans, so the shared cache has exactly one automatic writer. Scans you start yourself are never restricted.

## .auricignore

Put a file named `.auricignore` at the root of a workspace folder to keep files and folders out of scans. It uses a subset of `.gitignore` syntax:

```text
# comments and blank lines are ignored
generated/                 # a folder
legacy-theme.css           # an exact path
*.min.js                   # * and ? wildcards
**/__snapshots__/          # **/ matches at any depth, including the root
docs/**/*.html             # ** between folders
!generated/keep-this.css   # ! re-includes something an earlier line excluded
/anchored/path             # a leading / anchors to the folder root
```

Later lines win, so a `!` line can bring back a file an earlier pattern excluded. The common cases match `.gitignore`, but not every edge case of Git's rules is reproduced. `.auricignore` applies on top of `scan.exclude`. In a multi-root workspace each folder can have its own `.auricignore`. The command-line scanner reads it too.

## The .auric-artisan folder

The Studio keeps its workspace data in one folder, `.auric-artisan` by default, at the root of the workspace. In a multi-root workspace it is created in the first folder. All installed Studio extensions share it.

| File | What it is |
| --- | --- |
| `scan-cache.json` | The last scan, reused while fresh. |
| `settings.json` | A copy of the Studio's scan, data and picker settings, kept up to date as the Studio starts, scans and saves settings. |
| `health.json` | The fingerprinted health record. See [Exports and health records](exports-and-records.md). |
| `health.sarif` | The same issues in SARIF 2.1.0. |
| `health-history.json` | A capped trend log, one entry per recorded scan. |
| `project-health.md`, `.json`, `.html` | The project health report. |
| `ai-remediation-plan.md`, `.json` | The agent-ready remediation plan. |
| `knowledge.json`, `rulebook.md` | The generated knowledge database and rulebooks. |
| `knowledge-overrides.json` | Your team's validated additions to the knowledge database. |
| `README.md` | A short note explaining the folder, written the first time it is created. |
| `.gitignore` | Keeps the regenerated files out of source control. |

The bundled `.gitignore` excludes `scan-cache.json`, the remediation plan, the project health report, `health.json`, `health.sarif`, `health-history.json`, `knowledge.json`, `rulebook.md` and temporary files. It leaves `settings.json`, `knowledge-overrides.json`, `README.md` and `.gitignore` so you can commit team defaults and reviewed guidance. Edit it if you want to commit the health history.

You can delete the whole folder at any time; the Studio recreates it on the next scan or settings save. To rename it, set `data.folderName`. To stop the Studio writing workspace data at all, turn off `data.enabled` (Studio Settings › **Store workspace data locally**); scans then run without a cache.

## What static scanning can and cannot see

The scanner reads source text. It does not run your code or render pages. It finds colour pairs and markup problems it can resolve from the text: CSS rules, `<style>` blocks, inline `style=` attributes, JSX style objects (`style={{…}}`, `sx={{…}}`, `css={{…}}`), styled-components, Emotion and Linaria templates, and Vue, Angular and Svelte style bindings. It cannot see colours set by JavaScript at runtime, class-driven styles applied from another file, the full cascade between different selectors, or component state. See [Limits and accuracy](../others/limits-and-accuracy.md) for the details, and [Contrast diagnostics](../color/docs/contrast-diagnostics.md) for how contrast pairs are resolved.
