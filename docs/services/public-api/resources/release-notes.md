---
title: Public API — Release notes
description: The dated changes to the public API that its documentation states.
product: Services › Public API
updated: 2026-09-25
---

# Release notes

The API has no separate public changelog. These are the dated facts its documentation states. The current version is always reported by `GET /v1`.

## 3 September 2026 — Analyzer API guide

- A guide to the three analyzer endpoints was published: `GET /v1/analyzer/stages`, `POST /v1/analyzer/inspect` and `POST /v1/analyzer/render`.
- The analyzer endpoints read page source only, refuse checks that need a browser, and return no overall score.
- Costs: 1, 12 and 10 credits.

## 12 August 2026 — Credits, overage and new Industrial Pro allowance

- The REST API reference was updated.
- The monthly quota is counted in credits, with heavier endpoints costing more than one credit.
- Prepaid, opt-in pay-as-you-go overage, a monthly spend cap and a hard ceiling of ten times the included allowance.
- Industrial Pro's allowance became 10,000,000 credits a month for subscriptions started on or after this date. Earlier Industrial Pro subscriptions, sold as "Unlimited", keep 1,000,000,000 credits a month.

## 8 July 2026 — REST API reference

- The REST API reference was published, with API keys created in the account dashboard.

## Upcoming

The analyzer guide lists two things "not here yet": a rendered scan (contrast, the accessibility engine and deep DOM comparison through the API) and a whole-site crawl as a job.
