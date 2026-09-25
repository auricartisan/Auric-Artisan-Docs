---
title: Auric Artisan Emoji — Inspector, skin tones and output formats
description: Inspect an emoji, preview and set skin tones, and choose among the six output formats.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Inspector, skin tones and output formats

## Open the inspector

Select a card's **…** button, or focus an emoji and press `I`. In the narrow sidebar it opens as a sheet. Press `I` or `Escape`, or select **Close inspector**, to close it.

The inspector shows:

| Part | Contents |
| --- | --- |
| Stage | A large preview. |
| Name and shortcode | With **Copy shortcode**. |
| Pills | Emoji version (for example "Emoji 13.0"), **Skin tone** if tone-capable, **Favorite** if starred. |
| **Skin tone** | Previews of each tone. |
| **Copy as** | The six formats with their exact output. |
| **Keywords** | Search keywords. |
| Actions | **Insert**, **Copy**, **Favorite** / **Remove favorite**. |
| **Also try** | Related emoji. |

## Skin tones

Choose between **Yellow** (the standard appearance) and five tones: **Light**, **Medium light**, **Medium**, **Medium dark** and **Dark**. 330 catalog entries support tone changes.

- Set the default with the **Skin tone** filter, or `auricEmoji.preferredSkinTone` (`none`, `medium`, `light`, `mediumLight`, `mediumDark`, `dark`).
- In the inspector, select a tone to preview it ("Previewing {tone}. Your default is {default}."), then **Make {tone} my default**.
- Emoji that do not change with tone say "This emoji does not change with skin tone."

Your tone applies to card previews, insertion, Quick Insert, completions and shortcode replacement. Favorites and recents store the emoji, not the tone, so changing tone does not create duplicates.

## The six output formats

| Format | Setting value | Rocket example | Intended use |
| --- | --- | --- | --- |
| Emoji | `emoji` | The rocket character itself | Text and string contents |
| Shortcode | `shortcode` | `:rocket:` | Systems that understand emoji shortcodes |
| Unicode | `unicode` | `U+1F680` | Code-point references and documentation |
| HTML entities | `html` | `&#x1F680;` | HTML source |
| JavaScript escape | `javascript` | `\u{1F680}` | JavaScript and TypeScript string contents |
| CSS escape | `css` | `\1F680` | CSS strings, such as `content` |

In the **Copy as** list you can:

- copy a single format (**Copy as {format}**);
- use a format for this inspector's **Insert** and **Copy** (**Use {format} for Insert and Copy**);
- make a format your default copy format (**Make {format} my copy format**), which sets `auricEmoji.copyFormat`.

These are text representations, not complete snippets. Add the surrounding syntax your language needs; JavaScript code-point escapes, for example, are not valid JSON escapes.

The ledger also explains your insert spacing, for example "Insert spacing is Auto — a space is added only when text would touch the emoji."

## Result

You know exactly what text will be inserted or copied, in the tone and format you want.
