---
title: Design System Generator — Export tokens
description: Browse and search every token, then copy or download the system in any of twelve formats, and know what each format contains.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Export tokens

A **design token** is a named design decision stored as data, such as `--color-primary-500: #1f6feb` or `--space-4: 16px`. Tokens let designers and developers share one source of truth. The **Tokens** tab lists every token the system generates and exports them in twelve formats.

## The token list

- **Find token** filters the list by name or value as you type, for example `primary`, `radius` or `#1f`. **Clear** shows everything again.
- **Design tokens** shows the total and the tokens in groups, each with a count: Color · Primary, Color · Secondary, Color · Accent, Color · Neutral, Color · Semantic, Color · Roles (light), Color · Roles (dark), Color · Gradients, Typography, Typography · Size, Typography · Leading, Typography · Tracking, Spacing, Radius, Shadow, Motion, Z-index and Breakpoints.
- Colour tokens have a chip. Select any token to copy its value.

The default light-and-dark system has 177 tokens; with **Colour mode** set to **Light**, the fourteen dark role tokens are left out (163).

The names follow **Token naming** in the brief; see [Set the brief](set-the-brief.md).

## Export

Scroll to **Export tokens**. Select a format pill; the code below it changes, and its bar shows the file name and language. Three buttons:

- **Copy** copies the code shown.
- **Download** saves it under the format's file name.
- **Download all (.zip-less bundle)** saves every format, one after another with a comment line between them, in one text file, `design-system-bundle.txt`. It is not a zip archive; split it by hand or download formats one at a time.

| Pill | File | What you get |
| --- | --- | --- |
| **CSS** | `tokens.css` | A `:root` block with every token, and a dark block that applies under `[data-theme="dark"]` or `.dark`. |
| **CSS (modern)** | `tokens.modern.css` | Colour roles paired with `light-dark()` under `color-scheme: light dark`, and every colour restated in `oklch()` inside a `@media (color-gamut: p3)` block for wide-gamut screens. |
| **SCSS** | `_tokens.scss` | One `$variable` per token and a `$tokens` map. |
| **Tailwind v3** | `tailwind.config.js` | A `theme.extend` block: colour ramps, semantic solids, font families, font sizes with line heights, spacing, radius and shadows. |
| **Tailwind v4** | `theme.css` | An `@theme` block. |
| **Figma / W3C** | `design-tokens.json` | The W3C Design Tokens format for Figma Variables or Tokens Studio. |
| **JSON** | `design-system.json` | The whole system with its settings. The most complete export. |
| **TypeScript** | `tokens.ts` | The JSON as a typed constant with a `Tokens` type. |
| **Android XML** | `colors.xml` | Colour and dimension resources. |
| **SwiftUI** | `DesignTokens.swift` | A `Color` extension and dimension constants. |
| **Flutter** | `app_tokens.dart` | A class of `Color` and number constants. |
| **Compose** | `Tokens.kt` | Jetpack Compose Kotlin values. |

The CSS, SCSS, Tailwind and TypeScript files start with a comment naming the industry, style, target, seed and generation time; the JSON export carries the same details as data, and the Figma / W3C file has a one-line description.

## What each format covers

Not every format carries every token. Check before you choose one.

| Content | CSS, CSS (modern), Tailwind v4 | SCSS | Tailwind v3 | Figma / W3C | JSON, TypeScript | Android, SwiftUI, Flutter, Compose |
| --- | --- | --- | --- | --- | --- | --- |
| Colour ramps and semantic colours | Yes | Yes | Ramps and semantic solids | Ramps and semantic solids | Ramps and semantic solids | Yes |
| Light roles | Yes | Yes | No | No | Yes | Yes |
| Dark roles | CSS and CSS (modern) only | No | No | No | Yes | Yes |
| Gradients | Yes | Yes | No | No | Yes | No |
| Font families | Yes | Yes | Yes | Names only | Names only | No |
| Font sizes, spacing, radius | Yes | Yes | Yes | Yes | Yes | Yes |
| Shadows | Yes | Yes | Yes | Yes | Yes | No |
| Leading and tracking | Yes | Yes | Line heights with sizes | No | Yes | No |
| Motion, z-index | Yes | Yes | No | No | Yes | No |
| Breakpoints | Yes | Yes | No | No | Yes | Yes |

Notes:

- **Native formats** (Android, SwiftUI, Flutter, Compose) keep only plain HEX colours and pixel dimensions (spacing, radius, font sizes and breakpoints). Translucent colours, such as the focus ring and the dark theme's borders, are left out; define them by hand on those platforms.
- The roles `primary-active` and `primary-subtle` appear on the **Colour** tab and in the JSON and TypeScript exports, but not in the other formats.
- If you set a token prefix or a case other than kebab, the native formats may leave out the dimension tokens; export them with the default naming if you need them.
- For a production system, pick one complete format (CSS or JSON) as your source of truth and generate the rest from it, rather than mixing formats with different coverage.

## Example

The start of a **CSS** export:

```css
/* Auric Artisan · Design System */
/* Education · Playful · AA · seed #… */
/* Generated 2026-09-24T10:00:00.000Z */
:root {
  --color-primary-50: #…;
  --color-primary-100: #…;
  /* … */
}

/* Dark theme — apply [data-theme="dark"] or .dark on a wrapper */
[data-theme="dark"], .dark {
  --color-bg: #…;
  /* … */
}
```

## Related

- [Set the brief](set-the-brief.md) for token naming
- [Share, save and connect](share-save-and-connect.md)
- [Reference](reference.md)
