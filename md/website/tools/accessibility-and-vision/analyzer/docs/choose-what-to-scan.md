---
title: Analyzer — Choose what to scan
description: Pick which of the 13 checks run in Advanced mode, understand which sections each check fills, and read what a run costs in tokens.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Choose what to scan

A full audit runs every check the Analyzer has. You rarely need all of them. In Advanced mode you can switch checks off, which makes a run faster and can make it cheaper. In Simple mode the set of checks is fixed.

## The checks

One check, **Page structure**, always runs: it reads the page and its resources, and everything else is built on it. The other 13 can be switched on and off.

| Check | What it does | Fills the section | Notes |
| --- | --- | --- | --- |
| Project model | One deduplicated model of the page: resources, colours, media, schema, dependencies | Project | from Page structure |
| Colour contrast | Every text pair measured against WCAG, with a passing colour to replace it | Contrast | |
| Before / After | The page as it is beside the page with the contrast fixes applied | Before / After | from Colour contrast |
| Accessibility | The full rule engine: WCAG 2.1 and 2.2, the a11y tree, keyboard and screen-reader order | A11y+ | slow |
| Palette | Dominant colours and generated accessible palettes | Palette | |
| Vision simulation | The palette through colour-vision and low-vision filters | Simulation | from Palette |
| SEO and metadata | Title, description, headings, schema, robots, canonical, keyword density | SEO | |
| Media | Every image, video and audio file: size, dimensions, alt text, captions, loading | Media | |
| Performance | Core Web Vitals measured in your browser, bundle weight, network simulation | Performance | slow |
| Responsive behaviour | Viewport, breakpoints, tap-target sizes, fixed widths that will not fit a phone | Devices | |
| Deep DOM and framework | Rendered DOM against raw HTML, framework detection, what JavaScript wrote | Deep | slow |
| Security and reliability | Security headers, broken links, server stability | Security | |
| Site map | Discovers the rest of the site from robots.txt and the whole sitemap tree | Site Map | slow |

- **slow** marks the checks that take noticeably longer.
- **from …** marks a check that adds no measurement of its own and reads from another one. Ticking it turns its source on as well. Unticking the source turns off everything that reads from it.

Eight sections are never switched on or off, because they present what the checks found or what you saved: **Insights**, **Fixes**, **Playground**, **Rules**, **Workspace**, **Report**, **CSP Setup** and **Compare**. The **Overview** always has something, because Page structure always runs.

## What Simple mode runs

Simple mode has no picker. It always runs Page structure plus: Project model, Colour contrast, SEO and metadata, Site map, Accessibility and Responsive behaviour. Responsive behaviour and Accessibility count towards the overall score even though Simple has no Devices or A11y+ section to show them.

## Use the picker (Advanced)

1. Select **Advanced** in the strip.
2. Open the row under the strip that starts **What to scan**. Its heading shows how many checks are on and what they cost, for example "What to scan · 13 of 13 · 4 tokens".
3. Tick or untick checks. Ticking a check also opens its section in the workspace; unticking it closes that section.
4. Or use a shortcut button at the foot of the list:
   - **Everything** turns every check on.
   - **The fast three** keeps Page structure, Colour contrast and SEO and metadata, and turns the rest off.
5. Select **Analyze**.

Your choice is remembered in this browser for the next visit.

The notes at the foot of the picker repeat the rules: "4 checks to a token, rounded up. A blocked page adds the cost of rendering it on a server.", which section always runs, and which sections are always available.

## Sections whose check did not run

If you open a section whose check was switched off for the last run, it says that the check "was switched off for this run, so there is nothing measured to show here", with a **Turn it on and run again** button. The Analyzer never shows "no issues found" for a check that did not run.

Choosing such a section from the **Sections** picker has the same effect: its check is turned on and, if there is already a report, the audit runs again.

Categories whose check was switched off are also left out of the overall score, rather than counted as zero or as 100. The Overview says which categories were excluded.

## What a run costs

Tokens pay for work done on Auric Artisan's servers, such as rendering a page from another website in a real browser, or crawling a site. The token meter in the run line quotes the next run before you start it.

### The quote

- The chosen checks are priced at **four checks to a token**, rounded up, with a minimum of one token. Page structure is not counted.
- If the page blocks embedding and your checks need a live, rendered page, rendering it on a server adds **2 tokens**. The meter shows this as "+2 more if the page blocks embedding".
- Checks that only read the page's HTML never need a server render. A run made only of Project model, SEO and metadata, Responsive behaviour, Security and reliability and Site map costs the same whatever the page does. The meter's note then says so.

| Choice | Checks counted | Quote |
| --- | --- | --- |
| Everything | 13 | 4 tokens, +2 if the page blocks embedding |
| Simple mode's fixed set | 6 | 2 tokens, +2 if the page blocks embedding |
| The fast three | 2 | 1 token, +2 if the page blocks embedding |

The meter's **Remaining** figure is your balance. Signed-out visitors see "Sign in to claim 100 free tokens." and a **Sign in · 100 free tokens** button; signed-in accounts that have not claimed them see **Claim 100 free tokens**; **See plans** links to the pricing page.

### The token sheet

Select the token meter, or press `Enter` or `Space` while it has focus, to open a sheet that answers what the meter cannot. It has these parts:

- **Where you stand** — your balance and what this run would leave.
- **Why** followed by the cost — the lines that make up the price, such as "Reading the page, once" for one page, or "Finding the pages" plus a per-page line for a site scan. It notes that contrast, palette, media, accessibility and SEO run on your own machine and cost nothing, and that a token only ever buys work on a server. For a site scan it adds that tokens are "Held, not spent: you are charged for the pages that come back and refunded the rest."
- **What would fit** — what your balance still covers: another single page, a rendered snapshot, or a whole-site scan of a chosen size. A **Pages** stepper and a **Pages that block embedding** switch let you price a job before you run it. Pricing a job here does not change the run the **Analyze** button is about to make.
- **Lately** — your recent token activity, such as free tokens claimed or a monthly allowance added.

### Monthly analyses

Server-side URL analyses are also counted against a monthly allowance. The free Apprentice plan includes 20 URL analyses a month; the pricing page at https://auricartisan.com/company/pricing/ lists the allowance for each paid plan. When the allowance is used up, the Analyzer shows **You have used this month's scans**.

> **Note:** Auditing a page on auricartisan.com in your own browser does not need the server, so it works without an account. Vision simulations elsewhere on the site are not metered at all.

For plans, allowances and top-ups, see the account and billing docs in [Account and billing](../../../../account-and-billing/README.md).
