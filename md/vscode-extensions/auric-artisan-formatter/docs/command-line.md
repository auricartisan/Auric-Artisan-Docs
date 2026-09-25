---
title: Auric Artisan Formatter — command line and CI
description: Run the same Auric formatting engine from a terminal with auric-format, check formatting in CI, and use its flags and exit codes.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Command line and CI

`auric-format` runs the same engine, options, configuration files and safety gate as the extension, from a terminal. Use it to check formatting in continuous integration (CI) or to format many files in a script.

## Where it is

The command line ships inside the installed extension as the script `bin/auric-format.js`. It needs Node.js 16 or newer. It is not published as a separate npm package at the time of writing.

VS Code installs extensions in a folder named after the extension and version, for example:

```text
~/.vscode/extensions/auric-artisan.auric-artisan-formatter-0.1.0/bin/auric-format.js
```

On Windows, `~` is your user folder (`%USERPROFILE%`). Run it with Node:

```text
node ~/.vscode/extensions/auric-artisan.auric-artisan-formatter-0.1.0/bin/auric-format.js --check .
```

The examples below write `auric-format` for short. To use the bare name, create a shell alias or a small wrapper script that runs the command above. A CI machine needs the extension's files available in the same way; the engine itself has no runtime dependencies beyond Node.js.

## Common tasks

```text
auric-format --write src              # rewrite files in place
auric-format --check .                # exit 1 if anything is unformatted
auric-format --preset prettier -w .   # start from a preset
cat a.css | auric-format --stdin-filepath a.css
auric-format --explain src/weird.scss # why did it do that?
```

## Flags

| Flag | What it does |
| --- | --- |
| `-w`, `--write` | Rewrite each file in place |
| `-c`, `--check` | Report which files need formatting, change nothing, exit non-zero if any do |
| `-l`, `--list-different` | Print the names of files that differ from the formatted output |
| `--stdin-filepath <path>` | Treat standard input as this path, to pick a language and find configuration |
| `--config <path>` | Use this configuration file instead of searching |
| `--no-config` | Do not look for a configuration file |
| `--ignore-path <path>` | Use this ignore file instead of `.auricformatignore` |
| `--no-ignore` | Do not read any ignore file |
| `--no-editorconfig` | Do not read `.editorconfig` |
| `--preset <name>` | Start from a named preset |
| `--parser <name>` | Force a parser instead of inferring one |
| `--explain` | Explain the formatting decisions for each file instead of formatting |
| `--support-info` | Print the languages, parsers and options this build supports, as JSON |
| `--list-languages` | Print every supported language with its tier and extensions |
| `--list-presets` | Print every preset with its description |
| `--find-config` | Print the configuration file that would be used for the given path |
| `--loglevel <level>` | `silent`, `error`, `warn`, `log` or `debug` (default `log`) |
| `--concurrency <n>` | How many files to format at once (default: the number of processors) |
| `-v`, `--version` | Print the version |
| `-h`, `--help` | Print help |

`--check`, `--write`, `--list-different`, `--stdin-filepath`, `--config`, `--ignore-path` and `--no-config` behave as they do in Prettier's command line.

### Formatting options as flags

Every one of the 391 options is also a flag, written in kebab case: `printWidth` is `--print-width`. Booleans take a `--no-` form to switch them off. For example:

```text
auric-format --print-width 100 --single-quote --trailing-comma es5 --no-semi -w src
```

A mistyped flag suggests the one you probably meant. See the [options reference](options-reference.md) for every option.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Every file is formatted (or was formatted successfully) |
| `1` | Files need formatting, or one failed |
| `2` | A usage error, such as an unknown flag |

## Use it in CI

Add a step that runs the check and fails the build when anything is unformatted:

```text
node path/to/auric-format.js --check .
```

Output is deterministic: no clock, no randomness and no locale-dependent ordering, so the same input and configuration always give the same result on every machine.

Inside VS Code, **Auric Formatter: Check Formatting Without Writing (CI Mode)** runs the same check and lists the results in the Problems panel.

When the check passes, the command exits with code `0` and reports nothing to fix.
