---
title: Auric Accessibility — Inspect
description: Use Inspect to see any element's or CSS rule's accessible name, role, colours, contrast, colour-vision impact and WCAG issues, with a before-and-after preview.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Inspect

**Inspect** shows, in a hover card, everything the file tells Auric Accessibility about one element or CSS rule: its accessible name and role, the colours that apply, the contrast verdict with APCA and a colour-vision check, a rendered before-and-after preview, and the WCAG issues found there.

An element's **accessible name** is what a screen reader announces for it, such as a button's text or an image's alt text. Its **role** is what kind of thing it is, such as a button, link or heading.

## Open the Inspect card

- **Hover** an element or a CSS rule (when you are not over a colour value or an Auric finding).
- **Keyboard:** put the cursor inside the element or rule and press `Ctrl` + `Alt` + `A` (`Cmd` + `Alt` + `A` on macOS), or run **Auric Artisan: Inspect Accessibility of Element**. It is also on the editor's right-click menu.

Inspect works in HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JavaScript, TypeScript, JSX, TSX and every CSS dialect (CSS, SCSS, Sass, Less, PostCSS, Stylus).

If the command cannot inspect, it says why:

| Message | Meaning |
| --- | --- |
| **open a file and place the cursor on an element or CSS rule to inspect.** | No editor is active. |
| **Inspect works in HTML, JSX/TSX, Vue, Svelte, Astro, PHP, XML, JS/TS, and every CSS dialect.** | The file's language is not supported. |
| **place the cursor inside an element, a CSS rule, or a style region to inspect its accessibility.** | Nothing inspectable is at the cursor. |

## What it inspects

- **Elements**: the innermost element around the cursor. Inspect shows a card for text and interactive elements (links, buttons, form fields and labels, images, paragraphs, headings, list items, table cells, landmarks such as `nav` and `main`, dialogs and similar), for components, and for any element that has a `role`, an `aria-label`, an inline style or a finding.
- **CSS rules**: the innermost rule around the cursor in a stylesheet, a `<style>` block, or a styled-components, Emotion or `css` template.

In JavaScript and TypeScript, a `<tag>` counts as an element only when it is a real HTML tag or a capitalised component, so comparisons such as `a < b` and generics such as `Array<string>` are never mistaken for markup.

## The card

### Heading

- For an element: **Inspect `<button>` · button**, then either **Name "Save changes"** or **No accessible name — assistive tech can't announce this element.**
- For a rule: **Inspect rule `.card-title`**.

The name comes from `aria-label`, `title`, `alt`, `placeholder` or the element's text, in that order.

### Colours and contrast

When colours apply, the card shows:

- the text colour on the background, the ratio with a pass or fail icon and level, and **APCA Lc** with its use (for example **large/medium text ≥ 18px**);
- where the colours came from: **inline style**, **nearby rule**, **this rule**, **rule text on file bg** or **file colors** (the file's most used pair, when the element has no colours of its own);
- a **Now** and a **Fixed** (or **Passing**) preview, each a small surface with a heading, body text and a button drawn in the colours;
- when it fails, the fix: **Text #999999 → #767676 (hue & chroma preserved) reaches 4.54:1 for a 4.5:1 target.**;
- a **CVD** row with the pair under protanopia, deuteranopia and tritanopia and the worst ratio, marked **relies on hue** when it falls below the target.

Headings `h1` to `h3` use a 3:1 target, because browsers draw them as large text by default; other elements use 4.5:1.

### Issues here

Up to six WCAG findings inside the element or rule, each with a severity badge, a level badge, a link to the criterion, the message and the fix. With colours but no findings, the card says **No structural WCAG issues detected here.**

### Actions

- **Open in Preview**: opens the pair in the Studio's before-and-after [Preview](check-space.md#preview).
- **Go to element** or **Go to rule**: moves the cursor to it.
- **WCAG docs**: opens the first finding's criterion.

## Settings

| Setting | Default | Effect |
| --- | --- | --- |
| `auricA11y.inspect.enabled` | `true` | Turns Inspect on or off, including the command |
| `auricA11y.inspect.onHover` | `true` | Shows the card automatically on hover. When off, Inspect appears only through the command, the right-click menu or `Ctrl` + `Alt` + `A`. |

The Inspect card's findings follow your audit profile. Its contrast targets are fixed at 4.5:1, or 3:1 for `h1` to `h3`, whatever your `contrast.threshold`.

## Limits

Inspect reads the file you are in. It does not know about styles in other files, classes applied at runtime or the final rendered cascade, so the colours shown are the best the file itself reveals. The **via** label tells you how the colours were found.

## Related

- [Editor linting](editor-linting.md)
- [The Contrast Studio](../../docs/contrast-studio.md)
- [Rules](rules.md)
