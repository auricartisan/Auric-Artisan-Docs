---
title: Auric Artisan Formatter — the safety gate and formatting tiers
description: How Auric Artisan Formatter checks every result before it reaches your file, what the native and universal tiers can change, and how to see why a file was formatted as it was.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# The safety gate and formatting tiers

A formatter rewrites your source. That is only acceptable if it can show it did not change what the source means. Auric Artisan Formatter checks every file before you see the result.

## The five checks

| Check | What it proves | Option |
| --- | --- | --- |
| **Token stream** | The output re-reads to the same significant tokens as the input: no dropped argument, swallowed operator or mangled string | `safetyTokenCheck` (and `safetyTokenCheckComments` to include comments) |
| **Comments** | Every comment in the input appears in the output | `safetyCommentPreservation` |
| **String literals** | Every string and template keeps the same content | `safetyStringLiterals` |
| **Reparse** | The output parses again with the same parser | `safetyReparse` |
| **Idempotency** | Formatting the output again gives identical bytes | `safetyIdempotency` (off by default; `safetyIdempotencyPasses` sets the extra passes) |

`safetyNumericLiterals` also requires every number to keep its value when its spelling changes.

The gate knows which changes your options allow. With `singleQuote` on, it expects quotes to change; with `cssTrailingSemicolon` on, it knows the last `;` before `}` is optional in CSS. A change your options do not allow is treated as corruption and reverted.

## When a check fails

**Your original text is kept** — not partly applied, not a best effort. The status bar shows **Auric** with a shield and a warning background (**your original text was kept**), and the log records which check failed and where. Run **Auric Formatter: Show the Formatter Log** to read it.

`auricFormatter.safetyOnFailure` decides what happens:

| Value | Behaviour |
| --- | --- |
| `preserve` (default) | Return the original text unchanged, with a warning |
| `warn` | Return the formatted text, with a warning describing the check that failed |
| `throw` | Fail the whole run with a safety error, which is what CI wants (used by the `verified` preset) |

Because `warn` lets unverified output through, keep `preserve` unless you have a specific reason.

You can switch individual checks off with the `safety*` options, for example to save time on very large files, but they are the reason the formatter can safely be aggressive about layout. The `verified` preset turns every check on.

## The tiers

Not every language has a full parser, and pretending otherwise would be unsafe. Each language sits in one tier:

### Native

A real parser and pretty-printer. The file is rebuilt from its syntax tree, so any layout decision is available: line breaks are chosen, quotes, semicolons, trailing commas and property quotes are normalised, and comments are re-attached. 31 native modes are verified: JavaScript, TypeScript, JSON, JSONC, JSON5, JSON.stringify, YAML, TOML, CSS, SCSS, Less, PostCSS, HTML, XML, SVG, Vue, Svelte, Astro, Markdown, MDX, GraphQL queries and schema, Handlebars, and the YAML- and JSON-based OpenAPI, AsyncAPI, Swagger, RAML, Docker Compose, Pulumi, Ansible and Kubernetes formats.

### Universal

A structural engine for 220 other languages, guided by a grammar profile for each. It follows one rule: **one source line in, one source line out**. It only rewrites a line's leading whitespace and the gaps between tokens already on that line, so it cannot reorder, insert or delete a token. How much it does depends on the language:

| Depth | Languages | What it changes |
| --- | --- | --- |
| Reindent and spacing | 104 | Indentation and spacing, for languages whose blocks are in the syntax: C, C#, C++, Go, Java, Kotlin, Rust, Swift, Ruby, Lua, shell, PowerShell, Terraform and more |
| Spacing only | 60 | Spacing only, where indentation is meaning or layout is sensitive: Python, Haskell, OCaml, SQL, Sass, Pug, Lisp, Erlang and more |
| Whitespace only | 60 | Trailing whitespace, blank lines, line endings and the final newline, where leading whitespace is data: Makefiles, CSV, INI, COBOL, templates, prose markup |

Some things are deliberately left alone: `<` and `>` are never spaced (only a parser can tell `a > b` from `Vec<T>`), arithmetic spacing is enabled per language (in shell, `--flag` must not become `-- flag`), and brace padding (`{ a: 1 }` versus `{a: 1}`) is left to the author.

The engine declines rather than guesses: a file whose brackets do not balance keeps its indentation and says so, and a file the engine cannot fully read is returned untouched.

The full lists are in [Supported languages](supported-languages.md).

### Passthrough

For anything unrecognised, only the changes that cannot alter any language's meaning: trailing whitespace, runs of blank lines, line endings and the final newline.

### Falling back

A file whose native parse fails falls back a tier rather than going unformatted.

**JSX and TSX.** In version 0.1.0, a `.jsx` or `.tsx` file that contains JSX elements falls back to the universal tier: correctly indented and spaced, but not pretty-printed. Plain TypeScript in a `.tsx` file is formatted natively. The parser refuses JSX rather than guess, because a confidently wrong syntax tree is how a formatter corrupts a file.

## See why a file was formatted as it was

**Auric Formatter: Explain Formatting Decisions for This File** opens a Markdown report for the active file with:

- the language and parser chosen;
- the tier used and the time taken;
- which configuration layer (preset, configuration file, `.editorconfig`, VS Code setting or directive) set each option;
- the options changed from their defaults;
- any safety warnings.

Formatter Studio's **Explain** view shows the same for the code in Studio, and the command line has `--explain`.

When the gate passes, the status bar shows **Auric** with a tick and names the tier; when it reverts, your file is exactly as you wrote it.
