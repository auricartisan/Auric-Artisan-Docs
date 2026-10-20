---
title: Analyzer — Performance, SEO and page health
description: What the Performance, SEO, Media, Deep, Devices, Security, Project, Site Map and Insights sections measure, and how to read them.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Performance, SEO and page health

Beyond accessibility and colour, the Analyzer checks how fast the page is, how search engines see it, what JavaScript changes, how it copes with small screens, which security headers it sends, and how it fits into the rest of the site. This guide covers each of those sections. Most are available in Advanced mode only; **Project**, **Site Map** and **Insights** are also in Simple mode.

Every scored section has a **Why this score?** box, built like the one in the Overview, that explains its formula, what moved the score and the top recommendations. See [Read the Overview and scores](read-the-overview-and-scores.md).

## Performance

A Lighthouse-style audit built from the page's HTML, CSS, JavaScript, assets, DOM size and layout stability, and from real browser timing when it is available.

### What it shows

| Block | What it shows |
| --- | --- |
| Score and one-line verdict | For example "Fast, stable, and well within most budgets." |
| **Data Source** | Whether scores use real browser timing or estimates |
| **Performance Context** | Critical performance issues, acceptable architecture patterns, and the real-world load time |
| **Quick Wins** | The first changes to make |
| Sub-scores | **Loading**, **Interactivity**, **Visual Stability**, **Asset Weight**, **Maintainability** |
| **Browser Timing** | DOM content loaded, load event, transfer size and number of resources |
| **Top Performance Priorities** | Ranked issues with impact and fix |
| Page totals | Weights, scripts, stylesheets, CSS rules, DOM nodes and depth, images, iframes, third-party origins |
| **File-Level Assets** | Every script and stylesheet: blocking or not, origin, format, size, impact and fix |
| **Performance Budgets** | Pass or fail against fixed budgets (below) |
| **Performance Findings** | Each finding with why and fix |
| **Loading Timeline / Waterfall** | An estimated load order marking TTFB, FCP, LCP and page complete; red bars block rendering |
| **Asset Dependency Graph** | Every asset, grouped by type and origin |
| **Structural Analysis** | Repeated templates, template inconsistencies, z-index conflicts and layout-break risks |
| **Generated Performance CSS** | A small stylesheet of safe improvements, such as a visible focus style and responsive images |

### Performance budgets

| Budget | Limit |
| --- | --- |
| HTML weight | 250 KB |
| CSS weight | 160 KB |
| Inline JS | 120 KB |
| DOM size | 1,500 nodes |
| DOM depth | 32 levels |
| Blocking scripts | 2 |
| Image dimensions | 0 missing |
| Third-party origins | 8 |

### Core Web Vitals

Core Web Vitals are Google's measures of loading, visual stability and responsiveness. The Analyzer reports six metrics. They are shown in the **Insights** section, in a card headed **Core Web Vitals** followed by where the numbers came from: "(measured · lab)" when your browser measured them, "(measured · backend lab)" when a server browser did, or "(lab estimates)" when they were estimated from the page's size and structure.

| Metric | Good | Needs improvement | Poor |
| --- | --- | --- | --- |
| Largest Contentful Paint (LCP) | up to 2,500 ms | up to 4,000 ms | over 4,000 ms |
| Cumulative Layout Shift (CLS) | up to 0.10 | up to 0.25 | over 0.25 |
| Interaction to Next Paint (INP) | up to 200 ms | up to 500 ms | over 500 ms |
| First Contentful Paint (FCP) | up to 1,800 ms | up to 3,000 ms | over 3,000 ms |
| Time to First Byte (TTFB) | up to 800 ms | up to 1,800 ms | over 1,800 ms |
| Total Blocking Time (TBT) | up to 200 ms | up to 600 ms | over 600 ms |

The card's score is the share of metrics in the good range. Where it can, it names the element responsible (for example the LCP image) and the likely causes. When vitals are measured, the Performance score is capped by them, so a page cannot score 100 while its vitals are poor.

**Network Simulation** lets you re-estimate the numbers for **Fast 4G**, **Slow 4G**, **Fast 3G**, **Slow 3G** or **Offline**. It changes estimated values only, not measured ones, and your choice is remembered in this browser.

