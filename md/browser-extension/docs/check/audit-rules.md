---
title: Browser extension — Audit rules
description: Every rule in the extension's accessibility engine, grouped by category, with its impact, WCAG 2.2 success criteria and whether the audit runs it.
product: Browser extension › Check
updated: 2026-09-25
---

# Audit rules

The accessibility engine behind Audit and Findings has **80 rules** in eight categories, mapped to **32 WCAG 2.2 success criteria**. The audit runs at level AA, so it applies the **78 rules** that test levels A and AA. The two AAA rules, enhanced text contrast (1.4.6) and reduced motion (2.3.3), are part of the engine but are not run by the audit.

The engine uses the WCAG 2.2 success criteria, the ARIA 1.2 role and attribute definitions and the HTML accessibility mappings bundled in the extension, so questions such as "is this attribute allowed on this role" are answered from the specifications rather than guessed. Accessible names are computed with the standard accessible-name algorithm, following `aria-labelledby`, labels, `title` and content.

## Impact

Each finding has an impact, the same scale most accessibility tools use:

| Impact | Meaning |
|---|---|
| **critical** | Blocks some people from using the content at all |
| **serious** | A significant barrier; fix soon |
| **moderate** | Makes the content harder to use |
| **minor** | A nuisance or a best-practice gap |

A finding is either a **failure** or a **warning**. A warning means a person must decide, for example contrast over an image.

## How the score is calculated

The score, from 0 to 100, counts **distinct failing rules**, not each failing element, so one unlabelled button repeated down a long table is one problem to fix. Each failing rule costs points by impact (critical 10, serious 6, moderate 3, minor 1), multiplied by 1 plus the base-10 logarithm of how many times it failed. For example, one critical rule failing on 10 elements costs 10 × 2 = 20 points. Warnings never lower the score. The score appears in the JSON export.

## Rules

The ID is how each rule appears in an exported JSON report. "Page" rules check the document once; the others check each matching element.

### ARIA (17)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `aria-role-unknown` | Role must be a valid ARIA role (typos get a "did you mean" suggestion) | serious | 4.1.2 |
| `aria-role-abstract` | Abstract roles must not be used in markup | serious | 4.1.2 |
| `aria-role-deprecated` | Deprecated ARIA role | minor | 4.1.2 |
| `aria-role-redundant` | Explicit role duplicates the element's native role | minor | 4.1.2 |
| `aria-on-roleless-element` | ARIA is not allowed on this element | moderate | 4.1.2 |
| `aria-attr-unknown` | `aria-*` attribute is not in the specification | serious | 4.1.2 |
| `aria-attr-unsupported` | `aria-*` attribute is not supported on this role | serious | 4.1.2 |
| `aria-attr-invalid-value` | `aria-*` attribute has an invalid value | serious | 4.1.2 |
| `aria-attr-deprecated` | Deprecated ARIA attribute | minor | 4.1.2 |
| `aria-required-attr` | Role is missing a required attribute | critical | 4.1.2 |
| `aria-required-children` | Role is missing its required child roles | critical | 1.3.1 |
| `aria-required-parent` | Role is missing its required parent role | critical | 1.3.1 |
| `aria-idref-broken` | ARIA reference points at an element that does not exist | serious | 1.3.1, 4.1.2 |
| `aria-hidden-focusable` | `aria-hidden` element is still keyboard focusable | critical | 1.3.1, 4.1.2 |
| `aria-hidden-body` | `aria-hidden` must not be applied to `<body>` | critical | 4.1.2 |
| `aria-prohibited-name` | Role does not support an accessible name | moderate | 4.1.2 |
| `aria-presentation-focusable` | Focusable element has a presentational role | serious | 4.1.2 |

### Names (5)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `control-has-name` | Interactive element has no accessible name | critical | 4.1.2 |
| `name-is-whitespace` | Accessible name is only whitespace | serious | 4.1.2 |
| `label-in-name` | Accessible name does not contain the visible label | serious | 2.5.3 |
| `link-name-descriptive` | Link text is not descriptive ("click here", "read more") | moderate | 2.4.4 |
| `identical-links-differ` (page) | Links with the same name point to different destinations | moderate | 2.4.4 |

### Structure (12)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `heading-order` (page) | Heading levels skip a rank | moderate | 1.3.1 |
| `heading-empty` | Heading has no text | serious | 1.3.1, 2.4.6 |
| `page-has-h1` (page) | Page has no level-one heading | moderate | 1.3.1, 2.4.6 |
| `landmark-singleton` (page) | Duplicate top-level landmark | moderate | 1.3.1 |
| `landmark-main-exists` (page) | Page has no main landmark | moderate | 1.3.1, 2.4.1 |
| `landmark-duplicates-labelled` (page) | Repeated landmarks need distinguishing labels | moderate | 1.3.1 |
| `list-structure` | List contains elements other than list items | serious | 1.3.1 |
| `definition-list-structure` | Definition list has invalid children | moderate | 1.3.1 |
| `table-has-headers` | Data table has no header cells | serious | 1.3.1 |
| `th-has-text` | Header cell is empty | moderate | 1.3.1 |
| `duplicate-id` (page) | Duplicate id used by an ARIA reference or label | serious | 1.3.1, 4.1.2 |
| `content-outside-landmarks` (page) | Content sits outside any landmark | minor | 1.3.1 |

