---
title: Analyzer — Reference
description: Every control, option, section, input and output of the Analyzer in one place.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Analyzer reference

A complete list of the Analyzer's controls and outputs. Each entry links to the guide that explains it in more depth.

## Page elements

| Element | What it does |
| --- | --- |
| Masthead | The headline "One URL, audited seven ways.", a lede, and a rail with **Read the API reference** |
| API hint | The REST API equivalent and its price in API credits; dismissing it hides it on every tool page |
| **Save this run** | The site-wide library button, fixed at the bottom right |

## The strip

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| URL field | The address to audit | Any http or https address, a bare host name, or a path on auricartisan.com | Empty |
| **Analyze** | Starts a single-page audit. `Enter` in the URL field does the same. | Button | — |
| **Cancel** | Stops the running audit or site scan | Shown only while running | — |
| **Share** | Opens the share dialog with a link that re-runs the audit | Button | — |
| **Sections** | Opens the Sections picker. Shows `Ctrl` + `P`. | Advanced only | — |
| **Layouts** | Opens the layout menu | Advanced only | — |
| **Simple** / **Advanced** | Switches mode; remembered in this browser | Simple, Advanced | Simple |

URL field placeholder: "Enter a URL to analyze…" (Simple) or "Enter a URL for deep DOM, SEO, contrast & accessibility audit…" (Advanced). See [Run an analysis](run-an-analysis.md).

## What to scan (Advanced)

The row's heading reads "What to scan · N of 13 · N tokens". See [Choose what to scan](choose-what-to-scan.md).

| Control | What it does | Default |
| --- | --- | --- |
| 13 check boxes | One per switchable check (listed below) | All on |
| **Everything** | Turns every check on | — |
| **The fast three** | Keeps only Page structure, Colour contrast and SEO and metadata | — |

The 13 checks are Project model, Colour contrast, Before / After, Accessibility, Palette, Vision simulation, SEO and metadata, Media, Performance, Responsive behaviour, Deep DOM and framework, Security and reliability, and Site map.

Page structure always runs. Simple mode always runs Page structure, Project model, Colour contrast, SEO and metadata, Site map, Accessibility and Responsive behaviour.

## Site scan settings (Advanced)

See [Scan a whole site](scan-a-whole-site.md).

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Scan Site** | Starts a whole-site scan | Button | — |
| **Robots** | Follow robots.txt rules | On, off | On |
| **Subdomains** | Include subdomains | On, off | Off |
| **Pages** | Pages to audit, with a time estimate | 1–24 | 10 |
| **Show** | Rows per page of detailed results | 25, 50 | 25 |
| **Workers** | Concurrent scan workers | 1–20 | 3 |
| **Public proxy** | Fetch cross-origin pages through third-party public CORS proxies | On, off | Off |

## The run line

| Element | What it does |
| --- | --- |
| **1 Analyze** | Progress step; shows the Overview |
| **2 Issues** | Progress step; shows the Overview |
| **3 Fix** | Progress step; shows Fixes |
| **4 Preview** | Progress step; shows Before / After |
| **5 Export** | Progress step; shows Report |
| **This run** | The quoted cost of the next run, in tokens, with "+2 more if the page blocks embedding" when a render may be needed |
| **Remaining** | Your token balance |
| **Sign in · 100 free tokens** / **Claim 100 free tokens** / **See plans** | Account actions shown when they apply |
| Token meter (select it) | Opens the token sheet: **Where you stand**, **Why**, **What would fit**, **Lately** |

## Search results

| Control | What it does |
| --- | --- |
| **Search results** field | Filters cards and rows in open sections; shown after the first run |
| **Clear** | Empties the field |

## Workspace controls

See [Arrange the workspace](arrange-the-workspace.md).

| Control | What it does |
| --- | --- |
| Panel grip | Drag to move; `Left` / `Right` when focused |
| **Width** | Third, half or full row |
| **Focus** | Show only this panel; select again to restore |
| **Collapse** / **Expand** | Fold to the title bar |
| **Close** | Remove the panel |
| Sections picker | A filter field and three groups: **On screen**, **Ready to open**, **Not scanned** |
| Layouts menu | Ready-made, saved and kept layouts; **Save** a name; **Reset to the default layout** |

Ready-made layouts: **Accessibility review**, **Colour and vision**, **Speed and weight**, **Content and search**, **Everything, thin**.

## Sections

