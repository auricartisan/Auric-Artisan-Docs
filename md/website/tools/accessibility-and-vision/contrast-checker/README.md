---
title: Contrast Checker — Overview
description: What the Contrast Checker does, who it is for, and how to grade a colour pair in under a minute.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Contrast Checker

The Contrast Checker answers one question quickly: does this text colour work on this background? You give it two hex colours. It gives back the exact WCAG 2.1 contrast ratio to two decimal places, a **Pass** or **Fail** badge against five thresholds, and a preview panel painted in the pair you are testing.

Two buttons do the rest. **Make it pass AA** appears when body text fails and moves the text colour to the nearest value that reaches 4.5:1. **Copy link** copies the page address, which always carries both colours, so a pair can be pasted into a ticket or a review and reopened exactly as you left it.

The tool is deliberately small. All the maths runs in your browser: nothing is uploaded, nothing is stored, and no account is needed. It tests one pair at a time. To find every failing pair on a whole page, use the [Analyzer](../analyzer/README.md).

## Who it is for

- Designers choosing text and background colours for a component.
- Developers and reviewers who need a number, not an opinion, in a code or design review.
- Accessibility specialists checking a single pair reported by another tool.
- Anyone learning what the WCAG contrast levels mean.

## Where to find it

- Address: https://auricartisan.com/tool/contrast-checker/
- With a pair already loaded: `https://auricartisan.com/tool/contrast-checker/?fg=1A1400&bg=F7F3E6` (`fg` is the text colour, `bg` the background, as hex without the `#`).
- Site search opens it with a colour or a pair filled in when your search is about a colour.

## Quick start

1. Open https://auricartisan.com/tool/contrast-checker/. It opens with a default pair already graded.
2. Type or paste your text colour into **Text colour**, for example `#6B7280`.
3. Type or paste your background colour into **Background colour**, for example `#FFFFFF`.
4. Read the large ratio under **Contrast ratio**.
5. Read the five badges. **Body text · AA** at 4.5:1 is the one most laws and contracts point at.
6. If body text fails, select **Make it pass AA** to get a passing text colour.
7. Look at the preview panel to judge the pair at real reading sizes.
8. Select **Copy link** to share the result.

## What you can do

- Grade any pair of hex colours against WCAG 2.1 AA and AAA for body text, large text, and interface components and graphics.
- See the pair as large text, body text and an interface element.
- Swap the two colours with one button.
- Nudge the text colour to the nearest value that passes AA.
- Share or bookmark a pair as a link.
- Use it entirely from the keyboard and with a screen reader.

## In this folder

- [docs/](docs/README.md) — how to use the Contrast Checker
  - [Getting started](docs/getting-started.md) — the screen, part by part, and your first check
  - [Check a colour pair](docs/check-a-colour-pair.md) — entering colours and reading the ratio and grades
  - [Make a pair pass](docs/make-a-pair-pass.md) — using Make it pass AA well
  - [Share a pair](docs/share-a-pair.md) — links, bookmarks and ways in
  - [Reference](docs/reference.md) — every control, threshold and output
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material
  - [Glossary](others/glossary.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools and reading](others/related.md)
  - [Privacy](others/privacy.md)
