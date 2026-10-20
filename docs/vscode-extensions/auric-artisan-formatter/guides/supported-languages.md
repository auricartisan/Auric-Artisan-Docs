---
title: Auric Artisan Formatter — supported languages
description: Every language Auric Artisan Formatter formats, grouped by how much it can change.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Supported languages

The formatter recognises 253 languages by file extension, exact file name, shebang line and VS Code language id. What it does with each depends on its tier; see [The safety gate and formatting tiers](safety-gate-and-tiers.md).

| Tier | Languages | What changes |
| --- | --- | --- |
| Native | 33 registry entries; 31 verified native modes | Anything layout-related: the file is rebuilt from a real parse |
| Universal: reindent and spacing | 104 | Indentation and spacing |
| Universal: spacing only | 60 | Spacing between tokens; indentation untouched |
| Universal: whitespace only | 60 | Trailing whitespace, blank lines, line endings, final newline |

The two native entries that are not yet verified are JavaScript React (`jsx`) and TypeScript React (`tsx`): a file containing JSX elements falls back to the universal tier in version 0.1.0.

To see the list yourself, run `auric-format --list-languages` (see [Command line and CI](command-line.md)). Formatter Studio's **Lang** drop-down groups languages into **Native printers** and **Universal engine**.

## Native tier

The "Formatter id" is the name used in the formatter's `languages` configuration.

| Language | Formatter id | File extensions or names |
| --- | --- | --- |
| JavaScript | `javascript` | `.js` `.cjs` `.mjs` `.es` `.es6` `.pac` and more |
| JavaScript React | `jsx` | `.jsx` |
| TypeScript | `typescript` | `.ts` `.mts` `.cts` `.d.ts` `.d.mts` `.d.cts` |
| TypeScript React | `tsx` | `.tsx` `.mtsx` |
| JSON | `json` | `.json` `.geojson` `.topojson` `.jsonld` `.importmap` `.har` and more |
| JSON5 | `json5` | `.json5` |
| JSON with Comments | `jsonc` | `.jsonc` |
| JSON.stringify | `json-stringify` | `package.json` `package-lock.json` `bower.json` `.babelrc.json` |
| CSS | `css` | `.css` `.wxss` |
| SCSS | `scss` | `.scss` |
| Less | `less` | `.less` |
| PostCSS | `postcss` | `.pcss` `.postcss` `.sss` |
| HTML | `html` | `.html` `.htm` `.xhtml` `.xht` `.shtml` `.html.hl` and more |
| Vue | `vue` | `.vue` |
| Svelte | `svelte` | `.svelte` |
| Astro | `astro` | `.astro` |
| XML | `xml` | `.xml` `.xsd` `.xsl` `.xslt` `.rss` `.atom` and more |
| SVG | `svg` | `.svg` `.svgz` |
| Markdown | `markdown` | `.md` `.markdown` `.mdown` `.mkd` `.mkdn` `.mdwn` and more |
| MDX | `mdx` | `.mdx` |
| Handlebars | `handlebars` | `.handlebars` `.hbs` `.hbs.html` |
| YAML | `yaml` | `.yaml` `.yml` `.yaml.tmpl` `.mir` `.reek` `.rviz` and more |
| TOML | `toml` | `.toml` `.tml` |
| GraphQL | `graphql` | `.graphql` `.gql` |
| GraphQL SDL | `graphql-schema` | `.graphqls` `.gqls` `.sdl` |
| OpenAPI | `openapi` | `openapi.yaml` `openapi.yml` `openapi.json` `api.yaml` |
| AsyncAPI | `asyncapi` | `asyncapi.yaml` `asyncapi.yml` `asyncapi.json` |
| Swagger 2.0 | `swagger` | `swagger.yaml` `swagger.yml` `swagger.json` |
| RAML | `raml` | `.raml` |
| Docker Compose | `docker-compose` | `docker-compose.yml` `docker-compose.yaml` `docker-compose.override.yml` `docker-compose.override.yaml` |
| Pulumi | `pulumi` | `Pulumi.yaml` `Pulumi.yml` |
| Ansible | `ansible` | `playbook.yml` `playbook.yaml` `site.yml` `site.yaml` |
| Kubernetes manifest | `kubernetes` | `kustomization.yaml` `kustomization.yml` `kubeconfig` |

