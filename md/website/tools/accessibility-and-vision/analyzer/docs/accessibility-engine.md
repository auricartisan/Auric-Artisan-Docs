---
title: Analyzer — The accessibility engine (A11y+)
description: Read and act on every view of the A11y+ panel, from the grade and findings to the accessibility tree, screen-reader transcript, conformance table and exports.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# The accessibility engine (A11y+)

The **A11y+** panel holds the Analyzer's accessibility engine: 126 rules checked against the page as your browser actually renders it, plus widget-pattern checks, an accessibility tree, a screen-reader transcript, a colour-vision table, a focus and target map, a WCAG 2.2 conformance table and five exports. It is available in Advanced mode, and runs when the **Accessibility** check is on.

In Simple mode the same engine still runs and feeds the **Accessibility** category of the overall score; you just do not see its panel.

## How the panel is organised

A row of four groups sits at the top of the panel. Selecting a group opens its first view; groups with more than one view show a second row of view buttons.

| Group | Views |
| --- | --- |
| **Overview** | Overview |
| **Findings** (with the issue count) | **Issues**, **Fixes** |
| **Inspect** | **Widgets**, **Annotations**, **A11y tree**, **Screen reader**, **Vision**, **Focus & targets** |
| **Report** | **Conformance**, **Export** |

Most blocks inside a view are folding cards: select the card's title to open or close it.

## Key terms

- **Rule** — one automated check, such as "Buttons must have discernible text". Each rule applies to some elements and passes, fails, or needs review on each.
- **Impact** — how badly a failure affects someone using the page. The engine uses four levels, each with a one-line meaning in the panel:

| Impact | Meaning shown |
| --- | --- |
| critical | Blocks people from using the page at all. |
| serious | Makes a task very difficult or unreliable. |
| moderate | Causes friction and confusion. |
| minor | Polish — worth fixing, rarely blocking. |

- **Needs review** — the rule ran and could not decide. Text over a photograph or a gradient is the usual cause, because there is no single background colour to measure. A person has to look.
- **Not tested** — no rule can judge that WCAG criterion automatically. It is never counted as passing.
- **Accessible name** — the name assistive technology announces for an element, worked out from its text, its label, `aria-label`, `aria-labelledby` or `alt`.
- **Accessibility tree** — the simplified version of the page that browsers give to screen readers and other assistive technology.

## Overview view

The top of the view is the engine's headline:

- **Accessibility** with a score from 0 to 100 and a grade.
- A conformance line, for example "Does not conform to WCAG 2.2 AA." followed by how many criteria need manual review before a conformance claim can be made.
- A bar and key: how many rules **passed**, **failed** and **need review**, out of the rules that ran.

### The engine's grade scale

This scale is stricter than the one used for the overall score:

| Grade | Label | Score |
| --- | --- | --- |
| A+ | Excellent | 95–100 |
| A | Strong | 90–94 |
| B | Good | 80–89 |
| C | Needs work | 70–79 |
| D | Poor | 55–69 |
| F | Critical | 0–54 |

### How the engine scores

Every failing rule adds a penalty. The penalty is larger for higher impact (critical counts ten times as much as minor) and grows with the number of elements affected, but only slowly, so one component repeated forty times does not swamp an otherwise sound page. Rules that need review add a much smaller penalty. The score then falls smoothly as the penalty grows: it never jumps to zero, and a single critical failure is always visible.

Two kinds of rule run and are reported but are left out of the score, because no Level AA claim depends on them: **Level AAA** rules and **best-practice** rules (those with no WCAG criterion).

### The cards

| Card | What it shows |
| --- | --- |
| Severity summary | "N issues on N failing rules", with a button and a count for each impact level |
| **Coverage limits for this run** | Shown when computed styles or element geometry were unavailable; affected rules report needs review |
| **Where the problems are** | One bar per category with its issue count, for example Pointer & touch, Colour & contrast, Landmarks & regions |
| **Quick wins — highest value per unit of effort** | Up to eight low-effort, high-impact fixes, each with its node count and fix |
| **Reading level (WCAG 3.1.5)** | Flesch reading ease, reading grade, sentence length and long sentences, over the page's prose |
| **Full remediation backlog** | Every failing rule as a task, ranked by score gain per unit of effort |

