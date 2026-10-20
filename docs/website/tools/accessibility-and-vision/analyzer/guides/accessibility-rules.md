---
title: Analyzer — Accessibility rules
description: Every one of the 126 accessibility rules the Analyzer checks, grouped by category, with its impact, WCAG mapping and what it looks for.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Accessibility rules

The accessibility engine in the **A11y+** panel checks 126 rules. This page lists every one, grouped into the 15 categories the panel uses for its **Area** filter and its **Where the problems are** bars. For how to read the results, see [The accessibility engine](accessibility-engine.md).

## How to read the tables

- **Rule** is the title the Issues view shows.
- **ID** is the rule's identifier, shown in each rule's details and used in the exports.
- **Impact** is how badly a failure affects people: critical, serious, moderate or minor.
- **WCAG** lists the success criteria the rule maps to. "Best practice" means the rule maps to no criterion: it is good advice, but not part of conformance.
- The **Level** filter in the Issues view uses the lowest level among a rule's criteria. A rule mapped to a Level A criterion is filtered as **WCAG A**.

Rules that map to WCAG 2.0 Level A or AA criteria also carry a **Section 508** badge, and rules that map to WCAG 2.0 or 2.1 Level A or AA criteria carry an **EN 301 549** badge.

Across the catalogue, 18 rules are critical, 61 serious, 30 moderate and 17 minor. By level, 81 are filtered as Level A, 20 as Level AA, 5 as Level AAA and 20 as best practice.

### What every rule has in common

- Rules only judge what is actually exposed. Elements hidden from assistive technology are skipped, apart from a few rules that exist to check hidden content, such as `aria-hidden` misuse, `<meta>` tags and image-map areas.
- Rules that need the page's layout or computed styles (contrast, reflow, target size, focus order) report **needs review** instead of guessing when those are unavailable.
- Content inside open shadow roots (web components) is checked too.

## Text alternatives (12 rules)

Images and other non-text content need a text equivalent that a screen reader can announce.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Images must have an alt attribute | `image-alt` | critical | 1.1.1 | `<img>` with no `alt`, no ARIA name and no presentational role |
| Alt text must not be a file name | `image-alt-filename` | serious | 1.1.1 | Alt text such as `hero_banner.jpg` |
| Alt text must be meaningful | `image-alt-placeholder` | serious | 1.1.1 | Placeholder alt such as "image", "photo", "logo" or "icon" |
| Alt text should not duplicate adjacent text | `image-alt-redundant` | minor | Best practice | Alt that repeats the text of its link or figure, so it is announced twice |
| Alt text should be concise | `image-alt-long` | minor | Best practice | Alt text longer than about 150 characters |
| Image buttons must have alternative text | `input-image-alt` | critical | 1.1.1, 4.1.2 | `<input type="image">` with no text |
| Image map areas must have alternative text | `area-alt` | critical | 1.1.1, 2.4.4 | Clickable image-map regions with no name |
| Embedded objects must have alternative text | `object-alt` | serious | 1.1.1 | `<object>` with no text alternative |
| Elements with role="img" must have an accessible name | `role-img-alt` | serious | 1.1.1 | `role="img"` with no name |
| Informative SVGs must have an accessible name | `svg-img-alt` | serious | 1.1.1 | Meaningful inline SVG with no `<title>`, `aria-label` or `aria-labelledby` |
| Canvas elements need a text alternative | `canvas-fallback` | serious | 1.1.1 | `<canvas>` with no fallback content or ARIA name |
| Server-side image maps must not be used | `server-side-image-map` | minor | 1.1.1, 2.1.1 | Image maps that need a mouse |

## Audio & video (4 rules)