### Forms (10)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `form-field-has-label` | Form field has no label | critical | 1.3.1, 3.3.2, 4.1.2 |
| `label-for-broken` | `<label for>` points at no element | serious | 1.3.1, 3.3.2 |
| `label-orphaned` | `<label>` wraps or targets no form control | moderate | 1.3.1 |
| `placeholder-as-label` | Placeholder used instead of a label | serious | 3.3.2 |
| `autocomplete-valid` | `autocomplete` value is not a valid autofill field name | serious | 1.3.5 (AA) |
| `autocomplete-missing` | Personal-data field has no `autocomplete` attribute | minor | 1.3.5 (AA) |
| `radio-group-fieldset` (page) | Radio group has no group label | moderate | 1.3.1, 3.3.2 |
| `required-field-indicated` | Required field is not programmatically marked | moderate | 3.3.2 |
| `error-message-associated` | Invalid field does not reference its error message | serious | 3.3.1 |
| `select-has-options` | Select element has no options | moderate | 4.1.2 |

### Media (13)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `image-has-alt` | Image has no alt attribute | critical | 1.1.1 |
| `image-alt-meaningless` | Image alt text is not descriptive | serious | 1.1.1 |
| `image-alt-redundant` | Alt text repeats that this is an image | minor | 1.1.1 |
| `image-alt-duplicates-link` | Linked image alt duplicates the link text | moderate | 1.1.1, 2.4.4 |
| `input-image-alt` | Image button has no alt text | critical | 1.1.1, 4.1.2 |
| `area-has-alt` | Image map area has no alt text | serious | 1.1.1, 2.4.4 |
| `svg-has-name` | Meaningful SVG has no accessible name | serious | 1.1.1 |
| `svg-decorative-unhidden` | Decorative SVG is not hidden from assistive technology | minor | 1.1.1 |
| `video-has-captions` | Video has no captions track | critical | 1.2.2 |
| `video-has-audio-description` | Video has no audio description track | serious | 1.2.3, 1.2.5 |
| `media-autoplay-audible` | Media autoplays with sound | serious | 1.4.2 |
| `object-has-alt` | Embedded object has no text alternative | serious | 1.1.1 |
| `iframe-has-title` | Frame has no title | serious | 2.4.1, 4.1.2 |

### Keyboard (8)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `tabindex-positive` | Positive tabindex overrides the natural focus order | serious | 2.4.3 |
| `interactive-not-focusable` | Element behaves as a control but cannot be focused | critical | 2.1.1 |
| `focus-outline-removed` (page) | Focus indicator is removed by a stylesheet | serious | 2.4.7 (AA) |
| `target-size-minimum` (page) | Touch target is smaller than 24 × 24 px | serious | 2.5.8 (AA) |
| `accesskey-duplicate` (page) | `accesskey` value is used more than once | moderate | 2.1.1 |
| `focusable-hidden-offscreen` | Off-screen element is still in the tab order | moderate | 2.4.3, 2.4.7 |
| `autofocus-used` | `autofocus` moves focus on page load | minor | 2.4.3 |
| `nested-interactive` | Interactive element nested inside another | serious | 4.1.2 |

`interactive-not-focusable` understands "roving tabindex": a composite widget such as a tab list passes when one of its items holds the Tab stop. `target-size-minimum` respects WCAG's spacing exception for small targets that are well separated.

### Contrast (4)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `color-contrast` | Text contrast is below the AA threshold | serious | 1.4.3 (AA) |
| `color-contrast-enhanced` | Text contrast is below the AAA threshold (not run by the audit) | moderate | 1.4.6 (AAA) |
| `non-text-contrast` | Control boundary has insufficient contrast | serious | 1.4.11 (AA) |
| `link-distinguishable` | Link in text is identified by colour alone | serious | 1.4.1 |

Text over an image or gradient is reported as a warning for manual review, not a failure. Checkboxes and radio buttons drawn by the browser are exempt from `non-text-contrast`, as WCAG allows.

### Document (11)

| ID | Rule | Impact | WCAG |
|---|---|---|---|
| `html-has-lang` (page) | Page has no `lang` attribute | serious | 3.1.1 |
| `html-lang-valid` (page) | `lang` attribute is not a valid language tag | serious | 3.1.1 |
| `lang-parts-valid` | Inline `lang` attribute is not a valid language tag | moderate | 3.1.2 (AA) |
| `page-has-title` (page) | Page has no title | serious | 2.4.2 |
| `page-title-descriptive` (page) | Page title is not descriptive | minor | 2.4.2 |
| `viewport-scalable` (page) | Viewport prevents zooming | critical | 1.4.4, 1.4.10 (AA) |
| `skip-link-present` (page) | No mechanism to skip repeated content | moderate | 2.4.1 |
| `text-spacing-overridable` (page) | Text spacing is locked with `!important` | moderate | 1.4.12 (AA) |
| `meta-refresh` (page) | Page refreshes or redirects on a timer | serious | 2.2.1, 2.2.4 |
| `blink-marquee` | Auto-moving or blinking content cannot be paused | serious | 2.2.2 |
| `reduced-motion-respected` (page) | Long animation ignores `prefers-reduced-motion` (not run by the audit) | minor | 2.3.3 (AAA) |

## Related pages

- [Audit](audit.md)
- [Findings](all-findings.md)
- [Limits and accuracy](../../others/limits-and-accuracy.md)
