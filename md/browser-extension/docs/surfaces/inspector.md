---
title: Browser extension — Element inspector
description: Inspect any element on a page — the hover card, the pinned card with contrast first, its seven sections, copying, and every key.
product: Browser extension › Surfaces
updated: 2026-09-25
---

# Element inspector

The element inspector reads any element on a web page and shows what matters to a designer, developer or accessibility tester, with contrast first. It works in two states: a light **hover card** that follows the pointer, and a **pinned card** with everything. The same element is then available in depth in Code › Inspect (see [Inspect](../code/inspect.md)).

## Start it

Any of these starts the inspector on the current tab:

- Home › **Inspect**;
- Code › Inspect › **Select element**;
- the custom right-click menu › **Inspect element** (see [Right-click menu](../on-websites/right-click-menu.md));
- **Inspect element** in the browser's own right-click menu;
- the **Inspect an element on the page** shortcut, once you assign a key in the browser (it has none by default).

A bar appears at the bottom of the page. It says **Inspecting** (or **Pinned**), names the element, lists the main keys and has a **Stop** button.

## The hover card

Move the pointer over the page. A highlight box outlines the element under it, and a small card follows the pointer with:

- the element's name (tag, id and classes) and its size in pixels;
- its `display`, role and landmark;
- **contrast**: a small "Aa" sample in the element's own colours, the ratio, and **AA** and **AAA** marks (a tick or a cross);
- a warning when an image has no alt text or a control has no accessible name;
- **Font**, **Size** (size/line height · weight), **Text** colour, **Background** colour and **Padding**.

The card's footer says "Click or P to pin · Esc stop". An element with no text of its own says contrast does not apply.

## The pinned card

Click the element, or press `P`, to pin it. The full card docks to the side of the window away from the element. Drag its grip to move it, or focus the grip and use the arrow keys.

### Header

- **Inspector · Pinned**, a grip (**Move the card**) and a close button (**Close the inspector**).
- The element's name: click it to copy its CSS selector. Its width × height beside it.
- A toolbar: **Unpin** (`P`), **Selector** (`S`), **JSON** (`J`) and **CSS** (`C`).
- Chips for `display`, `position`, role, landmark, the number of children, and which sibling it is ("sibling 2 of 5").

### Contrast comes first

- An "Aa" sample in the element's own colours and font.
- Whether the text counts as **large text** or **normal text**, with its size and weight.
- The ratio. Click it to copy it. A "≈" in front means the ratio is an estimate, because the text sits on an image or gradient; check the lightest area under it by eye.
- **AA** and **AAA** badges: *pass*, or what it needs, such as *needs 7:1*.
- When AA fails, **Nearest text colour that passes AA**: the current colour, an arrow, the suggested colour and its ratio, with a **Copy** button.
- For an element with no text of its own, contrast "Does not apply", and **Inspect the first child with text** moves to the first descendant that has text.

### Seven sections

Each section can be opened and closed, and shows a one-line summary even when closed (for example `146 × 74`, `16/22 · 600` or "3 pass").

- **Box model**: A diagram of margin, border, padding and content, with every side's value
- **Colours**: Text, background and border colours
- **Layout**: Display, position, flow, gap, alignment, columns, rows, overflow and offsets, as they apply
- **Typography**: Family, size, weight, line height and spacing, with a specimen in the element's own font
- **Effects**: Radius, shadow (with its layer count), transform, filter, backdrop, transitions as chips, cursor and opacity. "Everything here is at its default" when nothing is set.
- **Accessibility**: Checks with a verdict and a fix: accessible name, keyboard reachability, alt text, text contrast. Then role (explicit or implicit), heading level, landmark, tab index and ARIA attributes as chips you can click to copy.
- **CSS**: A ready-to-copy CSS block for the element, with **Copy CSS** and **Copy JSON**

**Click any value to copy it.**

### The accessibility checks

| Check | When it appears |
|---|---|
| Has an accessible name / **No accessible name** | For interactive elements. Without a name a screen reader announces only the role. |
| Reachable by keyboard / **Not reachable by keyboard** | For interactive elements. "It acts like a control, but Tab skips it." |
| Has alt text / **Missing alt text** / Decorative image | For images. `alt=""` marks an image as decorative. |
| Text contrast passes AA (and AAA) / **Text contrast fails AA** | For elements with text; the failing case shows the ratio and the target |
| Contrast is an estimate | For text on an image or gradient |
| Contrast does not apply | For elements with no text of their own |

## Keys

| Key | What it does |
|---|---|
| `Up` | Move to the parent element |
| `Down` | Move to the first child |
| `Left` / `Right` | Move to the previous / next sibling |
| `P` | Pin or unpin |
| `C` | Copy the CSS |
| `S` | Copy the selector |
| `J` | Copy the element's data as JSON |
| `Enter` | Copy the CSS |
| `Esc` | Unpin; press again to stop inspecting |
| Arrow keys on the grip | Move the pinned card |

Keys are ignored while you are typing in a field on the page.

## When it closes

The inspector stays open while a page rewrites its own address as you click or scroll, as auricartisan.com does. It closes when you go to another page, press Back or Forward, or the site changes route. If the page removes the pinned element, the card lets go of it.

## After inspecting

The pinned element is kept as the last inspected element. Open Code › Inspect in the popup or side panel to see its full snapshot: every computed style, the matched rules, accessibility, attributes, markup and a Live CSS editor. See [Inspect](../code/inspect.md). If its text fails contrast, a finding is added to [Findings](../check/all-findings.md).

## Related pages

- [Inspect](../code/inspect.md)
- [On the page](on-the-page.md)
- [Keyboard shortcuts](../../others/shortcuts.md)