| Section | Simple | Advanced | Filled by | Contents |
| --- | --- | --- | --- | --- |
| Overview | Yes | Yes | Page structure (always) | Score, grade, categories, statistics, issue cards |
| Project | Yes | Yes | Project model | Shared entities, discovery, findings by module |
| Palette | No | Yes | Palette | Extracted colours, CVD previews, generated palettes |
| Contrast | Yes | Yes | Colour contrast | Every text pair, ratios, suggested colours |
| Performance | No | Yes | Performance | Sub-scores, budgets, assets, waterfall |
| SEO | No | Yes | SEO and metadata | Meta, raw versus rendered, sitemap, schema, keywords |
| A11y+ | No | Yes | Accessibility | The 126-rule engine and its views |
| Insights | Yes | Yes | Always available | Summary, benchmarks, priority engine, Core Web Vitals, fix simulator |
| Media | No | Yes | Media | Images, video and audio in detail |
| Deep | No | Yes | Deep DOM and framework | Raw HTML against rendered DOM |
| Site Map | Yes | Yes | Site map | Crawl, project tree, dependency graph |
| Simulation | No | Yes | Vision simulation | Page under colour-vision and low-vision filters |
| Devices | No | Yes | Responsive behaviour | Device profiles, Device Lab, screenshot wall |
| Security | No | Yes | Security and reliability | Header checks, links, detected policy |
| Playground | No | Yes | Always available | Element editor, palette generator, design lab |
| Fixes | Yes | Yes | Always available | Fix list, fix mode, heuristic auto-fix |
| Before / After | No | Yes | Before / After | Original and fixed previews |
| Rules | No | Yes | Always available | Custom selector rules and templates |
| Workspace | No | Yes | Always available | Saved projects, history, palettes, monitoring |
| Compare | Yes | Yes | Always available | Two saved versions side by side |
| CSP Setup | No | Yes | Always available | Server headers to allow embedding |
| Report | Yes | Yes | Always available | Full report and exports |

Section badges show finding counts on **Contrast**, **SEO**, **A11y+** and **Fixes**.

## A11y+ views

| Group | View | Contents |
| --- | --- | --- |
| Overview | Overview | Grade, conformance line, severity, categories, quick wins, reading level, backlog |
| Findings | Issues | Every failing or needs-review rule, with filters **Impact**, **Area**, **Level** and search |
| Findings | Fixes | Fix groups, confidence, the ready-to-paste CSS patch |
| Inspect | Widgets | Eight ARIA widget patterns checked |
| Inspect | Annotations | Errors, Contrast errors, Alerts, Features, Structural elements, ARIA |
| Inspect | A11y tree | The accessibility tree |
| Inspect | Screen reader | Transcript, rotor lists, speech |
| Inspect | Vision | Pairs under four colour-vision deficiencies, with APCA Lc |
| Inspect | Focus & targets | Tab order and target sizes |
| Report | Conformance | WCAG 2.2 verdict, scorecard, VPAT-style table |
| Report | Export | Five exports and run metadata |

See [The accessibility engine](accessibility-engine.md) and [Accessibility rules](accessibility-rules.md).

## Issue card statuses

| Status | Effect |
| --- | --- |
| **Open** | Default; still to do |
| **Fixed** | Marked as fixed |
| **Ignore** | Marked as accepted |
| **Recheck** | Marked, and the audit runs again at once |

## Scores and thresholds

| Item | Value |
| --- | --- |
| Overall and section grade bands | A+ 90–100, A 80–89, B 70–79, C 55–69, D 40–54, F 0–39 |
| A11y+ engine grade bands | A+ 95–100, A 90–94, B 80–89, C 70–79, D 55–69, F 0–54 |
| Category weights, first five | Accessibility 20%, contrast 16%, performance 13%, deep analysis 10%, metadata 9% |
| Category weights, last five | Responsive 8%, visual quality 8%, reliability 7%, security 7%, media 2% |
| Contrast thresholds | 4.5:1 normal text, 3:1 large text and UI, 7:1 and 4.5:1 enhanced |
| Large text | 24px, or 18.66px bold |
| Target size | 24 × 24 CSS px (AA), 44 × 44 CSS px (AAA) |
| Core Web Vitals, good | LCP ≤ 2,500 ms, CLS ≤ 0.10, INP ≤ 200 ms, FCP ≤ 1,800 ms, TTFB ≤ 800 ms, TBT ≤ 200 ms |

## Limits

| Limit | Value |
| --- | --- |
| Pages per site scan | 24 |
| Site Map crawl pages | 1–500 (default 60), 1–8 workers (default 4) |
| Saved copy of a page for fallback | Kept 7 days in this browser |
| History list in Workspace | 50 entries |
| Free plan URL analyses | 20 a month |
| Free plan saved projects | 20 |
| Layout names | 40 characters |
| Automatic kept layouts | The newest 3 |

## Links you can build

| Link | Effect |
| --- | --- |
| `https://auricartisan.com/tool/analyzer/?url=<address>` | Opens the Analyzer and audits the address |
| A **Share** or **Share Link** link | Opens the Analyzer and re-runs the audit of the shared address |

## Remembered in this browser

- Simple or Advanced mode, and each mode's panel arrangement
- Saved layouts and the three newest automatic ones
- Which checks are ticked in **What to scan**
- **Fix Mode** (Safe or Aggressive)
- The **Public proxy** choice
- The Network Simulation profile
- Issue statuses (Open, Fixed, Ignore, Recheck)
- Custom rules
- Every run's report, versions, palettes and history (see [Save, reopen and compare](save-reopen-and-compare.md))
- A copy of each audited page for up to 7 days, used as a last-resort fallback
- Whether you dismissed the API hint

For exports and file names, see [Export and share](export-and-share.md).
