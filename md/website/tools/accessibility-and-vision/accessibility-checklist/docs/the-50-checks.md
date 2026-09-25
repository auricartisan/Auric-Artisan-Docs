---
title: Accessibility Checklist — The 50 checks
description: Every check in the Accessibility Checklist, area by area, with its WCAG criterion, level and how much the Analyzer can decide.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# The 50 checks

The checklist has 50 checks in nine areas. This page lists them all, with the one-line summary the page shows for each (a few are slightly shortened to fit the table). Open a check on the page for its full explanation, test and fix.

## How to read the tables

- **ID** is the check's identifier. Open it directly with `#check-` plus the ID, for example `https://auricartisan.com/resources/accessibility-checklist/#check-k2`.
- **Tag** is the level and WCAG success criterion, as the page shows it. **Practice** means good practice with no criterion of its own.
- Checks at Level A or AA are **Required**; AAA and Practice checks are optional.
- **Decided by** says how much the Analyzer can do:
  - **AUTO** — "The analyzer decides this one on its own"
  - **PARTLY** — "The analyzer narrows this down; a person confirms it"
  - **BY HAND** — "Only a person can decide this one"

The checklist itself does not import Analyzer results. Run the [Analyzer](../../analyzer/README.md) and mark the checks yourself.

| Totals | Count |
| --- | --- |
| Level A | 22 |
| Level AA | 13 |
| Level AAA | 2 |
| Practice | 13 |
| Required (A and AA) | 35 |
| AUTO / PARTLY / BY HAND | 11 / 23 / 16 |

## 01 Semantics & structure

"What a screen reader builds its map from. Nothing below works if this is wrong."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| d1 | Landmarks wrap every region of the page | A 1.3.1 | PARTLY | header, nav, main, footer — one main per page, and any repeated nav named. |
| d2 | Headings describe structure, not size | A 1.3.1 | AUTO | One h1, no skipped levels. Style with CSS; never pick a heading level to get a font size. |
| d3 | html lang is set, and switches on foreign passages | A 3.1.1 | AUTO | It picks the speech synthesiser. A French quote inside English needs its own lang. |
| d4 | Every route has a unique, front-loaded title | A 2.4.2 | PARTLY | In a SPA the title is yours to set on navigation — the browser will not do it. |
| d5 | Lists, tables and figures use real elements | A 1.3.1 | PARTLY | A table needs th with scope and a caption. A div grid announces nothing. |
| d6 | The reading order matches the visual order | Practice | BY HAND | CSS order, grid placement and absolute positioning all move the eye without moving the DOM. |

## 02 Keyboard & focus

"The whole product, without a mouse. This is where most single-page apps fail."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| k1 | Every interactive element is reachable and operable by keyboard | A 2.1.1 | PARTLY | A div with onClick is not. Use a button, or add role, tabindex and both key handlers. |
| k2 | No keyboard trap — focus can always get back out | A 2.1.2 | BY HAND | Modals, embedded players and custom editors are the usual offenders. |
| k3 | Focus is always visible, and never removed without a replacement | AA 2.4.7 | PARTLY | outline: none with nothing in its place is the most common accessibility bug in the wild. |
| k4 | Focus order follows meaning | A 2.4.3 | PARTLY | No positive tabindex. tabindex="-1" for programmatic targets, "0" to add to the order. |
| k5 | Focus is managed across route changes and dialogs | Practice | BY HAND | On open, move focus in; on close, return it to the trigger. On navigation, move it to the new h1. |
| k6 | A skip link comes first and actually moves focus | A 2.4.1 | PARTLY | It must be the first tabbable thing, visible on focus, and target a focusable container. |
| k7 | Pointer targets are at least 24x24 CSS pixels | AA 2.5.8 | AUTO | New in WCAG 2.2. Spacing counts toward it — small icons need room around them. |

## 03 Forms & errors

"Where an inaccessible product stops being annoying and starts costing money."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| f1 | Every control has a programmatic label | A 3.3.2 | AUTO | A placeholder is not a label. It vanishes on input and many screen readers skip it. |
| f2 | Errors are identified in text and tied to the field | A 3.3.1 | PARTLY | aria-describedby links the message; aria-invalid marks the state. Colour alone says nothing. |
| f3 | Common fields declare autocomplete | AA 1.3.5 | AUTO | name, email, tel, address — it is a requirement, and it halves the typing for everyone. |
| f4 | Related controls are grouped with fieldset and legend | A 1.3.1 | PARTLY | Radio sets and checkbox groups are meaningless read one at a time. |
| f5 | Validation is announced, not just painted | Practice | BY HAND | A live region or a focus move — otherwise a screen reader user submits into silence. |
| f6 | Legal and financial submissions are reversible or confirmed | A 3.3.4 | BY HAND | Reversible, checked, or confirmed. Pick one before taking the payment. |

## 04 Images & media

"Alt text is a decision, not a field to fill in."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| m1 | Every image is either described or explicitly decorative | A 1.1.1 | PARTLY | alt="" and aria-hidden for decoration. A filename in the alt is worse than nothing. |
| m2 | Text in an image is repeated in real text | A 1.4.5 | BY HAND | It cannot be resized, restyled, translated or searched — screenshots of code are the worst case. |
| m3 | Video has captions; audio has a transcript | A 1.2.2 | BY HAND | Auto-captions are a draft. Someone reads them before they ship. |
| m4 | Video has audio description where it carries visual information | AA 1.2.5 | BY HAND | If the picture says something the soundtrack does not, it needs describing. |
| m5 | Nothing plays automatically for more than three seconds | A 1.4.2 | PARTLY | Or there is a control to stop it, reachable before everything else. |
| m6 | Icons carry an accessible name or are hidden | Practice | PARTLY | An icon-only button needs aria-label; an icon beside a label needs aria-hidden. |

