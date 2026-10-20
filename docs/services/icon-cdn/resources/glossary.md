---
title: Icon CDN — Glossary
description: Definitions of the icon and SVG terms used in the Icon CDN documentation.
product: Services › Icon CDN
updated: 2026-09-25
---

# Glossary

**`currentColor`.** A CSS keyword meaning "the current text colour". Icons drawn with it take the colour of the text around them.

**Data URI.** A way to put a small file, here an SVG, directly into an address, so an `<img>` needs no separate download.

**Default style.** The style the loader uses when you do not choose one, such as `regular` for Phosphor.

**Fill-drawn icon.** An icon made of filled shapes. Its weight comes from its style, not from a stroke width.

**Grid (viewBox).** The coordinate square an icon is drawn in, such as 24 × 24. It sets the icon's proportions, not its size on screen.

**Icon.** One symbol, such as "heart". **Variant:** one style of it, such as a bold or filled heart.

**Inline SVG.** SVG markup placed directly in the HTML, so CSS can colour and size it.

**JSX.** The HTML-like syntax React components are written in.

**Loader.** The `icon-cdn.js` script that fills `data-icon` placeholders and offers the `AuricIcons` API.

**Placeholder.** An element with a `data-icon` attribute that the loader fills with an icon.

**Sprite.** One hidden SVG containing many icons as `<symbol>` elements, each shown elsewhere with `<use href="#id">`.

**Stroke-drawn icon.** An icon made of lines, whose thickness can be changed with a stroke width.

**Style.** A version of a set's icons, such as outline or filled, or a weight such as thin or bold.

**SVG.** Scalable Vector Graphics, the format most icons are served in; it stays sharp at any size.

**Webfont icons.** Icons delivered as characters of a font, as with Material and Remix's webfont.
