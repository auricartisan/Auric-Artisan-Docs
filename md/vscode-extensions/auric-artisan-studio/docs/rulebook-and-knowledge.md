---
title: Auric Artisan Studio — Rulebook and knowledge database
description: Search the local rulebook and knowledge database, build knowledge.json and rulebook.md for your workspace, and add validated team guidance.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Rulebook and knowledge database

Every Studio extension ships a local, versioned **knowledge database**: a searchable collection of the rules the Studio checks, the standards they come from, manual test procedures, policies, articles, glossary terms and rulebooks. It works offline and is filtered to the capabilities you installed.

## What is in it

| Kind | What it is | Accessibility | Color | Code Health |
| --- | --- | --- | --- | --- |
| Automated rule | One entry per rule the engine runs, with severity, confidence and remediation | 72 WCAG rules | none | 68 signatures |
| Requirement | Every WCAG 2.2 success criterion | 86 | none | none |
| Manual check | A step-by-step manual test procedure | 8 | none | none |
| Rule category | The seven code-health categories | none | none | 7 |
| Policy | A governance policy | 3 brand | 3 brand | 4 code health |
| Article | A short practical guide | 3 accessibility, 1 brand | 1 brand | 2 code health |
| Rulebook | A structured rulebook | accessibility and brand | brand | code health |
| Glossary | Term definitions | yes | yes | yes |
| Official source | Links to the standards the entries cite | 14 shared sources | same | same |

The counts are for version 0.1.0. With all three extensions installed, the database holds 283 entries.

### Rulebooks

- **Accessibility engineering rulebook**
- **Accessible brand governance rulebook**
- **Code-health balanced baseline**

### Manual checks

- Confirm text alternatives communicate the same purpose
- Review media alternatives for accuracy and synchronization
- Complete error recovery and authentication flows
- Verify focus order preserves meaning and operation
- Operate every workflow with a keyboard
- Test zoom, reflow, and text spacing without loss
- Confirm name, role, value, and state in an accessibility tree
- Verify important status changes are announced without moving focus

See [Manual evidence](../accessibility/docs/manual-evidence.md) for what each one asks you to do.

### Policies

- Brand exceptions are narrow, owned, and temporary
- Brand classification cannot suppress structural findings
- Every brand token has provenance and a semantic role
- Report severity and confidence independently
- Never persist a detected secret value
- Each detector signature has a stable identity
- Suppressions are scoped and reviewable

### Articles

- Debug accessible names from the computed result backward
- Use automation as evidence, not as a conformance verdict
- Audit keyboard and focus as complete user workflows
- Govern brand exceptions without creating an accessibility loophole
- Triage code-health findings with confidence and evidence
- Treat a committed secret as an incident, not a text-edit task

### Official sources

WCAG 2.2, Understanding WCAG 2.2, Techniques for WCAG 2.2, WAI-ARIA 1.2, HTML Accessibility API Mappings 1.0, the ACT Rules Format 1.1, ACT Rules, OWASP Top 10:2025, the OWASP Application Security Verification Standard, the OWASP Cheat Sheet Series, the Common Weakness Enumeration and CWE-798 (hard-coded credentials), NIST's Secure Software Development Framework, and the Design Tokens Format Module.

### ACT alignment

The accessibility entries follow the structure of the W3C's Accessibility Conformance Testing (ACT) rules format: they record what each check applies to, what it expects, how it is assessed, the requirements it maps to and where it comes from. This makes the evidence consistent and reviewable. It is **not** a claim of ACT conformance, and every exported file says so (`actConformant: false`).

## Search the database

1. Run **Auric Artisan: Open Rulebook & Knowledge Database**, or select **Rulebook** on the Overview or at the foot of the Studio's rail, or **Open rulebook & knowledge database** in the Command Center.
2. A searchable list opens, titled **Auric Artisan Knowledge Base · 283 entries** (the number depends on what is installed). Rulebooks are listed first, then manual checks, automated rules, policies, articles, requirements, glossary entries, sources and rule categories.
3. Type to filter. The search matches titles, descriptions (kind, domain and ID) and summaries, so you can search for a rule ID such as `img-alt`, a criterion such as `1.4.3`, a term such as `ARIA`, or words such as `secret`.
4. Select an entry. It opens as a Markdown document with its summary, domain, kind, severity, confidence, requirements, remediation, applicability, procedure, pass and fail conditions, evidence to record, controls and official sources, whichever apply.

