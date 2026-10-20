---
title: Auric Artisan Font Hub — add a font to your code
description: Add fonts from the Auric font CDN to HTML, CSS and JavaScript files with a reviewable diff, insert explicit embed formats, and add several families at once.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Add a font to your code

Font Hub adds fonts from the Auric font CDN. Every embed points to a stylesheet at:

```text
https://fonts.auricartisan.com/css/<family-id>.css
```

For example, Inter is `https://fonts.auricartisan.com/css/inter.css`. Font Hub never substitutes another font service.

## Automatic insertion

**Add to code** (on a font card) and **Auric Artisan Font Hub: Add Font to Code** use *Automatic* mode by default. Automatic mode adds two things: the CDN stylesheet, and a reusable class named `.auric-font-<family-id>` that applies the font. It never replaces selected text, never changes your existing rules and never applies the font to the whole page. You decide where to use the class.

What it adds depends on the active file:

| Active file | What Automatic mode does |
| --- | --- |
| HTML with a `<head>` | Adds `<link rel="stylesheet" href="…">` and a small `<style>` rule for the class just before `</head>` |
| CSS, SCSS, Less, PostCSS | Adds `@import url('…');` before your normal rules (after any `@charset`, `@use` or `@forward`) and appends the class rule |
| JavaScript, TypeScript | Appends a small guarded block that adds the stylesheet and class to the page when it runs in a browser, and does nothing on the server |
| JSX, TSX, Vue, Svelte, Astro, data files and other languages | Copies an HTML embed to the clipboard for you to place in your layout or global stylesheet |
| No editor open | Copies the CDN embed to the clipboard |

For example, after adding Inter to a page, use:

```html
<p class="auric-font-inter">A considered choice of type.</p>
```

Running it again does not duplicate the setup: if the link and class are already present, Font Hub says the family is already configured. An HTML file without a `<head>` is not changed; you get **No HTML head found. Copy the embed into your page head or framework layout.** and the embed is copied.

Automatic insertion works on files up to 2 MiB. It is deliberately cautious and is not a full HTML, CSS or JavaScript parser.

## Preview before applying

1. Open the file you want to change.
2. Choose **Preview** on a font card, run **Auric Artisan Font Hub: Preview Font Insertion**, or choose **Preview CDN insertion** in **Quick Pick Font**.
3. VS Code's diff editor opens with your file on the left and the proposed file on the right, titled **Font Hub: *family* — proposed changes**.
4. A notification asks **Add CDN setup to *file*? Existing content stays unchanged.** Choose **Apply** or **Cancel**.
5. **Apply** checks that your file has not changed since the preview, then makes the edit. The file is left unsaved, and one undo removes the change.

If you edited the file after opening the preview: **The document changed. Preview the font insertion again before applying.** Open the preview again.

## Explicit formats

To insert a specific format instead of the automatic setup:

- In the details panel, open **Use & Embed** or **Develop**, choose a format and select **Insert**. The snippet is inserted at the cursor, or replaces each selection.
- Or set `auricFontLib.defaultFormat` to a format, and **Add Font to Code** inserts that format at the cursor.

Explicit formats insert text where you are. They do not merge anything into framework configuration files such as `tailwind.config.js`; you paste the entry where it belongs.

If no editor can be written to, the snippet is copied to the clipboard instead, and a message says why.

## Copy an embed

- **Auric Artisan Font Hub: Copy Font Embed As…** — choose a family, then **Choose a snippet format**: HTML stylesheet link, CSS @import, CSS font-family, @font-face, AuricFonts loader, Tailwind config, SCSS variable, Design tokens JSON or Family name.
- **Copy** in the details panel copies the current format.
- **Save** writes the current format to a new file you name.

## Several families at once

1. Select up to 12 families (the select button on each card).
2. Open the **Selected** tray.
3. Choose **Insert** to add every family's setup to the active file, each with its own class, or **Copy embed** to copy one combined embed.

After inserting, Font Hub reminds you to **Apply the generated .auric-font-* classes in your markup. File left unsaved.** A system font in the selection stops the insertion: **Remove system fonts from the CDN selection first.**

## From the editor's context menu

Right-click in an editor for the **Auric Fonts** submenu: **Quick Pick Font**, **Add Font to Code**, **Preview Font Insertion**, **Copy Font Embed As…** and **Open Font Hub**.

## Using the font in your CSS

To use the family in your own selectors instead of the generated class, copy its `font-family` value (**Copy family** in the specimen, or the **CSS font-family** format) and use it in your stylesheet. The stylesheet link or `@import` must still be present, or the browser has nothing to load.

If the font does not appear in the browser, see [Check CDN and browser delivery](cdn-and-browser-delivery.md).

When this works, the file contains the CDN setup, the element with the class shows the new font in a browser, and **Recent** in Font Hub lists the family.
