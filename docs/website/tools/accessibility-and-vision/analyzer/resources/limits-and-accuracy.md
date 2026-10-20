---
title: Analyzer — Limits and accuracy
description: What the Analyzer measures, how precisely, which pages it can reach, and what its results are not.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Limits and accuracy

The Analyzer gives you a short, specific, evidence-backed list of things that are wrong with a page. It does not certify a page, predict every visitor's experience, or replace a manual review. This page is honest about where the line is.

## What it measures

- **One page per run**, or up to 24 pages in a whole-site scan.
- **The page as it was at one moment.** Content that loads later, changes with an A/B test, or appears only after a user action may not be seen. A page part-way through an animation measures differently from a page at rest.
- **Lab results, not visitor data.** Performance figures come from one load in one browser, not from real visitors on real devices and networks.

## Which pages it can reach

| Page | Can it be audited? |
| --- | --- |
| Any page on auricartisan.com | Yes, in your browser, with or without an account |
| A public page on another website | Yes, when you are signed in: it is rendered in a real browser on Auric Artisan's servers |
| Another website, signed out | Only if that site allows cross-origin requests, or with **Public proxy** turned on, and then only from its HTML |
| A page behind a login, a bot challenge or a strict firewall | No. The scanner is refused, or receives a challenge page and declines to score it. |
| `localhost`, private network and link-local addresses | No. The scanner never visits private addresses. |
| Anything other than `http` and `https` | No |

When a page is read from its HTML rather than rendered, its scripts are removed first (apart from JSON-LD). Anything built by JavaScript is then missing.

## Accessibility

- **Automated coverage has a ceiling.** Of the 60 WCAG criteria the engine lists, 11 can never be checked automatically and always show as untested: Meaningful Sequence, Sensory Characteristics, Images of Text, No Keyboard Trap, Three Flashes, Pointer Cancellation, Motion Actuation, On Focus, Consistent Navigation, Consistent Identification and Redundant Entry.
- **A pass is not a good experience.** A link called "click here" has an accessible name; a heading order can be valid and meaningless.
- **Needs review is not a pass.** Text over images, gradients and video, and anything else the engine could not decide, is left for a person.
- **Level AAA and best-practice rules** run and are reported, but do not count in the accessibility score.
- **Hidden content is not judged**, apart from rules that exist to check hidden content. A closed dialog or collapsed menu is checked only when it is open.
- **Web components**: content inside open shadow roots is checked; content inside closed shadow roots cannot be seen.
- **Rules that need layout** (contrast, reflow, target size, focus order) report needs review when computed styles or geometry are not available, and a note under **Coverage limits for this run** says so.
- **The screen-reader transcript** is a model of what a screen reader announces, spoken with your browser's voice. It is not a real screen reader.
- **Suggested fixes** marked medium or review confidence need a person to check the wording.

## Colour and contrast

- Contrast is measured from the colours the page actually paints, with semi-transparent colours blended over what is behind them.
- Text over gradients, photographs or video has no single background colour and is reported as needs review, not given a number.
- The **Vision** view samples up to 400 text elements.
- The **Simulation** filters and the colour-vision tables are approximations of how a typical person with each condition sees colour. Real vision varies from person to person.
- APCA Lc is shown for reference and never affects a result.
- Suggested colours keep the hue and change only lightness. They meet the target ratio but may not suit your brand; any colour that meets the ratio is acceptable.

## Scores

- The overall score is a weighted summary of up to ten categories. Categories with nothing to measure, or whose check was switched off, are excluded rather than counted as zero or 100.
- Scores are designed to be hard to max out. A page with a couple of serious issues lands in the seventies or below.
- A score can fall after you improve a page, when a fix exposes content that was never checked before.
- The **Security** score checks whether protective headers are present, not how good they are. Scoring is softened for local development servers.
- **Reliability** reflects only the links that were checked. Read the count beside it.
- Benchmark, percentile and competitor-archetype figures in **Insights** and **SEO** are fixed reference values for orientation, not a live comparison with other sites.

## Performance

- Core Web Vitals are measured when possible and estimated otherwise; the card says which. Estimates depend on the **Network Simulation** profile.
- The waterfall is an estimated load order, not a recorded network trace.
- Performance budgets are fixed general-purpose limits; your own budgets may differ.

## Site scans

- Up to 24 pages per run, found from same-site links and the sitemap.
- In the current version, the **Robots**, **Subdomains** and **Workers** settings do not change a site scan on the live site.

## What the Analyzer is not

- It is not a legal conformance certificate. Regulations reference WCAG conformance, which needs manual review too.
- It is not a replacement for testing with real assistive technology and real users.
- It is not a security scanner. It reads headers and links; it does not probe for vulnerabilities.
- It is not real-user monitoring.

Use the Analyzer to clear the automatable problems first, so that a manual review can spend its time on what only a person can judge. The [Accessibility Checklist](../../accessibility-checklist/README.md) covers the manual side.