People who cannot hear or see media need captions, descriptions and transcripts, and nobody should be surprised by sound.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Video must have captions | `video-caption` | critical | 1.2.2 | Prerecorded video with no captions track |
| Video should provide audio description | `video-description` | serious | 1.2.3, 1.2.5 | Video with no description track or text alternative |
| Audio needs a transcript | `audio-transcript` | serious | 1.2.1 | Audio-only content with no transcript |
| Audio must not autoplay for more than 3 seconds without a control | `no-autoplay-audio` | serious | 1.4.2 | Sound that starts by itself with no pause control |

## Structure & semantics (12 rules)

Screen-reader users move through a page by its headings, lists and frames. The structure has to be real markup, not just styling.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Heading levels must not skip | `heading-order` | moderate | 1.3.1, 2.4.6 | A jump such as `h2` straight to `h4` |
| Headings must not be empty | `empty-heading` | moderate | 1.3.1, 2.4.6 | Headings with no text |
| Page must contain a level-one heading | `page-has-heading-one` | moderate | Best practice | A page with no `h1` |
| Lists may only contain list items | `list-structure` | serious | 1.3.1 | Other content placed directly inside `<ul>` or `<ol>` |
| List items must be inside a list | `listitem-parent` | serious | 1.3.1 | An `<li>` outside a list |
| Definition lists must be structured correctly | `definition-list` | serious | 1.3.1 | A `<dl>` with anything other than `dt`/`dd` pairs |
| dt and dd must be inside a definition list | `dlitem-parent` | serious | 1.3.1 | `<dt>` or `<dd>` outside a `<dl>` |
| Styled paragraphs must not be used as headings | `p-as-heading` | moderate | 1.3.1 | Bold, oversized paragraphs that look like headings |
| Frames must have a title | `frame-title` | serious | 2.4.1, 4.1.2 | Frames announced only as "frame" |
| Frame titles must be unique | `frame-title-unique` | serious | 4.1.2 | Two frames with the same title |
| IDs on interactive elements must be unique | `duplicate-id-active` | serious | 4.1.2 | Duplicate IDs that break labels and ARIA references |
| Hidden content should be reviewed | `hidden-content` | minor | Best practice | Hidden content that scripts may reveal later; check it is exposed properly when shown |

## Tables (9 rules)

Data tables must tell screen-reader users which header each cell belongs to.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Table headers must reference data cells | `th-has-data-cells` | serious | 1.3.1 | Header cells with no data cells, often a layout table marked as data |
| Data tables must have header cells | `table-headers` | serious | 1.3.1 | Data tables with no `<th>` |
| scope attribute must be valid and on a header cell | `scope-attr-valid` | moderate | 1.3.1 | Invalid or misplaced `scope` values |
| headers attribute must reference cells in the same table | `td-headers-attr` | serious | 1.3.1 | Broken `headers` references |
| Data tables should have a caption | `table-caption` | minor | Best practice | Data tables with no `<caption>` |
| Table header cells must not be empty | `empty-table-header` | minor | Best practice | Header cells with no name |
| Do not fake a caption with a full-width first-row cell | `table-fake-caption` | serious | 1.3.1 | A spanning first row used as a visual title instead of `<caption>` |
| Table caption and aria-label must not be identical | `table-duplicate-name` | minor | Best practice | A caption repeated in `aria-label` or `title` |
| Data cells in large tables must be associated with a header | `td-has-header` | serious | 1.3.1 | In tables of 3 or more rows and columns, data cells no header reaches |

## Forms & labels (15 rules)