## 05 Colour & contrast

"The part an automated tool can genuinely finish for you."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| c1 | Body text reaches 4.5:1, large text 3:1 | AA 1.4.3 | AUTO | Against the composited background — the colour after every translucent layer, not the token. |
| c2 | Controls and meaningful graphics reach 3:1 | AA 1.4.11 | AUTO | Input borders, toggles, chart series, focus rings. |
| c3 | Colour is never the only carrier of meaning | A 1.4.1 | PARTLY | Links underlined, errors iconned, chart series labelled or patterned. |
| c4 | Hover, focus, active and selected states all pass too | AA 1.4.11 | PARTLY | A rule that wins at rest can lose on hover — measure the state, not the resting colour. |
| c5 | Dark mode and forced-colors are checked separately | Practice | PARTLY | An inverted palette almost never passes, and Windows High Contrast drops your backgrounds. |
| c6 | Simulated for protanopia, deuteranopia and tritanopia | Practice | AUTO | On real screens, not only on the swatch sheet. |

## 06 Motion & preferences

"The settings the operating system already knows about."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| p1 | prefers-reduced-motion is honoured | AAA 2.3.3 | PARTLY | Not only decorative animation — parallax, autoplaying carousels and scroll-jacking. |
| p2 | Nothing flashes more than three times a second | A 2.3.1 | BY HAND | This one can cause seizures. It is not a preference. |
| p3 | Moving or auto-updating content can be paused | A 2.2.2 | PARTLY | Carousels, tickers, live feeds — pause, stop or hide. |
| p4 | Timeouts are announced, or there are none | AAA 2.2.6 | BY HAND | A session that dies silently loses the form someone spent twenty minutes on. |

## 07 ARIA & custom widgets

"No ARIA beats bad ARIA. Reach for a native element first, every time."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| a1 | Custom widgets expose name, role and value | A 4.1.2 | PARTLY | And keep them in sync as state changes. A silent aria-expanded is a broken disclosure. |
| a2 | The widget follows its APG keyboard pattern | Practice | BY HAND | Tabs, menus, comboboxes and trees each have an expected key map. Users know it already. |
| a3 | Status messages reach a live region | AA 4.1.3 | PARTLY | polite for confirmations, assertive only for genuine interruptions. Never both. |
| a4 | No aria-hidden on a focusable element | Practice | AUTO | It creates a control a screen reader cannot see but can still land on. |
| a5 | Link text makes sense out of context | A 2.4.4 | PARTLY | "Read more" repeated eleven times is a list of eleven identical links. |

## 08 Zoom, reflow & spacing

"The same page in the conditions people actually browse it."

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| z1 | No horizontal scroll at 320 CSS pixels wide | AA 1.4.10 | AUTO | Equivalent to 400% zoom on a desktop. Two-dimensional scrolling is the failure. |
| z2 | Text resizes to 200% without loss | AA 1.4.4 | PARTLY | Fixed-height containers with overflow: hidden are where the text goes. |
| z3 | User text-spacing overrides do not break the layout | AA 1.4.12 | PARTLY | Line height 1.5, paragraph 2em, letter 0.12em, word 0.16em — nothing may be clipped. |
| z4 | Both orientations work | AA 1.3.4 | PARTLY | No locking to portrait unless the content genuinely requires it. |
| z5 | Focused elements are not hidden behind sticky chrome | AA 2.4.11 | BY HAND | New in 2.2, and a sticky header plus scroll-into-view is exactly how it happens. |

## 09 Testing & proof

"How it stays fixed after the sprint that fixed it." All five are Practice checks, and each links to the W3C's guidance on evaluation.

| ID | Check | Tag | Decided by | Summary |
| --- | --- | --- | --- | --- |
| x1 | An automated pass runs in CI on every pull request | Practice | AUTO | It catches about a third. That third should never reach a human reviewer again. |
| x2 | A keyboard-only pass is part of review | Practice | BY HAND | Unplug the mouse and do the primary task. Ten minutes, most of the remaining bugs. |
| x3 | A screen reader pass on one real combination | Practice | BY HAND | NVDA with Firefox, or VoiceOver with Safari. Not the browser plugin that reads the DOM. |
| x4 | Findings carry evidence and a criterion | Practice | BY HAND | A screenshot and a number turn "this feels wrong" into something a developer can close. |
| x5 | People with disabilities are in the testing loop | Practice | BY HAND | Every checklist including this one is a proxy for that, never a replacement. |

## Links inside the checks

Every check links to the W3C Understanding document for its criterion ("Understanding 1.3.1" and so on); area 09 links to "W3C on evaluation". Some checks add a tool link:

| Check | Link | Opens |
| --- | --- | --- |
| d1 | Check the landmarks | The Analyzer |
| k3 | Check the focus ring | The Analyzer |
| c1 | Check a pair | The tools collection page |
| c2 | Audit the page | The Analyzer |
| c3 | Simulate it | The Vision Lab |
| c6 | Run the simulator | The Vision Lab |
| x1 | Automate with the API | The API documentation |

To check a single colour pair for c1, use the [Contrast Checker](../../contrast-checker/README.md).

Checks with no **What the fix looks like** block: d6, f6, m2, m3, m4, m5, c2, c3, c4, c6, p2, p3, p4, a2, z1, z4, x2, x3, x4 and x5.

For notes on the level tags of m2 and f6, see [Limits and accuracy](../others/limits-and-accuracy.md).
