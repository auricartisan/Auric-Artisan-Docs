---
title: Auric Artisan Font Hub — check CDN and browser delivery
description: Run Font Hub's CDN health check and fix fonts that preview in VS Code but do not load on your website.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Check CDN and browser delivery

A font that previews in Font Hub can still fail on your website. Previews are fetched by VS Code itself, while your page's fonts are fetched by the browser, which applies extra security rules. The main one is *CORS* (cross-origin resource sharing): a browser only uses a font from another address if that server says the page is allowed to.

## Run the check

1. Run **Auric Artisan Font Hub: Check Font CDN and Browser CORS**, or select **Check CDN health** (or **CDN diagnostics**, or **Run a live check**) in Font Hub.
2. Font Hub sends small `HEAD` requests to the CDN for three things:
   - **Catalog** — the catalogue file;
   - **Stylesheet** — a family's stylesheet;
   - **Font file** — that family's preview font.
3. Each request is made as if from the test address `http://localhost:5500`.
4. The report shows, for each item, whether it is available, whether its content type is right, and, for the font file, whether CORS allows the test address.

The overall result is **Browser delivery ready** only if every item is available with the right content type and the font file allows cross-origin use. Otherwise it says **Needs attention**, with **CORS missing for test origin** when that is the problem. **Check again** reruns it.

The check is a sample: one catalogue file, one stylesheet and one font file, from one test address. It is not an audit of every family or of your production address. It needs `auricFontLib.network.enabled`; if the network is switched off you see **Enable network access in Font Hub settings to run CDN checks.**

## When fonts do not load on your site

Work through these in your browser's developer tools (Network tab, filtered to fonts and CSS):

1. **Is the stylesheet loaded?** Look for `fonts.auricartisan.com/css/<family-id>.css` with status 200. If it is missing, the link or `@import` is not in the page, or it is in a file the page does not load.
2. **Is the font file loaded?** A successful stylesheet alone is not enough. Look for the font file request.
3. **Is it blocked by CORS?** The browser console reports a CORS error. A public font CDN can answer every site with:

   ```http
   Access-Control-Allow-Origin: *
   ```

   A restricted CDN should allow your exact website and development addresses instead.
4. **Is the content type right?** Stylesheets must be served as `text/css` and fonts as a font type.
5. **Is it blocked by your Content Security Policy?** If your site has a Content Security Policy, allow the CDN in `style-src` and `font-src`. Under a strict policy, inline `<style>` rules added by Font Hub may be refused; move the generated class rule into a stylesheet your policy allows.
6. **Is the class applied?** The generated setup only defines `.auric-font-<family-id>`. Add the class to your markup, or use the family in your own CSS.

Font Hub reports what the CDN answers. It cannot change a server's hosting configuration or get around browser security.

When delivery works, the browser's Network tab shows both the stylesheet and the font file loaded with status 200, and the text renders in the chosen family.