Every field and button needs a name a screen reader can announce and a speech-input user can say.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Radio and checkbox groups need a group label | `fieldset-legend` | moderate | 1.3.1, 3.3.2 | Related radios or checkboxes with no `<fieldset>` and `<legend>` |
| Form fields must not have multiple label elements | `form-field-multiple-labels` | moderate | 1.3.1, 4.1.2 | A field with more than one `<label>` |
| autocomplete attribute must use valid tokens | `autocomplete-valid` | serious | 1.3.5 | Invalid `autocomplete` values |
| Fields collecting user data should declare their purpose | `identify-input-purpose` | moderate | 1.3.5 | Personal-data fields (name, email, phone, address) with no `autocomplete` |
| Accessible name must contain the visible label | `label-in-name` | serious | 2.5.3 | An `aria-label` that replaces the visible text with something different |
| Changing a control must not automatically change context | `no-onchange-submit` | serious | 3.2.2 | A select that navigates as soon as its value changes |
| autofocus should not be used | `no-autofocus` | moderate | Best practice | `autofocus`, which drops users into the middle of the page |
| Form elements must have labels | `form-field-label` | critical | 1.3.1, 3.3.2, 4.1.2 | Fields with no programmatic label |
| Placeholder text must not be the only label | `label-placeholder-only` | serious | 3.3.2 | Fields labelled only by placeholder text |
| Required fields must be programmatically marked | `required-field-indicated` | moderate | 3.3.2 | Fields marked required visually but not with `required` or `aria-required` |
| Invalid fields must describe the error in text | `error-identification` | serious | 3.3.1, 3.3.3 | `aria-invalid` with no linked error message |
| Authentication must not depend on a cognitive test | `accessible-authentication` | serious | 3.3.8 | Login flows that block paste or require memorising or transcribing |
| Forms need an explicit submit control | `form-submit-control` | moderate | 3.2.2 | Forms with no submit button |
| Buttons must have discernible text | `button-name` | critical | 4.1.2 | Buttons announced only as "button" |
| Select elements must have an accessible name | `select-name` | critical | 4.1.2 | Selects announced only as a combo box |

## Zoom, reflow & motion (6 rules)

People who zoom, enlarge text or change spacing must still be able to use the page.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Content must not be locked to one orientation | `css-orientation-lock` | serious | 1.3.4 | Media-query transforms that lock portrait or landscape |
| Zooming and scaling must not be disabled | `meta-viewport` | critical | 1.4.4 | `user-scalable=no` or a maximum scale below 2 |
| Text spacing must be overridable | `avoid-inline-spacing` | serious | 1.4.12 | Inline `!important` spacing that user styles cannot override |
| Content must reflow at 320 CSS pixels | `reflow-fixed-width` | serious | 1.4.10 | Declared fixed widths that force two-way scrolling at 320px |
| Hover content must be dismissible, hoverable and persistent | `content-on-hover` | moderate | 1.4.13 | Native `title` tooltips, which fail all three |
| Users should be able to zoom to at least 500% | `meta-viewport-large` | minor | 1.4.4 | A maximum scale below 5 |

## Colour & contrast (4 rules)

Text and controls must stand out from what is behind them, and colour must not be the only cue.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Text must meet the minimum contrast ratio | `color-contrast` | serious | 1.4.3 | Body text under 4.5:1, or large text under 3:1 |
| Text should meet the enhanced contrast ratio | `color-contrast-enhanced` | moderate | 1.4.6 | Body text under 7:1, or large text under 4.5:1 (Level AAA) |
| Links in body text must not rely on colour alone | `link-in-text-block` | serious | 1.4.1 | Links in prose with no underline and under 3:1 against the surrounding text |
| UI component boundaries need 3:1 contrast | `non-text-contrast` | serious | 1.4.11 | Controls whose visible boundary is under 3:1, or that have no boundary at all |

Contrast is measured from what the page actually paints. Semi-transparent colours are blended with what sits behind them first. Text over a gradient, photograph or video has no single background colour, so it is reported as needs review. Each failing pair comes with a suggested colour that keeps the hue and adjusts only the lightness. See [Colour, contrast and vision](colour-contrast-and-vision.md).

## Keyboard & focus (12 rules)

