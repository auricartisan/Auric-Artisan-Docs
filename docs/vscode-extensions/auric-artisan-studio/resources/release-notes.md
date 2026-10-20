---
title: Auric Artisan Studio — Release notes
description: The version history of Auric Artisan Studio, taken from the changelog that ships with the extensions.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Release notes

All four Studio extensions share one version number. These notes are taken from the changelog bundled with the extensions (the **Changelog** tab of each Marketplace listing), rewritten for readers of these docs.

## Unreleased

The changelog lists the following changes under **Unreleased**, which means they are not yet recorded against a version number; they are the upcoming entries for the next numbered release. The rest of these docs describe the extensions as they behave in the package currently offered on the Marketplace.

### Accuracy

Every engine was measured against an external reference, and each defect found was fixed with a permanent regression test: colour science against published reference values, contrast against Chromium's rendering, the WCAG rules against axe-core, and code health against a labelled set of examples.

Colour:

- Every CSS Color 4 and 5 syntax is parsed: `oklch()`, `lab()`, `lch()`, `hwb()`, `color()` with Display-P3, Rec. 2020 and other spaces, `color-mix()`, relative colour, `none`, angle units and `transparent`. Wide-gamut colours use CSS gamut mapping.
- Invalid hex values such as `#12345g` are rejected.
- CIEDE2000 colour difference was added and matches all 34 Sharma test pairs; colour naming now uses it.
- Colour-vision simulation now uses the Brettel 1997 method in linear light. The previous method brightened red for protanopes. Achromatopsia keeps relative luminance.
- The suggested fix is the nearest passing colour: `#888` on white now becomes `#767676` (4.54:1), not `#717171`.
- Ratios just under a threshold never display as the threshold.
- Translucent colours blend with 8-bit alpha, matching Chromium's pixels.
- Writing colours back round-trips every CSS format exactly. Previously `hsl()` output rounded to whole numbers and moved the colour, and `lch()` used the wrong white point.

Contrast scanning, rebuilt on a CSS rule tree (agreement with Chromium on the audit set rose from 14 to 62 of 68 cases; the six left are deliberate skips):

- Large text is graded at 3:1.
- Translucent text, translucent backgrounds and `opacity` are blended.
- Dark-mode token overrides no longer grade the light theme; dark themes are graded as themselves (**in the dark theme**).
- Only real `body`, `html` and `:root` rules set the page background.
- Nested and `@media` rules are graded once, never paired across rules; comments are ignored.
- `color-mix()`, relative colours and `light-dark()` are graded; cyclic tokens fall back as the CSS specification says.
- Inline colours sit on their ancestor element's background.
- Disabled controls and Markdown code samples are exempt; pass or fail uses the exact ratio.
- The Quick Fix never corrupts source: it rewrites a value only when the whole value is one colour (or one side of `light-dark()`); anything else opens the Contrast Studio.
- The Contrast Studio writes token fixes to the light theme's `:root` value, not to a later dark override.

Code health (detector 1.2.0; on a labelled set including a held-out set, precision is 1.00 in every category and recall is 1.00 except secrets at 0.96, up from 0.53):

- Secret detection now covers JSON, PHP, typed and Go assignments, prefixed names such as `MYSQL_PASSWORD`, unquoted `.env`, YAML and INI values, OpenAI `sk-proj-` keys, Google keys ending in `-`, and Azure and ADO.NET connection strings.
- False positives removed: placeholders (`CHANGE_ME`, `{{API_KEY}}`, `$VAR`, SOPS `ENC[…]`), translation labels, autocomplete tokens and key-file paths, `redis.eval` and `model.eval()`, tagged SQL templates, phone masks read as `XXX` markers, and Markdown underlines read as merge markers.
- One credential is one finding.
- Secret bytes no longer leak through task-marker messages or security evidence into SARIF or `health.json`.
- A call whose arguments cannot be read is now reported at medium confidence instead of being passed.
- A mention of `auric-disable-file` in prose or a string no longer silences a whole file.
- Task markers, `debugger` and breakpoints are recognised only where they belong in each language.
- The underline covers the finding's real span.
- Worst-case inputs (a 200 KB minified line, a 5,000-line file) scan in 5–30 ms.
- Because findings are fingerprinted by detector 1.2.0, a CI baseline written by detector 1.1.0 may list some findings as new once.

WCAG rules (detector 1.2.0; on a 264-case regression suite, false positives fell from 132 to 0 and false negatives from 21 to 0; 80 of 83 rendered cases agree with axe-core, and the three that differ are contested or best practice):

