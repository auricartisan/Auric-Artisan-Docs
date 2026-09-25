---
title: Auric Accessibility — Rules
description: Every WCAG rule Auric Accessibility checks, grouped by success criterion, with its impact, what it catches and how to fix it.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Rules

Auric Accessibility runs 70+ static rules (72 in the current package) mapped to 29 WCAG success criteria, on top of the contrast checks. This page lists every rule by success criterion, in the order of WCAG's four principles: perceivable, operable, understandable and robust.

## How to read this page

- **Rule ID** is what the editor, the Project Issues view, `health.json` and SARIF show, and what you can put in a suppression comment, for example `auric-disable-next-line img-alt`.
- **Impact** is how much the problem affects users: **critical**, **serious**, **moderate** or **minor**. It sets the Problems severity (critical and serious are warnings, moderate is information, minor is a hint) and the weight in the score.
- **hint** marks a **best-practice** rule: a pattern worth fixing that does not by itself fail the criterion. Best-practice findings are shown as hints (`Best practice (related to WCAG …)`), have low confidence, and weigh half in the score.
- **Checks** says whether the rule reads markup (HTML, JSX, TSX, Vue, Svelte, Astro, PHP, XML and template dialects) or CSS (every CSS dialect).
- **Confidence** and **automation** are given where a rule reports them. Other rules are high-confidence and fully automated. **Assisted** means a person should confirm the finding.
- The level and WCAG version are those of the success criterion. The audit profile decides which criteria run; see [Audit profiles and contrast](audit-profiles-and-contrast.md).

Each finding links to the W3C's *Understanding* page for its criterion, and **Rule details** in the hover opens the rule's entry in the [knowledge database](../../docs/rulebook-and-knowledge.md).

## Contrast criteria

Contrast is graded by the contrast checks rather than by a markup rule. See [Contrast diagnostics](../../color/docs/contrast-diagnostics.md).

| Criterion | Level | What is checked |
| --- | --- | --- |
| 1.4.3 Contrast (Minimum) | AA | Text and background pairs against your threshold (4.5:1, large text 3:1) |
| 1.4.6 Contrast (Enhanced) | AAA | The same, when your threshold is 7 or more |
| 1.4.1 Use of Color | A | Pairs that pass normally but lose contrast under colour-vision deficiency (hint) |
| 1.4.11 Non-text Contrast | AA | Use a 3:1 threshold for UI parts and large text |

APCA is offered as an experimental alternative model. An APCA result means "meets the configured Lc target", not WCAG 3 conformance.

## Perceivable

### 1.1.1 Non-text Content

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `img-alt` | critical | Markup | Image has no alt attribute. |
| `area-alt` | serious | Markup | Image-map `<area>` has no alt text. |
| `input-image-alt` | critical | Markup | Image button (`<input type="image">`) has no alt text. |
| `svg-img-name` | moderate | Markup | `<svg role="img">` has no accessible name. |
| `object-name` | moderate | Markup | `<object>`/`<embed>` has no accessible name. |
| `redundant-alt` | minor | Markup | Alt text starts with “image of / photo of …” — screen readers already announce it as an image. |
| `alt-filename` | moderate | Markup | Alt text looks like a file name, not a description. |

How to fix:

- `img-alt`: Add alt="description" (or alt="" for purely decorative images). Apply fix adds alt="".
- `area-alt`: Add alt="link destination" to every `<area>` that has an href.
- `input-image-alt`: Add alt="action name" so the button has an accessible name.
- `svg-img-name`: Add aria-label / aria-labelledby, or a `<title>` as the first child of the `<svg>`.
- `object-name`: Add title="what it shows" (or aria-label) to the `<object>`/`<embed>`.
- `redundant-alt`: Describe the content directly; drop the “image of” prefix.
- `alt-filename`: Replace the file name with a real description of the image.

### 1.2.2 Captions (Prerecorded)

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `media-captions` | serious | Markup | `<video>`/`<audio>` has no captions or subtitles track. |
| `video-captions` | moderate | Markup | Playable `<video>` has no captions track. |

How to fix:

- `media-captions`: Add a `<track kind="captions">` (or provide a transcript) for the audio content. Muted video is skipped.
- `video-captions`: Add `<track kind="captions" src="…" srclang="…">` inside the `<video>` (not needed for silent/decorative video).

