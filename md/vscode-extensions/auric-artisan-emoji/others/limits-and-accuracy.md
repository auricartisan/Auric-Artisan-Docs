---
title: Auric Artisan Emoji — Limits and accuracy
description: What Auric Artisan Emoji can and cannot do.
product: VS Code extensions › Auric Artisan Emoji
updated: 2026-09-25
---

# Limits and accuracy

- The catalog has 1,914 entries in nine categories at the installed version; new emoji arrive with updates.
- Glyph appearance depends on your operating system's emoji fonts. Newer emoji may not display with older fonts.
- 330 entries support skin tones; others ignore the tone setting.
- Output formats are text representations, not complete code snippets. JavaScript code-point escapes are not JSON escapes.
- Hover actions are single-use and expire when the document changes; a failed hover edit does not fall back to the clipboard.
- Shortcode replacement leaves unknown tokens unchanged.
- Hindi search terms help you find emoji; names, shortcodes and code points stay in their catalog spelling.
- Editing remote or virtual files depends on the file system provider.
- Recent emoji are limited by `auricEmoji.maxRecents` (8 to 200, default 48). A sequence holds up to 50 emoji.
