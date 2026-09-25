---
title: Auric Accessibility — Audit profiles and contrast standards
description: Choose which WCAG version the audit targets, and choose between WCAG 2.x contrast ratios and APCA.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Audit profiles and contrast standards

## Audit profiles

WCAG has grown in versions: 2.1 and 2.2 each added success criteria to 2.0. An **audit profile** tells Auric Accessibility which version you are targeting, so it only reports criteria that apply.

| Profile | Studio label | Criteria checked |
| --- | --- | --- |
| `2.0` | WCAG 2.0 | Only criteria introduced in WCAG 2.0 |
| `2.1` | WCAG 2.1 | 2.0 plus 2.1 criteria, such as reflow, text spacing, label in name and character key shortcuts |
| `2.2` (default) | WCAG 2.2 (default) | Everything from 2.0 to 2.2, such as target size and accessible authentication |
| `3.0-draft` | WCAG 3.0 draft (+APCA) | All 2.x rules, plus APCA contrast on top of the WCAG 2.x ratio checks |

Criteria that depend on the profile:

| Introduced in | Criteria with rules |
| --- | --- |
| WCAG 2.1 | 1.3.5 Identify Input Purpose, 1.4.10 Reflow, 1.4.12 Text Spacing, 2.1.4 Character Key Shortcuts, 2.3.3 Animation from Interactions, 2.5.3 Label in Name |
| WCAG 2.2 | 2.5.8 Target Size (Minimum), 3.3.8 Accessible Authentication (Minimum) |

All other rules belong to WCAG 2.0 criteria and run in every profile.

### Change the profile

- Studio › Settings › **Accessibility audit** › **Audit profile**, then **Save settings**; or
- set `auricA11y.a11y.profile` in your settings.

Editor diagnostics update immediately. Rescan the project afterwards: a cache made under another profile is treated as stale, so the next **Scan project** reads the workspace again. The command-line scanner has its own `--profile` option.

## Contrast standards

### WCAG 2.x contrast ratio

The **contrast ratio** compares the relative brightness of two colours, from 1:1 (identical) to 21:1 (black on white). WCAG 2.x asks for:

| Target | Applies to |
| --- | --- |
| 4.5:1 | Normal text, level AA (1.4.3) |
| 3:1 | Large text (24 px, or 18.66 px bold) at AA, and user-interface parts (1.4.11) |
| 7:1 | Normal text at AAA (1.4.6); large text at AAA needs 4.5:1 |

Set your target with `auricA11y.contrast.threshold` (default 4.5). Large text automatically gets the lower target.

### APCA

**APCA** (Accessible Perceptual Contrast Algorithm) is the contrast model proposed for the WCAG 3 working draft. It reports **Lc** (lightness contrast), roughly 0 to 106, and accounts for which colour is the text and which the background, so dark-on-light and light-on-dark pairs are rated differently. The Studio shows what an Lc value is suitable for:

| Lc | Suitable for |
| --- | --- |
| 90 or more | Any text |
| 75 or more | Body text, 16 px and up |
| 60 or more | Large or medium text, 18 px and up |
| 45 or more | Large bold text, 24 px and up |
| 30 or more | Non-text and UI only |
| below 30 | Decorative only |

APCA uses APCA-W3 0.0.98G. WCAG 3 is an unfinished W3C working draft, so an APCA verdict means only "meets the configured Lc target". It is not a WCAG 3 conformance claim.

### Choose the standard

| `auricA11y.contrast.standard` | Studio label | What is flagged |
| --- | --- | --- |
| `wcag2` (default) | WCAG 2.x ratios | Pairs below the ratio target |
| `apca` | APCA (WCAG 3 draft) | Pairs below `auricA11y.contrast.apcaThreshold` (default Lc 60, range 15–106) |
| `both` | WCAG 2.x + APCA | WCAG failures first, then APCA shortfalls on pairs that pass WCAG |

With the **3.0-draft** profile, `wcag2` behaves like `both`.

APCA findings are shown as `Low APCA contrast Lc … [WCAG 3 draft]`, with the quick fix **Fix APCA contrast**. Project scores and the Studio's pass rates always use WCAG 2.x ratios.

### Colour-vision risk

Whichever standard you use, `auricA11y.contrast.flagCvdRisk` (on by default) adds a hint for pairs that pass for typical vision but fall below the target under protanopia, deuteranopia or tritanopia (WCAG 1.4.1, Use of Color).

## Related

- [Contrast diagnostics](../../color/docs/contrast-diagnostics.md)
- [Scores and grades](../../docs/scores-and-grades.md)
- [Reference](reference.md)