All of these are lab numbers from one load, not data from real visitors.

## SEO

Search-engine readiness: meta tags, headings, structured data, indexing, links, content depth and keyword distribution.

| Block | What it shows |
| --- | --- |
| Score | 100 minus weighted deductions per failed check (critical −14, medium −7, minor −3) |
| **Indexability** | Robots meta, whether the page is indexable and followable, and the canonical URL |
| **Content** | Word count, title length and meta description length |
| **Deep SEO Analysis — Raw + Rendered** | Raw and rendered SEO scores, **SEO Delta Score**, **Crawler Confidence**, **Dynamic SEO Risk** |
| **Dynamic SEO Detection** and **Dynamic SEO Flags** | Whether the title, description, canonical, robots, Open Graph tags, JSON-LD or H1 only appear after JavaScript runs |
| **Raw vs Rendered SEO** | Each field before and after rendering, marked stable or changed |
| **Raw/Rendered Check Matrix** | Around 27 checks, each pass or fail in the raw HTML and the rendered page |
| **SEO Checks** | 15 pass-or-fail checks, listed below the table |
| **Top SEO Priorities** | Ranked fixes |
| **Sitemap & Robots Discovery (hyper-detailed)** | robots.txt rules, every sitemap found, and **All discovered URLs**; **Re-probe** checks again |
| **Structured Data (JSON-LD)** | Blocks found, valid and invalid, and schema types |
| **Top Keywords (content density)** | The most frequent terms with counts and share |
| **SEO Findings** | Each finding with its fix |
| **SEO vs Competitor Archetypes** | Your SEO, performance and accessibility scores beside reference averages by site type |
| **Technical SEO** | Title, meta description, canonical, viewport, language, charset, robots |
| **Asset SEO** | Images, missing alt, decorative images, bad file names, heavy formats, below-the-fold images not lazy-loaded |
| **URL Quality** | Slug, slug length, lowercase, hyphens, path segments, query parameters |
| **Content Quality** | Word count, sentences, average words per sentence |
| **Schema (JSON-LD) Validation** | Types found, errors, and recommended types that are missing |
| **Crawl Quality** | Internal and external links, broken anchors, malformed links, H1 count, URL depth, duplicate headings, indexability |

The 15 **SEO Checks** are: title present, title length 30–65, meta description, canonical URL, lang attribute, viewport meta, Open Graph title, Open Graph image, robots not noindex, single H1, heading order, structured data (JSON-LD), internal links, content depth (at least 300 words) and descriptive link anchors.

Sitemap discovery reads robots.txt (user agents, allow and disallow rules, crawl delay and sitemap references) and every sitemap and sitemap index it finds, then lists every URL with a filter.

The competitor archetypes are fixed reference figures that the panel describes as industry averages based on HTTP Archive data. They are for orientation, not a live ranking.

## Media

Element-level detail for every image, video and audio file.

- Counts of **Images**, **Videos** and **Audio**.
- **Media Interpretation**: priority and LCP candidates, decorative images, and the alt-text model (missing alt is a real problem; empty alt is treated as decorative when the image is not content).
- **Media Checks**: images have alt decisions, images reserve layout space, autoplay control, visible controls, captions for video, audio transcripts.
- For each item: source URL, file size, dimensions, loading behaviour, alt text or captions, selector, parent, DOM path and layout impact.
- **Top Media Priorities**.

A page with no media says "No media assets detected" and is not scored for media.

## Deep

The **Deep Analyzer** compares the raw HTML the server sends with the DOM after JavaScript has run. Use it to find content, metadata or links that only exist after rendering, which some crawlers and assistive technologies may miss.

