---
title: Contrast Checker — Getting started
description: Open the Contrast Checker, learn each part of the screen, and grade your first colour pair.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Getting started with the Contrast Checker

## Open it

Go to https://auricartisan.com/tool/contrast-checker/. The page loads with a default pair, text `#1A1400` on background `#F7F3E6`, and grades it straight away, so there is no empty state to get past.

## The screen, part by part

On a wide screen the tool is two columns over a full-width strip: controls on the left, the result on the right, and the preview underneath. Below 720 pixels wide it becomes one column in the order controls, result, preview, and the swap button turns so its arrows point up and down. Nothing is hidden on a narrow screen.

| Area | What it holds |
| --- | --- |
| Breadcrumb | **Home**, **Tools** (links to the tools collection) and **Contrast Checker** |
| Heading | The kicker "WCAG 2.1 · Contrast", the title **Color Contrast Checker**, and a line saying nothing is uploaded |
| API hint | "Automate this — 1 API credit per call to `POST /v1/accessibility/check`", with **API docs** and a dismiss button |
| Controls | **Text colour** and **Background colour**, each a colour swatch beside a hex field, with the swap button between them |
| Result | The ratio (**Contrast ratio**), five grade rows, **Make it pass AA**, **Copy link** and a status line |
| Preview | A panel painted in your pair, with a line of large text, a paragraph of body text and an "Interface element" chip |
| Below | **What the numbers mean**, four questions and answers, and three cards linking to other tools |

The API hint is for developers who want to check pairs from code; API credits are a separate balance from tool tokens. Dismissing it hides it on every tool page in this browser.

## Check your first pair

1. Select the **Text colour** hex field and replace the value with `#6B7280`.
2. Select the **Background colour** hex field and replace the value with `#FFFFFF`.
3. Read the ratio. It updates as you type, and reads **4.83:1**.
4. Read the five rows. **Body text · AA** reads **Pass**; **Body text · AAA** reads **Fail**.
5. Look at the preview. Judge whether the paragraph is comfortable to read at length, not just whether it passes.

The result: you know the exact ratio and which WCAG levels the pair meets.

## Try the other controls

- Select the swap button (between the two colours) to exchange them. The ratio stays the same; the preview turns inside out.
- Type a failing pair, such as `#D3AF37` on `#F7F3E6`. A **Make it pass AA** button appears. Select it, and the text colour moves to the nearest value that reaches 4.5:1. The status line says what it chose.
- Select **Copy link**. The status line says "Share link copied." Paste the link anywhere to reopen this exact pair.

## Next steps

- [Check a colour pair](check-a-colour-pair.md) explains the ratio, the five grades and what counts as large text.
- [Make a pair pass](make-a-pair-pass.md) explains how the fix chooses its colour.
- To check every pair on a live page at once, use the [Analyzer](../../analyzer/README.md).
