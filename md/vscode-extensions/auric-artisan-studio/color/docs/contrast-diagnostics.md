---
title: Auric Color — Contrast diagnostics
description: How Auric Color finds low-contrast text as you type, what its messages mean, and how to fix one pair or a whole file.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Contrast diagnostics

Auric Color checks the text and background colours in your stylesheets, markup and components as you type, and underlines text that does not meet your contrast target.

When Auric Accessibility is installed too, it publishes these contrast diagnostics instead, with the same behaviour and its own `auricA11y.contrast.*` settings. Only one extension ever publishes them, so you never see a pair twice.

## Where contrast is checked

CSS, SCSS, Sass, Less, PostCSS, Stylus, HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JavaScript, TypeScript, JSX, TSX and Markdown files, up to 1 MB each.

The checker pairs a text colour with its background from:

- CSS rules and `<style>` blocks;
- inline `style="…"` attributes;
- JSX style objects: `style={{…}}`, `sx={{…}}`, `css={{…}}`;
- styled-components, Emotion and Linaria tagged templates (`` styled.x`…` ``, `` css`…` ``, `createGlobalStyle`);
- Vue, Angular and Svelte style bindings (`:style="{…}"`, `[ngStyle]="{…}"`, `style:color`).

It follows CSS custom properties (`color: var(--ink)` over `background: var(--surface)`), including fallbacks and chains, and grades dark themes separately. See [Limits and accuracy](../others/limits-and-accuracy.md) for exactly how pairs are resolved and what cannot be seen.

## Contrast standards

`auricColor.contrast.standard` chooses the model:

| Value | Studio label | What is flagged |
| --- | --- | --- |
| `wcag2` (default) | WCAG 2.x ratios | Pairs below `contrast.threshold` |
| `apca` | APCA (WCAG 3 draft) | Pairs whose APCA lightness contrast is below `contrast.apcaThreshold` |
| `both` | WCAG 2.x + APCA | WCAG failures first, then APCA shortfalls on pairs that pass WCAG |

With Auric Accessibility installed and its audit profile set to **WCAG 3.0 draft**, `wcag2` behaves like `both`.

### Targets

- `contrast.threshold` (default 4.5, range 1–21): 4.5 is WCAG AA for body text, 7 is AAA, 3 is AA for large text and UI parts.
- Large text (24 px, or 18.66 px and bold) gets a lower target: 3:1 when your threshold is 4.5, or 4.5:1 when it is 7.
- `contrast.apcaThreshold` (default 60, range 15–106): 90 is roughly AAA, 75 body text, 60 large or medium text, 45 large bold text, 30 non-text UI. APCA is experimental; meeting it is not a WCAG 3 conformance claim.

## What the diagnostics say

All appear in the Problems panel with the source `auric-artisan` and a violet wavy underline in the editor.

| Finding | Example message | Severity |
| --- | --- | --- |
| Low contrast | `Low contrast 2.32:1 — #AAAAAA on #FFFFFF (need 4.5:1, APCA Lc 46). [WCAG 1.4.3]` | `contrast.severity` (warning) |
| Low contrast, large text | `… (need 3:1 (large text), …)` | Same |
| Low contrast, dark theme | `Low contrast in the dark theme 3.10:1 — …` | Same |
| Possible low contrast | `Possible low contrast 3.25:1 — #8A8F99 on the page background #FFFFFF … Verify the real background.` | Information |
| Low APCA contrast | `Low APCA contrast Lc 55 — #999999 on #FFFFFF (need Lc 60; large bold ≥ 24px). [WCAG 3 draft]` | `contrast.severity` |
| Colour-vision risk | `Contrast relies on hue — <text> on <background> drops to <ratio>:1 under color-vision deficiency. [WCAG 1.4.1]` | Hint |
| Branding | `Branding — #D3AF37 on #FFFFFF (2.11:1, APCA Lc 41). Classified as intentional branding …` | Information |

The criterion is `1.4.3` when your threshold is below 7 and `1.4.6` (Contrast, Enhanced) when it is 7 or more.

