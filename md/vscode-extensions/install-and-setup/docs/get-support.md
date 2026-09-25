---
title: Get support for an Auric Artisan extension
description: Where to send a bug or question about an Auric Artisan VS Code extension, and how to gather the details that make it quick to solve.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Get support

## Where to ask

- **Contact Auric Artisan:** https://auricartisan.com/company/contact/ — the support address listed on every extension's Marketplace page.
- **Frequently asked questions:** https://auricartisan.com/company/faq/ — linked from the Marketplace pages as the place for questions.

## What to include

Collect these before you write. Each item saves a round of questions.

1. **The extension and its version.** Open the Extensions view, select the extension and read the version on its page, or run `code --list-extensions --show-versions` in a terminal.
2. **Your editor and its version.** In VS Code, **Help** › **About** has a **Copy** button. If you use Cursor, Windsurf, VSCodium or another fork, say so.
3. **Your operating system**, and whether you are working locally, over Remote SSH, in WSL, in a container or in a virtual workspace.
4. **What you did, what you expected and what happened.** A short numbered list of steps is best. Say which command, button or setting you used.
5. **The file language** (for example TypeScript or PHP) if the problem involves a file.
6. **The log or built-in summary** described below for your extension.

Before sending, remove private paths, secrets, tokens, customer data and the contents of private files. Reduce the example to the smallest file that still shows the problem.

## Logs and built-in summaries

### Auric Artisan Live

- **Auric Live: Show Log** opens the **Auric Artisan Live** output channel.
- **Auric Live: Diagnose Project and Runtime** opens a local diagnostic summary with credential fields redacted.
- **Auric Live: Show Dev Server Output** shows a run target's output.
- Set `auricLive.logLevel` to `debug` for more detail.

### Auric Artisan File System

- **Auric Files: Show Log** opens the **Auric Artisan File System** output channel.
- Set `auricFiles.logLevel` to `debug` for per-step detail. Paths are logged relative to the workspace and file contents are never written.

### Auric Artisan Font Hub

- **Auric Font Hub: Show Logs** opens the log.
- For fonts that do not load in a browser, run **Auric Artisan Font Hub: Check Font CDN and Browser CORS** and include the result.

### Auric Artisan Formatter

- **Auric Formatter: Report a Formatting Problem** opens a Markdown document with the formatter version, VS Code version, language, tier and the explanation for the active file. Add what happened and attach a small input file.
- **Auric Formatter: Show the Formatter Log** shows the log.

For other extensions, use the extension's own log command if it has one (search the Command Palette for the extension's prefix and "log"), and see that extension's documentation folder.

## Check before you send

- The Live diagnostic summary and log redact common credential fields, but free text can still contain private data. Read it first.
- The Formatter's problem template includes the explanation for your active file, not the file itself. Attach only a sample you are happy to share.
- Screenshots help with layout problems. Crop out anything private.

You should receive a reply through the contact channel you used.
