---
title: Auric Color — FAQ
description: Short answers about Auric Color.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Auric Color FAQ

### Which languages does it work in?

More than 40: CSS and its dialects, HTML, Vue, Svelte, Astro, PHP, JavaScript, TypeScript, JSX, TSX, JSON, YAML, TOML, Markdown, Python, Go, Rust, Java, C#, C and C++, Swift, Kotlin, Dart, Ruby and many more. See [Supported languages](hover-and-swatches.md#supported-languages). Contrast checks run in stylesheets, markup, JavaScript, TypeScript and Markdown.

### Why did VS Code's colour squares disappear?

Auric Color's default mode replaces them with its own swatches and picker, and turns `editor.colorDecorators` off. Run **Restore native color picker (use VS Code's)** to go back. See [Picker modes](picker-modes.md).

### Does editing keep my colour format?

Yes. Hover tiles and **Type exact…** write in the token's own syntax, using the fewest decimals that keep exactly the same colour. The picker panel writes the format tab you choose.

### Can I change every use of a colour at once?

Within one file, tick **Apply to all N matches in file** in the picker. For a colour that comes from a CSS custom property, use **Apply to --token** in the contrast hover or the Contrast Studio, which changes the definition so every use follows.

### What does "nearest passing, same hue" mean?

The colour with the same hue and chroma whose lightness has been moved just far enough to reach the contrast target. It is the smallest visible change that passes.

### Is APCA the same as WCAG 3?

No. APCA is the contrast model proposed in the WCAG 3 working draft, which is not finished. Auric Color offers it as an experimental option; meeting its target is not a conformance claim.

### Does it work with Tailwind?

It detects colour literals in Tailwind config files and exports palettes and shade scales as Tailwind config snippets. It does not resolve Tailwind utility classes such as `text-gray-500` to colours.

### Does it support wide-gamut colours?

It reads `oklch()`, `lab()`, `lch()` and `color(display-p3 …)` and other `color()` spaces. Colours outside sRGB are measured as a standard screen shows them, and the hover says so.

### Why does the status bar say "A11y" when I only installed Auric Color?

The score item shows the project's accessibility score (contrast and, where markup is present, WCAG). With Auric Color alone it appears once the Studio has graded the workspace in the background as you edit.

### Do I need Auric Accessibility for contrast checks?

No. Auric Color publishes contrast diagnostics on its own. When Auric Accessibility is installed, it takes over contrast diagnostics, with the same behaviour.

### Is anything sent to a server?

No. See [Privacy](../others/privacy.md).