Everything must work with a keyboard alone, and the user must always see where focus is.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Click handlers must be on focusable, named elements | `keyboard-handler-focusable` | critical | 2.1.1, 4.1.2 | A `div` or `span` with a click handler that keyboard users cannot reach |
| Interactive controls must not be nested | `nested-interactive` | serious | 4.1.2 | A button inside a link, or the reverse |
| accesskey values must be unique | `accesskeys-unique` | minor | Best practice | Duplicate `accesskey` values |
| Single-character shortcuts must be remappable or scoped | `character-key-shortcuts` | serious | 2.1.4 | Single-key shortcuts that fire while someone is dictating |
| Positive tabindex must not be used | `tabindex-positive` | serious | 2.4.3 | `tabindex` above 0 |
| Tab order must follow the visual reading order | `focus-order-visual` | serious | 2.4.3 | CSS reordering that makes the tab sequence jump around |
| Focused elements must show a visible focus indicator | `focus-visible` | serious | 2.4.7 | Outlines removed with nothing to replace them |
| Focus indicator must be large enough and contrast enough | `focus-appearance` | moderate | 2.4.13, 1.4.11 | Focus indicators thinner than 2 CSS pixels or under 3:1 |
| Focused elements must not be hidden behind sticky UI | `focus-not-obscured` | serious | 2.4.11 | Sticky headers, cookie bars or chat widgets covering the focused element |
| Scrollable regions must be keyboard-accessible | `scrollable-region-focusable` | serious | 2.1.1 | Scrolling areas that neither take focus nor contain anything focusable |
| Frames removed from the tab order must not contain focusable content | `frame-focusable-content` | serious | 2.1.1 | An `<iframe>` with `tabindex="-1"`; usually needs a manual check |
| Focusable elements should convey a role | `focus-order-semantics` | moderate | Best practice | Elements put in the tab order with no role |

## Timing & animation (3 rules)

Moving, blinking and refreshing content must be under the user's control.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Pages must not auto-refresh or redirect on a timer | `meta-refresh` | critical | 2.2.1 | A timed `<meta>` refresh or redirect |
| Blinking and scrolling content must be stoppable | `blink-marquee` | serious | 2.2.2 | `<blink>` and `<marquee>` |
| Long or infinite animation must respect reduced-motion | `animation-pausable` | serious | 2.2.2, 2.3.3 | Animation over five seconds, or motion that ignores the reduced-motion setting |

## Navigation (9 rules)

People need to skip repeated blocks, know where a link goes, and find pages more than one way.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Page must offer a way to skip repeated blocks | `bypass` | serious | 2.4.1 | No skip link, `<main>` landmark or heading structure |
| Page must have a descriptive title | `document-title` | serious | 2.4.2 | A missing or empty page title |
| Links must have discernible text | `link-name` | critical | 2.4.4, 4.1.2 | Links announced only as "link", often icon-only links |
| Link text must describe the destination | `link-name-generic` | moderate | 2.4.4, 2.4.9 | Generic text such as "click here", "read more" or "learn more" |
| Links with the same name must go to the same place | `identical-links-same-purpose` | minor | 2.4.9 | Two links with the same name and different destinations |
| Site should offer more than one way to find pages | `multiple-ways` | moderate | 2.4.5 | No search, sitemap or index alongside the navigation |
| Links opening a new window should say so | `link-new-window` | minor | Best practice | Links that open a new tab without warning |
| Help mechanisms must appear in a consistent place | `consistent-help` | minor | 3.2.6 | Help and contact links that move between pages |
| Skip links must point at an existing target | `skip-link` | moderate | Best practice | A skip link whose target ID is not on the page |

## Safe linking (1 rule)

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| target="_blank" should carry rel="noopener" | `target-blank-noopener` | minor | Best practice | New-tab links that let the opened page control the original tab |

## Pointer & touch (4 rules)

Targets must be big enough to hit, and gestures need simple alternatives.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Touch targets must be at least 24×24 CSS pixels | `target-size-minimum` | serious | 2.5.8 | Targets under 24×24px that are not inline and lack 24px of clear space |
| Touch targets should be at least 44×44 CSS pixels | `target-size-enhanced` | moderate | 2.5.5 | Targets under 44×44px (Level AAA) |
| Path-based and multipoint gestures need a single-pointer alternative | `pointer-gestures` | moderate | 2.5.1 | Swipe, pinch or drag with no tap or click equivalent |
| Drag interactions need a non-dragging alternative | `dragging-movements` | moderate | 2.5.7 | Drag-and-drop with no click alternative |

