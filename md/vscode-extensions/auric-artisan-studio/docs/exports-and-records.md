---
title: Auric Artisan Studio — Exports and health records
description: Generate the project health report, write health.json, SARIF and trend history, and export Markdown summaries from the Studio.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Exports and health records

The Studio can turn a scan into files you can read, print, share or feed to other tools. All of them are generated on your machine and written to your workspace; nothing is uploaded.

| Output | Made by | Format | Written to |
| --- | --- | --- | --- |
| Project health report | **Generate Project Health Report (Color, A11y & Code Health)** | Markdown, JSON, HTML | `.auric-artisan/project-health.*` |
| Health record | **Write Health Record (health.json + SARIF)**, or automatically after each scan | JSON | `.auric-artisan/health.json` |
| SARIF export | Same as the health record | SARIF 2.1.0 (JSON) | `.auric-artisan/health.sarif` |
| Trend history | Same as the health record | JSON | `.auric-artisan/health-history.json` |
| Accessibility summary | Studio › Home › **Report** (without Auric Code Health) | Markdown | Where you choose |
| WCAG summary | Studio › Check › Findings › **Export WCAG** | Markdown | Where you choose |
| Remediation plan | **Generate Agent-Ready Remediation Plan** | Markdown, JSON | `.auric-artisan/ai-remediation-plan.*` |
| Palette, shade and brand token exports | Studio › Color and Brand tools | CSS, JSON, Tailwind config | Where you choose |

The two commands that make the project health report and the health record come with Auric Code Health. The health record files are also written automatically after every project scan, whichever Studio extension ran it (see `health.writeOnScan` below). All outputs that go to `.auric-artisan` need a workspace folder to be open; without one you see, for example, **Auric Artisan: open a workspace folder before generating a Project Health report.**

## The project health report

### Generate it

1. Run **Auric Artisan: Generate Project Health Report (Color, A11y & Code Health)**, or select **Report** on the Overview, in the Studio's Home or Health space, or **Project health report** in the Command Center.
2. The Studio uses a fresh scan cache if there is one, or scans first.
3. It writes three files to `.auric-artisan` and opens the Markdown one.
4. A message confirms, for example **Auric Artisan: Project Health report ready — grade B, 14 code-health finding(s). Generated locally.**, with three buttons:
   - **Open in Browser** opens `project-health.html` in your default browser. The file is local; nothing is fetched.
   - **Open JSON** opens `project-health.json`.
   - **Open Data Folder** shows the folder in your file manager.

Although the command comes with Auric Code Health, the report covers colour, accessibility and code health even when Code Health is the only Studio extension installed.

### project-health.md

| Section | Contents |
| --- | --- |
| Heading | **Auric Artisan — Project Health Report**, the date and time, the WCAG profile, and **all analysis ran locally** |
| **Overview** | Overall grade and score, files and languages, unique colours, contrast pairs, accessibility score and issues, code-health score and findings |
| **Languages** | Up to 20 languages with their file counts |
| **Code Health** | Counts per category and the top 20 findings with file and line |
| **Accessibility (WCAG 2.2)** | Counts by impact and the top 15 findings with criterion, impact, message and location |
| **Worst contrast pairs** | Up to 15 pairs: foreground, background, ratio, ratio needed, location; large text and dark theme are marked |
| **Recommendations** | Up to 8 recommendations from the scan |

### project-health.json

A JSON file with `"schema": "auric-artisan.project-health"`, the time it was generated and the full scan result. Long lists are capped: up to 600 failing pairs, 300 colour-vision risks, 600 WCAG findings, 800 code-health findings, 600 branding findings, 96 colours and 20 file hotspots.

### project-health.html

A printable page styled like the Studio's paper theme. It is self-contained: the fonts are embedded, there are no scripts, and it loads nothing from the network, so it looks the same opened from disk, attached to an email or printed. It contains:

- the workspace name, scan date, number of files, WCAG profile and contrast target;
- score cards for **Overall**, **Accessibility**, **Contrast** and **Code health**;
- **Fix these first**: up to five recommendations with their priority;
- **Contrast pairs below 4.5:1** (your target): up to 12 pairs with a sample, the pair, its location, its ratio and the **nearest passing, same hue** colour with its ratio;
- **Accessibility by criterion**: up to 12 success criteria with counts;
- **Code health by kind**: counts per category, with secrets highlighted;
- **Files to fix first**: up to eight files with contrast, WCAG and colour-vision counts;
- a footer: **Nothing in this report left the machine it was made on.**

## The health record

The health record is a stable, versioned, machine-readable record of every issue in the project, for CI dashboards, code scanning and trend tracking.

### Write it

- Run **Auric Artisan: Write Health Record (health.json + SARIF)**, or select **SARIF** (Overview), **health.json + SARIF** (Overview or Studio › Health) or **Write health.json + SARIF** (Studio › Home › CI gate).
- The Studio uses a fresh scan cache or scans first, writes the formats listed in `health.formats`, and opens `health.json`.
- A message lists what was written, for example **Auric Artisan: wrote health.json, health.sarif, health-history.json — grade B, 14 code-health + 3 contrast + 21 a11y issues. Generated locally.**, with **Open SARIF** and **Open Data Folder**.

With `health.writeOnScan` on (the default), the record is also rewritten after every project scan, including automatic scans. Live re-grades never write files. If `health.enabled` is off, the command says **Auric Artisan: health report is disabled (auricCodeHealth.health.enabled).**

### Settings

