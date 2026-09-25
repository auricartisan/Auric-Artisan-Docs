==============================================================================
FONT CDN
==============================================================================
What the Auric Artisan Font CDN at fonts.auricartisan.com serves, who it is
for, and how to put a font on your page in a few steps.
Area: Services › Font CDN   Updated: 2026-09-25

The Auric Artisan Font CDN, at https://fonts.auricartisan.com, serves
open-licence font families to your web pages. Each family has its own
stylesheet of `@font-face` rules that you link like a Google Fonts stylesheet,
and a small loader script can load families declaratively or from JavaScript.
The font files themselves are served from the same host, so a page that uses
the CDN makes no request to any third party.

The catalogue holds 2,213 families and 4,883 font files, of which 550 families
are variable fonts. Most are under the SIL Open Font License; others use
Apache 2.0, public-domain dedications, MIT or other open licences, and every
family's own licence text is available. A small part of the catalogue is
tagged Installed: system fonts that are listed for reference but not served,
because their licences do not allow redistribution.

You browse the catalogue, preview families in your own words, and copy embed
code in the Font Library at https://auricartisan.com/tool/font/. That page is
documented with the website tools; these pages cover the CDN itself: what it
serves, how to embed a family, the loader, self-hosting and licences.

WHO IT IS FOR
=============

  - Web designers and developers who want open-licence fonts without a
    third-party font service.
  - Teams with privacy or offline requirements who prefer to self-host, using
    the downloadable kits.
  - Prototypers who need to try many families quickly from JavaScript.

WHERE TO FIND IT
================

  What                       | Where
  ---------------------------+-----------------------------------------------------
  CDN host                   | https://fonts.auricartisan.com
  Loader script              | https://fonts.auricartisan.com/font-cdn.js
  Family stylesheets         | `https://fonts.auricartisan.com/css/<family-id>.css`
  Browse and copy embed code | https://auricartisan.com/tool/font/
  Licence reference          | https://fonts.auricartisan.com/LICENSE.md

QUICK START
===========

  1. Open https://auricartisan.com/tool/font/ and find a family, for example
     Alegreya.
  2. Open the family and go to its Use & Embed tab.
  3. Copy the Link snippet:
         <link rel="stylesheet" href="https://fonts.auricartisan.com/css/alegreya.css">
  4. Paste it into the `<head>` of your page.
  5. Apply the family in your CSS:
         .headline { font-family: 'Alegreya', serif; }
  6. Check the family's License tab, and keep its terms.
  7. To host the files yourself instead, choose Download kit and follow
     Self-host a family [docs/self-host-a-family.txt].

WHAT YOU CAN DO
===============

  - Link a family's stylesheet, or `@import` it from your CSS.
  - Load one or many families with a single script tag, or from JavaScript
    with `AuricFonts.load()`.
  - Use variable fonts across their full weight range.
  - Register a single font face from any URL with `AuricFonts.face()`.
  - Search the catalogue and read a family's full metadata from JavaScript.
  - Download a self-hosting kit with the font files, a stylesheet, a demo page
    and the licence.
  - Copy a font stack with fallbacks, CSS variables, Tailwind, SCSS or
    design-token snippets from the Font Library.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt]
    - Getting started [docs/getting-started.txt]
    - Embed a family [docs/embed-a-family.txt]
    - Use the loader [docs/use-the-loader.txt]
    - Self-host a family [docs/self-host-a-family.txt]
    - Find a family [docs/find-a-family.txt]
    - Reference [docs/reference.txt]
    - Troubleshooting [docs/troubleshooting.txt]
    - FAQ [docs/faq.txt]
  - others/ [others/README.txt]
    - Glossary [others/glossary.txt]
    - Licences [others/licences.txt]
    - Limits and accuracy [others/limits-and-accuracy.txt]
    - Related [others/related.txt]
    - Privacy [others/privacy.txt]
