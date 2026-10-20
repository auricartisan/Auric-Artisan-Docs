---
title: Auric Artisan Emoji — Interface language
description: Show Emoji Studio in English or Hindi and search with Hindi words.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Interface language (English and हिन्दी)

## Choose a language

- In Emoji Studio's brand bar, use the **Language** switch: **Auto**, **EN** or **हिं**.
- Run **Auric Artisan Emoji: Choose Interface Language…** (also in the sidebar's title-bar **…** menu).
- Set `auricEmoji.interfaceLanguage` to `auto`, `en` or `hi`.

| Value | Behaviour |
| --- | --- |
| `auto` (default) | Follows VS Code's display language: Hindi locales use Hindi; others use English. |
| `en` | Always English in Emoji Studio. |
| `hi` | Always Hindi in Emoji Studio. |

Changing the language keeps your search, filters and sequence.

## What changes

| Part | Language |
| --- | --- |
| Emoji Studio controls, categories, tones, formats and announcements | Your `auricEmoji.interfaceLanguage` choice. |
| Command Palette titles, Settings descriptions and notifications | VS Code's display language (Hindi versions are included). |
| Emoji names, shortcodes and code points | Their catalog spelling, always. |

## Hindi search

Common Hindi words find emoji whatever the interface language, for example `दिल` (heart), `रॉकेट` (rocket) and `धन्यवाद` (thanks).

## Result

Emoji Studio appears in your chosen language, and Hindi words help you find emoji.