| Block | What it shows |
| --- | --- |
| Headline | Score, rendering classification (for example "Static HTML / progressively enhanced") and detected framework |
| **Rendering** | Mode, confidence, framework, DOM delta, whether content and SEO are in the raw HTML |
| **Page Size** | Raw HTML against rendered DOM: size, nodes, words, scripts and media |
| **SEO Generation** | How metadata is produced, and the canonical |
| **Accessibility Signals** | Live regions, dialogs, canvases with no fallback, hidden focusable elements |
| **Raw HTML Summary (Pre-JS)** | Metadata, social tags, schema, semantics, forms, media, scripts, fonts and hydration signals |
| Completeness checks | 13 raw SEO, 11 raw accessibility and 20 deep HTML quality checks, each with a fix |
| **Rendered DOM Analysis (Post-JS)** | Rendered SEO fields, headings, links, controls, media, hydrated content and a text sample |
| **Framework Detection** | The detected framework with evidence and confidence |
| **Detected Script Tools** | Analytics, tag managers, ads, chat, replay, A/B testing, consent, bundles, routers and more |
| **Execution Risks** | Large bundles, inline event handlers, suspicious script URLs, mixed-content scripts |
| **Third-Party Hosts** and **Script Loading Order** | Where scripts come from, and loading-order warnings |

## Devices

The **Responsive Design Analyzer** checks viewport metadata, fixed-width risk, image dimensions and interactive density across common device profiles. This section never opens by itself after a run; open it from the Sections picker.

### Device profiles

Each profile gets a score and a risk level. Select one to test it in the Device Lab.

| Profile | Size (CSS pixels) | Profile | Size (CSS pixels) |
| --- | --- | --- | --- |
| Small phone | 320 × 568 | iPad landscape | 1024 × 768 |
| Android small | 360 × 640 | iPad Pro portrait | 1024 × 1366 |
| iPhone SE | 375 × 667 | iPad Air landscape | 1180 × 820 |
| iPhone 12/13 | 390 × 844 | HD laptop | 1280 × 720 |
| Android large | 412 × 915 | Laptop | 1366 × 768 |
| Phone Max | 428 × 926 | Desktop | 1440 × 900 |
| Fold compact | 540 × 720 | Wide desktop | 1536 × 864 |
| Small tablet | 600 × 960 | MacBook Pro | 1728 × 1117 |
| iPad portrait | 768 × 1024 | Full HD | 1920 × 1080 |
| iPad Air portrait | 820 × 1180 | QHD monitor | 2560 × 1440 |

The headline names the most broken device, for example "Most broken device: Small phone at 320 x 568. Risk: Low."

### Device Lab

The Device Lab shows the page at the chosen size, with **Auto**, **Live**, **Screenshot**, **Rotate** and **Fullscreen** buttons, and the usual preview controls. If the site blocks embedding, the same **Couldn't embed this page** overlay appears as in Simulation.

**Live custom CSS** lets you type CSS that is applied to the preview as you type, with no reload. Use **Import page CSS**, **Format**, **Clear**, **Copy** and **Export** (downloads `device-custom.css`). The text is stored locally for the session, and the last edit is re-applied.

### Device Screenshot Wall

**Capture all devices** renders the page in a real headless browser on Auric Artisan's servers at every device size, with full-page captures and measured overflow, tap-target and text-size checks. It works even when the site blocks embedding. Capturing another site needs you to be signed in, and server captures are metered in tokens.

> **Note:** On a page that blocks embedding, the Device Lab starts server-rendered captures by itself a few seconds after it opens. That is why the Devices section is never opened for you automatically.

**Responsive Signals** sums up: viewport meta, touch target inventory, fixed-width risk, image dimensions and render-blocking scripts.

## Security

The **Security Policy** section checks HTTPS, the Content-Security-Policy, framing, referrer and permissions policies, MIME sniffing, link reliability and server timing.

It shows a **Security** score, a **Reliability** score and the number of **Broken Links**, then these checks, each ticked or crossed with a fix:

| Check | What passes |
| --- | --- |
| HTTPS | The page is served over HTTPS |
| Strict Transport Security | An HSTS header is sent |
| Content Security Policy | A CSP header is sent |
| CSP default source | The CSP includes `default-src` |
| CSP object restriction | The CSP includes `object-src 'none'` |
| Frame protection | CSP `frame-ancestors` or `X-Frame-Options` is set |
| Referrer policy | A referrer policy is set |
| Permissions policy | A permissions policy is set |
| MIME sniffing protection | `X-Content-Type-Options: nosniff` is sent |
| Cross-origin isolation policy | COOP, CORP or COEP is set where compatible |
| No mixed content | No insecure resources on a secure page |
| Safe new-tab links | New-tab links carry `rel="noopener"` |
| Secure forms | Forms submit securely |
| Inline script surface | Inline script use is limited |

