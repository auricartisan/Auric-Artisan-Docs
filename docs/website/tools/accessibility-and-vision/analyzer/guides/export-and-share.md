---
title: Analyzer — Export and share
description: Every way to take a result out of the Analyzer — reports, data files, stylesheets and share links — with formats and file names.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Export and share

This guide lists every export the Analyzer offers, what each file contains, and the ways to share a result. Most exports are in the **Report** section; others live in the section they come from.

## The Report section

**Report** opens with **Full Analysis Report**, the date it was generated and the audited address, the score and the issue count. Then comes the **Export** row.

| Button | What you get | File |
| --- | --- | --- |
| **Export JSON** | The full report data, for automation, regression checks and comparing fields over time | `analysis.json` |
| **Export HTML** | A self-contained HTML report that opens in any browser and can be printed | `auric-analyzer-report.html` |
| **Export PDF** | A PDF of the report (paid plans; see below) | `auric-report-<number>.pdf`, or your browser's print dialog |
| **Export Fix CSS** | One clean stylesheet of the generated fixes | `auric-analyzer-fixes.css` |
| **Developer Report** | A Markdown report written for developers | `auric-developer-report.md` |
| **Client Report** | A Markdown report written for clients and stakeholders | `auric-client-report.md` |
| **Copy Report** | The developer report, copied to the clipboard as Markdown | — |
| **Share Link** | A link to re-run this audit (see below) | — |

### Export PDF

PDF is a Pro export format, included with paid plans. On the free plan, selecting it opens an upgrade prompt that explains the audit stays free and that **Export HTML**, **Export JSON**, the fix CSS and both Markdown reports carry the same data.

When you are entitled, the button shows its progress ("Building PDF…"). If a server PDF cannot be built, the Analyzer opens the HTML report in a new window with your browser's print dialog ("Opening print view…"): choose **Save as PDF** there. If your browser blocks that window, the HTML report is downloaded instead, with a message telling you to open it and print it to PDF.

### Copy Report

When the copy works, a message says "Report copied to the clipboard as Markdown." If the browser refuses clipboard access, the message says nothing was copied and suggests **Developer Report** to download the same Markdown instead.

### What the Report section shows

Below the buttons, **Details** repeats the whole audit in one long page:

- **Category Scores**, with a button per category;
- **Narrative Insights** (human summary, confidence, estimated score after top fixes, recommended next steps);
- **Score Weighting Transparency**;
- **Meta & SEO**, **Accessibility**, **Contrast**, **Color Palette**, **Fonts**, **DOM Structure**, **Performance**, **Metadata Intelligence**, **Responsive Devices**, **Security & Reliability** and **Custom Rules** summaries;
- **All Issues**, each with its fix;
- **How Your Score Was Calculated**, a table of **Category**, **Score**, **Weight**, **Contribution** and **Points lost**, with the final score. Excluded categories show why, for example "excluded (13% unused — no value produced)". The button **How this score is combined, and what it cannot tell you** explains the method;
- a footer naming the engine version, the rule sets used ("WCAG 2.1 AA + 2.2 + WCAG 3 (preview) + Core Web Vitals 2024 + HTTP Archive 2024"), the data sources, the run time, and the limitations ("Cross-origin pages cannot be deeply inspected; some metrics are lab estimates and not real-user data (RUM).").

## Exports in other sections

| Section | Button | File |
| --- | --- | --- |
| A11y+ › Export | **Results JSON (axe format)** | `a11y-<site>.json` |
| A11y+ › Export | **Issues CSV** | `a11y-<site>-issues.csv` |
| A11y+ › Export | **Remediation brief (Markdown)** | `a11y-<site>-remediation.md` |
| A11y+ › Export | **Contrast fix CSS** | `a11y-<site>-contrast.css` |
| A11y+ › Export | **Conformance report CSV** (Specialist plan) | `a11y-<site>-conformance-report.csv` |
| A11y+ › Fixes | **Copy the whole stylesheet** | Clipboard |
| Fixes | **Export Fix CSS** | `auric-analyzer-fixes.css` |
| Fixes | **Copy Batch CSS** | Clipboard |
| Palette | **Export as CSS** / **Export as JSON** | `palette.css` / `palette.json` |
| Project | **Export project model JSON** | `project-model-<date>.json` |
| Site Map | **Export map JSON** | `site-map-<date>.json` |
| Playground | **Export CSS Fixes** / **Export Palette** | `accessibility-fixes.css` / `fixed-palette.css` |
| Playground › Design Lab | **Download .css**, **Theme tokens (JSON)**, **Runtime JS**, **Palette JSON** | `auric-design-lab.css`, `auric-design-tokens.json`, `auric-design-lab.js`, `auric-palette.json` |
| Devices | Live custom CSS **Export** | `device-custom.css` |
| Rules | **Export rules** | `analyzer-custom-rules.json` |
| Workspace | **Export Workspace** | `workspace.json` |
| Compare | **Download it** | `<host>-<date>.json` |

In these names, `<site>` is a short form of the audited address and `<date>` is the date in year-month-day form.

## Share a result

There are four ways to share, and none of them sends the full report. Each link makes the recipient's Analyzer run the audit again on the same address, so they see the page as it is when they open the link.

| Where | Control | What the recipient gets |
| --- | --- | --- |
| Strip | **Share** | A link that re-runs the audit on the same URL; the original score travels as context only |
| Report | **Share Link** | A copied link carrying the score, issue count and URL; the scanned pages stay on your machine |
| Insights | **Copy share link** | A link that re-runs the audit on the same address |
| Insights | **Email** | Opens your email app with a message titled "Auric Artisan audit:" and the URL, containing the score and the headlines |

The strip's **Share** opens the site-wide share dialog. The Report's **Share Link** copies its link straight away and shows it in a **Share this report** sheet with **Copy again** and **Done**.

You can also build a link by hand: `https://auricartisan.com/tool/analyzer/?url=https://example.com` opens the Analyzer and starts an audit of that address.

> **Note:** Because a shared link re-runs the audit, the recipient needs whatever the audit needs. Auditing another website requires them to be signed in, and the run uses their own tokens and monthly allowance.

For the site-wide share dialog, see [Shareable links](../../../../site-features/shareable-links/README.md).

## Which format should I use?

| You want to | Use |
| --- | --- |
| Hand results to a developer | **Developer Report**, or the A11y+ **Remediation brief** and **Issues CSV** |
| Send a summary to a client or manager | **Client Report**, or **Export HTML** |
| Keep a record for an audit trail | **Export HTML** or **Export PDF**, plus **Export JSON** |
| Feed a pipeline or compare runs programmatically | **Export JSON**, or the A11y+ **Results JSON (axe format)** |
| Paste fixes straight into a stylesheet | **Export Fix CSS**, or the A11y+ **Contrast fix CSS** |
| Support a procurement or VPAT request | The A11y+ **Conformance report CSV** (Specialist), reviewed by a person |
| Show a colleague the live result | **Share** |