- One tag reader for every rule: a JSX `=>` or a Vue `v-if="n > 0"` no longer cuts a tag short; attributes are whole names; bound values are respected.
- Components such as `<Input>`, `<Button>` and `<Form>` are no longer judged as native elements.
- Correct markup no longer fails: required owned roles on `<ul role="list">`, radio groups and table rows; required context in component files; `aria-selected` on `option`; `lang` on `<style lang="scss">`; image alt with `aria-label` or spreads; Razor, Material and shadcn labels; unnamed forms as landmarks; duplicate IDs inside `<template>`.
- Accessible names now come from labelled `svg` and `img` children, template output and `v-text`; `aria-hidden` text no longer counts.
- `focus-outline-none`: one `:focus-visible` rule no longer exempts a whole file.
- `interactive-keyboard` understands `tabIndex={0}` and catches Vue, Angular and Svelte click handlers.
- New rule `input-placeholder-label` (3.3.2, advisory).
- Six rules are now marked best practice rather than WCAG failures: `accesskey`, `autofocus`, `heading-skip`, `positive-tabindex`, `tiny-font` and `text-spacing-important`. They are shown as hints and weigh half in the score.
- A case that never finished (60,000 links) now takes 0.28 s; scanning 2,930 real markup files went from 7.6 s to 6.2 s.

### Studio redesign

- Every Studio screen now uses the Auric look shared with auricartisan.com and the browser extension: warm near-black on dark themes, paper on light themes, Fraunces headings and scores, Manrope text and gold primary actions. The fonts are bundled; nothing is fetched. High-contrast themes keep VS Code's own colours.
- The Studio is one tab with a rail of five spaces (Home, Color, Check, Health, Brand) plus Settings, Rulebook and Icon Studio at the foot. Each space opens with a header, and spaces with several tools have their own tab row. Each extension shows only the spaces it carries.
- A new Home space: the score ring with Accessibility, Contrast and Code-health tiles, files to fix first, suggestions, the CI gate command and the project palette. The findings list moved to **Check › Findings**, which the **pattern-rule** suggestion now opens.
- The Overview was rebuilt: a workspace card, a **This file** card with **Fix N in this file**, suggestions, recent colours and doors into the Studio, Rulebook, Icon Studio and fix plan, with one gold action per view.
- **Generate Project Health Report** also writes a printable, self-contained `project-health.html`, with **Open in Browser**.
- Contrast hovers lead with the ratio and verdict, show the pair, APCA Lc and the nearest passing colour of the same hue, and offer **Apply to --token**, **Open in Contrast Studio** and **Intentional branding**.
- New **Auric: N in this file** status-bar item.
- The Studio's Contrast tool is now the Contrast Studio: the pair on its background with four WCAG checks, passing colours that keep the hue, where the token is used, and write-back to the token or one use.
- The issue hover's **Apply fix** button is gold.

## 0.1.0 — Initial Studio release

The first public release of Auric Artisan Studio: a privacy-first workstation delivered as three focused extensions and one Full Pack.

| Package | Focus |
| --- | --- |
| Auric Color | Colour picking, contrast, palettes, OKLCH scales and colour-vision previews |
| Auric Accessibility | WCAG 2.0, 2.1 and 2.2 auditing, APCA analysis, Inspect and project scans |
| Auric Code Health | Secrets, debug leftovers, task markers, risky APIs, size checks and SARIF |
| Full Pack | Installs Color, Accessibility and Code Health only |

Studio experience:

- A Workstation that lets independently installed extensions behave as one product, without duplicate views, scans or diagnostics, with live host switching when extensions are installed or removed.
- The Full Pack installs only the three Studio extensions; icon themes and icon libraries are not included.
- A navigation rail, page summaries, action cards, consistent dialogs and a theme-aware settings experience.
- Custom dropdowns, switches, tooltips, focus management, keyboard navigation, visible focus, reduced-motion and forced-colours support throughout.
- Issue hovers built around priority, confidence, conformance, source context, fix guidance, ignore actions and rule references.
- Command Center shortcuts, capability-aware actions and deterministic suggestions.

Colour:

- Colour detection and editable swatches across CSS and 40+ programming, template, data and markup languages.
- WCAG contrast, APCA, RGB, HSL, OKLCH, Display-P3, colour naming, accessible alternatives, palette generation, shade scales and colour-vision simulation.
- Colour editing inline, from the hover and in the docked picker.

Accessibility:

- A WCAG 2.2 engine with structural, semantic, ARIA, language, form, media, focus, motion and contrast checks.
- Inspect for element-level names, roles, colours, contrast, colour-vision impact, issues and fixes.
- Workspace scans, grouped findings, score summaries, suppressions, quick fixes, remediation plans and rule documentation.
- Framework and template awareness, so comments, runtime bindings and inert source are not reported.

Code health and reporting:

- Checks for exposed secrets, injection risks, unsafe APIs, merge markers, debug code, task markers, oversized files and maintainability problems.
- Secret evidence redacted before it reaches diagnostics, reports or the Studio.
- Project health records, JSON and SARIF 2.1.0 output, stable fingerprints, baselines, trend history and an offline command-line scanner.
- A versioned local knowledge base of rules, requirements, procedures, policies, glossary entries, sources and remediation guidance.

Accessibility and trust:

- Every Studio screen designed for WCAG 2.2 AA and checked across light, dark, high-contrast, narrow and zoomed layouts.
- A no-network runtime, a strict content security policy for the Studio's screens, local-only analysis and deterministic builds.
