---
title: Security Policy — summary
description: A plain-language summary of Auric Artisan's legal Security Policy — principles, data protection, web-analysis scope, your responsibilities, limits, vulnerability reporting and incidents.
product: Website › Company and legal
updated: 2026-09-25
---

# Security Policy

Official page: https://auricartisan.com/legal/security/ — **Security Policy & Safe Use**, version 2.2, effective 27 April 2026, last updated 23 May 2026. **The official policy is authoritative.** For the technical description of how the platform is protected, see the separate [Security page](security-page.md).

## Key points

- Account, session, billing, API and tool traffic are protected where those features are enabled.
- Web analysis must only be used on sites you own or are authorised to test.
- Security checks in web analysis are informational — not a certified audit or penetration test.
- Collection and retention of submitted URLs, reports and metadata is kept to a minimum.
- No system can guarantee perfect security.

## Section by section

1. **Principles** — Minimisation, least privilege, responsible tooling, and improving controls as infrastructure matures.
2. **Current infrastructure status** — Payments are valid only through official live checkout flows.
3. **Data and transmission security** — Encrypted transport; limited access to submitted inputs and reports; secure, HttpOnly session cookies and CSRF checks for signed-in requests; origin checks, request-size limits, security headers and rate limits on sign-in routes; local storage for preferences where practical.
4. **Web analysis scope** — Only for sites, pages and assets you own, control or have permission to test. Do not probe, stress or exploit others' systems; do not present results as certification; do not submit private URLs, credentials or admin pages unless authorised; do not misrepresent another organisation's security.
5. **Access control and internal practices** — Restricted administrative access, separate development and production, no secrets in public code, reviewed dependencies.
6. **Your responsibilities** — Submit only what you may analyse; keep credentials and confidential URLs out of tool inputs; check outputs before relying on them; use vision tools only for exploration and learning; report issues responsibly rather than attempting unauthorised access.
7. **Limitations and non-certification** — No guarantee of absolute security; outputs are not certified industrial, medical, regulatory or safety-critical results.
8. **Vulnerability reporting** — Report through the contact page with enough detail to reproduce. Do not access, change, delete, download or disclose data that is not yours; act in good faith.
9. **Security incidents** — Investigate, contain, fix, and notify affected users or authorities where the law requires.
10. **Changes** — May be updated.

## Reporting a vulnerability in practice

The Security page gives the specific route: email security@auricartisan.com, or use the contact form's **Security** topic (https://auricartisan.com/company/contact/?topic=security). It aims to acknowledge within 24 hours. See [Security page](security-page.md#responsible-disclosure).

## Related

- [Security page](security-page.md)
- [Acceptable Use Policy](acceptable-use-policy.md)