## Language & readability (5 rules)

The page's language drives the screen reader's voice, and plain prose helps everyone.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| `<html>` must have a lang attribute | `html-has-lang` | serious | 3.1.1 | A page with no language |
| lang attribute must be a valid BCP 47 tag | `html-lang-valid` | serious | 3.1.1 | An invalid language tag |
| lang attributes on page parts must be valid | `valid-lang` | serious | 3.1.2 | Invalid `lang` on passages in another language |
| Text should be readable at lower-secondary level | `reading-level` | minor | 3.1.5 | Prose harder than lower-secondary level (Level AAA) |
| Abbreviations should be expanded | `abbr-expansion` | minor | 3.1.4 | Abbreviations with no expansion (Level AAA) |

## ARIA correctness (24 rules)

ARIA adds roles, states and names for assistive technology. Used wrongly, it silently breaks them.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| role attribute must contain a valid, non-abstract role | `aria-role-valid` | critical | 4.1.2 | Unknown or abstract roles, which browsers drop |
| role must be allowed on the element it is placed on | `aria-allowed-role` | moderate | 4.1.2 | A role the element may not carry |
| ARIA attributes must be spelled correctly | `aria-attr-valid` | critical | 4.1.2 | Misspelt `aria-*` attributes, such as `aria-labeledby` |
| ARIA attribute values must be valid | `aria-attr-value-valid` | critical | 4.1.2 | Out-of-range tokens, non-numbers and broken ID references |
| ARIA attributes must be allowed on the element's role | `aria-allowed-attr` | serious | 4.1.2 | States and properties the role does not support |
| Roles must carry their required ARIA attributes | `aria-required-attr` | critical | 4.1.2 | For example `role="checkbox"` with no `aria-checked` |
| Composite roles must own the right child roles | `aria-required-children` | critical | 1.3.1, 4.1.2 | For example a `tablist` that does not own `tab` elements |
| Roles must sit inside their required parent role | `aria-required-parent` | critical | 1.3.1, 4.1.2 | For example an `option` outside a `listbox` |
| aria-hidden elements must not contain focusable content | `aria-hidden-focus` | serious | 1.3.1, 4.1.2 | Focusable elements inside `aria-hidden` |
| aria-hidden must not be on `<body>` | `aria-hidden-body` | critical | 4.1.2 | The whole page hidden from assistive technology |
| Naming attributes must not be used on roles that prohibit names | `aria-prohibited-attr` | serious | 4.1.2 | `aria-label` on roles such as generic, paragraph or code |
| Deprecated ARIA attributes should be removed | `aria-deprecated-attr` | minor | Best practice | ARIA drag-and-drop attributes, which nothing supports |
| Dialogs must have an accessible name | `aria-dialog-name` | serious | 4.1.2 | Dialogs announced only as "dialog" |
| ARIA commands must have an accessible name | `aria-command-name` | serious | 4.1.2 | Elements with a widget role and no name |
| ARIA input fields must have an accessible name | `aria-input-field-name` | serious | 4.1.2 | Custom input widgets with no name |
| Meters and progress bars must have an accessible name | `aria-meter-progress-name` | serious | 4.1.2 | Meters and progress bars announced as a bare number |
| Tooltips must have an accessible name | `aria-tooltip-name` | serious | 4.1.2 | Empty tooltips |
| role=presentation must not be combined with ARIA or focus | `presentation-role-conflict` | moderate | 4.1.2 | Presentational elements that are focusable or carry global ARIA |
| ARIA ID references must resolve | `aria-reference-valid` | serious | 1.3.1, 4.1.2 | `aria-labelledby` and similar pointing at missing IDs |
| Status messages must be exposed to assistive technology | `status-messages` | moderate | 4.1.3 | Toasts, cart counts or errors that appear with no live region |
| Live regions must be configured correctly | `aria-live-valid` | moderate | 4.1.3 | Misconfigured or over-assertive live regions |
| Conditional ARIA state must match the element's native state | `aria-conditional-attr` | serious | 4.1.2 | An `aria-checked` that disagrees with a native checkbox |
| aria-roledescription must be on an element with a semantic role | `aria-roledescription` | serious | 4.1.2 | `aria-roledescription` on an element with no role |
| role="text" must not contain focusable descendants | `aria-text` | serious | 4.1.2 | Links or fields inside `role="text"`, which disappear from the tree |

