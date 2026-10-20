---
title: Analyzer — Getting started
description: Open the Analyzer, learn what each part of the screen does, and run your first audit.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Getting started with the Analyzer

This guide takes you from opening the Analyzer to reading your first result. It takes about five minutes.

## Open the Analyzer

Go to https://auricartisan.com/tool/analyzer/, or open the **Tools** menu in the site header and select **Analyze URLs**.

You do not need an account to audit a page on auricartisan.com. To audit another website you need to be signed in, because that page is rendered on Auric Artisan's servers. See [Run an analysis](run-an-analysis.md) for the details.

## The screen, top to bottom

### The masthead

The top of the page names the tool: the kicker "Auric Artisan · Analyzer", the headline "One URL, audited seven ways.", and a line explaining that accessibility, metadata, palette, contrast, performance, reliability and security are all checked against the page's own markup. Under it, a thin rail lists **WCAG 2.1 / 2.2** and **LCP · CLS · INP**, with a link, **Read the API reference**, to the public API documentation.

### The API hint

A one-line note may appear under the masthead: "Automate this — 12 API credits per call to `POST /v1/analyzer/inspect`." It tells developers that the same kind of audit is available from the REST API, and that API credits are a separate balance from your tool tokens. Select **API docs** to open that endpoint's documentation, or the **×** button to dismiss the note. Dismissing it hides the hint on every tool page in this browser.

### The strip

The dark strip is where you work. From left to right:

| Control | What it does |
| --- | --- |
| URL field | Where you type or paste the address to audit. The placeholder reads "Enter a URL to analyze…" in Simple mode. |
| **Analyze** | Starts the audit. Pressing `Enter` in the URL field does the same. |
| **Cancel** | Appears only while an audit or site scan is running. Stops it. |
| **Share** | Copies a link that opens the Analyzer on the same URL and re-runs the audit. |
| **Sections** and **Layouts** | Advanced mode only. Open the section picker and the saved-layout menu. |
| **Simple** / **Advanced** | Switches mode. Your choice is remembered in this browser. |

In Advanced mode two folding rows appear under the strip: **What to scan**, which lets you choose the checks and shows their cost, and **Site scan settings**, which holds the whole-site scan controls.

### The run line

Under the strip is one line that shows where the run is and what it costs:

- The **progress rail** has five steps: **1 Analyze**, **2 Issues**, **3 Fix**, **4 Preview** and **5 Export**. It lights up as a run moves on. Each step is also a button: **Fix** shows the Fixes section, **Preview** shows Before / After, **Export** shows Report, and **Analyze** and **Issues** show the Overview.
- The **token meter** shows **This run** (the cost of the next run in tokens) and **Remaining** (your balance). When you are signed out it says "Sign in to claim 100 free tokens." with a **Sign in · 100 free tokens** button. Select the meter to open a sheet that explains the price. See [Choose what to scan](choose-what-to-scan.md).

### The search bar

After the first run, a **Search results** bar appears with the placeholder "Filter issues, fixes, files, media, rules…". Typing filters the cards and rows in the open sections. **Clear** empties it.

### The workspace

Below everything is the workspace: a grid of panels, one per section of the report. Before your first run it holds only the **Overview** panel, which lists what a run will give you:

- Accessibility, against WCAG 2.1 and 2.2, with the rule each finding breaks
- Every text pair that fails contrast, and a passing colour to replace it
- How the page looks with colour-vision and low-vision filters on
- The palette, the type, and every image, video and audio file
- Rendered DOM against raw HTML: framework, SEO signals, what JavaScript wrote
- Core Web Vitals, security headers, broken links, and a report you can export

Each panel has a title bar with a grip (drag it to move the panel) and four buttons: **Width**, **Focus**, **Collapse** and **Close**. See [Arrange the workspace](arrange-the-workspace.md).

## Simple or Advanced?

| | Simple | Advanced |
| --- | --- | --- |
| Sections you can open | 8: Overview, Project, Insights, Site Map, Contrast, Fixes, Compare, Report | All 22 |
| Checks that run | A fixed set (see below) | Your choice of 13, from the **What to scan** picker |
| Opening more sections | `Ctrl` + `P`, or the progress-rail steps | The **Sections** button, or `Ctrl` + `P` |
| Saved layouts | No menu (your arrangement is still remembered) | **Layouts** menu with ready-made and named layouts |
| Whole-site scan | Not available | **Site scan settings** |
| Custom rules, Playground, CSP Setup | Not available | Available |

Simple runs these checks: page structure (always), Project model, Colour contrast, SEO and metadata, Site map, Accessibility and Responsive behaviour. Some of these feed the score without having a section in Simple mode.

Switching mode does not re-run anything. Each mode remembers its own panel arrangement.

## Run your first audit

1. Select **Simple** in the strip if it is not already selected.
2. Select the URL field and type `https://auricartisan.com/tool/contrast-checker/`. Any auricartisan.com page works without an account.
3. Select **Analyze**.
4. Watch the Overview panel. A card titled **Auditing** shows a live line ("Opening the page…", "Reading the page…", "Checking the page against the accessibility rules…") and a list of the steps this run is doing, each ticked off as it finishes.
5. When the run ends, the progress rail moves to **2 Issues** and the workspace opens the sections your checks filled. In Simple mode that is **Overview** across the full width, then **Project**, **Contrast** and **Site Map**.
6. In the Overview panel, read the large score and the **Overall Audit Score** grade.
7. Open **Why this score?** under the score to see which categories cost points.
8. Scroll to **Top 3 Things To Improve Score**. Each card gives the estimated points it is worth, why it matters, and the fix.
9. Press `Ctrl` + `P`, select **Fixes**, and read the **Fix This First** list.

The result: you have a score, a ranked list of what to fix, and the code for each fix. The run is also filed in your browser, so it appears in **Compare** and in the library the next time you open the Analyzer.

## Where to go next

- [Read the Overview and scores](read-the-overview-and-scores.md) to understand the numbers.
- [The accessibility engine](accessibility-engine.md) to work through accessibility findings in Advanced mode.
- [Export and share](export-and-share.md) to keep a copy or send the result to someone.
