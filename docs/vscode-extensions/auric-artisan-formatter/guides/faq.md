---
title: Auric Artisan Formatter — FAQ
description: Short answers to common questions about Auric Artisan Formatter.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# FAQ

## Will it rewrite my repository when I install it?

No. The startup scan only formats in memory and reports a count. Files are written only when you format them: on save (if you turn it on), with a Format command, with **Apply**, or with **Format selected** or **Format all files**.

## Can it produce exactly the same output as Prettier?

The `prettier` preset is byte-compatible with Prettier 3 at its own defaults, with every Auric-only enhancement off. A project with only a Prettier configuration gets that preset automatically.

## How do I keep `git blame` useful?

Set `auricFormatter.formatOnSaveMode` to `modifications` so format on save only touches lines you changed, or use the `minimal-diff` preset. When you do format everything, use the Workspace tab to take a folder at a time.

## Could it break my code?

Every result passes the safety gate: tokens, comments, strings and a reparse are checked before anything is written, and on failure your original text is kept. The universal engine can only change whitespace. Keep using version control as usual.

## Which languages does it support?

253 languages: 31 native modes plus 220 on the universal tier. See [Supported languages](supported-languages.md).

## Does it format JSX?

In version 0.1.0, files containing JSX elements are indented and spaced by the universal tier but not pretty-printed.

## Where do I put my settings?

In a `.auricformatrc` at the project root, so everyone gets the same result. VS Code settings work too. See [Configuration](configuration.md).

## How do I find the option I want?

Open Formatter Studio, load your file and choose **Find what matters**. It lists only the options that would change that file.

## Can I use it in CI?

Yes. Run the command-line check, which exits with code 1 when files need formatting. See [Command line and CI](command-line.md).

## Does it send my code anywhere?

No. Formatting runs locally with no network requests and no runtime dependencies.

## Is the interface available in Hindi?

Not at present; the interface is in English.
