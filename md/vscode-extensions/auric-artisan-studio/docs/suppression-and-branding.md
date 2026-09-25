---
title: Auric Artisan Studio — Suppression and branding
description: Silence a false positive with auric-disable comments, or classify a deliberate brand colour with auric-brand comments, by hand or with quick fixes.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Suppression and branding

Two families of comment directives let you tell the Studio about decisions you have made:

- **Suppression** (`auric-disable-…`) removes a WCAG or code-health finding from the results and the score. Use it for false positives or rules you have consciously decided not to follow in one place.
- **Branding** (`auric-brand-…`) re-classifies a colour finding as intentional brand identity. The finding stays visible in its own **Branding** group but leaves the score. Use it for deliberate brand colours, such as a logo lock-up or a decorative accent.

A **directive** is a special comment the Studio reads, written in the comment syntax of the file's language.

## Suppression directives

| Directive | Silences |
| --- | --- |
| `auric-disable-line` | Findings on the same line |
| `auric-disable-next-line` | Findings on the following line |
| `auric-disable-file` | Findings anywhere in the file |

Each directive can be followed by a **scope**: one or more tokens separated by commas or spaces, optionally after a colon. Without a scope, a directive silences every WCAG and code-health finding it covers.

### Scopes for WCAG findings

| Token | Example | Silences |
| --- | --- | --- |
| A rule ID | `auric-disable-line img-alt` | That rule only |
| A success criterion | `auric-disable-line 1.1.1` | Every rule mapped to that criterion |
| `a11y` | `auric-disable-file a11y` | All WCAG findings |
| `all` | `auric-disable-line all` | All WCAG and code-health findings |

### Scopes for code-health findings

| Token | Example | Silences |
| --- | --- | --- |
| A category | `auric-disable-line secret,security` | Findings in those categories: `secret`, `security`, `risk`, `debug`, `todo`, `conflict`, `size` |
| A rule ID | `auric-disable-line ch-risk-eval` | That signature only (the ID shown on the diagnostic) |
| `codehealth` | `auric-disable-file codehealth` | All code-health findings |
| `all` | `auric-disable-line all` | All WCAG and code-health findings |

Whatever rule ID or category the editor shows on a finding can be pasted into a directive and will work.

### Examples

```html
<!-- auric-disable-next-line img-alt -->
<img src="spacer.gif">
```

```css
/* auric-disable-file a11y */
```

```python
cache_key = hashlib.md5(data).hexdigest()  # auric-disable-line security
```

```js
// auric-disable-next-line ch-risk-eval
const result = eval(trustedTemplate);
```

In JSX markup, put the directive in braces so it is not rendered as text: `{/* auric-disable-next-line img-alt */}`.

### Rules the Studio applies

- **Code-health directives must be inside a real comment.** A directive that is only mentioned in prose or a string literal never silences anything. In Markdown, directives shown inside fenced code blocks are treated as examples and ignored.
- **Suppression does not apply to contrast.** Contrast, APCA and colour-vision findings are not silenced by `auric-disable-…` directives. To take a deliberate colour pair out of the score, mark it as branding (below), or change the colours.
- **Suppressed findings disappear** from the Problems panel, the Project Issues view, the Studio, reports, `health.json`, SARIF and the score.

## Suppress with a quick fix or hover

You rarely need to type a directive. The Studio writes one for you in the right comment syntax:

| Where | Action | What it inserts |
| --- | --- | --- |
| Quick fix on a WCAG finding (`Ctrl` + `.`) | **Ignore this WCAG 1.1.1 finding here** | `auric-disable-next-line 1.1.1` on the line above, with the line's indentation |
| Quick fix on a WCAG finding | **Ignore all accessibility findings in this file** | `auric-disable-file a11y` at the top of the file |
| Quick fix on a code-health finding | **Ignore this secret finding here** (the category varies) | `auric-disable-next-line secret` on the line above |
| Quick fix on a code-health finding | **Ignore all secret findings in this file** | `auric-disable-file secret` at the top of the file |
| **Ignore here** in an issue hover | | `auric-disable-next-line` followed by the rule ID, on the line above |

After **Ignore here**, the status bar confirms, for example `Auric Artisan: img-alt ignored on this line`.

### Comment syntax used

