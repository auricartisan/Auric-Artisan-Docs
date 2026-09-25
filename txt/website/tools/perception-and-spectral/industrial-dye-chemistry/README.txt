==============================================================================
INDUSTRIAL DYE CHEMISTRY (DYE IN SOLUTION)
==============================================================================
What the Dye in Solution tool does, who it is for, where to find it and how to
watch a first pH indicator change colour.
Area: Website › Tools › Perception and spectral › Industrial Dye Chemistry   Updated: 2026-09-25

The Industrial Dye Chemistry tool, whose page is titled Dye in solution,
models a dye bath one wavelength at a time. You choose up to four dyes, their
concentrations and the bath's pH and path length. The tool works out how much
light the bath absorbs at each of 81 wavelengths from 380 to 780 nm, what
colour that makes under a light source you name, and how far that colour moves
under the other lights it holds.

Each dye is modelled as two forms, an acid form and a base form, each with its
own absorption band. The pH sets how much of the dye is in each form, so a pH
indicator changes colour as the two bands trade places, and the curves for
every pH cross at one wavelength, the isosbestic point. Absorbance follows the
Beer–Lambert law, and the page flags when the bath is too strongly coloured
for that law to hold. Colour is computed against the CIE 1931 standard
observer under daylight D65 or D50, tungsten illuminant A, or equal-energy
light E, and colour differences use CIEDE2000.

The model is real; the dyes are not. The six preset dyes stand for classes of
dye (for example "the methyl-orange family") with constants chosen by the
tool, and their bands are drawn as Gaussians. You can replace a band with a
measured UV–Vis spectrum. The page holds no safety or toxicological data, does
not perform colour-fastness tests and does not offer fluorescent illuminants
such as F11. Everything runs in your browser.

WHO IT IS FOR
=============

  - Students of chemistry and colour science learning absorbance, indicators
    and isosbestic points.
  - Textile and dye professionals who want to see, in principle, how
    concentration, path length, pH and the light source move a colour, and how
    far a colour shifts between lights.
  - Colour enthusiasts curious about why a solution's colour depends on the
    lamp.

WHERE TO FIND IT
================

Open
https://auricartisan.com/tool/general/spectral-tools/industrial-dye-chemistry/
in a current browser. It is listed as Industrial Dye Chemistry on the
Collections page (https://auricartisan.com/collections/) and in the site menu.

QUICK START
===========

  1. Open the tool. The bath holds one Weak-acid indicator at pH 3.50, in a
     1.0 cm path, under D65.
  2. Look at the spectrum: two dashed bands (acid and base form), the filled
     curve you would measure, and a green circle at the isosbestic point.
  3. Select Run the titration and watch the pH sweep from 0 to 14 while the
     swatch and curves change.
  4. Drag pH back to 3.5 and raise Concentration until Beer–Lambert holds
     reads no.
  5. Change the light to A — a blackbody at 2856 K and compare the four
     swatches under The same bath under every light this tool holds.
  6. Add a second dye: pick one from the list under The components and select
     Add.
  7. Open Export and select Download the spectrum to save the 81-row CSV.

WHAT YOU CAN DO
===============

  - Build a bath of up to four dyes from six presets, and set each dye's pKa
    and concentration.
  - Set pH (0–14) and path length (0.1–10 cm), and animate a titration.
  - See both forms of the selected dye, their weighted sum and the isosbestic
    point.
  - Read the colour as sRGB and CIE Lab*, the peak absorbance and its
    wavelength, the Beer–Lambert check, the dominant wavelength and excitation
    purity.
  - Compare the bath under D65, D50, A and E as CIEDE2000 colour differences.
  - Run a tolerance sweep over concentration, path length and molar
    absorptivity.
  - Replace a dye band with your own measured spectrum.
  - Export the spectrum as CSV, the whole bath as JSON, or a link.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt] — open it, the screen tour,
      the first bath.
    - Build a bath [docs/build-a-bath.txt] — dyes, concentration, path length
      and the Beer–Lambert law.
    - Run a titration [docs/run-a-titration.txt] — pH, the two forms, the base
      fraction and the isosbestic point.
    - Compare lights [docs/compare-lights.txt] — illuminants, Lab*, colour
      inconstancy, metamerism and dominant wavelength.
    - Run a tolerance sweep [docs/run-a-tolerance-sweep.txt] — how far the
      colour moves when the recipe varies.
    - Use a measured spectrum [docs/use-a-measured-spectrum.txt] — replace a
      drawn band with your own data.
    - Export and share [docs/export-and-share.txt] — the spectrum CSV, the
      bath JSON and links.
    - Reference [docs/reference.txt] — every control, readout, tab and file
      format.
    - Troubleshooting [docs/troubleshooting.txt] — symptoms, causes and fixes.
    - FAQ [docs/faq.txt] — short answers to common questions.
  - others/ [others/README.txt] — background material.
    - Glossary [others/glossary.txt] — terms used in this tool.
    - Shortcuts [others/shortcuts.txt] — keyboard and pointer actions.
    - Limits and accuracy [others/limits-and-accuracy.txt] — what is
      published, what is the tool's own, what is not held, and safety.
    - Related [others/related.txt] — related tools and Learn articles.
    - Release notes [others/release-notes.txt] — user-facing history.
    - Privacy [others/privacy.txt] — what stays in your browser.