**Environment-Aware Scoring** notes when the page is on a local development server; HTTPS and deployment-only headers are then scored more gently, and the raw score is shown beside the adjusted one. **Code-Level vs Server-Level** separates findings you fix in your code from those you fix in server configuration. **Reliability & Stability** lists links checked, internal and external links, broken links and wall time. **Detected Policy** shows the Content-Security-Policy, Permissions-Policy and Referrer-Policy the page actually sent.

The security score checks whether protective headers are present, not how good they are.

## Project

The **Unified Project Model** is one shared model for every section: pages, links and the sitemap are discovered once and reused, so totals stay consistent and shared files are counted once.

- **Project**: URL, origin, source, pages in the model and when it was scanned. **Export project model JSON** downloads it as `project-model-<date>.json`.
- **Shared Entities**: tiles for pages, stylesheets, scripts, fonts, images, media items, colours, contrast pairs, schema objects, classes, IDs and dependencies. Select a tile to open the section that owns it.
- **Page Discovery vs Scan**: discovered, scanned (completed), failed, not yet scanned, and duplicate URLs removed.
- **Findings by Module** and **Unified Findings (cross-linked)**: every finding with the section it belongs to.

## Site Map

The **Full Site Map** crawls the site, builds a project tree, and shows which CSS and JavaScript files connect to which pages, with each shared file listed once and a "used on N pages" count.

| Block | What it shows |
| --- | --- |
| **Crawl & Map** | **Crawl Full Site**, **Cancel**, **Pages** (1 to 500, default 60) and **Workers** (1 to 8, default 4) |
| **Resources (deduped)** | Unique stylesheets, scripts, font files, images and external files; duplicate references collapsed |
| **Design tokens (deduped)** | Unique colours, font families, classes, and IDs reused across pages |
| **Export map JSON** | Downloads the map as `site-map-<date>.json` |
| **Project Tree** and **Page Map** | Files and pages as folders |
| **Dependency Graph** | An interactive graph of pages and files (controls below the table) |
| **Page → CSS & JS Connections** | Each page with its stylesheets and scripts |
| **Dependency Chains** | Full CSS `@import` and JavaScript import trees, filled in by a crawl |
| **Stylesheets → Pages & imports**, **Scripts → Pages & imports**, **Images → Pages** | Each file with the pages that use it |
| **Site-wide Findings (merged)** | Findings that repeat across pages, with the pages they appear on |

The **Dependency Graph** has three layouts, **Radial**, **Force** and **Grouped**; check boxes to show or hide **Pages**, **CSS**, **JS**, **Fonts** and **All labels**; a search field ("Find a file or page…"); and zoom in, zoom out, **Fit**, **Reset** and full-screen buttons. Select a node to highlight what connects to it, drag nodes to rearrange them, and scroll to zoom.

**Crawl Full Site** is available when the audited page is on auricartisan.com, or when the run used Auric Artisan's servers. For another website otherwise, the button is disabled with the hint "Cross-origin page — use Scan Site (backend) instead". The token meter prices a site-map crawl at one token for the whole job, not per page.

## Insights

**Smart Insights** is an overview of the whole report written for decision-makers: a summary, prioritised fixes, a fix simulator, a benchmark percentile and progress over time.

| Block | What it shows |
| --- | --- |
| Health | A health score, a tier, a percentile ("Better than N% of audited sites") and a UX score |
| **Headlines** | Two or three plain sentences about the result |
| **Benchmark Breakdown** | Your percentile per category against a reference median |
| **vs. Competitor Archetypes** | Reference scores by site type, each marked "you beat this" or "below this" |
| **Share Report** | **Copy share link** and **Email** |
| **Top 5 Things to Fix First** | Each with **Plain language**, **Developer view**, **Suggested fix** and an estimated score gain |
| **Priority Engine** | A ranked table: issue, severity, impact, effort, business impact, UX and revenue |
| **Core Web Vitals** | The six vitals (see Performance above) and **Network Simulation** |
| **Fix Simulator** | Tick fixes to see the projected score change as you go |
| **Progress Over Time** | Your past runs of this URL |

The benchmark and archetype figures are fixed reference values for orientation. They are not a live comparison with other sites.