| Languages | Comment written |
| --- | --- |
| JavaScript, TypeScript, JSX, TSX, JSON, Go, Rust, C, C++, C#, Java, Swift, Kotlin, Dart, PHP, Scala, Groovy, SCSS, Less | `// …` |
| Python, Ruby, YAML, TOML, shell, Perl, R, Elixir, Dockerfile, Makefile | `# …` |
| SQL, Lua, Haskell | `-- …` |
| HTML, XML, Vue, Svelte, Astro, Markdown, Handlebars | `<!-- … -->` |
| CSS, PostCSS, Sass, Stylus, and any other language | `/* … */` |

> **Note:** Strict JSON does not allow comments. A directive inserted into a `.json` file makes it invalid for most JSON parsers. For JSON files, prefer `.auricignore` or leave the finding and review it.

## Branding directives

| Directive | Covers |
| --- | --- |
| `auric-brand-line` | Colour findings on the same line |
| `auric-brand-next-line` | Colour findings on the following line |
| `auric-brand-file` | Colour findings anywhere in the file |

Optional scope tokens narrow the claim: `contrast`, `apca` or `cvd` (colour-vision risk). `color` or `all`, or no scope at all, cover every colour kind. Example: `/* auric-brand-line: contrast,cvd */`.

```css
.logo-mark { color: #d3af37; background: #fff; }  /* auric-brand-line */
/* auric-brand-next-line */
.hero { color: var(--brand-gold); background: var(--brand-ink); }
```

### What branding changes

- In the editor, the finding becomes an information-level diagnostic starting **Branding —**, and its hover is titled **Intentional branding**.
- In the Project Issues view it moves to a **Branding** group marked **excluded from score**, with a heart icon. In the Studio's Findings tool it moves to a **Branding** section.
- It is left out of the contrast sub-score, the failing-pair lists and the colour-vision penalty.
- In `health.json` and SARIF it is still recorded, as an informational issue from the source `branding`, marked as excluded from the score. The exclusion is always visible, so a reviewer can audit every excluded pair.

Every branding explanation carries the same reminder: **Classified as intentional branding — shown separately and excluded from the accessibility score. Brand colors still need a readable pairing wherever they carry text or UI meaning.**

### Branding is not a loophole

Only colour findings (contrast, APCA and colour-vision risk) can be classified as branding. Structural WCAG findings, such as a logo image without alt text or an unlabelled button, keep counting on a marked line. Their message adds: **(A branding mark covers this line, but structural accessibility issues are not brandable — the finding still counts.)** The Findings tool reports how many such marks were ignored. Code-health findings, including secrets, are never brandable.

### Mark a line with a command

1. Put the cursor on the line (or one cursor on each of several lines).
2. Run **Auric Artisan: Mark Line as Intentional Branding (Toggle)** from the Command Palette or the editor's right-click menu. It is on the menu in HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JavaScript, TypeScript, JSX, TSX, CSS, SCSS, Less, Sass, PostCSS, Stylus and Markdown files.
3. The command adds `auric-brand-line` at the end of the line in a comment, and the status bar says **Auric Artisan: line marked as intentional branding — color findings here move to the Branding group.**
4. Run it again on the same line to remove the mark: **Auric Artisan: branding mark removed — findings here are graded again.**

You can also select **Intentional branding** in a contrast hover, or **Mark as intentional branding** in the Contrast Studio.

The command writes `# …` in hash-comment languages, `<!-- … -->` in markup languages, `/* … */` in CSS dialects, and `// …` everywhere else. Inside a `<style>` block of an HTML, Vue or Svelte file you can change the comment to `/* auric-brand-line */`; it works the same.

### The branding.enabled setting

`auricColor.branding.enabled` and `auricA11y.branding.enabled` (both on by default) control whether the editor honours branding marks. When off, marked pairs are shown as ordinary contrast findings in the editor. Project scans and reports always honour the marks.

### Branding colours in your theme

The Branding group's colours can be changed with VS Code's `workbench.colorCustomizations`. See [Theme colours](reference.md#theme-colours).

## Suppression or branding?

| Situation | Use |
| --- | --- |
| The checker is wrong about this code | Suppression, scoped to the rule ID |
| You deliberately accept a rule's risk here, after review | Suppression, scoped to the rule ID, with a comment explaining why |
| A deliberate brand colour pair that fails contrast | Branding |
| A structural failure on a brand element | Fix it; neither directive can hide it from the score as branding |

## Related

- [Scores and grades](scores-and-grades.md)
- [Rulebook and knowledge database](rulebook-and-knowledge.md), which includes the accessible brand governance rulebook and policies such as **Brand classification cannot suppress structural findings**.