Impact levels with no issues are listed together, for example "Nothing critical, minor." The reading-level card measures paragraphs, list items and quotes only; a page that is mostly interface copy says a reading grade would not mean anything. The backlog says what score fixing everything would reach, and its table has these columns: **Fix** (with category and WCAG criterion), **Impact**, **Nodes**, **Effort**, **Gain** and **Value**.

## Findings: Issues view

Every failing rule and every rule that needs review, as one folding row each. The row shows the rule's title, a badge for its impact (or **needs review**), its level (**WCAG A**, **WCAG AA**, **WCAG AAA** or **best practice**) and the number of elements affected.

### Filter the list

| Filter | Options |
| --- | --- |
| **Impact** | **All**, critical, serious, moderate, minor |
| **Area** | **All**, plus one button per category that has findings |
| **Level** | **WCAG A**, **WCAG AA**, **WCAG AAA**, **Best practice** |
| Search | "Search rules, elements, selectors…" matches rule names, IDs, descriptions and categories |

### Inside a rule

Open a row to see:

- a plain-language description of the rule;
- the rule ID (for example `color-contrast`), the WCAG criterion with its level as a link (for example "1.4.3 Contrast (Minimum) (AA)"), and badges for **Section 508** and **EN 301 549** when the rule maps to them;
- **How to meet this ↗**, a link to the W3C Understanding page for that criterion;
- each affected element, with:
  - its impact and the exact problem, for example "Contrast 1.19:1 is below the required 4.5:1 for normal text (12px). #ffffff on #efebe0.";
  - **Where**, the element's CSS selector;
  - for contrast, a live specimen of the text as it is ("Now") and with the recommended colour ("Recommended"), each with its ratio;
  - for other rules, the element's code as it is now and as recommended;
  - **Fix**, the concrete change;
  - **Copy selector** and **Copy fix** buttons.

A rule with many elements shows the first few and says "Showing N of M affected elements."

## Findings: Fixes view

Every failure the engine could turn into a concrete patch, grouped so that a component repeated many times is one job. Groups are ordered by impact, then by how many places they affect.

The summary lists **Fix groups**, **Auto-fixable** (for example "31 of 40"), **High confidence** and **Need human wording**.

**Ready-to-paste CSS patch** is one stylesheet with every CSS change the engine proposes, each labelled with its rule. Select **Copy the whole stylesheet** to copy it. Review it against your design system before you ship it.

Each fix group shows:

- a one-line summary, such as "#d3af37 on #e5e0d1 is 1.6:1 — below the 4.5:1 minimum. #74601e reaches 4.62:1.";
- badges for impact, confidence, **auto-fixable** and the number of places;
- the rule and criterion;
- the code before and after;
- a note, for example "Keeps the original hue and only moves lightness, so the design stays recognisable.";
- **Where (N)**, a list of every selector with its own **Copy** button;
- **Copy fix** and **Copy CSS**.

### Confidence

| Confidence | Meaning shown |
| --- | --- |
| high | Derived from the element's own markup or computed colours — safe to apply nearly verbatim. |
| medium | Inferred from a filename, icon class or URL — the shape is right, read the wording. |
| review | The defect is certain, the wording is not — a person has to supply the text. |

For example, a missing `alt` inside a link that already has a name is proposed as `alt=""`, and an icon link's name is taken from where it points rather than from its icon. Always read medium and review suggestions before you use them.

## Inspect: Widgets view

Per-element rules ask "is this attribute legal?". This view asks "is this widget wired up correctly?", checked against the W3C ARIA Authoring Practices. It recognises eight widget patterns:

- Tabs
- Disclosure / Accordion
- Combobox
- Dialog (modal)
- Menu / Menubar
- Tree view
- Slider
- Carousel

