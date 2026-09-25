---
title: Analyzer — Overview
description: What the Auric Artisan Analyzer audits, who it is for, and how to run your first audit.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Analyzer

The Analyzer audits a web page from its URL. It reads the page, measures what it can in a real browser, and reports back across accessibility, colour contrast, palette, performance, SEO and metadata, media, responsive behaviour, security and reliability. The page it lives on introduces it as "One URL, audited seven ways." Every finding names the element that caused it, explains why it matters, and, where it can, gives you the code to fix it.

At its centre is an accessibility engine of 126 rules mapped to WCAG 2.0, 2.1 and 2.2 success criteria, Section 508 and EN 301 549. Around it sit a contrast audit with suggested replacement colours, a colour-vision simulation of the page's own palette, Core Web Vitals, a raw-versus-rendered HTML comparison, a site map built from robots.txt and the sitemap, a security-header check, and exports in JSON, HTML, PDF, CSS, CSV and Markdown.

The Analyzer has two modes. **Simple** shows the sections most people need and runs a fixed set of checks. **Advanced** opens all 22 sections as a workspace of panels you can arrange, lets you choose which checks run, and adds whole-site scanning, live editing and custom rules. Every run is filed in your browser so you can reopen it and compare it with later runs of the same site.

## Who it is for

- **Accessibility specialists** who want a rule-by-rule WCAG audit, an accessibility tree, a screen-reader transcript and a VPAT-shaped conformance table.
- **Front-end and full-stack developers** who want the failing selectors, a paste-ready CSS patch and a comparison of raw and rendered HTML.
- **Designers** who want to see every failing colour pair, a passing replacement that keeps the hue, and the palette under colour-vision filters.
- **SEO and content teams** who want metadata, headings, structured data, robots rules and sitemap discovery in one place.
- **Site owners** who want a score to track over time and a short list of what to fix first.

## Where to find it

- Address: https://auricartisan.com/tool/analyzer/
- From any page: open the **Tools** menu in the site header and select **Analyze URLs**.
- A link of the form `https://auricartisan.com/tool/analyzer/?url=https://example.com` opens the Analyzer and starts an audit of that address straight away.

The Analyzer runs in any modern browser with JavaScript enabled. Auditing Auric Artisan's own pages needs no account. Auditing another website needs you to be signed in, because that page is rendered on Auric Artisan's servers (see [Limits and accuracy](others/limits-and-accuracy.md)).

## Quick start

1. Open https://auricartisan.com/tool/analyzer/.
2. Type or paste a full address into the URL field, for example `https://example.com`.
3. Select **Analyze**, or press `Enter` in the field.
4. Watch the progress card in the Overview panel. It lists each check as it runs.
5. Read the **Overall Audit Score** and the **Top 3 Things To Improve Score** in the Overview panel.
6. Open the **Contrast** panel to see failing colour pairs, and the **Fixes** panel for the code to change.
7. Open the **Report** panel and select **Export HTML** or **Export JSON** to keep a copy.
8. Run the same URL again after you fix something, then open **Compare** to see what changed.

## What you can do

- Audit one page, or crawl up to 24 pages of a site in one run (Artisan plan and above).
- Choose which of 13 checks run, and see the token cost before you start (Advanced).
- Read an accessibility grade, a WCAG 2.2 conformance verdict and a success-criteria scorecard.
- Filter accessibility findings by impact, area and WCAG level, and copy the selector or the fix for each one.
- Get a ready-to-paste CSS patch for contrast, focus and target-size failures.
- See every text colour pair with its WCAG ratio and a passing replacement colour.
- Preview the page through colour-vision and low-vision filters.
- Compare raw HTML with the rendered DOM to find what JavaScript adds or changes.
- Measure Core Web Vitals and see a loading waterfall and performance budgets.
- Check metadata, headings, schema, robots.txt and every sitemap.
- Write your own selector rules and run them on every audit.
- Arrange sections into a saved workspace layout (Advanced).
- Reopen past runs, compare two versions of the same site, and keep a copy in your account.
- Export JSON, HTML, PDF, CSS, CSV and Markdown reports, or share a link that re-runs the audit.

## In this folder

- [docs/](docs/README.md) — how to use the Analyzer
  - [Getting started](docs/getting-started.md) — open it, the screen tour, your first audit
  - [Run an analysis](docs/run-an-analysis.md) — what happens when you select Analyze, and how pages are reached
  - [Choose what to scan](docs/choose-what-to-scan.md) — the 13 checks, the scan picker and what a run costs
  - [Scan a whole site](docs/scan-a-whole-site.md) — site scan settings, progress and paged results
  - [Arrange the workspace](docs/arrange-the-workspace.md) — panels, sections, layouts and Focus
  - [Read the Overview and scores](docs/read-the-overview-and-scores.md) — the score, grades, weights and issue cards
  - [The accessibility engine](docs/accessibility-engine.md) — every view of the A11y+ panel
  - [Accessibility rules](docs/accessibility-rules.md) — all 126 rules, category by category
  - [Colour, contrast and vision](docs/colour-contrast-and-vision.md) — Contrast, Palette, Simulation, Before / After
  - [Performance, SEO and page health](docs/performance-seo-and-page-health.md) — Performance, SEO, Media, Deep, Devices, Security, Project, Site Map, Insights
  - [Fix and preview](docs/fix-and-preview.md) — Fixes, Playground, Rules and CSP Setup
  - [Save, reopen and compare](docs/save-reopen-and-compare.md) — the library, Workspace, Compare and your account
  - [Export and share](docs/export-and-share.md) — every export format and share link
  - [Reference](docs/reference.md) — every control, option and output
  - [Troubleshooting](docs/troubleshooting.md) — symptom, cause and what to do
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material
  - [Glossary](others/glossary.md)
  - [Keyboard shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools and reading](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
