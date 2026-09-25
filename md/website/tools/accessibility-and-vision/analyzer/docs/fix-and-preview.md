---
title: Analyzer — Fix and preview
description: Turn findings into code with the Fixes panel, try changes live in the Playground, add your own checks in Rules, and let your site be previewed with CSP Setup.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Fix and preview

Four sections help you act on what the audit found. **Fixes** gives you the code. **Playground** lets you try colour changes on the page and watch the score move. **Rules** adds your own checks to every audit. **CSP Setup** explains how to let the Analyzer preview a site you own.

**Fixes** is available in both modes; the other three are Advanced only. For the accessibility engine's own patches (the ready-to-paste CSS and per-element suggestions), see the Fixes view in [The accessibility engine](accessibility-engine.md).

## Fixes

The developer hand-off: every actionable fix for the page, grouped by type.

### Parts of the section

| Part | What it does |
| --- | --- |
| **How to use this** | Explains that colour fixes give exact CSS values and structural fixes describe the HTML to change |
| **Total** | The number of actionable fixes |
| **Fix This First** | The top fixes, numbered, each with its reason and an impact label such as "Low impact" |
| **Fix Mode** | **Safe fixes** or **Aggressive fixes** (below) |
| **Heuristic Auto-Fix** | Four buttons that apply or export the generated fix stylesheet (below) |
| **Fix Details** | **Color Fixes (High Priority)** with a **Copy fix** button on each, and **Structural & Semantic Fixes** |

### Fix Mode

- **Safe fixes** favours brand-safe contrast changes and structural recommendations. This is the default.
- **Aggressive fixes** also includes broader CSS normalisation.

Changing the mode rebuilds the generated stylesheet. Your choice is remembered in this browser.

### Heuristic Auto-Fix

The generated stylesheet contains safe visual fixes: focus rings, media sizing, motion reduction and generated contrast colours.

| Button | What it does |
| --- | --- |
| **Apply in Playground** | Applies the stylesheet to the Playground preview only, and updates its live score. Nothing on your site changes. |
| **Copy Batch CSS** | Copies the whole stylesheet to the clipboard |
| **Diff View** | Shows the affected rules as they are now beside the fixed version |
| **Export Fix CSS** | Downloads the stylesheet as `auric-analyzer-fixes.css` |

If the Playground preview is not open yet, **Apply in Playground** opens it first. If it still cannot apply, it says "Open the Playground preview first, then apply heuristic fixes."

### A safe way to apply fixes

1. Copy a small group of fixes, not all of them.
2. Apply them in your code.
3. Re-run the audit and check **Before / After** and **Compare**.
4. Repeat, then export the final report.

## Playground

An editor over the analysed page. Select any element in the preview, change its colours, and watch the score change live. It also holds a palette generator and a design lab that map a palette onto the page's elements.

### Palette Generator

Open the **Palette Generator** bar to show it.

| Control | What it does | Range or options | Default |
| --- | --- | --- | --- |
| Undo, redo, save, reverse | Step through palette history, save a version, reverse the order | Buttons | — |
| Colour slots | Each colour has a picker, a lock (kept when regenerating) and a remove button; **+** adds a slot | — | 5 slots |
| **Size** | Number of colours | 2 to 12 | 5 |
| **Base hue** | Starting hue in degrees | 0 to 360 | 220° |
| **Seed** | Text that makes seeded palettes repeatable | Any text | `auric` |
| Generation mode | How the next palette is built | Ten modes (below) | — |

The generation modes are **Random**, **Seeded**, **Harmony**, **Gradient**, **Contrast**, **WCAG-friendly**, **CVD-safe**, **Accessible**, **Compliant** and **Comparable**.

### Score Comparison

Shows **Original Score** and **Live Score** side by side, or "No changes yet" before you edit anything.

### Filter & Rules

- An element filter: **All Elements**, **Images (img)**, **Buttons**, **Links (a)**, **Headings (h1-h6)**, **Forms & Inputs**, **Text Elements**, **Interactive**.
- A rule set for the live score: **WCAG 2.1 AA**, **WCAG 2.2**, **Core Web Vitals**, **WCAG 3 (Preview)**, **All Rules**.

### Element Editor

Select any text or element in the **Live Preview**. The editor then lets you change its text colour and background and shows accessible alternatives straight away. Every change is logged and counted in the live score.

| Button | What it does |
| --- | --- |
| **Export CSS Fixes** | Downloads your element edits as `accessibility-fixes.css` |
| **Export Palette** | Downloads the fixed palette as `fixed-palette.css` |
| **Reset All** | Removes every edit |

### Design Lab Editor

Maps each kind of element to a slot in your palette, and applies the result live.

- **Element Mapping** has one menu each for **Backgrounds**, **Text**, **Headings**, **Buttons**, **Button text**, **Cards**, **Sections**, **Borders**, **Accent / Links**, **Shadows** and **Form fields**. Each can be set to a palette slot or **(unset)**.
- **Live Audit Warnings** flags pairs that are hard to read or not safe for colour-vision deficiencies. When all is well it says "No accessibility warnings — palette looks readable and CVD-friendly."
- **Detected Site Colors → Suggestions** lists the page's own colours with a suggested replacement and an **Apply** button.
- **Generated CSS** shows the stylesheet for the mapping, with these buttons:

| Button | File |
| --- | --- |
| **Copy CSS** | Copies it to the clipboard |
| **Download .css** | `auric-design-lab.css` |
| **Theme tokens (JSON)** | `auric-design-tokens.json` |
| **Runtime JS** | `auric-design-lab.js`, a small script that applies the palette to a live page |
| **Palette JSON** | `auric-palette.json` |

**Optional Runtime JS** shows the script before you download it.

### When the page will not load in the preview

The Playground needs to load the page in a frame. If the site blocks embedding, the preview shows **Couldn't embed this page** with **Run in browser**, **Open in new tab**, **Try again** and **View CSP setup**. See [Colour, contrast and vision](colour-contrast-and-vision.md) for what each does.

## Rules

Create your own selector-based checks without writing JSON. Each rule becomes part of the next analysis and can check that something exists, count it, or require an attribute. Custom rule results appear in the report under **Custom Rules**.

### Pre-built templates

Select a template to fill in the form below, then adjust and save it.

- **SEO** (10): SEO title exists; Meta description exists; Canonical link present; Open Graph title; Open Graph image; H1 heading present; Single H1 per page; HTML lang attribute; No accidental noindex; Viewport meta tag.
- **A11Y** (9): Buttons have names; Images have alt text; Inputs have labels; Links have descriptive text; Skip navigation link; Main landmark present; Nav landmark present; No outline:none on focused elements; Tables have header cells.
- **UX** (5): No hidden priority content; 404 page has search or nav; No positive tabindex values; Print stylesheet present; No links pointing to #.
- **Performance** (6): Lazy-load non-critical images; Scripts defer or async; Preconnect to font origins; No `<style>` blocks in body; Images declare width/height; No autoplay videos without muted.
- **Security** (5): No inline handlers; External links use rel noopener; No mixed-content resources; Meta charset declared; Password fields allow autocomplete.

### Add a rule

1. Enter a **Rule name**, for example "Primary CTA has label".
2. Enter a **CSS selector**, for example `.cta-primary, #signup-btn`.
3. Choose a **Check type**: **Element exists**, **Element must not exist**, **Minimum count**, **Maximum count** or **Attribute required**.
4. Fill in **Min**, **Max** or **Attribute** (for example `aria-label`) if the check type needs it.
5. Choose a **Severity**: **Medium** (default), **Critical** or **Minor**.
6. Write an **Issue message** and a **Fix suggestion**.
7. Select **Add Rule**.
8. Select **Save and re-run** to audit the page again with your rule.

The result: your rule appears under **Rule Results** and in **Latest Results** as passed or failed, with the number of matches.

### Manage rules

| Control | What it does |
| --- | --- |
| Filter Rules | Show **All Checks**, or only **Critical**, **Medium** or **Minor** rules |
| **Advanced JSON editor** | Edit every rule as JSON directly |
| **Save and re-run** | Saves the rules and runs the audit again |
| **Reset defaults** | Restores the two starting rules |
| **Export rules** | Downloads your rules as `analyzer-custom-rules.json` |
| **Disable** / **Remove** | On each rule in **Rule Results** |

The Analyzer starts with two rules: **Main landmark** (a `main` element or `role="main"` must exist, Medium) and **Primary heading** (at least one `h1`, Critical). Your rules are stored in this browser.

## CSP Setup

**CSP & Access Setup** explains how to configure a server you own so the Analyzer can load its pages in the **Simulation**, **Device Preview**, **Before / After** and **Playground** sections. It is a guide to your own server's headers; it does not change anything by itself.

### What it covers

- **Why pages are blocked**: `X-Frame-Options: DENY` or `SAMEORIGIN`, CSP `frame-ancestors 'none'`, and CORS restrictions, with the solution: add the Auric Artisan origin to `frame-ancestors` and remove `X-Frame-Options`.
- **Minimum required**: the header to add to every page you want to preview (shown below), and removing or updating `X-Frame-Options`, which overrides CSP in some browsers.
- **Current page detection**: the analysed URL, its origin, and the CSP it sent.
- **Server Config Snippets** with a **Copy** button each, for **Nginx**, **Apache (.htaccess)**, **Express / Node.js**, **Cloudflare (Transform Rules)**, **Netlify (_headers file)**, **Vercel (vercel.json)**, **HTML Meta Tag (limited)** and **CORS Headers (full set)**.
- **Verification Checklist**: check the headers in your browser's developer tools, confirm `X-Frame-Options` is gone, re-analyse your URL, check the console for CSP errors, and review the **Security** section. **→ Open Security Tab** takes you there.
- **How to Remove / Delete These Rules**: snippets that undo the change for each platform, and **Removal Verification Steps**.

The minimum header is:

```text
Content-Security-Policy: frame-ancestors 'self' https://auricartisan.com https://www.auricartisan.com
```

> **Important:** In some of the platform snippets the header value repeats the header name, as in `"Content-Security-Policy: frame-ancestors …"` inside a `Content-Security-Policy` header. Before you deploy, make sure the value starts with `frame-ancestors`, exactly as in the **Minimum required** line above. A duplicated name makes the header invalid.

> **Note:** `frame-ancestors` cannot be set with a `<meta>` tag. It only works as an HTTP response header.

Only allow embedding on sites you control, and remove the rule when you no longer need it.
