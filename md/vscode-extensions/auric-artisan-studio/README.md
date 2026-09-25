---
title: Auric Artisan Studio — Colour, accessibility and code health for VS Code
description: What Auric Artisan Studio is, which of its four extensions to install, and how to get your first result in a few minutes.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Auric Artisan Studio

Auric Artisan Studio is a family of Visual Studio Code extensions that check and improve the colour, accessibility and code hygiene of your project while you write it. It is published as four Marketplace extensions: three focused extensions that each do one job, and a Full Pack that installs all three at once.

- **Auric Color — Picker, Palettes & Contrast** reads every colour literal in your code, shows its values and contrast in a hover, lets you edit it with a picker, flags text that is too faint to read, and generates accessible palettes and shade scales.
- **Auric Accessibility — WCAG 2.2 Linter** checks your markup and CSS against 70+ static rules mapped to the Web Content Accessibility Guidelines (WCAG) 2.0, 2.1 and 2.2, grades the whole project, and lets you inspect any element's name, role and colours on hover.
- **Auric Code Health — Secrets, TODOs & Risk** looks in every file, in more than 40 languages, for hardcoded secrets, security footguns, risky APIs, debug leftovers, task markers, merge markers and oversized code, and writes machine-readable records for continuous integration (CI).
- **Auric Artisan Studio — Full Pack** installs the three extensions above in one step.

Each extension works on its own. When you install two or three of them, they cooperate as one **Workstation**: one sidebar, one Command Center and one Studio tab that shows every capability you installed, instead of three separate dashboards. Everything runs on your machine. The extensions make no network requests, need no account and have no paid tier.

## Who it is for

- Front-end and full-stack developers who want contrast and accessibility problems caught in the editor, before review.
- Designers and design-system maintainers who manage colour tokens, palettes and brand colours in code.
- Accessibility specialists who want a searchable rulebook, manual test procedures and a prioritised worklist for a codebase.
- Teams that want a local, repeatable gate for pull requests, with SARIF output for code scanning.

## Where to find it

| Extension | Marketplace ID | Install command |
| --- | --- | --- |
| Auric Artisan Studio — Full Pack | `auric-artisan.auric-artisan` | `code --install-extension auric-artisan.auric-artisan` |
| Auric Color — Picker, Palettes & Contrast | `auric-artisan.auric-color` | `code --install-extension auric-artisan.auric-color` |
| Auric Accessibility — WCAG 2.2 Linter | `auric-artisan.auric-a11y` | `code --install-extension auric-artisan.auric-a11y` |
| Auric Code Health — Secrets, TODOs & Risk | `auric-artisan.auric-codehealth` | `code --install-extension auric-artisan.auric-codehealth` |

Marketplace pages:

- https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan
- https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-color
- https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-a11y
- https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-codehealth

All four need VS Code 1.74 or newer. The current version is 0.1.0. They work in single-folder and multi-root workspaces. Publisher website: https://auricartisan.com.

### Which extension should I install?

| If you mainly want to… | Install |
| --- | --- |
| Edit colours, check contrast as you type, build palettes and shade scales | Auric Color |
| Lint HTML, JSX, Vue, Svelte, Astro, PHP and CSS for WCAG problems and grade the project | Auric Accessibility |
| Find secrets, security footguns and debug leftovers in any language, and gate CI | Auric Code Health |
| All of the above in one Workstation | The Full Pack |

The page [Choose what to install](docs/choosing-an-install.md) compares the install shapes in detail, including which extension owns which feature when several are installed.

## Quick start

These steps assume the Full Pack. With a single extension, the same screens appear with only that extension's tools.

1. Open the Extensions view (`Ctrl` + `Shift` + `X`), search for **Auric Artisan Studio — Full Pack**, and select **Install**.
2. Open a project folder with **File › Open Folder…**. The extensions start automatically when VS Code finishes loading.
3. Select the Auric icon in the Activity Bar (the vertical bar at the far left). The **Overview** view opens with the Workstation card.
4. Select **Scan project** on the Overview. A progress notification appears while the Studio reads your stylesheets, templates and components. When it finishes, the score ring shows a 0–100 score and a letter grade.
5. Open a stylesheet or component. Problems are underlined with a violet wavy line. Hover one to see what is wrong, how urgent it is and how to fix it.
6. Press `Ctrl` + `Alt` + `.` (`Cmd` + `Alt` + `.` on macOS) to open the **Command Center**, a searchable list of suggested actions, tools, recent colours, findings and files the Studio has written.
7. Select **Studio** on the Overview (or the status-bar score) to open the Studio tab with the Home, Color, Check, Health and Brand spaces.
8. When you are ready to share results, run **Auric Artisan: Generate Project Health Report (Color, A11y & Code Health)**. It writes a Markdown, JSON and printable HTML report to the `.auric-artisan` folder in your workspace.

You should now see a score in the status bar, findings in the editor and a report you can open in your browser. The [getting started guide](docs/getting-started.md) walks through the same steps with a tour of every screen.

## What you can do