- **Possible low contrast** appears when a rule sets only a text colour and the background was taken from the page background declared on `body`, `html` or `:root` in the same file (`contrast.checkPageBackground`, on by default). It is softer because the real surface might differ.
- **Colour-vision risk** appears when a pair passes for typical vision but its contrast under protanopia, deuteranopia or tritanopia falls below the target (`contrast.flagCvdRisk`, on by default).
- **Branding** replaces a finding on a line marked with `auric-brand-…`. See [Suppression and branding](../../docs/suppression-and-branding.md).

## The contrast hover

Hover an underlined colour for a card that reads, top to bottom:

1. **Auric Artisan · Contrast** (or **APCA contrast**).
2. The verdict, for example `2.32 : 1 — fails WCAG AA for normal text`, or for APCA `Lc 55 — below the APCA target of Lc 60`.
3. The pair as an **Aa** sample, its values, the other model's figure, and the token it reads, for example `from --muted · used in 12 places`.
4. A note when the background was assumed from the page.
5. **Nearest passing, same hue:** the colour, its ratio and level, and **reuse --token** when an existing token fits. If no colour of that hue can pass, it says so.
6. Actions: the gold **Apply to --token** (changes the token's definition, so every use follows) or **Apply fix**, **Open in Contrast Studio** and **Intentional branding**.
7. Smaller links: **Apply only here**, **Go to code**, the WCAG criterion, and **Copy reference** (copies a one-line description for a commit or ticket).

**Apply to --token** appears when the text colour comes from a custom property defined in the same file.

## Quick fixes

Put the cursor on the underline and press `Ctrl` + `.`:

| Quick fix | What it does |
| --- | --- |
| **Fix contrast → #767676 (4.54:1)** (preferred) | Replaces the colour with the nearest passing colour of the same hue |
| **Fix APCA contrast → #hex (Lc N)** | For APCA findings: raises contrast until the APCA target is met |
| **Open in Auric Artisan Studio** | Opens the pair in the Contrast Studio, linked to this line |
| **Open in the Contrast Studio** | Offered instead of a fix for mixes, relative colours, faded text and shared dark-theme values |

Those values are left for the Contrast Studio because a one-click rewrite could change more than this text. A one-click fix rewrites a value only when the whole value is one colour, one `var()`, or one side of `light-dark()`.

## Fix every pair in a file

1. Open the file and run **Auric Artisan: Fix All Contrast Issues in File** (or **Fix all contrast in file** in the Command Center, **Fix N in this file** on the Overview, or **Fix all in file** on the suggestion).
2. A dialog lists the changes, up to six as `before → after` and **… and N more**, and explains that this is a single undoable edit.
3. Select **Apply fixes**.
4. A message confirms **Auric Artisan: fixed N contrast pair(s). Undo with Ctrl+Z (Cmd+Z) to revert all at once.**

Only pairs that can be fixed with one rewrite are included; each keeps its hue and chroma and reaches its WCAG 2.x target. Other messages you may see:

- **no failing contrast pairs in this file.**
- **nothing to change — failing pairs are already at their best-effort fix.** (when no colour of that hue can pass)

## Refresh

**Auric Artisan: Refresh Contrast Diagnostics** re-checks every open file. You rarely need it: files are re-checked as you type and whenever you change a setting.

## Settings

| Setting | Default | What it does |
| --- | --- | --- |
| `auricColor.contrast.enabled` | `true` | Turns contrast diagnostics in the editor on or off |
| `auricColor.contrast.standard` | `wcag2` | `wcag2`, `apca` or `both` |
| `auricColor.contrast.threshold` | `4.5` | WCAG 2.x target (1–21) |
| `auricColor.contrast.apcaThreshold` | `60` | APCA target (15–106) |
| `auricColor.contrast.severity` | `warning` | `error`, `warning`, `information` or `hint` for failures |
| `auricColor.contrast.flagCvdRisk` | `true` | Adds colour-vision risk hints |
| `auricColor.contrast.checkPageBackground` | `true` | Grades colour-only rules against the page background |
| `auricColor.branding.enabled` | `true` | Honours branding marks in the editor |

## Related

- [The Contrast Studio](../../docs/contrast-studio.md)
- [Scores and grades](../../docs/scores-and-grades.md)
- [Colour vision](colour-vision.md)
