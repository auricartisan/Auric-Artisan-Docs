---
title: Accessibility of the site
description: How to use the Auric Artisan website with a keyboard, a screen reader or comfort settings, what the site aims to support, its known limits, and how to report a barrier.
product: Help
updated: 2026-09-25
---

# Accessibility of the site

This page is about using the Auric Artisan website itself with a disability or with assistive technology. (For checking the accessibility of your own designs, see the accessibility tools under [Website tools](../website/tools/README.md).) The official statement is https://auricartisan.com/company/accessibility/, summarised in [Accessibility statement](../website/company-and-legal/docs/accessibility-statement.md).

## What the site aims to support

The Accessibility Statement names these aims: semantic HTML with headings and landmarks; keyboard access to all core functionality; readable, contrast-aware and scalable text; compatibility with modern screen readers; ARIA semantics for dynamic widgets; and visible focus with a logical tab order. It says important areas are reviewed against WCAG 2.1 Level AA where practical.

## Using the keyboard

| Keys | What it does |
| --- | --- |
| `Tab` / `Shift` + `Tab` | Move between controls |
| `Enter` / `Space` | Activate a button or link |
| `Esc` | Close dialogs, panels and menus |
| `Ctrl` + `K` | Open search |
| `?` | Open the guide (when not typing) |
| `Ctrl` + `,` | Open or close **Settings** |
| `Alt` + `R` | Reading mode on or off |
| `Alt` + `T` | Switch theme (light, dark, system) |
| `Alt` + `+` / `Alt` + `−` / `Alt` + `0` | Larger, smaller, or reset text size |
| `Alt` + `M` | Reduced motion on or off |

Tab lists — for example the dashboard sections and the sign-in tabs — are a single stop: use the arrow keys, `Home` and `End` inside them. The full list is in [Keyboard shortcuts](../website/site-features/keyboard-shortcuts/README.md).

## Comfort and reading settings

Open **Settings** (`Ctrl` + `,`):

| Tab | Setting | What it does |
| --- | --- | --- |
| **Appearance** | **Theme** | **Light**, **Dark** or **System** |
| **Appearance** | **Text size** | Scales text across the site |
| **Appearance** | **Accent color** | Changes the highlight colour, with a preview of its contrast |
| **Appearance** | **Language** | English or हिन्दी |
| **Comfort** | **Reading mode** | Distraction-free layout with comfortable typography |
| **Comfort** | **Reduce motion** | Minimises animations and transitions |
| **Comfort** | **Reduce transparency** | Turns off blur and translucency |
| **Comfort** | **Boost contrast** | Stronger text and borders |
| **Comfort** | **Underline links** | Always underlines links in articles |
| **Comfort** | **Custom cursor** | Turn off to use your system pointer |
| **Comfort** | **Eye-rest reminders** | Reminders to rest your eyes on a schedule |
| **Tooltips** | **Show tooltips**, **Detailed tooltips** | Turn rich tooltips off or simplify them |

The first-visit welcome animation is shortened when your device asks for reduced motion, and any key or click skips it. Full details: [Settings panel](../website/site-features/settings-panel/README.md) and [Accessibility aids](../website/site-features/accessibility-aids/README.md).

## Screen readers

- Pages use headings and landmarks, so heading and region navigation work.
- Dialogs such as the upgrade dialog keep focus inside while open and return it when closed.
- Status messages (saved, copied, errors) are announced as they appear on the account pages and in forms.
- Charts in the account dashboard have a **Show as table** equivalent.
- The human check on the sign-in page names each mark for assistive technology ("Add" and the mark's name).

## Known limits

The statement is candid that some things may not be fully accessible: spectral visualisations, the Ishihara-style generator and real-time rendering experiments depend on colour and graphics by nature. It says alternative text and data views are provided where possible, and that full accessibility across every feature may not always be achievable.

## Reporting a barrier

Tell Auric Artisan what stopped you:

1. Email developer@auricartisan.com (the address the statement gives), or use https://auricartisan.com/company/contact/ with the topic **A bug**.
2. Say which page, what you were trying to do, what happened, and which browser and assistive technology you use.
3. A screenshot helps if you can take one; the contact form accepts up to four images.

See [Contact and support](contact-and-support.md).
