---
title: Changelog — Release summaries
description: A user-facing summary of every release in the Auric Artisan changelog, newest first.
product: Website › Library › Changelog
updated: 2026-09-25
---

# Release summaries

A plain-language summary of each release listed in the changelog, newest first. Each heading gives the version and date as published. For the full notes, open the release on https://auricartisan.com/library/changelog/.

## v0.9.11 — 12 August 2026 (release)

The REST API became a metered product, and the site gained a recorder.

- **API credits.** API calls are now measured in credits: one credit is one standard request, and heavier endpoints cost more. Specialist includes 1,000,000 credits a month and Industrial Pro 10,000,000, refreshing each billing month. Subscriptions to Industrial Pro started before 12 August 2026 keep their previous allowance.
- **Overage, only if you want it.** Extra usage is opt-in and prepaid at $1.00 (₹85) per 100,000 credits, so you are never invoiced after the fact. You can set a monthly spend cap, and a hard ceiling of ten times your included allowance always applies.
- **Top-ups.** You can buy credit packs from **Dashboard → API keys → Add credits**. Purchased credits do not expire at the end of the period.
- **API console** on the dashboard's API Keys tab: burn-down, projection, usage chart, spend by endpoint, credit balance, spend cap, overage switch and a live call feed.
- **New API areas:** colour science (63 colour spaces, colour difference, colour temperature), design tokens (ten export targets), a catalogue, and live usage.
- **API access** is now for Specialist and above; other plans get a clear upgrade message.
- **Recorder.** A site-wide screen, tab, region and canvas recorder, exporting video, animated GIF, PNG frames and posters, with trimming.
- **Tokens and credits are separate:** tokens pay for server-side tool work, credits pay for API calls, and neither pays for the other.

## v0.9.10 — 27 July 2026 (release)

- **One browser extension.** The browser extensions were combined into one redesigned product, Auric Studio, with a responsive sidebar, a Side Panel, pickers that upgrade colour inputs on any page, a custom right-click menu and a settings search.
- **Analyzer accessibility.** The Analyzer's A11y+ tab was rebuilt on a 112-rule accessibility engine, with an accessibility tree, a screen-reader transcript, colour vision simulation and a VPAT export. The rules load only when you open the tab.
- **Analytics** that are first-party, consent-based and free of third-party trackers.
- **Payments.** One-time checkout went live.
- **VS Code extension 0.13.2**, with colour and accessibility updates.

## v0.9.9 — 5 June 2026 (release)

- **New libraries:** Font, Palette, Accessibility, Shade, Harmony, Color, Gradient and Icon libraries.
- **Design System Generator** added.
- **Documentation, Learn and Blog** content added.
- **Beta** replaced the "In Development" label across the site.
- **Installable app (PWA)**, **user settings**, **guide content**, the **UX Kit**, security improvements and better control of basic and advanced tools.
- Faster, more consistent interface: colour picker and rendering improvements, keyboard shortcut improvements, and fixes to navigation, lag and library behaviour.

## v0.9.8 — 2 May 2026 (patch)

- Clearer home page summary and a new logo.
- Vision Simulation and the Color Science Model moved into the unified panel-based simulation system.
- News, Libraries and Announcement pages removed to simplify the site.
- Fixes to the welcome screen, search, and interface consistency; improved Analyzer.
- Legal pages restructured.
- The Advanced Kit was improved and control of tool complexity added.

## v0.9.75 — 19 April 2026 (changelog entry)

- Split-screen fixes: address, refresh, resizing, embedded pages and closing windows.
- Interface fixes across colour lists, colour overview, conversion tools, contrast panels and the CIE graph.
- More consistent search results.
- Ishihara plate generator and the Material Lighting lab added.
- Accessibility fixes: ARIA, keyboard focus and screen-reader announcements.
- Fixes to the Menu Kit and Status Kit, illuminant handling in light and dark modes, the Color Formulation Lab, the converter and the Palette Visualizer lab.

## v0.9.7 — 15 April 2026 (release)

"Deployment — Site marked 'In Development'". The website went live marked as in development, with reliability fixes to delivery, the server and the Analyzer (which now handles malformed pages more gracefully). The ASCII Art Generator and the Ishihara Plate Generator were promoted to beta.

## v0.9.6 — 13 April 2026 (release)

"Vision Simulation & Color Model Lab Advancement". More accurate protanopia, deuteranopia and tritanopia simulations; a comparison view for RGB, LAB, OKLab and experimental colour models; side-by-side analysis and sample export in the lab; simulations up to 35% faster on large scenes.

## v0.9.6 — 8 April 2026 (release)

"System Integration & Validation". The engine, tools, perception systems and lab were connected into one validated workflow, for fewer failures between parts of the platform.

## v0.9.5 — 24 March 2026 (release)

"Spectral & Experimental Layer". Spectral approximation for higher-fidelity colour, experimental interfaces for trying new colour models, and documentation with examples for spectral experiments. Spectral features were marked experimental.

## v0.9.4 — 20 February 2026 (patch)

"Tool Accuracy Refinement". Smoother gradients using LAB and OKLab interpolation, palette generation that clashes less and is more accessible, and fixes to rounding and edge cases in colour conversion.

## v0.9.0 — 31 December 2025 (release)

"Auric Artisan Pre-Release Stabilization". The platform reached a near-complete state with its engine, tools, rendering and research modules unified, and was tuned for performance and memory ahead of public release.