For each, it checks structure and state: whether a tab actually controls a panel, whether `aria-expanded` matches what is really on screen, whether an auto-rotating carousel can be paused. The summary shows **Widgets detected**, **Fully conformant**, **Not conformant** and **Pattern findings**, and each widget gets a card with its name, pattern, status and any findings.

Closed dialogs and collapsed menus are hidden from the accessibility tree and are deliberately not judged. If no widgets are found, the view says "No composite widgets detected".

## Inspect: Annotations view

A pass over the whole page in the style of a visual annotation tool, grouped and counted. Six tiles sit at the top; select one to isolate that category:

| Tile | Contains |
| --- | --- |
| **Errors** | Accessibility failures that will block users |
| **Contrast errors** | Text that does not meet the contrast minimum |
| **Alerts** | Likely problems that need a human decision |
| **Features** | Accessibility features found on the page |
| **Structural elements** | Headings, landmarks and lists that shape the page |
| **ARIA** | ARIA roles, states and properties in use |

Each group lists its items with a count and code; open **Show elements** to see every selector.

## Inspect: A11y tree view

What assistive technology actually sees. Generic wrappers are transparent and `aria-hidden` subtrees are removed, the way a browser builds the tree. Each node shows its role, its accessible name (or "(no accessible name)") and its selector.

The summary lists **Exposed nodes**, **Landmarks**, **Interactive widgets**, **Widgets/landmarks with no name** and **Subtrees hidden from AT**. Very large pages are cut off, with a note such as "Tree truncated at N nodes."

## Inspect: Screen reader view

The linear announcement stream a screen reader would produce, followed by the lists screen-reader users navigate by.

- **▶ Speak transcript** reads the stream aloud with your browser's built-in speech. **■ Stop** stops it. **Copy transcript** copies the text.
- **Announcement stream** lists each line in order, such as "Site header, banner landmark" or "Company, button, collapsed, has pop up menu". The intro says how many lines announce a bare role with no name.
- The rotor lists: **Headings** (with level), **Landmarks**, **Links** and **Form controls & widgets**. Items with no name are flagged.
- **Heading outline problems** appears when the heading order has gaps.

The speech is your browser's voice, not a real screen reader. Test with a real screen reader before you rely on the result.

## Inspect: Vision view

Every text colour pair on the page, re-rendered through four colour-vision deficiencies, with the WCAG contrast ratio for each and the APCA Lc value for reference.

- A summary line per condition: **Protanopia**, **Deuteranopia**, **Tritanopia** and **Achromatopsia**, each with how many pairs drop below AA and how many lose contrast.
- **Palette under colour-vision deficiency** — a table with the original pair and its contrast (ratio and Lc), the ratio under each condition, and how many times the pair is used.
- **Colours that collide** — palette colours that become indistinguishable from each other under a simulated deficiency. If none do, it says "No colour collisions".

Up to 400 text elements are sampled. See [Colour, contrast and vision](colour-contrast-and-vision.md) for what the ratio and Lc mean.

## Inspect: Focus & targets view

Keyboard focus and touch target sizes.

- The summary lists **Elements in the tab order**, **Positive tabindex**, **Focusable with no name**, **Focusable off-screen**, **Targets below 24×24px** and **Targets below 44×44px**.
- **Tab order** lists every stop in the order the `Tab` key reaches it, with its name, role, size and selector.
- **Touch target sizes** is a table with **Control**, **Role**, **Size**, **2.5.8 (24px)** and **2.5.5 (44px)**. Each size column reads **Pass** or **Below**.

WCAG 2.5.8 (Level AA) asks for targets of at least 24 by 24 CSS pixels, or enough clear space around them; 2.5.5 (Level AAA) asks for 44 by 44.

## Report: Conformance view

The WCAG 2.2 conformance picture, separate from the score.

