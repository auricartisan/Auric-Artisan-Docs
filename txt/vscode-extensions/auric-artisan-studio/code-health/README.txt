==============================================================================
AURIC CODE HEALTH — SECRETS, TODOS & RISK
==============================================================================
What Auric Code Health does, who it is for, how to install it, and a quick
start from first finding to CI record.
Area: VS Code extensions › Auric Artisan Studio › Auric Code Health   Updated: 2026-09-25

Auric Code Health is a language-agnostic hygiene scanner for every file in
your repository. It finds hardcoded secrets and credentials in URLs, security
footguns such as disabled TLS verification, weak hashing, unsafe
deserialization, command and SQL injection patterns and XSS sinks, risky APIs
such as `eval`, forgotten debug statements, task markers such as `TODO` and
`FIXME`, unresolved merge-conflict markers, and oversized lines and files. It
works in more than 40 languages.

It reads source text with argument-aware analysis: it can tell a constant from
a dynamic value, so `eval('use strict')` is downgraded while `eval(userInput)`
is reported with high confidence. Every finding has a stable signature ID, a
confidence level and a fix, and any secret it finds is redacted before it
reaches the editor, the Studio, reports or files. Findings appear as you type,
in a Code Health Studio with filters, and in `health.json` and SARIF 2.1.0
records for continuous integration (CI), with a bundled command-line scanner
for pull-request gates.

Auric Code Health is one of the four Auric Artisan Studio extensions. It works
on its own and joins the others in one Workstation. Everything runs on your
machine.

WHO IT IS FOR
=============

  - Developers in any language who want leftovers, secrets and risky patterns
    caught before they are committed.
  - Reviewers and tech leads who want a repeatable hygiene score for a
    repository.
  - Teams who want SARIF in GitHub code scanning and a CI gate that fails only
    on new issues.

It is a high-signal heuristic linter, not a full security scanner. Use it
alongside, not instead of, dedicated security tools where compliance requires
them.

WHERE TO FIND IT
================

  - Marketplace ID: `auric-artisan.auric-codehealth`
  - Marketplace page:
    https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-codehealth
  - Install: `code --install-extension auric-artisan.auric-codehealth`
  - Version 0.1.0; VS Code 1.74 or newer. Also installed by the Full Pack
    [../full-pack/README.txt].

QUICK START
===========

  1. Install Auric Code Health from the Extensions view (`Ctrl` + `Shift` +
     `X`).
  2. Open a project. Findings in open files are underlined and listed in the
     Problems panel with the source `auric-artisan`.
  3. Hover a finding for its title, category, confidence, priority and fix.
     Press `Ctrl` + `.` for Ignore this … finding here.
  4. Select the Auric Code Health icon in the Activity Bar. The Overview shows
     the code-health ring and seven category chips.
  5. Select Report. The Studio scans the project and writes the project health
     report; select Open in Browser to read the printable page.
  6. Run Auric Artisan: Open Code Health Studio to filter findings by
     category, confidence and text.
  7. Select health.json + SARIF to write the CI records to `.auric-artisan`.
  8. Read The CI gate [../docs/ci-gate.txt] to fail pull requests on new
     issues.

WHAT YOU CAN DO
===============

  - Find 24 kinds of hardcoded secret, including AWS, GitHub, GitLab, Slack,
    Google, Stripe, OpenAI, Anthropic, npm, SendGrid and DigitalOcean
    credentials, private keys, JWTs, webhook URLs, credentials in URLs and
    connection strings, and secret-named assignments, and add your own
    patterns.
  - Find disabled TLS verification, weak MD5 and SHA-1 hashing, unsafe
    deserialization, string timers, raw-HTML sinks, wildcard CORS, and command
    and SQL injection built from dynamic values.
  - Find risky APIs, leftover debug statements, task markers, merge markers,
    lines over 240 characters and files over 800 lines.
  - See confidence on every finding, and filter by it.
  - Silence one finding, one category or one file with a comment, inserted for
    you in the right syntax.
  - Score the repository from 0 to 100 with a letter grade.
  - Write `health.json`, SARIF 2.1.0 and a trend history, and a Markdown, JSON
    and HTML project health report covering colour, accessibility and code
    health.
  - Gate CI with the bundled scanner and a baseline, so only new issues fail a
    build.
  - Generate a local remediation plan with secret and security tasks.
  - Search the code-health rulebook, policies and official OWASP, CWE and NIST
    sources.

IN THIS FOLDER
==============

  Folder or file: docs/ [docs/README.txt]
  What it covers: Guides and reference for Auric Code Health.

  Folder or file: docs/getting-started.md [docs/getting-started.txt]
  What it covers: First run and a tour.

  Folder or file: docs/categories-and-signatures.md
                  [docs/categories-and-signatures.txt]
  What it covers: Every category and signature, what it detects and where.

  Folder or file: docs/secrets-and-redaction.md
                  [docs/secrets-and-redaction.txt]
  What it covers: How secrets are found, filtered, scored and redacted.

  Folder or file: docs/code-health-studio.md [docs/code-health-studio.txt]
  What it covers: The Health space in the Studio and the Overview.

  Folder or file: docs/health-records.md [docs/health-records.txt]
  What it covers: `health.json`, SARIF, history, fingerprints and baselines.

  Folder or file: docs/reference.md [docs/reference.txt]
  What it covers: Every command, keybinding, setting and view.

  Folder or file: docs/troubleshooting.md [docs/troubleshooting.txt]
  What it covers: Symptoms and fixes.

  Folder or file: docs/faq.md [docs/faq.txt]
  What it covers: Short answers.

  Folder or file: others/ [others/README.txt]
  What it covers: Glossary, shortcuts, limits and accuracy, related pages,
                  release notes and privacy.

Shared Studio features are in the Studio docs [../docs/README.txt].

Back to the Studio overview [../README.txt].
