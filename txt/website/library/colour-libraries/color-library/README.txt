==============================================================================
COLOR LIBRARY
==============================================================================
What the Color Library is, who it is for, where to find it and how to look up
your first colour.
Area: Website › Library › Colour libraries › Color Library   Updated: 2026-09-25

The Color Library is a searchable atlas of 8,192 colours. Every colour in it
carries the same set of precomputed data: its values in seven colour notations
(HEX, RGB, HSL, CIE L*a*b*, OKLab, OKLCH and CMYK), perceptual measures such
as chroma and relative luminance, its contrast ratio against white and against
black, how it looks to people with three kinds of colour blindness, and five
descriptive labels (emotion, art movement, mood, design usage and design tag).
The page headline sums it up: "Eight thousand colours, measured."

You can use the atlas in three ways. You can paste a colour you already have,
in almost any CSS format, and see the five catalogued colours nearest to it
and what each of them can do. You can ask for what a colour has to do, such as
"readable on white" or "for typography", and see how many colours are left
after each requirement. Or you can browse the whole atlas with a search box,
eight filters and six sort orders, then open any colour to read everything the
atlas knows about it.

Everything you browse is worked out in your browser from data the page
downloads. You can copy a colour in six formats, download it as JSON, SVG or
PNG, download the whole filtered set in seven formats, and save colours to a
list that stays in your browser and also appears in your Library.

WHO IT IS FOR
=============

  - Designers who arrive with a brand colour and want to know what it is good
    for before they commit to it.
  - Front-end developers who need a colour that passes a contrast threshold
    and want its value in OKLCH, Lab or HSL.
  - Accessibility specialists checking how many colours clear WCAG AA or AAA
    against white or black.
  - Students and colour enthusiasts exploring how hue, lightness and chroma
    are distributed across a large set.

WHERE TO FIND IT
================

Open https://auricartisan.com/library/color/ in a current desktop or mobile
browser. It is also listed as Color Library ("Color science data") under
Libraries in the site header's Learn menu. No installation or account is
needed.

QUICK START
===========

  1. Open https://auricartisan.com/library/color/. The Start from a colour you
     already have field already holds `#D3AF37`, and its nearest neighbours
     are shown under it.
  2. Replace that value with your own colour, for example `oklch(0.62 0.19
     29)` or `rebeccapurple`, and select Find its neighbours.
  3. Read the five nearest colours, their ΔE distance and their contrast on
     white and on black.
  4. Select one of the neighbours. The The colour tab opens with its full
     record.
  5. Scroll down to Browse the atlas and choose Readable on white in Or from
     what it has to do to narrow the grid.
  6. Select Export, then CSS variables under Style formats to download the
     matching colours as a stylesheet.

WHAT YOU CAN DO
===============

  - Find the five nearest atlas colours to any colour you paste, measured as
    ΔE in CIE Lab.
  - Filter by seven requirement chips that show, before you select them, how
    many colours each one would leave.
  - Search by hex, atlas id or label, and filter by hue, lightness, chroma,
    emotion, art movement, mood, design usage and WCAG level.
  - Sort by hue, lightness, chroma or luminance, or shuffle the grid.
  - Read a colour's contrast on white and black, its colour-blindness
    simulations, every notation and its nearest neighbours.
  - See histograms of hue, lightness, chroma and contrast for the current set.
  - Copy a colour in six formats; download it as JSON, SVG or PNG.
  - Download the whole filtered set as JSON, CSV, plain text, CSS, SCSS or a
    Tailwind fragment.
  - Save colours in your browser and find them again in the Saved tab and in
    your Library.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the Color Library.
    - Getting started [docs/getting-started.txt] — open the page, the screen
      tour and a first lookup.
    - Find a colour's nearest neighbours [docs/find-nearest-colours.txt] —
      paste any CSS colour and read the matches.
    - Choose colours by requirement [docs/choose-by-requirement.txt] — the
      seven requirement chips and their counts.
    - Browse, search and filter [docs/browse-search-and-filter.txt] — search,
      filters, sort, shuffle and the grid.
    - Read a colour [docs/read-a-colour.txt] — everything on the The colour
      tab.
    - Read the statistics [docs/read-the-statistics.txt] — the four histograms
      on the Stats tab.
    - Copy and export [docs/copy-and-export.txt] — every copy format and
      download, with examples.
    - Save colours [docs/save-colours.txt] — the star, the Saved tab and your
      Library.
    - Reference [docs/reference.txt] — every control, filter, sort, output and
      message.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in the Color Library.
    - Shortcuts [others/shortcuts.txt] — keyboard and pointer actions.
    - Limits and accuracy [others/limits-and-accuracy.txt] — what the figures
      mean and what they are not.
    - Related [others/related.txt] — related libraries, tools and Learn
      articles.
    - Privacy [others/privacy.txt] — what stays in your browser and what uses
      the network.
    - Release notes [others/release-notes.txt] — user-facing history.
