---
title: Language — Reference
description: Every language control, what it does, and how the language choice is kept.
product: Website › Site features › Language
updated: 2026-09-25
---

# Language reference

## Controls

| Control | Where | What it does |
|---|---|---|
| Globe button (**Language / भाषा**) | Header, wide screens | Switches English ⇄ Hindi |
| **English** / **हिन्दी** | Settings › Appearance › **Language** | Picks a language |
| **English** / **हिन्दी** | Drawer › Preferences › **Language** | Picks a language |
| **Switch language** | Spotlight, command mode (`>`) | Switches English ⇄ Hindi; shows the current language |
| `?lang=hi` / `?lang=en` | Any page address | Opens the page in that language and remembers it |

## Behaviour

| Item | Behaviour |
|---|---|
| Languages | English (`en`), Hindi (`hi`) |
| Default | English |
| Switching to Hindi | Translates the page in place, then every page after |
| Switching to English | Reloads the page |
| Remembered | In this browser, for every page, until you switch |
| Page language | Marked as Hindi while in Hindi, so screen readers and translation tools know |
| Date and time format | Hindi (India) while in Hindi; English (United States) style in English, except where your Clock settings choose a format |
| Fonts | Devanagari system fonts such as Nirmala UI, Noto Sans Devanagari, Mukta, Hind or Kohinoor Devanagari, depending on your device |
| In the settings export file | No |
| Offline | Hindi text is included in the offline download when you prepare it while the site is in Hindi |

## Opting parts of a page out

Some elements are deliberately never translated: the language buttons, code, keyboard keys, and the header detail lines of the right-click menu that show addresses, hex codes and quoted text.