- Hover any colour literal in CSS, JavaScript, TypeScript, HTML, Vue, Svelte, Python, Go, Rust, YAML and many more languages to read its RGB, HSL, OKLCH and Display-P3 values, its contrast on white and black, and how it looks to people with colour-vision deficiency.
- Edit colours in place with a picker in the hover, a full spectrum picker beside the editor, or a picker docked in the sidebar.
- Catch low-contrast text as you type, including text that uses CSS custom properties, CSS-in-JS and dark themes, and fix it with one click to the nearest passing colour of the same hue.
- Open any failing pair in the **Contrast Studio**, see where its token is used, and write the fix back to the token so every use follows.
- Lint markup and CSS against 70+ WCAG rules with an audit profile for WCAG 2.0, 2.1, 2.2 or the 3.0 draft, and apply safe fixes from the hover.
- Inspect any element or CSS rule for its accessible name, role, colours, contrast and colour-vision impact, with a before-and-after preview.
- Scan the whole project, browse findings grouped by type, file or severity, and see a prioritised list of files to fix first.
- Find hardcoded secrets (with the secret itself redacted everywhere), injection and TLS-bypass patterns, weak cryptography and debug leftovers in more than 40 languages.
- Write `health.json`, SARIF 2.1.0 and a trend history for CI, and gate pull requests on new issues only with the bundled command-line scanner.
- Generate an agent-ready remediation plan: a deterministic, local backlog of fixes and a prompt you can give to a coding agent you already use.
- Search a local rulebook and knowledge database covering every rule, all 86 WCAG 2.2 success criteria and eight manual test procedures, and add your team's own guidance.
- Mark deliberate brand colours as intentional branding so they stay visible but leave the score, while structural failures can never be waived.
- Re-theme the Studio with 13 accent presets or any custom colour.

## In this folder

This folder documents the Studio as a whole and each extension in its own subfolder.

| Folder or file | What it covers |
| --- | --- |
| [docs/](docs/README.md) | Guides and reference shared by all four extensions: the Workstation, the Overview, the Command Center, the Studio, scanning, scores, reports, the CI gate and more. |
| [others/](others/README.md) | Glossary, shortcuts, limits and accuracy, related tools, release notes and privacy for the whole Studio. |
| [full-pack/](full-pack/README.md) | The Full Pack: what it installs and how to enable, disable or remove its members. |
| [color/](color/README.md) | Auric Color: hover, swatches, pickers, contrast diagnostics, palettes, shades, colour vision and the brand audit. |
| [accessibility/](accessibility/README.md) | Auric Accessibility: editor linting, Inspect, project scans, every rule by WCAG success criterion, profiles and manual evidence. |
| [code-health/](code-health/README.md) | Auric Code Health: every finding category and signature, redaction, health records, SARIF and baselines. |

### docs/

| File | What it covers |
| --- | --- |
| [README](docs/README.md) | Contents of the shared docs. |
| [Getting started](docs/getting-started.md) | Install, first scan and a tour of every screen. |
| [Choose what to install](docs/choosing-an-install.md) | The four extensions compared and who owns which feature. |
| [The Workstation](docs/workstation.md) | How co-installed extensions become one product. |
| [The Overview view](docs/overview-view.md) | The sidebar home in each of its three layouts. |
| [The Command Center](docs/command-center.md) | The `Ctrl` + `Alt` + `.` list and the smart suggestions. |
| [The Studio](docs/studio.md) | The Studio tab, its spaces, Home, Findings and Settings. |
| [The Contrast Studio](docs/contrast-studio.md) | Tuning one pair and writing the fix back to its file or token. |
| [Scanning](docs/scanning.md) | Project scans, live re-grading, the cache, `.auricignore` and the data folder. |
| [Scores and grades](docs/scores-and-grades.md) | How every score is calculated. |
| [Suppression and branding](docs/suppression-and-branding.md) | `auric-disable-*` and `auric-brand-*` comments. |
| [Exports and health records](docs/exports-and-records.md) | The project health report, `health.json`, SARIF, history and exports. |
| [The remediation plan](docs/remediation-plan.md) | The agent-ready fix plan. |
| [Rulebook and knowledge database](docs/rulebook-and-knowledge.md) | Searching rules and adding team guidance. |
| [The CI gate](docs/ci-gate.md) | The `auric-artisan` command-line scanner. |
| [The Icon Studio bridge](docs/icon-studio-bridge.md) | Opening the combined Auric icon library. |
| [Appearance](docs/appearance.md) | Accent colours, themes and high contrast. |
| [Accessibility of the Studio](docs/studio-accessibility.md) | Using the Studio with a keyboard and screen reader. |
| [Reference](docs/reference.md) | Every command, shortcut, setting and file in one place. |
| [Troubleshooting](docs/troubleshooting.md) | Symptoms, causes and fixes. |
| [FAQ](docs/faq.md) | Short answers. |

### others/

| File | What it covers |
| --- | --- |
| [README](others/README.md) | Contents of this folder. |
| [Glossary](others/glossary.md) | Every term used in these docs. |
| [Shortcuts](others/shortcuts.md) | Keyboard shortcuts and Command Palette titles. |
| [Limits and accuracy](others/limits-and-accuracy.md) | What the checks measure and what they cannot. |
| [Related](others/related.md) | Related extensions, website tools and articles. |
| [Release notes](others/release-notes.md) | Version history from the changelog. |
| [Privacy](others/privacy.md) | What stays on your machine and what is written to disk. |
