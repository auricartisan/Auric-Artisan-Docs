---
title: Auric Artisan Theme — Check contrast
description: Read the Audit tab and the plain-text contrast report, and control the contrast guard that keeps your theme readable.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Check contrast

Every colour the theme produces is checked against the surface it actually sits on. You can read the results in three places: the **Audit** tab in Theme Studio, the **Contrast** section of the sidebar, and a plain-text contrast report.

## Key terms

- **Contrast ratio (WCAG):** a number from 1:1 to 21:1 comparing the luminance of text and background. WCAG 2 AA asks for 4.5:1 for body text and 3:1 for large text and control boundaries; AAA asks for 7:1.
- **APCA Lc:** a perceptual contrast measure from the draft WCAG 3 work. Unlike the ratio, it accounts for polarity (dark on light versus light on dark). Roughly, Lc 60 suits body text, Lc 45 large text, and Lc 30 is the floor for anything you must read. A negative value means light text on a dark background.
- **Minimum:** the threshold a particular pair is held to. Decorative washes are held to less than text.

## What is audited

The audit checks 81 pairs per theme: editor text, all 26 syntax roles, the 14 text-bearing ANSI terminal colours, source control decorations, and the text and borders of dropdowns, inputs, checkboxes, radios, buttons, badges, menus and quick picks. Form-control borders are held to 3:1 against the fill they enclose (WCAG 1.4.11).

## Use the Audit tab

1. Open Theme Studio and select **Audit** (or press `4`). If any pair fails, the tab shows a badge with the number of failures.
2. The top card shows the worst pair in the theme, its ratio, and either "{n} failing" or **All clear**.
3. The **Measured pairs** table lists every pair, failures first, then by ratio.

| Column | Meaning |
| --- | --- |
| Pair | An "Aa" sample drawn in the real colours, followed by the pair name. |
| Ratio | The WCAG contrast ratio, such as 7.12:1. |
| APCA | The APCA Lc value. |
| Minimum | The threshold for this pair. |
| Result | **AAA** (7:1 or more), **AA** (meets its minimum), **Tight**, **Fail** (below minimum) or **Missing** (a colour the pair depends on is missing, so it could not be measured). |

A **How to read this** card at the bottom repeats these definitions.

## Use the sidebar

In the **Auric Theme** view, the **Contrast** section shows the worst pair, a **Pass** or **Fail** chip and its ratio. Select it (**Open audit ›**) to open Theme Studio on the Audit tab. Before the first audit it reads **Not audited yet**.

## Open the plain-text contrast report

1. Run **Auric Theme: Show Contrast Report**, or select the checklist icon in the sidebar's title bar.
2. A read-only document called "Auric contrast report" opens in a preview tab.

The report lists the theme name and polarity, the number of audited and failing pairs, then one row per pair with a result flag (**AAA**, **AA** or **FAIL**), the WCAG ratio, the APCA Lc value, the minimum and the pair name. Failures are sorted first. The footer explains AA, AAA and APCA Lc.

The report updates when the theme is re-applied. You can copy it or save it like any other document.

## The contrast guard

When **Enforce contrast** (`auricTheme.a11y.enforceContrast`) is on, the default, every colour the customiser produces is adjusted along its OKLCH lightness until it clears your minimum, keeping its hue and chroma. The guard runs after your own colour overrides: a colour you choose is treated as a strong preference, but not as permission to make text unreadable.

To change the guard:

1. Open the **Dials** tab, **Accessibility** card.
2. Set **Minimum contrast** between 3 and 7 (default 4.5). Use 7 for AAA-level text.
3. Turn **Enforce contrast** off if you want exact colours. The audit still reports failures.
4. Turn **Audit on apply** off if you do not want a warning notification each time failures appear.

When **Audit on apply** is on and a change leaves pairs below the minimum, VS Code shows "Auric Theme: {n} colour pairs no longer meet your contrast minimum." Select **Show report** to open the contrast report.

## Result

You know which pairs pass, which are tight and which fail, and you can adjust the dials or overrides until the Audit tab shows **All clear**.

> **Note:** The audit measures the colour pairs the theme defines. It is guidance, not a guarantee that every possible customisation meets accessibility requirements. See [Limits and accuracy](../others/limits-and-accuracy.md).
