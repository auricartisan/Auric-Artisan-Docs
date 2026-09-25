---
title: Auric Color — The brand audit
description: Audit a brand's colour roles against real headings, body text, links and buttons, fix failing roles, export accessible tokens, and use the brand governance rulebook.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# The brand audit

The Studio's **Brand** space checks a set of brand colours the way a reader meets them: as headings, body copy, captions, links, buttons and borders on your backgrounds. You can do it by hand, with no project, or start from the colours your last scan found.

## Open it

- Select **Brand** on the Studio rail, or **Open Studio: Brand** in the Command Center.
- Select **Brand** in a colour hover's **Open in Studio** row. That colour becomes the **Primary** role.
- Select **Audit as a brand** on the Studio's Home (project palette), **Audit as brand →** in the Palette tool, or **Audit a brand by hand →** on Home before a scan.

## The header

The header card is titled **Brand accessibility audit** (*real text · WCAG + APCA + CVD*) and shows:

- a score ring with the brand score and grade;
- **roles pass**, for example `6/8`; **text pass**, for example `5/6`; and **CVD risk**, the number of checks that fail under colour-vision simulation;
- **Auto-fix N roles** when any check fails, or **✓ All roles pass**;
- **Load from scan** and **Reset**.

## Brand colours

Eight roles, each with a colour field:

| Role | Meaning | Starting value |
| --- | --- | --- |
| **Background** | Page background | `#FFFFFF` |
| **Surface** | Cards, panels, raised areas | `#F4F6F8` |
| **Body text** | Primary reading text | `#1A1A1A` |
| **Secondary text** | Captions, hints, metadata | `#5B6470` |
| **Primary** | Brand or action colour | `#2563EB` |
| **On primary** | Text on the primary colour | `#FFFFFF` |
| **Link** | Inline hyperlink colour | `#1D4ED8` |
| **Border** | Dividers, outlines, inputs | `#D6DAE0` |

## Real-text preview

Two sample surfaces, **On background** and **On surface**, each with a headline, body text, a secondary caption, a **Primary action** button and a **Read the guidelines** link, drawn in your colours. Edit **Headline text** and **Body text** to preview your own copy. The vision dropdown shows the surfaces as seen with protanopia, deuteranopia, tritanopia or achromatopsia; a note reminds you when a simulation is on.

## Role checklist

| Check | Target |
| --- | --- |
| Body text on background | 4.5:1 |
| Body text on surface | 4.5:1 |
| Secondary text on background | 4.5:1 |
| Secondary text on surface | 4.5:1 |
| Link on background | 4.5:1 |
| Button label on primary | 4.5:1 |
| Primary as UI on background | 3:1 |
| Border / divider on background | 3:1 |

Each row shows the pair, its hex values, **need 4.5:1** (or 3:1), the ratio, a **CVD** badge with the worst ratio under protanopia, deuteranopia or tritanopia, and ✓ or ✕. A failing row has a **fix** button that adjusts only that role.

## Fix failing roles

- **fix** on a row changes that check's foreground role (for example **Secondary text**) until it reaches the target on its background, keeping its hue.
- **Auto-fix N roles** does the same for every failing check.

A toast confirms each change.

## Load from scan

**Load from scan** fills the roles from your last project scan: the lightest colour becomes **Background**, the next lightest **Surface**, the darkest **Body text**, and the most used strongly coloured one **Primary**. **On primary** is set to black or white, and **Link**, **Secondary text** and **Border** are derived so they pass on the background. Without a scan, a toast says **Run a project scan first**.

## The brand score

Each check earns credit: text checks count fully, UI checks (primary and border) count 0.6.

| Text check | Credit |
| --- | --- |
| 7:1 or more | 1 |
| 4.5:1 or more | 0.92 |
| 3:1 or more | 0.5 |
| below 3:1 | ratio ÷ 3 × 0.3 |

| UI check | Credit |
| --- | --- |
| 4.5:1 or more | 1 |
| 3:1 or more | 0.9 |
| below 3:1 | ratio ÷ 3 × 0.4 |

A check that fails under colour-vision simulation has its credit multiplied by 0.85. The score is the weighted average × 100, with the usual letter grades. It is separate from the project score.

## Export

| Button | Output |
| --- | --- |
| **Export CSS vars** | `brand-tokens.css`: a comment with the score and each check's result, then `--brand-bg`, `--brand-surface`, `--brand-text`, `--brand-muted`, `--brand-primary`, `--brand-on-primary`, `--brand-link` and `--brand-border` in `:root` |
| **Export JSON** | `brand-tokens.json`: the score, the eight colours and every check with its ratio, target, result and CVD ratio |
| **Copy hexes** | All eight values, comma-separated |

Exports open a save dialog in your first workspace folder. Your brand colours stay in the Brand space while the Studio tab is open; export them to keep them.

## Brand governance in the knowledge database

Auric Color's knowledge database includes an **Accessible brand governance rulebook**, the article **Govern brand exceptions without creating an accessibility loophole**, and three policies:

- **Brand exceptions are narrow, owned, and temporary**
- **Brand classification cannot suppress structural findings**
- **Every brand token has provenance and a semantic role**

Open them with **Auric Artisan: Open Rulebook & Knowledge Database**. Teams can add their own reviewed brand exceptions in `knowledge-overrides.json`. See [Rulebook and knowledge database](../../docs/rulebook-and-knowledge.md).

## Branding in your code

To keep a deliberate brand colour pair in your code visible but out of the score, mark it as intentional branding. See [Suppression and branding](../../docs/suppression-and-branding.md).

## Related

- [Palettes and shades](palettes-and-shades.md)
- [Colour vision](colour-vision.md)
