---
title: Auric Artisan Emoji — Overview
description: What the Auric Artisan Emoji extension is, who it is for, how to install it and where to find each guide.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Auric Artisan Emoji

Auric Artisan Emoji is a local emoji workspace for Visual Studio Code. It lets you search 1,914 emoji and put them straight into your code: from a searchable Quick Pick, from **Emoji Studio** in the sidebar or an editor tab, from shortcode suggestions as you type, or from a hover over a shortcode such as `:rocket:`.

Emoji Studio has four views (**Library**, **For you**, **Favorites** and **Recent**), nine categories, six skin-tone choices, quick filters and grid or list layouts. An inspector shows each emoji's shortcode, code points, emoji version, keywords and related emoji, and previews its text in six output formats: the emoji itself, a shortcode, Unicode code points, HTML entities, a JavaScript escape or a CSS escape. You can also collect several emoji into a sequence and insert them together.

The Studio can be shown in English or Hindi, and Hindi search words such as `दिल` or `धन्यवाद` find emoji. Everything is bundled and stays on your machine.

## Who it is for

- Developers writing commit messages, documentation, UI strings, tests or chat bots that use emoji.
- Front-end developers who need the right escape for HTML, JavaScript or CSS.
- Hindi-speaking users who want a Hindi Emoji Studio.

## Where to find it

| Item | Value |
| --- | --- |
| Marketplace listing | https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-emoji |
| Extension ID | `auric-artisan.auric-artisan-emoji` |
| Current version | 0.2.0 |
| Requires | Visual Studio Code 1.85 or later |
| Price | Free to install and use; no account required |

```text
code --install-extension auric-artisan.auric-artisan-emoji
```

Emoji is also installed by the [Auric Artisan Icon Pack](../auric-artisan-icon-pack/README.md).

## Quick start

1. Install the extension.
2. Open a text file and place the cursor where the emoji should go.
3. Press `Ctrl` + `Alt` + `J` (`Cmd` + `Alt` + `J` on macOS) for **Quick Insert Emoji**.
4. Type a word, such as `rocket`, and press `Enter`. The emoji is inserted.
5. Type `:spa` in your file and accept the `:sparkles:` suggestion (the sparkles emoji).
6. Press `Ctrl` + `Alt` + `E` (`Cmd` + `Alt` + `E`) to open Emoji Studio beside your code.
7. In the Studio, select a skin tone, then select **Insert** on a card.

## What you can do

- Search by name, keyword, exact emoji, shortcode, code point (such as `U+1F680`) or common Hindi words.
- Browse nine categories, and filter to curated, skin-tone-capable or newest emoji.
- Insert at every cursor in one undo step, with automatic spacing.
- Copy in six formats and set your default copy format.
- Choose a default skin tone (330 catalog entries support tones).
- Keep favorites and recent emoji, and get **For you** suggestions.
- Compose a sequence of up to 50 emoji and insert or copy it at once.
- Replace `:shortcodes:` in a selection with emoji, get completions after `:`, and insert from a code hover.
- Switch the Studio between English and Hindi.

## In this folder

### docs/

- [Contents of docs/](docs/README.md)
- [Getting started](docs/getting-started.md)
- [Insert from the editor](docs/insert-from-the-editor.md)
- [Use Emoji Studio](docs/emoji-studio.md)
- [Inspector, skin tones and output formats](docs/inspector-tones-and-formats.md)
- [Compose a sequence](docs/sequences.md)
- [Interface language](docs/interface-language.md)
- [Reference](docs/reference.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)

### others/

- [Contents of others/](others/README.md)
- [Glossary](others/glossary.md)
- [Shortcuts and commands](others/shortcuts.md)
- [Limits and accuracy](others/limits-and-accuracy.md)
- [Related extensions and comparison](others/related.md)
- [Release notes](others/release-notes.md)
- [Privacy](others/privacy.md)
