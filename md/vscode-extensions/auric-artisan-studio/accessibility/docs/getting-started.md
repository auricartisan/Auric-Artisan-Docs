---
title: Auric Accessibility — Getting started
description: Install Auric Accessibility, read your first WCAG finding, inspect an element, scan the project and find everything it adds to VS Code.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Getting started with Auric Accessibility

## Install

1. Open the Extensions view (`Ctrl` + `Shift` + `X`).
2. Search for `auric-artisan.auric-a11y` and select **Install**. Or run `code --install-extension auric-artisan.auric-a11y`.

It starts when VS Code finishes loading. You need VS Code 1.74 or newer. Nothing needs configuring: the default audit profile is WCAG 2.2 and the default contrast target is 4.5:1.

## Your first finding

1. Open an HTML file, or a JSX, TSX, Vue, Svelte, Astro or PHP component.
2. Problems are underlined with a violet wavy line and listed in the Problems panel (`Ctrl` + `Shift` + `M`) with the source `auric-artisan`. For example, an `<img>` without `alt` shows:

```text
Image has no alt attribute.  —  WCAG 1.1.1 Non-text Content (Level A, WCAG 2.0). Add alt="description" (or alt="" for purely decorative images).
```

3. Hover the underline. The card shows the criterion, a severity pill such as **CRITICAL**, the level and WCAG version, a priority such as **Priority 94/100 · fix now**, the file and line, the problem, the fix, and a before-and-after when a safe rewrite exists.
4. Select **Apply fix** to apply the rewrite, or press `Ctrl` + `.` for **Ignore this WCAG 1.1.1 finding here** and **Ignore all accessibility findings in this file**.

See [Editor linting](editor-linting.md).

## Inspect an element

1. Put the cursor inside an element, such as a `<button>`, or inside a CSS rule.
2. Press `Ctrl` + `Alt` + `A` (`Cmd` + `Alt` + `A` on macOS), or hover it.
3. The **Inspect** card shows its role and accessible name (or **No accessible name**), the colours that apply with contrast, APCA and a colour-vision check, a before-and-after preview, and the WCAG issues found there.

See [Inspect](inspect.md).

## Scan the project

1. Select the **Auric Accessibility** icon in the Activity Bar.
2. In the **Overview**, select **Scan project**.
3. When the scan finishes, a message reports the score, for example `Accessibility 82/100 (B) — 12 contrast + 30 WCAG issue(s) across 214 files (scanned).`, with **Open Studio**, **Show Issues** and **Force Rescan**.
4. The status bar now shows `A11y 82 B`, and **Project Issues** lists every finding.

See [Project scans](project-scans.md) and [The Project Issues view](project-issues-view.md).

## Where Auric Accessibility appears

| Place | What you get |
| --- | --- |
| Editor | WCAG and contrast underlines, issue hovers, Inspect cards, quick fixes |
| Activity Bar, **Auric Accessibility** | **Overview** (the accessibility dashboard), **Project Issues**, and **Color Picker** when Auric Color is installed |
| Status bar | The score item, and **Auric: N in this file** |
| Editor right-click menu | **Inspect Accessibility of Element**, **Check Contrast of Selection** (with a selection), **Mark Line as Intentional Branding (Toggle)** |
| Studio (**Auric Artisan: Open Accessibility Studio**) | **Home**, **Check** (Findings, Contrast, Preview) and **Settings** |
| Command Center (`Ctrl` + `Alt` + `.`) | Scan, rescan, Studio tools, rulebook, remediation plan, worst findings |

## With the other Studio extensions

Auric Accessibility has the highest priority, so when it is installed with Auric Color or Auric Code Health it hosts the shared Workstation: its sidebar, Overview, Studio and Command Center include every installed capability. See [The Workstation](../../docs/workstation.md).

## Next steps

- [Rules](rules.md): what each rule checks.
- [Audit profiles and contrast](audit-profiles-and-contrast.md): choose WCAG 2.0, 2.1, 2.2 or the 3.0 draft.
- [Manual evidence](manual-evidence.md): what to test by hand.
- [The remediation plan](../../docs/remediation-plan.md).
