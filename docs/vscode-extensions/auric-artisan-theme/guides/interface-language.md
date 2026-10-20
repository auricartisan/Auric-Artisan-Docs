---
title: Auric Artisan Theme — Interface language
description: Switch Theme Studio and the Theme sidebar between English and Hindi, and understand what follows VS Code's own display language.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Interface language (English and हिन्दी)

Theme Studio and the Theme sidebar can be shown in English or Hindi. You do not need a VS Code language pack for this.

## Choose a language

Use any of these:

- In Theme Studio's top bar, select **Auto**, **English** or **हिन्दी**.
- In the sidebar's language bar, select **Auto**, **EN** or **हिं**.
- Run **Auric Theme: Choose Interface Language…** and pick **Auto (VS Code)**, **English** or **Hindi**. The current choice is marked **current**.
- Set `auricTheme.interfaceLanguage` in Settings to `auto`, `en` or `hi`.

| Value | Behaviour |
| --- | --- |
| `auto` (default) | Follows the VS Code display language. Hindi locales use Hindi; every other locale uses English. |
| `en` | Always English in Theme Studio and the sidebar. |
| `hi` | Always Hindi in Theme Studio and the sidebar. |

The choice is saved in your user settings and shared by both panels. The switch rebuilds the labels immediately. Your current tab, filters, expanded groups, scroll position and any text you had typed in the Share tab are kept.

## What changes and what does not

| Part of VS Code | Language used |
| --- | --- |
| Theme Studio and the Theme sidebar | Your `auricTheme.interfaceLanguage` choice. |
| Theme names in the pickers and status bar | VS Code's display language. With Hindi as the display language, all 54 names appear in Hindi, for example "ऑरिक आर्टिजन — ऑब्सिडियन गोल्ड". |
| Command Palette titles, Settings descriptions, notifications and the walkthrough | VS Code's display language. The extension ships Hindi versions of all of them. |
| Setting IDs, slot paths and hex values | Always English and unchanged. |

To change VS Code's own language, run **Configure Display Language** and install or pick a language pack.

Hindi text in the panels uses Devanagari-friendly fonts and line height.

## Result

The Studio and sidebar appear in your chosen language, while VS Code's own menus follow its display language.
