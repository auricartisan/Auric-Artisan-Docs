---
title: Analyzer — FAQ
description: Short answers to the questions people most often ask about the Analyzer.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Analyzer FAQ

## Is the Analyzer free?

Yes. The tool, every section and most exports are free. Work that runs on Auric Artisan's servers is metered: auditing another website (rendered on a server), whole-site scans, and server screenshots. Signed-in accounts can claim 100 free tokens, and the free plan includes 20 server-side URL analyses a month. PDF export is a paid Pro export, and the VPAT-shaped conformance CSV is a Specialist-plan perk. See [Choose what to scan](choose-what-to-scan.md).

## Do I need an account?

Not to audit pages on auricartisan.com. To audit another website you need to be signed in, because your browser is not allowed to read another site's pages directly; the page is rendered on Auric Artisan's servers instead.

## Can I audit a page on my computer, or on a company intranet?

Generally no. The server scanner refuses private and local addresses such as `localhost` and `192.168.x.x`, and your browser cannot read another origin's pages unless that server explicitly allows it. Put a copy of the page somewhere publicly reachable, such as a staging site.

## What is the difference between Simple and Advanced?

Simple shows 8 sections and runs a fixed set of checks. Advanced shows all 22 sections, lets you choose which of 13 checks run, and adds site scanning, the Playground, custom rules, saved layouts and CSP Setup. The audit itself is the same quality in both. See [Getting started](getting-started.md).

## How many accessibility rules does it check?

126 rules, mapped to WCAG 2.0, 2.1 and 2.2 success criteria, Section 508 and EN 301 549, plus checks for eight ARIA widget patterns. See [Accessibility rules](accessibility-rules.md).

## Does a good score mean my site is accessible, or legally compliant?

No. Automated testing proves failures; it rarely proves success. Some WCAG criteria cannot be checked by software at all, and they are shown as untested rather than passed. A clean report is strong evidence that you have done the automatable work, not a certificate. For a conformance claim you need manual review as well; the [Accessibility Checklist](../../accessibility-checklist/README.md) helps with that.

## Why does another tool score my page 100 when the Analyzer does not?

The tools measure different things. The Analyzer checks more criteria than many automated tools, counts "needs review" results instead of treating them as passes, weights findings by severity and by how many elements they affect, and measures the page as rendered. Compare individual findings instead: when two tools disagree about one element and one rule, look at the element.

## Why are there two different grade scales?

The overall score and each section use one set of bands (A+ from 90). The accessibility engine in A11y+ uses a stricter scale (A+ from 95, F below 55), because its score is meant to track WCAG conformance closely. See [Read the Overview and scores](read-the-overview-and-scores.md).

## What does "needs review" mean?

The rule ran and could not decide, usually because the answer depends on something only a person can judge, such as text over a photograph. It costs a little in the accessibility score, less than a failure, because "we could not tell" is not evidence that something is fine.

## What is APCA Lc, and does it affect my score?

APCA is a newer model of perceived contrast being developed for a future version of WCAG. Lc is its lightness contrast value. The Analyzer shows it beside the WCAG ratio for reference only; it never affects a pass, a fail or a score. See [Colour, contrast and vision](colour-contrast-and-vision.md).

## Can I scan my whole site?

Yes, on the Artisan plan and above, up to 24 pages per run. See [Scan a whole site](scan-a-whole-site.md).

## Where are my results stored?

In your browser on this device. Every run is filed as a version of its site, with the full report, so you can reopen and compare it. Nothing is uploaded unless you choose **Keep in my account** in Compare. See [Save, reopen and compare](save-reopen-and-compare.md) and [Privacy](../others/privacy.md).

## Can I compare before and after a fix?

Yes. Run the page, fix something, run it again, then open **Compare**. It shows what was fixed (**Gone**), what appeared (**New**) and what stayed.

## Can I share a report with someone who has no account?

A share link re-runs the audit for the recipient, so they need what the audit needs: an account if the page is on another website. To send the results themselves, export **Export HTML**, **Client Report** or **Export PDF** and send the file.

## Why does `Ctrl` + `P` not print?

While the Analyzer is open, `Ctrl` + `P` opens its Sections picker. Use the exports in **Report** for a printable copy.

## Can I automate audits?

Yes, through the REST API. The API hint on the page names the endpoint and its price in API credits, which are a separate balance from tool tokens. See the public API documentation at https://auricartisan.com/library/documentation/api/.

## Why do some sections say the page could not be embedded?

The site forbids other sites from showing it in a frame. Use **Run in browser** to open a captured copy in a pop-up window, or, for your own site, follow **CSP Setup**. See [Fix and preview](fix-and-preview.md).