Selecting a rulebook opens the whole rulebook.

**Rule details** in an issue hover opens the entry for that finding's rule directly.

## Build the workspace knowledge database

**Auric Artisan: Build Workspace Knowledge Database (JSON + Markdown)** writes the database into your workspace so it can be read by other tools, reviewed or shared.

1. Open a workspace folder and run the command (or **Build workspace knowledge database** in the Command Center).
2. The Studio writes:
   - `.auric-artisan/knowledge.json`: every entry, with the schema version, knowledge version, content hash, alignment, `actConformant: false`, domains and statistics;
   - `.auric-artisan/rulebook.md`: every installed rulebook in full, with a note that the database makes no ACT conformance claim;
   - `.auric-artisan/knowledge-overrides.json`: an empty template for team additions, created only if the file does not exist yet. An existing file is never overwritten.
3. `rulebook.md` opens. A message confirms, for example **Auric Artisan: built 283-entry knowledge.json and 3 rulebook(s) locally. A team override template was also created.**, with **Open JSON**, **Open Overrides** and **Open Data Folder**.

`knowledge.json` and `rulebook.md` are regenerated each time and are excluded from source control. `knowledge-overrides.json` is meant to be committed.

## Add team guidance with knowledge-overrides.json

`knowledge-overrides.json` lets your team add reviewed guidance: manual checks, articles, policies, glossary entries and rulebooks. Added entries appear in search and in the generated files alongside the built-in ones. They can never replace a built-in entry.

The template looks like this:

```json
{
  "schemaVersion": 1,
  "kind": "auric-artisan.knowledge-overlay",
  "entries": []
}
```

An example entry:

```json
{
  "id": "custom:a11y:modal-focus-return",
  "kind": "manual-check",
  "domain": "a11y",
  "title": "Return focus when a modal closes",
  "summary": "After any modal closes, focus returns to the control that opened it.",
  "sourceIds": ["w3c-wcag22"],
  "tags": ["focus", "modal"]
}
```

### Rules for entries

| Field | Rule |
| --- | --- |
| `id` | Required. Must start with `custom:`, then 3 to 128 lowercase letters, digits, `:`, `.`, `_` or `-`. Must be unique and must not match a built-in ID. |
| `kind` | Required. One of `manual-check`, `article`, `policy`, `glossary`, `rulebook`. |
| `domain` | Required. One of `shared`, `a11y`, `code-health`, `brand`, `color` (also accepted: `accessibility`, `codehealth`, `health`, `branding`, `colour`). |
| `title`, `summary` | Required, non-empty, up to 12,000 characters each. |
| `sourceIds` | Optional. Must name built-in sources, for example `w3c-wcag22`, `w3c-aria12`, `owasp-top10-2025`. |
| `sections` | Required for a rulebook: a list of sections, each with a `title` and optional `entryIds` that must exist. |

A policy with `"policyType": "brand-exception"` must also have `scope`, `rationale`, `owner`, `approvedAt` and `expiresAt` (ISO dates, expiry after approval and not already passed), a non-empty `allowedFindingKinds` limited to `contrast`, `color-vision` and `branding`, and non-empty `ruleIds` limited to colour rules (`low-contrast…`, `cvd-risk…`, `branding-…`, `contrast:…`). A brand exception can never cover a structural accessibility rule.

The whole file must be under 256 KB and hold at most 500 entries. Entries whose domain is not installed are kept in the file but not shown.

### When the file is invalid

- **Searching** falls back to the built-in database and shows a warning that starts **Auric Artisan: workspace knowledge overrides are invalid; using the built-in database.**, followed by the problems found.
- **Building** stops and shows **Auric Artisan: could not build the knowledge database —** followed by every problem, one per line, such as `overlay.entries[0].id must start with custom: and use stable lowercase characters`.

Fix the listed problems and run the command again.

## Related

- [Manual evidence](../accessibility/docs/manual-evidence.md)
- [The accessibility rules](../accessibility/docs/rules.md)
- [Code-health categories and signatures](../code-health/docs/categories-and-signatures.md)
- [Suppression and branding](suppression-and-branding.md)
