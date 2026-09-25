---
title: Auric Accessibility — Release notes
description: Auric Accessibility's version history, taken from the Studio changelog.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Auric Accessibility release notes

Auric Accessibility shares one version number and one changelog with the other Studio extensions. This page lists the entries that concern accessibility. The complete history is in the [Studio release notes](../../others/release-notes.md).

## Unreleased

Listed under **Unreleased** in the changelog, as upcoming entries for the next numbered release (detector 1.2.0):

- The rules were checked against axe-core on rendered HTML: on a 264-case regression suite, false positives fell from 132 to 0 and false negatives from 21 to 0; 80 of 83 rendered cases agree with axe.
- One tag reader for every rule: a JSX `=>` or a Vue `v-if="n > 0"` no longer cuts a tag short; attributes are whole names; bound values are respected.
- Components such as `<Input>`, `<Button>` and `<Form>` are no longer judged as native elements.
- Correct markup no longer fails: required owned roles on `<ul role="list">`, radio groups and table rows; required context in component files; `aria-selected` on `option`; `lang` on `<style lang="scss">`; image alt with `aria-label` or spreads; Razor, Material and shadcn labels; unnamed forms; duplicate IDs inside `<template>`.
- Accessible names now come from labelled `svg` and `img` children, template output and `v-text`; `aria-hidden` text no longer counts.
- `focus-outline-none`: one `:focus-visible` rule no longer exempts a whole file.
- `interactive-keyboard` understands `tabIndex={0}` and catches Vue, Angular and Svelte click handlers.
- New rule `input-placeholder-label` (3.3.2, advisory).
- Six rules became best-practice hints, weighted at half: `accesskey`, `autofocus`, `heading-skip`, `positive-tabindex`, `tiny-font`, `text-spacing-important`.
- Performance: a case that never finished (60,000 links) now takes 0.28 s; 2,930 real markup files scan in 6.2 s instead of 7.6 s.
- The contrast scanner, hovers and Contrast Studio changes listed in the Studio notes also apply, because Auric Accessibility publishes contrast diagnostics.
- The Studio's new Home and Check spaces, and the **pattern-rule** suggestion now opening **Check › Findings**.

## 0.1.0 — Initial Studio release

- A specification-backed WCAG 2.2 engine with structural, semantic, ARIA, language, form, media, focus, motion and contrast checks.
- Inspect for element-level names, roles, colours, contrast, colour-vision impact, issues and fixes.
- Workspace scans, grouped findings, score summaries, suppressions, quick fixes, remediation plans and rule documentation.
- Framework and template awareness, so comments, runtime bindings and inert source are not reported.
