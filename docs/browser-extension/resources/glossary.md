---
title: Browser extension — Glossary
description: Plain-language definitions of the colour, contrast, accessibility and browser terms used in the browser extension documentation.
product: Browser extension
updated: 2026-09-25
---

# Glossary

## Colour

**Accent colour.** The colour the extension uses for its buttons, focus rings and highlights. You choose it in Settings › Appearance.

**ASE.** Adobe Swatch Exchange, a palette file format many design applications can import.

**Chroma.** How colourful a colour is, from grey (no chroma) to fully saturated. **Chroma room** in the Picker is how much more chroma a colour can take before it leaves a gamut.

**CMYK.** Cyan, magenta, yellow and black, the inks of print. The extension converts to CMYK with a simple formula, not a print profile.

**Colour space.** A system for describing colours with numbers, such as sRGB, LAB or OKLCH. Mixing or blending in different spaces gives different in-between colours.

**Display P3 (P3).** A wider gamut than sRGB, used by many modern screens. Colours outside sRGB can be written in CSS with `color(display-p3 …)` or `oklch()`.

**ΔE (delta E).** A number for how different two colours look. Under about 2, most people cannot see the difference.

**Gamut.** The range of colours a screen or colour space can show.

**Harmony.** A set of colours chosen by their positions on the colour wheel, such as complementary (opposite) or triadic (evenly spaced three).

**HEX.** A colour written as `#RRGGBB` in hexadecimal, for example `#d3af37`. An eight-digit form adds opacity.

**HSL, HSV, HWB.** Ways of writing a colour by hue (its position on the wheel) plus saturation and lightness (HSL), saturation and value (HSV), or whiteness and blackness (HWB).

**Hue.** The quality that makes a colour red, green, blue and so on, measured in degrees around a wheel.

**k-means.** A method that groups many colours into a few representative ones. Page palette's **Dominant (k-means)** mode uses it to find eight.

**LAB and LCH.** Colour spaces designed around how people perceive lightness and colour. LCH is LAB written as lightness, chroma and hue.

**Linear RGB.** RGB without the brightness curve screens apply, so light adds up as it does physically.

**OKLAB and OKLCH.** Newer perceptual colour spaces. Equal steps in OKLCH lightness look like equal steps to the eye, and hue stays steady as lightness changes, which makes them good for scales and gradients. CSS supports both with `oklab()` and `oklch()`.

**Opacity (alpha).** How transparent a colour is, from 0 (invisible) to 1 or 100% (solid).

**Scale.** A series of steps of one colour, from light to dark, such as Tailwind's 50 to 950.

**sRGB.** The standard colour space of the web. HEX, `rgb()` and `hsl()` colours are sRGB.

**Tint, shade, tone.** A colour mixed toward white (tint), toward black (shade) or toward grey (tone).

**XYZ.** A reference colour space from which the others are calculated.

## Contrast and accessibility

**AA and AAA.** WCAG conformance levels. AA is the common legal and industry target; AAA is stricter.

**Accessible name.** The name assistive technology announces for an element, such as a button's text or an `aria-label`. It is computed by a standard algorithm.

**APCA and Lc.** The Accessible Perceptual Contrast Algorithm, used in the WCAG 3 drafts. It gives a lightness contrast score, Lc, whose sign shows polarity (dark on light or light on dark). A higher absolute Lc reads more easily, and the score needed depends on font size and weight.

**ARIA.** Accessible Rich Internet Applications, attributes such as `role` and `aria-label` that tell assistive technology what an element is and does.

**Borderline.** In the audit, text that passes its contrast threshold by less than 1.5.

**Colour-vision deficiency.** Reduced ability to tell some colours apart. Protanopia, deuteranopia and tritanopia are the absence of red-, green- or blue-sensitive cones; the "-anomaly" forms are weaker versions; achromatopsia is the absence of colour vision.

**Contrast ratio.** WCAG's measure of contrast between two colours, from 1:1 to 21:1, based on their relative luminance.

**Finding.** One problem the extension found, with its severity and the actions that fit it.

**Impact.** How much a finding affects people: critical, serious, moderate or minor.

**Landmark.** A region of a page, such as main, navigation or footer, that assistive technology lets people jump between.

**Large text.** In WCAG, text at least 24 px, or at least 18.66 px when bold. It needs less contrast than body text.

**Low vision.** Sight that glasses cannot fully correct. The extension simulates cataracts, general low vision, glaucoma (tunnel vision) and AMD (age-related macular degeneration, loss in the centre).

**Relative luminance.** How bright a colour is to the eye, on a scale from 0 (black) to 1 (white).

**Roving tabindex.** A pattern where a group of controls, such as tabs, holds one Tab stop and arrow keys move inside it.

**Success criterion.** A single testable requirement in WCAG, numbered like 1.4.3 (contrast).

**WCAG.** The Web Content Accessibility Guidelines. The extension audits against WCAG 2.2.

## Browser and code

**Content script (page script).** The small part of the extension that runs inside web pages so the tools can read them.

**CSS custom property (CSS variable).** A named value in CSS, written `--name`, and used with `var(--name)`.

**Design token.** A named design decision, such as a colour or spacing value, stored so tools can share it. **W3C design tokens** is the standard JSON format for them.

**Eyedropper.** A tool that samples the colour of any pixel on screen.

**Locator.** Code that finds an element on a page, such as a CSS selector or a Playwright `page.locator(…)`.

**Manifest V3.** The current format for browser extensions in Chromium browsers and Firefox.

**Selector.** A CSS pattern that identifies an element, such as `main > .card h2`.

**Shadow root.** An isolated part of a page. The extension draws its panels in shadow roots so the site's styles and its own cannot affect each other.

**Side panel, sidebar.** A panel docked beside the page, in Chromium browsers and Firefox respectively.

**Tailwind `@theme`.** The block Tailwind CSS version 4 uses to define design tokens as CSS variables.

**XPath.** A way of addressing an element by its path in the page's structure.