### Files identified by name

Some formats share an extension with another, and a few files are recognised by name. For example, `docker-compose.yml`, `compose.yaml`, `openapi.yaml`, `swagger.json`, `asyncapi.yaml`, `Pulumi.yaml`, `playbook.yml` and `kustomization.yaml` get their own native handling. Ambiguous extensions are resolved to one language by default: `.h` is C, `.m` is Objective-C, `.pl` is Perl, `.sql` is SQL and `.ts` is TypeScript. Set `auricFormatter.parser` or a `languages` entry if you need a different interpretation.

## Universal tier: reindent and spacing (104)

Indentation and spacing are normalised. JavaScript, TypeScript and their React variants appear here because this is where they fall back when a native parse is not possible.

ABAP, Ada, Alloy, ANTLR, Apache Avro IDL, Apache config, Apache Thrift, Apex, AppleScript, ASN.1, AWK, Bash, BASIC, Bicep, C, C#, C++, Caddyfile, Cairo, Cap'n Proto, CMake, Crystal, CUDA, CUE, D, Dart, Delphi, Elixir, Fish, FlatBuffers, Fortran, Gleam, GLSL, GNU Octave, gnuplot, Go, Gradle, Graphviz DOT, Groovy, Hack, Haxe, HCL, Hjson, HLSL, Java, JavaScript, JavaScript React, jq, Jsonnet, Julia, KDL, Kotlin, Lex / Flex, Lua, M4, MATLAB, Metal Shading Language, Move, nginx, Nix, Nushell, Objective-C, Objective-C++, Odin, OpenCL, Pascal, Perl, PHP, PowerShell, Protocol Buffers, Puppet, R, Raku, Reason, ReScript, REXX, Ruby, Rust, Rusty Object Notation, Scala, Shell script, Smalltalk, Solidity, Stan, Stata, Swift, SystemVerilog, Tcl, Terraform, TypeScript, TypeScript React, TypoScript, V, Vala, Verilog, VHDL, Vim script, Visual Basic, Web IDL, WGSL, XQuery, Yacc / Bison, Zig, Zsh.

## Universal tier: spacing only (60)

Indentation is left exactly as written, because it carries meaning or the layout is sensitive; spacing between tokens is normalised.

Agda, AutoHotkey, Batch file, Bazel, Clojure, ClojureScript, CoffeeScript, Common Lisp, Coq / Rocq, Cypher, Cython, Dhall, EDN, Elm, Emacs Lisp, Erlang, F#, Fennel, GDScript, Haml, Haskell, HiveQL, Idris, Isabelle, Jade, Janet, Lean, LiveScript, Mercury, Meson, Michelson, MySQL, Nim, OCaml, PL/SQL, PostgreSQL, Prolog, Pug, PureScript, Python, Racket, SAS, Sass (indented), Scheme, Slim, SMT-LIB, Spark SQL, SPARQL, SPSS, SQL, SQLite SQL, Standard ML, Starlark, Stylus, T-SQL, TLA+, Vyper, WebAssembly, WebAssembly Text, Wolfram Mathematica.

## Universal tier: whitespace only (60)

Only trailing whitespace, blank-line runs, line endings and the final newline change, because leading whitespace is data in these formats.

Apache Ant, AsciiDoc, ASP.NET Web Forms, Assembly, BibTeX, Blade, COBOL, ColdFusion Markup, Containerfile, Creole, CSV, Diff / patch, Dockerfile, Document Type Definition, Dotenv, EditorConfig, EJS, ERB, Forth, FreeMarker, Gherkin, Git attributes, Git commit message, Git config, Git ignore, Git rebase todo, Go module, Helm chart, INI, Java Properties, JavaServer Pages, Jinja, JSON Lines, Just, LaTeX, Liquid, LLVM IR, Makefile, MediaWiki, Mermaid, Mustache, Ninja, Nunjucks, Org Mode, PlantUML, Razor, reStructuredText, Robot Framework, RPG (IBM i), sed, Smarty, systemd unit, Texinfo, Textile, Thymeleaf, TSV, Turtle / RDF, Twig, Velocity, XAML.