| Setting | Default | Effect |
| --- | --- | --- |
| `auricCodeHealth.health.enabled` | `true` | Maintain the record at all |
| `auricCodeHealth.health.writeOnScan` | `true` | Rewrite it after each project scan |
| `auricCodeHealth.health.formats` | `["json","sarif","history"]` | Which files to write |
| `auricCodeHealth.health.fileName` | `health.json` | Name of the JSON file; the SARIF and history names follow it |
| `auricCodeHealth.health.maxIssues` | `5000` | Most issues recorded, worst first (100–100000) |
| `auricCodeHealth.health.historyLimit` | `200` | Most history entries kept (10–5000) |

For example, with `health.fileName` set to `quality.json`, the files are `quality.json`, `quality.sarif` and `quality-history.json`.

### health.json

The top-level fields:

| Field | Contents |
| --- | --- |
| `$schema`, `schemaVersion`, `kind` | `https://auricartisan.com/schema/health-v1.json`, `1`, `auric-artisan.health` |
| `tool` | Name, version and website of the tool |
| `knowledge` | Version, content hash and domains of the knowledge database used, and `actConformant: false` |
| `generatedAt`, `workspace` | When the scan ran, and the workspace name |
| `git` | The branch and commit, read from the `.git` folder when there is one |
| `profile`, `thresholds` | The WCAG profile, the contrast ratio target and the APCA target |
| `scores` | `overall`, `grade`, `contrast`, `accessibility`, `codeHealth` |
| `summary` | Files, languages, colours, pairs, total issues, counts by source and severity, branding, categories, WCAG impacts |
| `languages`, `colors` | Files per language, and up to 64 colours with their use and file counts |
| `issues` | Every issue, worst first, up to `health.maxIssues` |

Each issue has:

| Field | Contents |
| --- | --- |
| `id` | An 8-character fingerprint that identifies the issue across runs |
| `source` | `accessibility`, `contrast`, `color-vision`, `branding` or `code-health` |
| `ruleId` | For example `img-alt`, `low-contrast`, `low-contrast-inherited`, `cvd-risk`, `branding-contrast`, `ch-secret-jwt` |
| `severity` | `critical`, `high`, `medium`, `low` or `info` |
| `file`, `line`, `col` | Workspace-relative path with forward slashes, and position |
| `message`, `fix` | What is wrong and how to fix it |
| Other fields | `wcag`, `knowledgeRuleId`, `detectorVersion`, `confidence`, `automation`, `category`, `data`, `excludedFromScore`, `redacted` |

`wcag` holds the criterion, title, level and version. `data` holds the colours and ratios of a colour issue. `excludedFromScore` marks branding. `redacted` marks secrets.

How severities are assigned:

| Finding | Severity |
| --- | --- |
| WCAG critical, serious, moderate, minor | critical, high, medium, low |
| Contrast failure | high (low when the background was assumed from the page) |
| Colour-vision risk | medium |
| Branding | info |
| Code health: merge markers | high |
| Code health: secrets, security, risky APIs | medium |
| Code health: debug leftovers | low |
| Code health: task markers, oversized | info |

Secrets are never written: their evidence is replaced by a note such as `[redacted secret; 40 characters]`. See [Secrets and redaction](../code-health/docs/secrets-and-redaction.md).

### Fingerprints

The fingerprint is calculated from the issue's source, rule, file, line and a key detail (the colour pair for colour issues, the message or evidence otherwise). It stays the same from run to run while those stay the same, which is what makes baselines work. If a finding moves to another line, for example because you added lines above it, it gets a new fingerprint and counts as new against a baseline.

### health.sarif

SARIF (Static Analysis Results Interchange Format) 2.1.0 is the format GitHub code scanning and many CI tools read. The file has one run whose tool is **Auric Artisan**, with:

- a **rules** list: each rule's ID, a short description (for WCAG, the criterion and its title), a help link (the W3C Understanding page for WCAG rules, auricartisan.com otherwise) and a default level;
- a **result** per issue: rule, level, message with the fix, file and position, a `partialFingerprints.auricArtisanId` fingerprint, and properties such as source, severity, confidence and whether evidence was redacted;
- the commit and branch, when known.

Levels: critical and high issues are `error`, medium issues are `warning`, low and info issues are `note`.

### health-history.json

An append-only trend log. Each recorded scan adds one entry with its time, commit and branch, grade, scores, number of files, total issues and counts by source and severity. When the log exceeds `health.historyLimit` entries, the oldest are dropped. The bundled `.gitignore` excludes it; remove that line if you want to commit the history.

## Studio Markdown exports

Both open a save dialog in your first workspace folder, then open the saved file.

### Accessibility summary (accessibility-report.md)

From Studio › Home › **Report** when Auric Code Health is not installed. It contains the score and grade, files scanned, unique colours, contrast pair counts and harmony, the contrast distribution, the recommendations, up to 20 file hotspots, up to 500 failing pairs and up to 200 colour-vision risk pairs.

### WCAG summary (wcag-report.md)

From Studio › Check › Findings › **Export WCAG**. It contains the accessibility sub-score and overall score, issue counts by level, impact and WCAG version, a table by success criterion, and every WCAG finding with criterion, impact, message and location. It ends with **Automated checks cover only part of WCAG; manual testing is still required.**

## Related

- [The CI gate](ci-gate.md), which writes the same `health.json` and SARIF from the command line.
- [The remediation plan](remediation-plan.md)
- [Palettes and shades](../color/docs/palettes-and-shades.md) and [The brand audit](../color/docs/brand-audit.md) for the colour exports.
