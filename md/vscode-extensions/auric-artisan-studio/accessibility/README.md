---
title: Auric Accessibility — WCAG 2.2 linter for VS Code
description: What Auric Accessibility does, who it is for, how to install it, and a quick start from first scan to first fix.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Auric Accessibility — WCAG 2.2 Linter

Auric Accessibility finds accessibility problems in your markup and CSS while you write it. It checks HTML, JSX and TSX, Vue, Svelte, Astro, PHP, XML, common template languages and every CSS dialect against 70+ static rules mapped to the Web Content Accessibility Guidelines (WCAG) 2.0, 2.1 and 2.2: missing alternative text, unlabelled fields, empty buttons and links, invalid ARIA, blocked zoom, invisible focus, keyboard traps, small targets, accessible authentication and more. ARIA checks use the WAI-ARIA 1.2 role matrix and the HTML autofill grammar, so role and attribute errors are judged against the specification rather than a word list.

**WCAG** is the W3C's standard for accessible web content. Each requirement is a **success criterion** with a level: A, AA or AAA. **ARIA** attributes such as `role` and `aria-label` describe elements to assistive technology such as screen readers.

Beyond the editor, Auric Accessibility scans the whole project, grades it from 0 to 100, lists every finding in a searchable tree, and shows a before-and-after preview of contrast fixes. **Inspect** shows any element's accessible name, role, colours and contrast when you hover it. A local knowledge database adds all 86 WCAG 2.2 success criteria and eight manual test procedures for what automation cannot decide. Everything runs on your machine.

## Who it is for

- Front-end developers who want accessibility problems flagged as they type, with safe fixes.
- Accessibility specialists who want a prioritised worklist and manual test procedures for a codebase.
- Teams who want a repeatable accessibility score and a CI gate.

## Where to find it

- Marketplace ID: `auric-artisan.auric-a11y`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-a11y
- Install: `code --install-extension auric-artisan.auric-a11y`
- Version 0.1.0; VS Code 1.74 or newer. Also installed by the [Full Pack](../full-pack/README.md).

## Quick start

1. Install Auric Accessibility from the Extensions view (`Ctrl` + `Shift` + `X`).
2. Open a project with HTML, JSX, Vue, Svelte or similar files.
3. Open a component. Problems are underlined with a violet wavy line and listed in the Problems panel.
4. Hover an underline to see the WCAG criterion, how urgent it is and how to fix it. Select **Apply fix** where one is offered.
5. Put the cursor inside an element and press `Ctrl` + `Alt` + `A` (`Cmd` + `Alt` + `A` on macOS) to **Inspect** its name, role and colours.
6. Select the **Auric Accessibility** icon in the Activity Bar and select **Scan project**. The score ring shows the project's score and grade.
7. Expand **Project Issues** to browse every finding by type, file or severity.
8. Run **Auric Artisan: Generate Agent-Ready Remediation Plan** for a local, prioritised backlog of fixes.

## What you can do

- Lint markup and CSS as you type against 70+ WCAG rules, each with its criterion, level, WCAG version, impact and a one-line fix.
- Choose the audit profile: WCAG 2.0, 2.1, 2.2 (default) or the 3.0 draft (which adds APCA contrast).
- Apply safe fixes from the hover, such as adding `lang="en"` or replacing a positive `tabindex`.
- Silence a false positive for one line, one rule or one file, or classify a brand colour as intentional.
- Inspect any element or CSS rule: accessible name, role, colours, contrast, APCA, colour-vision impact, a before-and-after preview and the issues found there.
- Check contrast in stylesheets, markup and CSS-in-JS, with WCAG 2.x or APCA targets and colour-vision risk hints.
- Scan the project, see a 0–100 score and grade, and triage findings in the Project Issues view or the Studio.
- Preview failing contrast pairs next to their accessible repair before changing code.
- Export a WCAG summary as Markdown, and generate an agent-ready remediation plan.
- Search the rulebook: every rule, every WCAG 2.2 criterion, manual procedures, policies and articles.

## In this folder

| Folder or file | What it covers |
| --- | --- |
| [docs/](docs/README.md) | Guides and reference for Auric Accessibility. |
| [docs/getting-started.md](docs/getting-started.md) | First run and a tour. |
| [docs/editor-linting.md](docs/editor-linting.md) | Diagnostics, hovers, quick fixes and supported languages. |
| [docs/inspect.md](docs/inspect.md) | The Inspect card. |
| [docs/project-scans.md](docs/project-scans.md) | Scanning the project and reading the score. |
| [docs/project-issues-view.md](docs/project-issues-view.md) | The Project Issues tree. |
| [docs/check-space.md](docs/check-space.md) | The Studio's Findings and Preview tools. |
| [docs/rules.md](docs/rules.md) | Every rule, grouped by WCAG success criterion. |
| [docs/audit-profiles-and-contrast.md](docs/audit-profiles-and-contrast.md) | Audit profiles, WCAG 2.x and APCA contrast. |
| [docs/manual-evidence.md](docs/manual-evidence.md) | The manual test procedures and how to record evidence. |
| [docs/reference.md](docs/reference.md) | Every command, keybinding, setting, view and menu. |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Symptoms and fixes. |
| [docs/faq.md](docs/faq.md) | Short answers. |
| [others/](others/README.md) | Glossary, shortcuts, limits and accuracy, related pages, release notes and privacy. |

Shared Studio features are in the [Studio docs](../docs/README.md).

Back to the [Studio overview](../README.md).