## Landmarks & regions (6 rules)

Landmarks let people jump straight to the main content, the navigation or the footer.

| Rule | ID | Impact | WCAG | Looks for |
| --- | --- | --- | --- | --- |
| Page must have exactly one main landmark | `landmark-one-main` | moderate | Best practice | No `<main>`, or more than one |
| banner and contentinfo landmarks must be unique | `landmark-no-duplicate` | moderate | Best practice | More than one top-level header or footer landmark |
| Landmarks of the same type must have distinct names | `landmark-unique` | moderate | Best practice | Two `<nav>` landmarks both announced as "navigation" |
| Top-level landmarks must not be nested inside another landmark | `landmark-top-level` | moderate | Best practice | A banner, main or contentinfo landmark inside another landmark |
| All page content should be inside a landmark | `region` | moderate | Best practice | Content outside every landmark |
| Form landmarks should be named | `form-landmark-name` | minor | Best practice | Several unnamed form landmarks |

## ARIA widget patterns

In addition to the 126 rules, the **Widgets** view checks eight composite widget patterns: Tabs, Disclosure / Accordion, Combobox, Dialog (modal), Menu / Menubar, Tree view, Slider and Carousel. Its findings are reported under the category **ARIA widget patterns** and count in the score like any other rule. When a widget finding repeats a rule that has already failed (for example an unnamed dialog), it is reported once, not twice.

## WCAG criteria the engine knows

The Conformance view lists 60 WCAG success criteria. Eleven of them are never checked by any rule, because software cannot judge them. They always appear as untested and need a person:

| Criterion | Name | Level |
| --- | --- | --- |
| 1.3.2 | Meaningful Sequence | A |
| 1.3.3 | Sensory Characteristics | A |
| 1.4.5 | Images of Text | AA |
| 2.1.2 | No Keyboard Trap | A |
| 2.3.1 | Three Flashes or Below Threshold | A |
| 2.5.2 | Pointer Cancellation | A |
| 2.5.4 | Motion Actuation | A |
| 3.2.1 | On Focus | A |
| 3.2.3 | Consistent Navigation | AA |
| 3.2.4 | Consistent Identification | AA |
| 3.3.7 | Redundant Entry | A |

A criterion can also show as untested on a particular page when none of its rules found anything to check, for example the captions criteria on a page with no video.

The other 49 criteria are covered by at least one rule: 1.1.1, 1.2.1, 1.2.2, 1.2.3, 1.2.5, 1.3.1, 1.3.4, 1.3.5, 1.4.1, 1.4.2, 1.4.3, 1.4.4, 1.4.6, 1.4.10, 1.4.11, 1.4.12, 1.4.13, 2.1.1, 2.1.4, 2.2.1, 2.2.2, 2.3.3, 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.4.7, 2.4.9, 2.4.11, 2.4.13, 2.5.1, 2.5.3, 2.5.5, 2.5.7, 2.5.8, 3.1.1, 3.1.2, 3.1.4, 3.1.5, 3.2.2, 3.2.6, 3.3.1, 3.3.2, 3.3.3, 3.3.8, 4.1.2 and 4.1.3.

To check the untested criteria yourself, work through the [Accessibility Checklist](../../accessibility-checklist/README.md).