- **Automated verdict** — the highest level the page meets with no failures (**A**, **AA** or **AAA**), or **Does not conform**, plus how many criteria need manual review. Conformance is all or nothing: one failure at a level denies that level.
- A note that automated testing can only confirm a subset of WCAG, and that criteria shown as untested need human evaluation and are never counted as passing.
- Three level cards, **WCAG 2.2 A**, **WCAG 2.2 AA** and **WCAG 2.2 AAA**, each with passes out of the total and counts of fail, review and untested.
- **Success criteria scorecard** — all 60 criteria the engine knows, each marked ✓ pass, ✗ fail, ? review or – untested.
- **Accessibility Conformance Report (VPAT-style)** — one row per Level A and AA criterion, with **Criterion**, **Level**, **Conformance** and **Remarks**.

| Conformance | Remark shown |
| --- | --- |
| Supports | Automated checks found no failures. |
| Partially Supports | N item(s) require manual verification. |
| Does Not Support | N instance(s) found, with the failing rule |
| Not Evaluated | Not covered by automated testing — manual evaluation required. |

A VPAT (Voluntary Product Accessibility Template) is the format most procurement processes ask for. This table is evidence to support a claim, not the claim itself.

## Report: Export view

"Everything the engine produced, in the formats the rest of your toolchain expects." File names start with `a11y-` followed by a short form of the audited address.

| Export | Contents | File |
| --- | --- | --- |
| **Results JSON (axe format)** | Violations, passes and incomplete results in the shape continuous-integration tools already read | `a11y-<site>.json` |
| **Issues CSV** | One row per affected element: rule, impact, WCAG, selector, problem, fix, suggested patch, confidence | `a11y-<site>-issues.csv` |
| **Remediation brief (Markdown)** | A developer write-up: score, conformance, every violation with selectors and fixes, and the suggested patches | `a11y-<site>-remediation.md` |
| **Contrast fix CSS** | A stylesheet patch that raises every failing text pair to the AA minimum | `a11y-<site>-contrast.css` |
| **Conformance report CSV** | VPAT-shaped Section 508 and EN 301 549 rows with conformance level and remarks. Marked **Specialist**. | `a11y-<site>-conformance-report.csv` |

The conformance report CSV is a paid perk of the Specialist plan. The other four exports are free.

**Run metadata** at the foot of the view lists the **Engine** ("Auric Accessibility Engine"), the **Rule set** ("WCAG 2.2 (A/AA/AAA) · Section 508 · EN 301 549 · ARIA 1.2 · APCA preview"), **Rules available**, **Rules evaluated**, **Run at**, **URL**, and whether **Computed styles** and **Element geometry** were available, with how many **Stylesheets** were read. The card's badge is how long the engine took.

## Below the engine: Advanced Accessibility

Under the engine block, the panel continues with a summary card headed **Advanced Accessibility**: the same score, a **Score Breakdown**, **Conformance Levels** (Level A and Level AA, with how many were not tested), and **Voice Flow** (steps a screen reader visits, landmarks announced, issues in the flow, and **▶ Play** / **■ Stop** buttons that speak the flow).

What comes after depends on your plan:

- **Paid plans** see **Top Accessibility Priorities**, detailed cards comparing raw and rendered accessibility (keyboard, ARIA and contrast findings, and a WCAG mapping), and, for a site scan, **A11y+ · Page-by-Page**.
- **Free and signed-out visitors** see a card headed **The full accessibility report** in their place. It says how many findings are shown, lists what the paid report adds, and offers **See plans** and **Sign in**. It also states that every other tool on the site stays free and that this is the one report that is not.

## A practical order of work

1. In **Overview**, read the grade and the conformance line, then open **Quick wins**.
2. In **Issues**, filter **Impact** to critical, then serious. Fix what blocks a task first: controls with no name, fields with no label, keyboard traps.
3. In **Fixes**, copy the CSS patch for contrast and target-size failures, and review the medium and review suggestions by hand.
4. In **Inspect**, check **Focus & targets** by pressing `Tab` through the real page, and read the **Screen reader** transcript for unnamed controls.
5. Work through **needs review** items yourself: text over images, whether animation can be paused, whether focus order still makes sense visually.
6. Re-run the audit and open **Compare** to confirm what changed.

For every rule the engine checks, see [Accessibility rules](accessibility-rules.md).
