---
title: Personalization Generator — Design tokens
description: The token system the Personalization Generator builds from the top palette — semantic roles, tonal ramps, light, dark and high-contrast themes, a WCAG and APCA audit, and data-visualisation scales — and how to copy it.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Design tokens

The **Tokens** tab turns the leader (the top palette of the last sweep) into a complete set of design tokens. It always uses the leader, whichever palette is open in the Studio, and it changes whenever a new sweep produces a new leader.

The heading reads, for example, **Semantic roles, 88 tonal stops, light/dark/high-contrast themes, APCA + WCAG audit, and chart scales — from your top palette.** Four figures sit beside it: **Roles**, **Tones**, **WCAG floor** and **APCA floor**. The two floors are the weakest of the first four contrast checks in the light theme (body text, muted text, text on surface and the primary button).

## Semantic roles

Eight role chips. Select one to copy its HEX.

| Role | How it is chosen |
| --- | --- |
| primary | The most chromatic palette colour with a usable mid lightness. |
| secondary | The most chromatic remaining colour. |
| accent | A strongly coloured palette colour whose hue is furthest from the primary. |
| neutral | The least chromatic palette colour. |
| success | A green, pulled a little towards the nearest palette hue. |
| warning | An amber, pulled the same way. |
| danger | A red, pulled the same way. |
| info | A blue, pulled the same way. |

If the palette is missing something (for example, it has only one strongly coloured colour), the generator makes a suitable colour instead.

**Copy CSS** and **Copy JSON** sit beside the heading. See Copying the tokens, below.

## Theme preview

**Light** and **Dark** switch a small console preview (**Acme Console**, a revenue card, **Get started** and **Learn more** buttons, and **Active**, **Pending**, **Failed** and **Info** chips) and list its background, surface, text, primary and accent values. The switch also changes which theme the contrast audit checks.

The generator builds three themes. The high-contrast theme is not previewed; it is included in the CSS and JSON.

| Theme | Character |
| --- | --- |
| Light | Near-white background and white surfaces with a faint tint of the neutral's hue, dark text, the primary and accent as they are. |
| Dark | Dark tinted background and surfaces, near-white text, a lighter primary with near-black text on it. |
| High contrast | White background and surfaces, near-black text, a darker primary and accent with white text on them. |

Each theme has fourteen values: background, surface, surface alt, border, text, text muted, primary, primary text, accent, accent text, success, warning, danger and info.

## Tonal ramps

One ramp for each of the eight roles, eleven steps each: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900 and 950. Lightness falls on a fixed OKLCH ladder from the light end to the dark end, and chroma is eased at both ends so the palest and darkest tones stay believable. The neutral ramp is kept almost grey.

Select any step to copy its HEX. Hover to see the role, the step and the value.

## Contrast audit

A table for the theme you are previewing, with four columns: **Pair**, **WCAG**, **APCA** and **Use for**.

| Pair | Checks |
| --- | --- |
| Body text | text on background |
| Muted text | muted text on background |
| Text on surface | text on surface |
| Primary button | primary text on primary |
| Accent on bg | accent on background |
| Primary on bg | primary on background |

**WCAG** is the WCAG 2.1 contrast ratio. **APCA** is the APCA Lc value, and **Use for** names what that value supports:

| Lc | Use for |
| --- | --- |
| 75 or more | Body text |
| 60 to 74 | Fluent text |
| 45 to 59 | Large / bold |
| 30 to 44 | Headlines |
| 15 to 29 | Non-text only |
| under 15 | Insufficient |

## Data-visualisation scales

Three strips, each with **Copy** (which copies the HEX values separated by spaces):

- **Categorical**: eight colours for separate series, chosen from the palette's colourful members to be as far apart in hue as possible, with extra hues made up if the palette has fewer than eight.
- **Sequential**: seven steps from light to dark in the hue of the most chromatic colour.
- **Diverging**: nine steps between two clearly different hues, meeting at a light neutral in the middle.

## Copying the tokens

- **Copy CSS** (in the Tokens tab) copies the three themes as CSS custom properties named `--aa-background`, `--aa-surface`, `--aa-surface-alt`, `--aa-border`, `--aa-text`, `--aa-text-muted`, `--aa-primary`, `--aa-primary-text`, `--aa-accent`, `--aa-accent-text`, `--aa-success`, `--aa-warning`, `--aa-danger` and `--aa-info`:
  - the light theme under `:root`;
  - the dark theme under `:root[data-theme="dark"], .dark`;
  - the high-contrast theme under `:root` inside `@media (prefers-contrast: more)`.
- **Copy JSON** copies everything: roles, themes, ramps, the audit for both previewed themes, the data-visualisation scales, the CSS and the summary figures.
- The **Export** tab adds these tokens to its CSS as well. See [Export, save and share](export-and-save.md).

The ramps and data-visualisation scales are in the JSON only, not in the CSS.

## Related

- [Brand Studio](brand-studio.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Glossary](../others/glossary.md)
