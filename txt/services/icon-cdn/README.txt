==============================================================================
ICON CDN
==============================================================================
What the Auric Artisan Icon CDN at icons.auricartisan.com serves, who it is
for, and how to put an icon on your page in a few steps.
Area: Services › Icon CDN   Updated: 2026-09-25

The Auric Artisan Icon CDN, at https://icons.auricartisan.com, serves 12,896
icons from seven open-source sets, in 32,803 variants: Lucide, Phosphor,
Tabler, Remix, Heroicons, Feather and Material. A small loader script turns
placeholders such as `<i data-icon="lucide:house">` into inline SVG you can
colour and size with CSS, and a JavaScript API returns any icon's markup or
searches the catalogue. The SVG files are also served directly, for use in
`<img>` tags or your own build.

Every set keeps its own open-source licence (MIT, ISC, Apache 2.0 or the Remix
Icon License), all of which allow commercial use. The icons are drawn with
`currentColor`, so they take the colour of the surrounding text unless you set
one.

You browse, recolour and resize icons, copy their code, and export selections
as a ZIP or an SVG sprite in the Icon Library at
https://auricartisan.com/tool/icon/. That page is documented with the website
tools; these pages cover the CDN itself: the collections, the loader,
embedding and licences.

WHO IT IS FOR
=============

  - Web developers who want icons in plain HTML without a build step or an npm
    package.
  - Designers and prototypers who want to try icons from several sets under
    one name scheme.
  - React developers who want a quick JSX component for a single icon.
  - Teams that self-host and want to download SVGs or sprites.

WHERE TO FIND IT
================

  What                 | Where
  ---------------------+----------------------------------------------
  CDN host             | https://icons.auricartisan.com
  Loader script        | https://icons.auricartisan.com/icon-cdn.js
  SVG files            | `https://icons.auricartisan.com/icon/<set>/…`
  Browse and copy code | https://auricartisan.com/tool/icon/
  Licence reference    | https://icons.auricartisan.com/LICENSE.md

QUICK START
===========

  1. Add the loader to your page:
         <script src="https://icons.auricartisan.com/icon-cdn.js"></script>
  2. Place an icon where you want it:
         <i data-icon="lucide:house"></i>
  3. Load the page. The placeholder is replaced by the inline SVG.
  4. Size and colour it with attributes, or with CSS on the element:
         <i data-icon="phosphor:heart" data-style="fill" data-size="32" data-color="#e11"></i>
  5. To find icon names, search the Icon Library at
     https://auricartisan.com/tool/icon/, open an icon and use Copy CDN tag.
  6. Keep the set's licence notice where its licence asks for it; see Licences
     [others/licences.txt].

WHAT YOU CAN DO
===============

  - Turn `<i data-icon="set:name">` placeholders into inline, themeable SVG.
  - Choose a style (such as Phosphor's thin to duotone weights, or Tabler's
    outline and filled), a size, a colour and a stroke width.
  - Get an icon's markup from JavaScript with `AuricIcons.svg()`, or search
    the catalogue with `AuricIcons.search()`.
  - Link SVG files directly, or use the Material and Remix webfonts.
  - Copy SVG, JSX, a data-URI `<img>` or a CDN tag from the Icon Library, and
    export selections as a ZIP or a `<symbol>` sprite.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt]
    - Getting started [docs/getting-started.txt]
    - Collections [docs/collections.txt]
    - Embed an icon [docs/embed-an-icon.txt]
    - Use the loader [docs/use-the-loader.txt]
    - Style, size and colour [docs/style-size-and-colour.txt]
    - Export and self-host [docs/export-and-self-host.txt]
    - Reference [docs/reference.txt]
    - Troubleshooting [docs/troubleshooting.txt]
    - FAQ [docs/faq.txt]
  - others/ [others/README.txt]
    - Glossary [others/glossary.txt]
    - Licences [others/licences.txt]
    - Limits and accuracy [others/limits-and-accuracy.txt]
    - Related [others/related.txt]
    - Privacy [others/privacy.txt]
