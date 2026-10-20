---
title: Auric Artisan Formatter — configuration
description: Configure Auric Artisan Formatter with presets, configuration files, per-language and per-file overrides, .editorconfig, Prettier settings, inline directives and ignore files.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Configuration

The formatter has 391 options (see the [options reference](options-reference.md)). You rarely need more than a handful: start from a preset and set only what you disagree with.

## Where options come from

From lowest to highest precedence:

1. **A preset** — `"preset": "prettier"` and twelve others. See [Presets](presets.md).
2. **A configuration file** — see the list below.
3. **`.editorconfig`** — for the options it can express.
4. **VS Code settings** under `auricFormatter.*`, a command-line flag, or an inline directive in the file itself.

Inside a configuration file, `languages` (by language id) and `overrides` (by file pattern) beat the file's top-level values.

**Auric Formatter: Explain Formatting Decisions for This File** shows which layer set each option for the current file.

## Configuration files

The formatter looks for the first of these files, searching from the file's folder upward. Within a folder, this order is the precedence:

| File | Format |
| --- | --- |
| `.auricformatrc` | JSON or YAML, detected automatically |
| `.auricformatrc.json` | JSON |
| `.auricformatrc.yaml`, `.auricformatrc.yml` | YAML |
| `.auricformatrc.js`, `.auricformatrc.cjs` | JavaScript (CommonJS) |
| `.auricformat.config.js`, `.auricformat.config.cjs` | JavaScript (CommonJS) |
| `auric.format.json` | JSON |
| `package.json` | Under an `auricFormatter` (or `auric-formatter`) key |
| `.prettierrc`, `.prettierrc.json`, `.prettierrc.yaml`, `.prettierrc.yml`, `.prettierrc.js`, `prettier.config.js` | Prettier configuration, read for compatibility |
| `package.json` | Under a `prettier` key |

Auric files come first, so adding one to a Prettier project is additive; Prettier files come last, so an existing project keeps working untouched. JSON configuration files get validation and completion in VS Code for `.auricformatrc`, `.auricformatrc.json` and `auric.format.json`.

JavaScript configuration files are not run in an untrusted workspace. A JavaScript file written as an ES module must be renamed to `.cjs`, converted to CommonJS, or replaced with `.auricformatrc.json`.

### An example

```json
{
  "preset": "prettier",
  "printWidth": 100,
  "languages": {
    "markdown": { "proseWrap": "always" }
  },
  "overrides": [
    { "files": "**/*.test.ts", "options": { "printWidth": 200 } }
  ]
}
```

- `preset` — the starting point.
- Top-level options — apply to every file.
- `languages` — options for one language id.
- `overrides` — options for files matching a glob.

## Create a configuration file

- **Auric Formatter: Generate a Configuration File** writes `.auricformatrc` in the first workspace folder, with your current preset and the options you have set in VS Code settings, and opens it.
- **Copy config** in Formatter Studio copies only the options you changed, ready to paste.

## Choose a preset

- **Auric Formatter: Switch Formatting Preset** — pick from the 13 presets (**Every option you set yourself still wins over the preset**). It saves `auricFormatter.preset` in the workspace settings (or user settings with no folder open) and re-runs the workspace scan.
- Or write `"preset": "<name>"` in a configuration file; that wins over the VS Code setting.
- Or put `@auric-preset <name>` in a file's leading comment for that file.

## Coming from Prettier

If a project only has Prettier configuration, the formatter reads it and adopts the `prettier` preset automatically, so the output matches Prettier 3 at its defaults with every Auric-only enhancement off.

**Auric Formatter: Import Settings From Prettier** finds the first Prettier configuration in the workspace (outside `node_modules`) and opens an unsaved JSONC document containing the equivalent Auric configuration, starting from the `prettier` preset, with comments. Save it as `.auricformatrc` when you are happy. If there is no Prettier configuration: **No Prettier configuration found in this workspace.**

`.prettierignore` and Prettier's `prettier-ignore` comments are honoured too.

## .editorconfig

With `auricFormatter.editorconfig` on (the default), the formatter reads `.editorconfig` and uses `indent_style`, `indent_size`, `end_of_line`, `max_line_length` and the final-newline settings.

## VS Code settings

Every option is also a VS Code setting, `auricFormatter.<option>`, with resource scope, so it can be set for the user, the workspace or one folder of a multi-root workspace. Search Settings for `auricFormatter`.

## Inline directives

Put directives in a comment, in the file's own comment syntax. File-level directives only count at the top of the file, before any code (a byte order mark, shebang, XML declaration, front matter and earlier comments are allowed before them). A directive must be the whole content of its comment line, optionally followed by a reason, so a comment that merely mentions one does nothing.

| Directive | Effect |
| --- | --- |
| `auric-format-ignore` | Leave the next node unformatted |
| `auric-format-ignore-file` | Leave the whole file unformatted |
| `auric-format-ignore-start` … `auric-format-ignore-end` | Leave everything between unformatted |
| `auric-format-off` … `auric-format-on` | The same, other spelling |
| `@auric printWidth=120 singleQuote` | Options for this file only |
| `@auric-preset compact` | A preset for this file only |
| `@format` | Marks the file as opted in when `requirePragma` is on |

Each directive also works with the short `auric` spelling and the `prettier` spelling (such as `prettier-ignore`). `@auric-format`, `@auric` and `@prettier` also mark a file as opted in.

Related options: `auricFormatter.respectIgnoreComments` (honour ignore comments; on by default), `auricFormatter.requirePragma` (format only files with the pragma), `auricFormatter.insertPragma` (add `@format` to formatted files) and `auricFormatter.pragmaKeyword`.

A malformed option value in a directive becomes a warning; the directive is dropped and the file still formats.

## Ignore files

- `.auricformatignore` uses `.gitignore` syntax. Files it matches are not formatted by the editor, the scan or the command line.
- `.prettierignore` is honoured too.
- The command line can use a different file with `--ignore-path`, or none with `--no-ignore`.

## Plugins

`auricFormatter.plugins` lists additional formatter plugins by module path or registered name. Plugin languages go through the same option handling and safety gate as the built-ins, and a plugin that fails disables itself with a warning. Plugins are not run in an untrusted workspace.

## Clear the cache

The formatter caches configuration it has read. If a change to a configuration file does not seem to apply, run **Auric Formatter: Clear the Configuration Cache** (**Auric Formatter: configuration cache cleared.**).

When your configuration is in place, **Explain Formatting Decisions** for any file lists your file as the source of the options you set.