### 1.3.1 Info and Relationships

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `fieldset-legend` | moderate | Markup | `<fieldset>` has no `<legend>` to name the group. |
| `duplicate-main` | moderate | Markup | More than one main landmark — a page should have exactly one. |
| `heading-skip` | minor, hint | Markup | Heading level skipped — breaks the document outline. |
| `aria-required-owned` | serious | Markup | Composite ARIA role is missing a required owned role. |
| `aria-required-context` | serious | Markup | ARIA role appears outside the context role it requires. |
| `table-headers` | moderate | Markup | Data table has no header cells (`<th>`). |
| `details-summary` | moderate | Markup | `<details>` has no `<summary>` label. |
| `landmark-unique-name` | moderate | Markup | Repeated landmarks of the same type need unique accessible names. |
| `content-text` | minor | CSS | Meaningful text inserted via CSS content is unreliable for assistive tech and can't be translated or selected. |

How to fix:

- `fieldset-legend`: Add a `<legend>` as the first child describing the grouped controls.
- `duplicate-main`: Keep a single `<main>` / role="main"; remove or relabel the extras.
- `heading-skip`: Don't jump heading levels (e.g. h2 → h4); step one at a time. Best-practice hint.
- `aria-required-owned`: Add the required child role, or use the equivalent native HTML control. Uses the WAI-ARIA 1.2 role matrix. In a component or partial, reported only when the wrong parent is visible in the same file. Confidence high, automated.
- `aria-required-context`: Nest it in the required composite/container role, or use native HTML with equivalent semantics. Uses the WAI-ARIA 1.2 role matrix. In a component or partial, reported only when the wrong parent is visible in the same file. Confidence high, automated.
- `table-headers`: Mark header cells with `<th scope="col/row">` (or role="presentation" for layout tables).
- `details-summary`: Add a direct `<summary>` child that names the disclosure. Confidence high, automated.
- `landmark-unique-name`: Give each repeated landmark a short, unique aria-label or aria-labelledby reference. Needs review. Confidence medium, assisted.
- `content-text`: Move real words into the markup; keep CSS content for decoration only.

### 1.3.5 Identify Input Purpose

Level AA, introduced in WCAG 2.1. Runs in the 2.1, 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `input-autocomplete` | minor | Markup | Identity input has no autocomplete token. |
| `autocomplete-invalid` | serious | Markup | autocomplete value is not a valid autofill field name. |

How to fix:

- `input-autocomplete`: Add an autocomplete token (e.g. email, tel, name, current-password) to help users autofill.
- `autocomplete-invalid`: Use a token from the HTML autofill vocabulary — an unrecognised value turns autofill off entirely. Checked against the HTML autofill vocabulary.

### 1.4.2 Audio Control

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `media-autoplay` | moderate | Markup | Media autoplays — provide a way to pause/stop or mute. |

How to fix:

- `media-autoplay`: Avoid autoplay, or add muted (video) and visible media controls.

### 1.4.4 Resize Text

Level AA, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `viewport-zoom` | serious | Markup | Viewport meta disables zoom (user-scalable=no / maximum-scale below 2). |
| `tiny-font` | minor, hint | CSS | Font size below 10px is illegible for many readers even after zooming. |

How to fix:

- `viewport-zoom`: Remove user-scalable=no and let maximum-scale be ≥ 2 so users can zoom. Flags user-scalable=no, or maximum-scale below 2. Apply fix rewrites the viewport.
- `tiny-font`: Use at least 12px (0.75rem) for any text users must read. Best-practice hint.

### 1.4.8 Visual Presentation

Level AAA, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `justify-text` | minor | CSS | Justified text creates uneven “rivers” of space that hurt dyslexic readers. |
| `line-height-tight` | minor | CSS | Line height under 1.2 squeezes lines together and clips ascenders/descenders. |

How to fix:

- `justify-text`: Use text-align: left (or start) for body copy.
- `line-height-tight`: Use a line-height of at least 1.2 for text (1.5 for body copy). Unitless or em values only; a px line-height is not judged.

### 1.4.10 Reflow

Level AA, introduced in WCAG 2.1. Runs in the 2.1, 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `viewport-fixed-width` | moderate | Markup | Viewport meta locks a fixed pixel width — content can't reflow on small screens. |

How to fix:

- `viewport-fixed-width`: Use content="width=device-width, initial-scale=1". Apply fix rewrites the viewport.

### 1.4.12 Text Spacing

