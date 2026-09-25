==============================================================================
AURIC ARTISAN STUDIO
==============================================================================
What Auric Artisan Studio is, which of its four extensions to install, and how
to get your first result in a few minutes.
Area: VS Code extensions › Auric Artisan Studio   Updated: 2026-09-25

Auric Artisan Studio is a family of Visual Studio Code extensions that check
and improve the colour, accessibility and code hygiene of your project while
you write it. It is published as four Marketplace extensions: three focused
extensions that each do one job, and a Full Pack that installs all three at
once.

  - Auric Color — Picker, Palettes & Contrast reads every colour literal in
    your code, shows its values and contrast in a hover, lets you edit it with
    a picker, flags text that is too faint to read, and generates accessible
    palettes and shade scales.
  - Auric Accessibility — WCAG 2.2 Linter checks your markup and CSS against
    70+ static rules mapped to the Web Content Accessibility Guidelines (WCAG)
    2.0, 2.1 and 2.2, grades the whole project, and lets you inspect any
    element's name, role and colours on hover.
  - Auric Code Health — Secrets, TODOs & Risk looks in every file, in more
    than 40 languages, for hardcoded secrets, security footguns, risky APIs,
    debug leftovers, task markers, merge markers and oversized code, and
    writes machine-readable records for continuous integration (CI).
  - Auric Artisan Studio — Full Pack installs the three extensions above in
    one step.

Each extension works on its own. When you install two or three of them, they
cooperate as one Workstation: one sidebar, one Command Center and one Studio
tab that shows every capability you installed, instead of three separate
dashboards. Everything runs on your machine. The extensions make no network
requests, need no account and have no paid tier.

WHO IT IS FOR
=============

  - Front-end and full-stack developers who want contrast and accessibility
    problems caught in the editor, before review.
  - Designers and design-system maintainers who manage colour tokens, palettes
    and brand colours in code.
  - Accessibility specialists who want a searchable rulebook, manual test
    procedures and a prioritised worklist for a codebase.
  - Teams that want a local, repeatable gate for pull requests, with SARIF
    output for code scanning.

WHERE TO FIND IT
================

  Extension:       Auric Artisan Studio — Full Pack
  Marketplace ID:  `auric-artisan.auric-artisan`
  Install command: `code --install-extension auric-artisan.auric-artisan`

  Extension:       Auric Color — Picker, Palettes & Contrast
  Marketplace ID:  `auric-artisan.auric-color`
  Install command: `code --install-extension auric-artisan.auric-color`

  Extension:       Auric Accessibility — WCAG 2.2 Linter
  Marketplace ID:  `auric-artisan.auric-a11y`
  Install command: `code --install-extension auric-artisan.auric-a11y`

  Extension:       Auric Code Health — Secrets, TODOs & Risk
  Marketplace ID:  `auric-artisan.auric-codehealth`
  Install command: `code --install-extension auric-artisan.auric-codehealth`

Marketplace pages:

  - https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan
  - https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-color
  - https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-a11y
  - https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-codehealth

All four need VS Code 1.74 or newer. The current version is 0.1.0. They work
in single-folder and multi-root workspaces. Publisher website:
https://auricartisan.com.

Which extension should I install?
---------------------------------

  If you mainly want to…: Edit colours, check contrast as you type, build
                          palettes and shade scales
  Install:                Auric Color

  If you mainly want to…: Lint HTML, JSX, Vue, Svelte, Astro, PHP and CSS for
                          WCAG problems and grade the project
  Install:                Auric Accessibility

  If you mainly want to…: Find secrets, security footguns and debug leftovers
                          in any language, and gate CI
  Install:                Auric Code Health

  If you mainly want to…: All of the above in one Workstation
  Install:                The Full Pack

The page Choose what to install [docs/choosing-an-install.txt] compares the
install shapes in detail, including which extension owns which feature when
several are installed.

QUICK START
===========

