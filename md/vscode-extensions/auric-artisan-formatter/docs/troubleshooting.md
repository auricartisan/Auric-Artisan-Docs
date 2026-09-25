---
title: Auric Artisan Formatter — troubleshooting
description: Symptoms, causes and fixes for common Auric Artisan Formatter problems.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Troubleshooting

For anything not listed, run **Auric Formatter: Report a Formatting Problem**, add what happened and a small sample file, and see [Get support](../../install-and-setup/docs/get-support.md). **Show the Formatter Log** has the details of each run; set `auricFormatter.logLevel` to `debug` for more.

## Nothing happens when I save

- **Why:** Auric is not the default formatter, format on save is off, or the language is excluded.
- **Fix:** run **Toggle Format on Save**, or check `editor.defaultFormatter` and `editor.formatOnSave` (including language-specific blocks such as `"[typescript]"`). Check `auricFormatter.enabledLanguages` and `auricFormatter.disabledLanguages`.

## VS Code asks which formatter to use on every save

- **Why:** several formatters are installed and no default is set.
- **Fix:** run **Toggle Format on Save**, which sets `editor.defaultFormatter`, or set it yourself per language.

## The status bar shows a shield: "your original text was kept"

- **Why:** a safety check failed, so the formatter refused to change the file.
- **Fix:** open the log to see which check failed and where. Often the file has a construct the parser does not handle yet; the file is safe as it is. Report it with **Report a Formatting Problem** if you think the change should have been allowed.

## The file was skipped

- **Why:** it is larger than `auricFormatter.maxFileSizeKb`, looks minified, is in `.auricformatignore` or `.prettierignore`, has an ignore directive, or `requirePragma` is on and it has no `@format`.
- **Fix:** hover the status bar item for the reason. Raise the size limit, turn on `auricFormatter.formatMinified`, or remove the ignore entry, as appropriate.

## JSX or TSX is only indented, not reformatted

- **Why:** in version 0.1.0 a file containing JSX elements falls back to the universal tier.
- **Fix:** none yet; the output is still safe. Plain TypeScript in `.tsx` files is formatted natively.

## A language is only lightly formatted

- **Why:** it uses the universal tier, which only changes whitespace, and for some languages only spacing or only trailing whitespace. See [Supported languages](supported-languages.md).
- **Fix:** none needed; this is deliberate so the meaning cannot change.

## My configuration file is ignored

- **Why:** another file takes precedence, the workspace is untrusted and the file is JavaScript, the JavaScript file is an ES module, or the cache is stale.
- **Fix:** run **Explain Formatting Decisions** to see which file and layer set each option. Trust the workspace, rename an ES module config to `.cjs` or use `.auricformatrc.json`, and run **Clear the Configuration Cache**.

## Output matches Prettier, not the Auric style

- **Why:** the project has only a Prettier configuration, so the `prettier` preset was adopted automatically.
- **Fix:** add an `.auricformatrc` with the preset you want, or run **Import Settings From Prettier** and remove `"preset": "prettier"`.

## "Select some code first."

- **Fix:** select text before **Format Selection**.

## Preview problems

- **"The source changed. Refresh the preview before applying."** — you edited the source after opening the preview. Refresh, review, then apply.
- **"Close or discard an existing formatting preview before opening another."** — 24 previews are open. Discard some.
- **"focus the source editor to create a preview."** — the preview itself is focused. Click in the source file first.
- **No preview opened, with a warning** — formatting failed or the safety gate refused the change; the warning says which.

## Formatter Studio problems

- **"Preview is limited to 200,000 characters."** — use editor formatting or the native preview for larger files.
- **"Unsupported rule: *name*"** — the custom rules JSON contains a name that is not a formatting option (or a range option). Check the spelling in the [options reference](options-reference.md).
- **"The file changed since this preview. Reload from the editor and review again."** — select **Reload editor** and review again before **Yes, apply**.
- **A blank or scratch preview cannot be applied** — text typed into Studio, or a truncated preview, can only be copied.

## Workspace scan problems

- **The status bar shows no count** — the scan is off (`auricFormatter.scanOnStartup`) or no folder is open. Run **Scan the Workspace Without Writing**.
- **Files are missing from the scan** — they match `auricFormatter.scanExclude` or the built-in exclusions, exceed `maxFileSizeKb`, or the scan stopped at `scanMaxFiles`.
- **Format Every File in the Workspace formatted more than one folder** — in this version it formats every pending file in the workspace. Use the Workspace tab's tick boxes and **Format selected** to take one folder at a time.

## "No Prettier configuration found in this workspace."

- **Why:** **Import Settings From Prettier** found no `.prettierrc`, `.prettierrc.json`, `.prettierrc.yaml`, `.prettierrc.yml`, `.prettierrc.js` or `prettier.config.js` outside `node_modules`.
- **Fix:** none needed if you do not use Prettier; create a configuration with **Generate a Configuration File** instead.

## The command line is not found

- **Why:** `auric-format` is a script inside the installed extension, not a command on your `PATH`.
- **Fix:** run it with Node from the extension folder, or create an alias. See [Command line and CI](command-line.md).