Level AA, introduced in WCAG 2.1. Runs in the 2.1, 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `text-spacing-important` | minor, hint | CSS | !important text spacing blocks user style-sheet overrides (WCAG text-spacing test). |

How to fix:

- `text-spacing-important`: Drop !important from line-height / letter-spacing / word-spacing so users can adapt spacing. Best-practice hint. Apply fix removes !important.

## Operable

### 2.1.1 Keyboard

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `interactive-keyboard` | serious | Markup | Click handler on a non-interactive element is not keyboard accessible. |

How to fix:

- `interactive-keyboard`: Use a `<button>`/`<a>`, or add role + tabindex="0" and a key handler. Understands tabIndex={0}; catches Vue, Angular and Svelte click handlers.

### 2.1.4 Character Key Shortcuts

Level A, introduced in WCAG 2.1. Runs in the 2.1, 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `accesskey` | minor, hint | Markup | accesskey creates a single-character shortcut users can't remap or turn off. |

How to fix:

- `accesskey`: Remove accesskey, or provide a way to disable/remap the shortcut. Best-practice hint. Apply fix removes the attribute.

### 2.2.1 Timing Adjustable

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `meta-refresh` | serious | Markup | Timed `<meta refresh>` reloads/redirects the page without user control. |

How to fix:

- `meta-refresh`: Remove the timed refresh (an instant 0-second server redirect is exempt).

### 2.2.2 Pause, Stop, Hide

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `blink-marquee` | serious | Markup | `<blink>`/`<marquee>` auto-moves content and can't be paused. |

How to fix:

- `blink-marquee`: Remove it; use CSS animation gated behind prefers-reduced-motion if needed.

### 2.3.3 Animation from Interactions

Level AAA, introduced in WCAG 2.1. Runs in the 2.1, 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `smooth-scroll-motion` | minor | CSS | scroll-behavior: smooth without a prefers-reduced-motion fallback. |
| `reduced-motion` | minor | CSS | Infinite animation without a prefers-reduced-motion fallback. |

How to fix:

- `smooth-scroll-motion`: Wrap it in @media (prefers-reduced-motion: no-preference) { … }.
- `reduced-motion`: Wrap or disable it inside @media (prefers-reduced-motion: reduce).

### 2.4.1 Bypass Blocks

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `bypass-blocks` | moderate | Markup | Page has navigation but no skip link, `<main>` landmark or headings to bypass it. |

How to fix:

- `bypass-blocks`: Add `<main>` (or role="main"), headings, or a “skip to content” link as the first focusable element.

### 2.4.2 Page Titled

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `doc-title` | serious | Markup | Document has no non-empty `<title>`. |

How to fix:

- `doc-title`: Add a descriptive `<title>` in `<head>`.

### 2.4.3 Focus Order

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `positive-tabindex` | minor, hint | Markup | Positive tabindex disturbs the natural focus order. |

How to fix:

- `positive-tabindex`: Use tabindex="0" (focusable, natural order) or "-1" (programmatic) — never > 0. Best-practice hint. Apply fix sets tabindex="0".

### 2.4.4 Link Purpose (In Context)

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `link-name` | serious | Markup | Link has no discernible text. |
| `link-generic` | minor | Markup | Link text is not descriptive out of context. |

How to fix:

- `link-name`: Give the link meaningful text, or an aria-label for icon links. Apply fix adds an aria-label placeholder to replace.
- `link-generic`: Replace generic text like “click here” / “read more” with the link's destination.

### 2.4.6 Headings and Labels

Level AA, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `empty-heading` | moderate | Markup | Heading is empty — it labels nothing. |

How to fix:

- `empty-heading`: Give the heading text (or remove it; don't use headings for spacing).

### 2.4.7 Focus Visible

Level AA, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `focus-outline-none` | serious | CSS | Focus outline removed without a visible replacement. |

How to fix:

- `focus-outline-none`: Keep a visible focus indicator — add box-shadow / border, or use :focus-visible. One :focus-visible rule elsewhere in the file does not exempt every rule.

### 2.5.3 Label in Name

Level A, introduced in WCAG 2.1. Runs in the 2.1, 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `label-in-name` | moderate | Markup | aria-label doesn't contain the visible text — speech-input users can't activate it by name. |

How to fix:

- `label-in-name`: Start the aria-label with the visible text (or drop the aria-label).

### 2.5.8 Target Size (Minimum)

Level AA, introduced in WCAG 2.2. Runs in the 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `target-size` | minor | CSS | Interactive target may be smaller than 24×24 CSS px. |

How to fix:

- `target-size`: Give buttons/links/icons a min target of 24×24px (padding or min-width/height). Flags a CSS rule for a button, link, form control, `summary`, a `.btn` or `.button` class, `[role=button]` or `.chip` whose width and height are both set in pixels below 24.

## Understandable

### 3.1.1 Language of Page

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `html-lang` | serious | Markup | `<html>` element is missing a lang attribute. |
| `lang-invalid` | moderate | Markup | `<html lang>` value is not a valid language tag. |

How to fix:

- `html-lang`: Add lang="en" (or the page's language) to `<html>`. Apply fix adds lang="en".
- `lang-invalid`: Use a BCP-47 tag like lang="en", "en-US", "hi", "pt-BR".

### 3.1.2 Language of Parts

Level AA, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `lang-part-invalid` | moderate | Markup | lang on an element is not a valid language tag. |

How to fix:

- `lang-part-invalid`: Use a BCP-47 tag like lang="fr", "es-MX", "hi" — or drop the attribute. The html element is left to 3.1.1, so one problem is never reported twice; templated values are skipped. Confidence high, automated.

### 3.2.1 On Focus

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `autofocus` | minor, hint | Markup | autofocus moves focus on load — disorienting for screen-reader and zoom users. |

How to fix:

- `autofocus`: Avoid autofocus, or reserve it for single-purpose pages (like a lone search box). Best-practice hint.

### 3.2.2 On Input

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `select-onchange-nav` | moderate | Markup | Changing this control submits or navigates automatically — a context change on input. |

How to fix:

- `select-onchange-nav`: Trigger submit/navigation from an explicit button instead of onchange.

### 3.3.2 Labels or Instructions

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `input-placeholder-label` | minor | Markup | Field is labelled only by its placeholder, which disappears as soon as the user types. |
| `select-textarea-label` | serious | Markup | `<select>`/`<textarea>` has no label or accessible name. |

How to fix:

- `input-placeholder-label`: Add a visible `<label>` (keep the placeholder as an example or hint, not the label). Advisory: the placeholder does give the field a name, but it disappears as soon as someone types. Confidence medium, assisted.
- `select-textarea-label`: Associate a `<label for>`, or add aria-label / title. Apply fix adds an aria-label placeholder to replace.

### 3.3.8 Accessible Authentication (Minimum)

Level AA, introduced in WCAG 2.2. Runs in the 2.2 and 3.0-draft profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `no-paste-auth` | serious | Markup | Blocking paste / autocomplete on a password field fails accessible authentication. |

How to fix:

- `no-paste-auth`: Allow paste and autocomplete="current-password" so password managers work.

## Robust

### 4.1.2 Name, Role, Value

Level A, introduced in WCAG 2.0. Runs in all profiles.

| Rule ID | Impact | Checks | What it catches |
| --- | --- | --- | --- |
| `aria-attr-unknown` | minor | Markup | Unknown ARIA attribute — likely a typo. |
| `input-label` | serious | Markup | Form field has no associated label or accessible name. |
| `button-name` | serious | Markup | Button has no discernible text. |
| `duplicate-id` | moderate | Markup | Duplicate id — breaks label/aria references and scripting. |
| `aria-role-invalid` | moderate | Markup | Unknown ARIA role. |
| `aria-abstract-role` | moderate | Markup | Abstract ARIA role must not be used by authors. |
| `redundant-role` | minor | Markup | Redundant ARIA role duplicates the element's native semantics. |
| `aria-reference-missing` | moderate | Markup | ARIA reference points to a missing id. |
| `aria-attr-unsupported` | serious | Markup | ARIA attribute is not supported on this element's role. |
| `aria-attr-invalid-value` | serious | Markup | ARIA attribute has a value outside its allowed set. |
| `aria-required-attr` | critical | Markup | Role is missing an attribute it requires. |
| `aria-required-name` | serious | Markup | ARIA role requires an accessible name. |
| `aria-roledescription-name` | moderate | Markup | aria-roledescription is present on an unnamed element. |
| `aria-attr-deprecated` | minor | Markup | Deprecated ARIA attribute has no effect. |
| `aria-prohibited-name` | minor | Markup | This role does not support an accessible name. |
| `iframe-title` | serious | Markup | `<iframe>` has no accessible title. |
| `aria-hidden-focusable` | serious | Markup | aria-hidden="true" on a focusable element hides it from assistive tech but not the keyboard. |
| `role-presentation-interactive` | serious | Markup | role="presentation"/"none" on an interactive element strips its semantics but keeps it focusable. |
| `nested-interactive` | serious | Markup | Interactive element nested inside another interactive element. |
| `dialog-name` | serious | Markup | Dialog has no accessible name. |
| `summary-name` | serious | Markup | `<summary>` has no accessible name. |
| `aria-hidden-body` | critical | Markup | The document body is hidden from the accessibility tree. |

How to fix:

- `aria-attr-unknown`: Use a valid WAI-ARIA attribute (e.g. aria-label, aria-describedby, aria-expanded). Checked against the WAI-ARIA 1.2 attribute list.
- `input-label`: Add a `<label for>` tied to the field's id, or an aria-label / title. Apply fix adds an aria-label placeholder to replace.
- `button-name`: Add visible text, or an aria-label / title for icon-only buttons. Apply fix adds an aria-label placeholder to replace.
- `duplicate-id`: Make every id unique within the document. An id nothing refers to is a best-practice hint (minor); one a label or ARIA attribute points at stays moderate.
- `aria-role-invalid`: Use a valid WAI-ARIA role (or remove it).
- `aria-abstract-role`: Replace it with a concrete role (e.g. button, navigation, region) or remove it.
- `redundant-role`: Remove the role — the native element already exposes it. Deliberately narrow: never flags a list or list item given its role again (the fix for lists that lose their semantics when styled), a header or footer inside article, aside, main, nav or section, or an unnamed section or form given a role.
- `aria-reference-missing`: Make the referenced id exist, or remove the broken ARIA reference. Templated and framework-bound references are skipped.
- `aria-attr-unsupported`: Remove the attribute, or change the role to one that supports it.
- `aria-attr-invalid-value`: Use one of the values the specification defines — anything else is treated as absent.
- `aria-required-attr`: Add the required state — without it the role is announced but its value is not.
- `aria-required-name`: Provide visible text, aria-label, or aria-labelledby as appropriate for the role. Confidence high, automated.
- `aria-roledescription-name`: Give the element an accessible name, or remove aria-roledescription. Confidence high, automated.
- `aria-attr-deprecated`: Remove it — no current browser or screen reader implements it.
- `aria-prohibited-name`: Move the label to an element with a naming role, or give this one a role that accepts a name.
- `iframe-title`: Add title="what the frame contains" to the `<iframe>`. Apply fix adds a title placeholder to replace.
- `aria-hidden-focusable`: Remove aria-hidden, or also remove it from the tab order (tabindex="-1" / disabled). Apply fix adds tabindex="-1".
- `role-presentation-interactive`: Remove the role — interactive elements must expose their role to assistive tech. Applies to native controls and to any element with both a tab stop and a handler; purely decorative markup is not flagged.
- `nested-interactive`: Un-nest them — a link/button must not contain another link, button, or form control.
- `dialog-name`: Add aria-label or aria-labelledby pointing at the dialog's heading.
- `summary-name`: Put concise visible text in `<summary>`, or provide an accessible name. Confidence high, automated.
- `aria-hidden-body`: Remove aria-hidden="true" from `<body>`; hide only the specific inactive subtree. Confidence high, automated.

## Rules that offer Apply fix

`img-alt`, `iframe-title`, `input-label`, `select-textarea-label`, `button-name`, `link-name`, `html-lang`, `aria-hidden-focusable`, `positive-tabindex`, `accesskey`, `text-spacing-important`, `viewport-zoom` and `viewport-fixed-width`. See [Apply fix](editor-linting.md#apply-fix) for what each rewrite does. Every other rule suggests a fix for you to make.

## What the rules cannot judge

These rules read source text. They do not run your code, compute the final CSS cascade, expand component state or see markup that JavaScript generates. Several rules flag things that need human judgement, such as alt-text quality, link purpose, dialog naming, field labels and authentication; for those, the fix is a suggestion to review, never an automatic repair. Automated checks cover only part of WCAG; use the [manual checks](manual-evidence.md) for the rest. See [Limits and accuracy](../others/limits-and-accuracy.md).

## Related

- [Editor linting](editor-linting.md)
- [Suppression and branding](../../docs/suppression-and-branding.md)
- [Scores and grades](../../docs/scores-and-grades.md)