These steps assume the Full Pack. With a single extension, the same screens
appear with only that extension's tools.

  1. Open the Extensions view (`Ctrl` + `Shift` + `X`), search for Auric
     Artisan Studio — Full Pack, and select Install.
  2. Open a project folder with File › Open Folder…. The extensions start
     automatically when VS Code finishes loading.
  3. Select the Auric icon in the Activity Bar (the vertical bar at the far
     left). The Overview view opens with the Workstation card.
  4. Select Scan project on the Overview. A progress notification appears
     while the Studio reads your stylesheets, templates and components. When
     it finishes, the score ring shows a 0–100 score and a letter grade.
  5. Open a stylesheet or component. Problems are underlined with a violet
     wavy line. Hover one to see what is wrong, how urgent it is and how to
     fix it.
  6. Press `Ctrl` + `Alt` + `.` (`Cmd` + `Alt` + `.` on macOS) to open the
     Command Center, a searchable list of suggested actions, tools, recent
     colours, findings and files the Studio has written.
  7. Select Studio on the Overview (or the status-bar score) to open the
     Studio tab with the Home, Color, Check, Health and Brand spaces.
  8. When you are ready to share results, run Auric Artisan: Generate Project
     Health Report (Color, A11y & Code Health). It writes a Markdown, JSON and
     printable HTML report to the `.auric-artisan` folder in your workspace.

You should now see a score in the status bar, findings in the editor and a
report you can open in your browser. The getting started guide
[docs/getting-started.txt] walks through the same steps with a tour of every
screen.

WHAT YOU CAN DO
===============

  - Hover any colour literal in CSS, JavaScript, TypeScript, HTML, Vue,
    Svelte, Python, Go, Rust, YAML and many more languages to read its RGB,
    HSL, OKLCH and Display-P3 values, its contrast on white and black, and how
    it looks to people with colour-vision deficiency.
  - Edit colours in place with a picker in the hover, a full spectrum picker
    beside the editor, or a picker docked in the sidebar.
  - Catch low-contrast text as you type, including text that uses CSS custom
    properties, CSS-in-JS and dark themes, and fix it with one click to the
    nearest passing colour of the same hue.
  - Open any failing pair in the Contrast Studio, see where its token is used,
    and write the fix back to the token so every use follows.
  - Lint markup and CSS against 70+ WCAG rules with an audit profile for WCAG
    2.0, 2.1, 2.2 or the 3.0 draft, and apply safe fixes from the hover.
  - Inspect any element or CSS rule for its accessible name, role, colours,
    contrast and colour-vision impact, with a before-and-after preview.
  - Scan the whole project, browse findings grouped by type, file or severity,
    and see a prioritised list of files to fix first.
  - Find hardcoded secrets (with the secret itself redacted everywhere),
    injection and TLS-bypass patterns, weak cryptography and debug leftovers
    in more than 40 languages.
  - Write `health.json`, SARIF 2.1.0 and a trend history for CI, and gate pull
    requests on new issues only with the bundled command-line scanner.
  - Generate an agent-ready remediation plan: a deterministic, local backlog
    of fixes and a prompt you can give to a coding agent you already use.
  - Search a local rulebook and knowledge database covering every rule, all 86
    WCAG 2.2 success criteria and eight manual test procedures, and add your
    team's own guidance.
  - Mark deliberate brand colours as intentional branding so they stay visible
    but leave the score, while structural failures can never be waived.
  - Re-theme the Studio with 13 accent presets or any custom colour.

IN THIS FOLDER
==============

