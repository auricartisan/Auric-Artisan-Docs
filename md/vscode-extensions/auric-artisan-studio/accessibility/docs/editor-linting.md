---
title: Auric Accessibility — Editor linting
description: Where Auric Accessibility checks your code as you type, how to read its diagnostics and hovers, and which fixes it can apply for you.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Editor linting

Auric Accessibility checks every open file it supports about 300 ms after you stop typing, and shows problems as underlines, hovers and entries in the Problems panel. No scan is needed for this.

## Supported languages

| Rules | VS Code languages |
| --- | --- |
| Markup rules | HTML, JavaScript React (JSX), TypeScript React (TSX), Vue, Svelte, Astro, PHP, XML, Handlebars |
| Markup rules, template dialects | Twig, Liquid, Jinja, ERB, Razor, Blade, EJS, Nunjucks, Mustache, Edge (when VS Code recognises the file type) |
| CSS rules | CSS, SCSS, Sass, Less, PostCSS, Stylus |
| Contrast checks | CSS dialects, HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JavaScript, TypeScript, JSX, TSX, Markdown |

Plain JavaScript and TypeScript files (`.js`, `.ts`) get contrast checks for CSS-in-JS but not the markup rules; JSX and TSX files get both. Files larger than 1 MB are not checked.

The markup rules understand framework syntax: JSX attribute names such as `htmlFor` and `tabIndex`, bound values such as `:attr`, `[attr.x]` and `attr={…}`, and template output such as `{{ }}`, `<%= %>` and `@expr`. Values supplied at runtime are treated as unknown rather than wrong. Components such as `<Button>` are not judged as the native `<button>`. See [Limits and accuracy](../others/limits-and-accuracy.md).

## Diagnostics

Every WCAG finding appears in the Problems panel with the source `auric-artisan` and a code such as `WCAG 1.1.1`, which links to the W3C's *Understanding* page for that criterion. The message has this shape:

```text
<problem>  —  WCAG <criterion> <title> (Level <level>, WCAG <version>). <how to fix>
```

| Impact | Problems severity |
| --- | --- |
| Critical, serious | Warning |
| Moderate | Information |
| Minor | Hint |
| Best-practice hint (any impact) | Hint, with `Best practice (related to WCAG …)` instead of the level |

In the editor, findings get a violet wavy underline (lighter in dark themes) and a mark in the overview ruler.

When a branding mark covers the line of a structural finding, the message ends with **(A branding mark covers this line, but structural accessibility issues are not brandable — the finding still counts.)**

Contrast findings are covered in [Contrast diagnostics](../../color/docs/contrast-diagnostics.md); when Auric Accessibility is installed, it publishes them with its own `auricA11y.contrast.*` settings.

## The issue hover

Hover an underline (or anywhere on its line) for the finding's card. Reading from the top:

1. **Title**: the criterion's name, for example **Non-text Content**.
2. **Badges**: a severity pill (**CRITICAL**, **SERIOUS**, **MODERATE** or **MINOR**), **Accessibility**, **Level A** (or AA, AAA), **WCAG 2.0** (the version that introduced the criterion), and a confidence chip when the rule reports one.
3. **Priority**: a ten-segment meter with **Priority N/100** and advice: **fix now**, **fix soon**, **worth fixing** or **low urgency**. See [Priority in hovers](../../docs/scores-and-grades.md#priority-in-hovers).
4. **Where**: the file and line (select it to go there) and a link to the WCAG criterion.
5. **The problem**, as a quotation.
6. **How to fix**: a `diff` of the line before and after, when a safe rewrite exists; otherwise **In your code** shows the line. Then the fix in words.
7. **Actions**: the gold **Apply fix** button (when a rewrite exists), **Go to code**, **Rule details** (opens the rule in the knowledge database), **WCAG docs**, **Ignore here** and **Copy reference** (copies a one-line reference such as `WCAG 1.1.1 Non-text Content — src/index.html:12`).
8. **Footer**: the rule ID and detector version, for example `img-alt v1.2.0`.

## Apply fix

**Apply fix** replaces the flagged tag or declaration with a corrected version in one edit you can undo. It is offered only where a deterministic rewrite is safe:

| Rule | What Apply fix does |
| --- | --- |
| `img-alt` | Adds `alt=""` (marks the image as decorative; write a real description if it carries meaning) |
| `iframe-title` | Adds `title="Describe this frame"` |
| `input-label` | Adds `aria-label="Describe this field"` |
| `select-textarea-label` | Adds `aria-label="Describe this field"` |
| `button-name` | Adds `aria-label="Describe this action"` |
| `link-name` | Adds `aria-label="Describe this link"` |
| `html-lang` | Adds `lang="en"` |
| `aria-hidden-focusable` | Adds `tabindex="-1"` |
| `positive-tabindex` | Replaces the attribute with `tabindex="0"` |
| `accesskey` | Removes the `accesskey` attribute |
| `text-spacing-important` | Removes `!important` from the text-spacing declaration |
| `viewport-zoom`, `viewport-fixed-width` | Sets the viewport's `content` to `width=device-width, initial-scale=1` |

> **Important:** The placeholder text such as `Describe this field` must be replaced with a real, meaningful label. An empty `alt=""` is right only for purely decorative images. Judgement calls, such as alt-text quality or link purpose, are never applied automatically.

## Quick fixes

Put the cursor on a WCAG underline and press `Ctrl` + `.`:

| Quick fix | What it inserts |
| --- | --- |
| **Ignore this WCAG 1.1.1 finding here** | `auric-disable-next-line 1.1.1` on the line above |
| **Ignore all accessibility findings in this file** | `auric-disable-file a11y` at the top of the file |

**Ignore here** in the hover inserts `auric-disable-next-line` with the rule ID instead, so only that rule is silenced. See [Suppression and branding](../../docs/suppression-and-branding.md).

## The status bar

**Auric: N in this file** shows how many contrast and accessibility findings the active file has, for example `Auric: 5 in this file`; its tooltip splits them into contrast and accessibility. Select it to open the Project Issues view. It hides when the file is clean.

## Settings that affect linting

| Setting | Default | Effect |
| --- | --- | --- |
| `auricA11y.a11y.enabled` | `true` | Turns WCAG diagnostics in the editor on or off. Project scans still grade WCAG findings. |
| `auricA11y.a11y.profile` | `2.2` | Which WCAG versions' rules run. See [Audit profiles and contrast](audit-profiles-and-contrast.md). |
| `auricA11y.branding.enabled` | `true` | Honours branding marks in the editor. |
| `auricA11y.contrast.*` | see [Reference](reference.md) | Contrast checks. |

## Related

- [Rules](rules.md)
- [Inspect](inspect.md)
- [Reference](reference.md)