This folder documents the Studio as a whole and each extension in its own
subfolder.

  Folder or file: docs/ [docs/README.txt]
  What it covers: Guides and reference shared by all four extensions: the
                  Workstation, the Overview, the Command Center, the Studio,
                  scanning, scores, reports, the CI gate and more.

  Folder or file: others/ [others/README.txt]
  What it covers: Glossary, shortcuts, limits and accuracy, related tools,
                  release notes and privacy for the whole Studio.

  Folder or file: full-pack/ [full-pack/README.txt]
  What it covers: The Full Pack: what it installs and how to enable, disable
                  or remove its members.

  Folder or file: color/ [color/README.txt]
  What it covers: Auric Color: hover, swatches, pickers, contrast diagnostics,
                  palettes, shades, colour vision and the brand audit.

  Folder or file: accessibility/ [accessibility/README.txt]
  What it covers: Auric Accessibility: editor linting, Inspect, project scans,
                  every rule by WCAG success criterion, profiles and manual
                  evidence.

  Folder or file: code-health/ [code-health/README.txt]
  What it covers: Auric Code Health: every finding category and signature,
                  redaction, health records, SARIF and baselines.

docs/
-----

  File:           README [docs/README.txt]
  What it covers: Contents of the shared docs.

  File:           Getting started [docs/getting-started.txt]
  What it covers: Install, first scan and a tour of every screen.

  File:           Choose what to install [docs/choosing-an-install.txt]
  What it covers: The four extensions compared and who owns which feature.

  File:           The Workstation [docs/workstation.txt]
  What it covers: How co-installed extensions become one product.

  File:           The Overview view [docs/overview-view.txt]
  What it covers: The sidebar home in each of its three layouts.

  File:           The Command Center [docs/command-center.txt]
  What it covers: The `Ctrl` + `Alt` + `.` list and the smart suggestions.

  File:           The Studio [docs/studio.txt]
  What it covers: The Studio tab, its spaces, Home, Findings and Settings.

  File:           The Contrast Studio [docs/contrast-studio.txt]
  What it covers: Tuning one pair and writing the fix back to its file or
                  token.

  File:           Scanning [docs/scanning.txt]
  What it covers: Project scans, live re-grading, the cache, `.auricignore`
                  and the data folder.

  File:           Scores and grades [docs/scores-and-grades.txt]
  What it covers: How every score is calculated.

  File:           Suppression and branding [docs/suppression-and-branding.txt]
  What it covers: `auric-disable-*` and `auric-brand-*` comments.

  File:           Exports and health records [docs/exports-and-records.txt]
  What it covers: The project health report, `health.json`, SARIF, history and
                  exports.

  File:           The remediation plan [docs/remediation-plan.txt]
  What it covers: The agent-ready fix plan.

  File:           Rulebook and knowledge database
                  [docs/rulebook-and-knowledge.txt]
  What it covers: Searching rules and adding team guidance.

  File:           The CI gate [docs/ci-gate.txt]
  What it covers: The `auric-artisan` command-line scanner.

  File:           The Icon Studio bridge [docs/icon-studio-bridge.txt]
  What it covers: Opening the combined Auric icon library.

  File:           Appearance [docs/appearance.txt]
  What it covers: Accent colours, themes and high contrast.

  File:           Accessibility of the Studio [docs/studio-accessibility.txt]
  What it covers: Using the Studio with a keyboard and screen reader.

  File:           Reference [docs/reference.txt]
  What it covers: Every command, shortcut, setting and file in one place.

  File:           Troubleshooting [docs/troubleshooting.txt]
  What it covers: Symptoms, causes and fixes.

  File:           FAQ [docs/faq.txt]
  What it covers: Short answers.

others/
-------

  File:           README [others/README.txt]
  What it covers: Contents of this folder.

  File:           Glossary [others/glossary.txt]
  What it covers: Every term used in these docs.

  File:           Shortcuts [others/shortcuts.txt]
  What it covers: Keyboard shortcuts and Command Palette titles.

  File:           Limits and accuracy [others/limits-and-accuracy.txt]
  What it covers: What the checks measure and what they cannot.

  File:           Related [others/related.txt]
  What it covers: Related extensions, website tools and articles.

  File:           Release notes [others/release-notes.txt]
  What it covers: Version history from the changelog.

  File:           Privacy [others/privacy.txt]
  What it covers: What stays on your machine and what is written to disk.
