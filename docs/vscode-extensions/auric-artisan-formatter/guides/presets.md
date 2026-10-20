---
title: Auric Artisan Formatter — presets
description: The 13 Auric Artisan Formatter presets, what each is for and which options each sets.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Presets

A *preset* is a named starting point: a coherent set of option values. Choose the one closest to how your team already writes code, then override the few things you disagree with. Anything you set yourself wins over the preset; options you do not mention keep the preset's value. The default preset is `auric`.

## Set a preset

- **Auric Formatter: Switch Formatting Preset** — pick from the list; it saves `auricFormatter.preset` and re-runs the workspace scan.
- In a configuration file: `"preset": "prettier"`. This wins over the VS Code setting.
- In VS Code settings: `"auricFormatter.preset": "prettier"`.
- For one file: a leading comment with `@auric-preset compact`.
- On the command line: `--preset prettier`.
- In Formatter Studio: the **Preset** drop-down, to compare presets on your own file before choosing.

```json
{
  "preset": "prettier",
  "printWidth": 100
}
```

This gives Prettier's exact behaviour at 100 columns instead of 80.

## The 13 presets

| Preset | Builds on | Options it sets | Description |
| --- | --- | --- | --- |
| `auric` | — | 50 | The Auric house style: Prettier's layout plus the Auric enhancements. |
| `prettier` | — | 281 | Byte-compatible with Prettier 3 at its own defaults, with every Auric-only enhancement switched off. |
| `standard` | `prettier` | 14 | StandardJS: no semicolons, single quotes, and a space before every function parameter list. |
| `google` | `prettier` | 18 | The Google style guide: single quotes, tight object braces, and maintained documentation blocks. |
| `airbnb` | `prettier` | 19 | The Airbnb style guide: single quotes, wider lines, grouped imports, and concise arrow bodies. |
| `compact` | `auric` | 35 | Minimise vertical space: wider lines, collapsed collections, and no decorative blank lines. |
| `expanded` | `auric` | 28 | Maximise readability and diff granularity: one item per line almost everywhere. |
| `legacy-tabs` | — | 25 | Tabs, four columns, CRLF line endings and Allman braces, for codebases that were here first. |
| `minimal-diff` | — | 143 | Change as little as possible: preserve the author's layout everywhere it is legal to do so. |
| `aligned` | `auric` | 29 | Turn the column alignment engine on everywhere it is safe, for code that reads like a table. |
| `sorted` | `auric` | 30 | Turn on every ordering rule the safety gate can verify, from import groups to stylesheet declarations. |
| `docs` | `auric` | 19 | Tuned for prose: reflowed paragraphs, generated tables of contents and maintained documentation blocks. |
| `verified` | `auric` | 11 | Run every safety check, re-format to prove idempotency, and fail the run rather than emit unverified output. |

## Which preset

| If you | Choose |
| --- | --- |
| Want the house style this formatter was designed around | `auric` |
| Are moving from Prettier and want identical output on day one | `prettier` |
| Follow StandardJS | `standard` |
| Follow the Google style guides | `google` |
| Follow the Airbnb JavaScript style guide | `airbnb` |
| Want more code on screen | `compact` |
| Want maximum readability in review, one thing per line | `expanded` |
| Have a tab-indented codebase that is staying that way | `legacy-tabs` |
| Are formatting an existing codebase and want the smallest diff | `minimal-diff` |
| Like code aligned into columns | `aligned` |
| Want imports, keys and members sorted | `sorted` |
| Mostly write documentation and comments | `docs` |
| Want every safety check and a hard failure on anything unverified | `verified` |

## What each preset sets

### auric

The Auric house style: Prettier's layout plus the Auric enhancements.

```json
{
  "preset": "auric",
  "printWidth": 100,
  "endOfLine": "lf",
  "insertFinalNewline": true,
  "trimTrailingWhitespace": true,
  "objectWrap": "preserve",
  "preserveObjectShape": true,
  "preserveArrayFormatting": true,
  "singleLineIfStatement": "fit",
  "lastArgumentHugging": true,
  "firstArgumentHugging": true,
  "blankLineAfterImports": "always",
  "blankLineAfterDirectives": true,
  "blankLineBetweenMethods": "always",
  "maxBlankLinesAtStart": 0,
  "maxBlankLinesAtEnd": 0,
  "collapseEmptyBlockBlankLines": true,
  "commentSpacing": "always",
  "blockCommentStarAlign": true,
  "blockCommentStarPad": true,
  "preserveBannerComment": true,
  "jsdocAlign": true,
  "jsdocNormalizeTags": true,
  "jsdocTagOrder": [
    "@module",
    "@description",
    "@template",
    "@typedef",
    "@property",
    "@param",
    "@returns",
    "@yields",
    "@throws",
    "@example",
    "@remarks",
    "@see",
    "@link",
    "@since",
    "@version",
    "@author",
    "@deprecated",
    "@internal"
  ],
  "alignTrailingComments": true,
  "alignmentBreakOnBlankLine": true,
  "alignmentMaxPadding": 24,
  "alignmentUseSpacesOnly": true,
  "blankLineBetweenRules": 1,
  "nestedRuleBlankLine": true,
  "atRuleBlankLine": true,
  "propertyCase": "lower",
  "valueKeywordCase": "lower",
  "unitCase": "lower",
  "atRuleCase": "lower",
  "keyframeSelectorCase": "lower",
  "hexCase": "lower",
  "mdOrderedNumbering": "one",
  "mdEmphasisMarker": "asterisk",
  "mdStrongMarker": "asterisk",
  "mdTableAlign": true,
  "mdFormatCodeBlocks": true,
  "mdFrontmatterFormat": "format",
  "jsonPackageJsonOrder": true,
  "yamlCommentIndent": "align",
  "safetyTokenCheck": true,
  "safetyReparse": true,
  "safetyCommentPreservation": true,
  "safetyStringLiterals": true,
  "safetyNumericLiterals": true,
  "safetyOnFailure": "preserve"
}
```

### prettier

Byte-compatible with Prettier 3 at its own defaults, with every Auric-only enhancement switched off.

It sets 281 options, too many to list usefully here. Choose it in Formatter Studio's **Preset** drop-down and use the **Diff** view to see what it changes in your own files.

### standard

StandardJS: no semicolons, single quotes, and a space before every function parameter list. It builds on `prettier`.

```json
{
  "preset": "standard",
  "semi": false,
  "singleQuote": true,
  "jsxSingleQuote": true,
  "quoteProps": "as-needed",
  "trailingComma": "none",
  "arrowParens": "avoid",
  "spaceBeforeFunctionParen": "always",
  "spaceBeforeBlocks": true,
  "spaceAfterKeyword": true,
  "semiColonBeforeIIFE": true,
  "curlyBraces": "multi-line",
  "objectWrap": "preserve",
  "printWidth": 80,
  "commentSpacing": "always"
}
```

### google

The Google style guide: single quotes, tight object braces, and maintained documentation blocks. It builds on `prettier`.

```json
{
  "preset": "google",
  "printWidth": 80,
  "tabWidth": 2,
  "singleQuote": true,
  "quoteProps": "consistent",
  "trailingComma": "all",
  "bracketSpacing": false,
  "arrowParens": "always",
  "semi": true,
  "curlyBraces": "all",
  "blankLineBetweenMethods": "always",
  "jsdocWrap": "always",
  "jsdocNormalizeTags": true,
  "jsdocTagOrder": [
    "@module",
    "@description",
    "@template",
    "@typedef",
    "@property",
    "@param",
    "@returns",
    "@yields",
    "@throws",
    "@example",
    "@remarks",
    "@see",
    "@link",
    "@since",
    "@version",
    "@author",
    "@deprecated",
    "@internal"
  ],
  "commentSpacing": "always",
  "htmlQuoteAttributes": "double",
  "propertyCase": "lower",
  "unitCase": "lower",
  "hexCase": "lower"
}
```

### airbnb

The Airbnb style guide: single quotes, wider lines, grouped imports, and concise arrow bodies. It builds on `prettier`.

```json
{
  "preset": "airbnb",
  "printWidth": 100,
  "singleQuote": true,
  "semi": true,
  "trailingComma": "all",
  "arrowParens": "always",
  "arrowBodyStyle": "as-needed",
  "bracketSpacing": true,
  "arrayBracketSpacing": false,
  "spaceBeforeBlocks": true,
  "spaceInParens": false,
  "objectWrap": "preserve",
  "maxBlankLines": 1,
  "blankLineAfterImports": "always",
  "sortImports": true,
  "importOrder": [
    "<BUILTIN_MODULES>",
    "<THIRD_PARTY_MODULES>",
    "^@/",
    "^~/",
    "^[.][.]/",
    "^[.]/"
  ],
  "importOrderSeparation": true,
  "importOrderSortSpecifiers": true,
  "importOrderCaseInsensitive": true,
  "commentSpacing": "always"
}
```

### compact

Minimise vertical space: wider lines, collapsed collections, and no decorative blank lines. It builds on `auric`.

```json
{
  "preset": "compact",
  "printWidth": 120,
  "objectWrap": "collapse",
  "preserveObjectShape": false,
  "preserveArrayFormatting": false,
  "shortArrayThreshold": 8,
  "jsonSingleLineArrays": true,
  "arrowBodyStyle": "as-needed",
  "singleLineArrowBody": true,
  "singleLineIfStatement": "fit",
  "curlyBraces": "multi-line",
  "emptyBlockStyle": "collapse",
  "preserveEnumOneLine": true,
  "maxBlankLines": 1,
  "maxBlankLinesInsideBlocks": 0,
  "blankLineBetweenMethods": "never",
  "blankLineAfterImports": "preserve",
  "blankLineAfterDirectives": false,
  "padClassBody": false,
  "padFunctionBody": false,
  "padBlocks": false,
  "blankLineBetweenRules": 0,
  "nestedRuleBlankLine": false,
  "atRuleBlankLine": false,
  "singleLineRuleThreshold": 1,
  "selectorSeparator": "space",
  "mediaQueryFormat": "compact",
  "scssMapFormat": "compact",
  "htmlBlankLineBetweenBlocks": 0,
  "htmlAttributeWrap": "auto",
  "singleAttributePerLine": false,
  "mdListItemBlankLine": "tight",
  "mdTableCompact": true,
  "graphqlSeparateOperations": 0,
  "tomlTableBlankLine": 0,
  "iniSectionBlankLine": 0
}
```

### expanded

Maximise readability and diff granularity: one item per line almost everywhere. It builds on `auric`.

```json
{
  "preset": "expanded",
  "printWidth": 80,
  "objectPropertyNewline": "always",
  "objectDestructuringNewline": "always",
  "functionParameterNewline": "always",
  "typeParameterNewline": "always",
  "arrayElementsPerLine": 1,
  "jsonExpandArrayThreshold": 2,
  "jsonSingleLineArrays": false,
  "unionFormat": "expanded",
  "intersectionFormat": "expanded",
  "mappedTypeFormat": "expanded",
  "emptyBlockStyle": "expand",
  "switchCaseBlankLine": "always",
  "blankLineBetweenMethods": "always",
  "blankLineBeforeReturn": "always",
  "blankLineBetweenTopLevel": "always",
  "singleAttributePerLine": true,
  "htmlAttributeWrap": "always",
  "jsxSingleAttributeSameLine": false,
  "selectorSeparator": "newline",
  "blankLineBetweenRules": 1,
  "nestedRuleBlankLine": true,
  "atRuleBlankLine": true,
  "mediaQueryFormat": "expanded",
  "scssMapFormat": "expanded",
  "mdListItemBlankLine": "loose",
  "graphqlArgumentWrap": "always",
  "tomlArrayWrap": "always"
}
```

### legacy-tabs

Tabs, four columns, CRLF line endings and Allman braces, for codebases that were here first.

```json
{
  "preset": "legacy-tabs",
  "useTabs": true,
  "tabWidth": 4,
  "printWidth": 120,
  "endOfLine": "crlf",
  "insertFinalNewline": true,
  "trimTrailingWhitespace": true,
  "alignmentUseSpacesOnly": false,
  "semi": true,
  "singleQuote": false,
  "trailingComma": "none",
  "bracketSpacing": true,
  "curlyBraces": "all",
  "elsePosition": "new-line",
  "catchPosition": "new-line",
  "doWhilePosition": "new-line",
  "switchCaseIndent": true,
  "universalBraceStyle": "next-line",
  "universalIndentSize": 4,
  "universalContinuationIndent": 4,
  "universalCaseIndent": true,
  "cPointerAlignment": "left",
  "javaAnnotationPosition": "above",
  "maxBlankLines": 2,
  "commentSpacing": "always",
  "blockCommentStarAlign": true
}
```

### minimal-diff

Change as little as possible: preserve the author's layout everywhere it is legal to do so.

It sets 143 options, too many to list usefully here. Choose it in Formatter Studio's **Preset** drop-down and use the **Diff** view to see what it changes in your own files.

### aligned

Turn the column alignment engine on everywhere it is safe, for code that reads like a table. It builds on `auric`.

```json
{
  "preset": "aligned",
  "alignObjectValues": true,
  "alignAssignments": "consecutive",
  "alignConsecutiveDeclarations": true,
  "alignTrailingComments": true,
  "alignTernaryBranches": true,
  "alignEnumValues": true,
  "alignTypeMembers": true,
  "alignImportSpecifiers": true,
  "alignmentMaxPadding": 40,
  "alignmentMinGroupSize": 2,
  "alignmentBreakOnBlankLine": true,
  "alignmentUseSpacesOnly": true,
  "propertyValueAlign": true,
  "vendorPrefixAlign": true,
  "gridTemplateAlign": true,
  "yamlAlignValues": true,
  "tomlAlignValues": true,
  "iniAlignValues": true,
  "graphqlFieldAlign": true,
  "jsdocAlign": true,
  "universalAlignAssignments": true,
  "universalAlignTrailingComments": true,
  "universalAlignConsecutive": true,
  "goAlignStructTags": true,
  "goAlignComments": true,
  "rustAlignMatchArms": true,
  "rustAlignStructFields": true,
  "sqlAlignSelectColumns": true,
  "pythonAlignDictValues": true
}
```

### sorted

Turn on every ordering rule the safety gate can verify, from import groups to stylesheet declarations. It builds on `auric`.

```json
{
  "preset": "sorted",
  "sortImports": true,
  "importOrder": [
    "<BUILTIN_MODULES>",
    "<THIRD_PARTY_MODULES>",
    "^@/",
    "^~/",
    "^[.][.]/",
    "^[.]/"
  ],
  "importOrderSeparation": true,
  "importOrderSortSpecifiers": true,
  "importOrderCaseInsensitive": true,
  "importOrderGroupNamespaceSpecifiers": true,
  "importOrderSideEffectsFirst": true,
  "importOrderTypeImports": "last",
  "exportOrder": "alphabetical",
  "sortObjectKeys": true,
  "sortUnionMembers": true,
  "sortInterfaceMembers": true,
  "sortClassMembers": true,
  "classMemberOrder": [
    "static-field",
    "field",
    "constructor",
    "static-method",
    "method",
    "getter",
    "setter"
  ],
  "sortCaseSensitivity": "insensitive",
  "sortNaturalNumeric": true,
  "sortPreserveComments": true,
  "sortRespectBlankLineGroups": true,
  "jsxSortProps": true,
  "htmlSortAttributes": true,
  "xmlSortAttributes": true,
  "declarationOrder": "grouped",
  "yamlKeySort": true,
  "jsonSortKeys": true,
  "jsonPackageJsonOrder": true,
  "tomlSortKeys": true,
  "graphqlSortDefinitions": true,
  "graphqlSortFields": true,
  "jsdocTagOrder": [
    "@module",
    "@description",
    "@template",
    "@typedef",
    "@property",
    "@param",
    "@returns",
    "@yields",
    "@throws",
    "@example",
    "@remarks",
    "@see",
    "@link",
    "@since",
    "@version",
    "@author",
    "@deprecated",
    "@internal"
  ],
  "jsdocNormalizeTags": true
}
```

### docs

Tuned for prose: reflowed paragraphs, generated tables of contents and maintained documentation blocks. It builds on `auric`.

```json
{
  "preset": "docs",
  "printWidth": 80,
  "proseWrap": "always",
  "commentWrap": "always",
  "commentWrapWidth": 80,
  "commentSpacing": "always",
  "jsdocWrap": "always",
  "jsdocAlign": true,
  "jsdocNormalizeTags": true,
  "jsdocTagOrder": [
    "@module",
    "@description",
    "@template",
    "@typedef",
    "@property",
    "@param",
    "@returns",
    "@yields",
    "@throws",
    "@example",
    "@remarks",
    "@see",
    "@link",
    "@since",
    "@version",
    "@author",
    "@deprecated",
    "@internal"
  ],
  "jsdocBlankLineAfterDescription": true,
  "mdTocGenerate": true,
  "mdTocMaxDepth": 3,
  "mdHeadingBlankLines": 1,
  "mdTableAlign": true,
  "mdLinkStyle": "inline",
  "mdFormatCodeBlocks": true,
  "mdEscapeSpecial": true,
  "mdFrontmatterFormat": "format",
  "experimentalCommentReflow": true
}
```

### verified

Run every safety check, re-format to prove idempotency, and fail the run rather than emit unverified output. It builds on `auric`.

```json
{
  "preset": "verified",
  "safetyTokenCheck": true,
  "safetyTokenCheckComments": true,
  "safetyIdempotency": true,
  "safetyIdempotencyPasses": 2,
  "safetyReparse": true,
  "safetyCommentPreservation": true,
  "safetyStringLiterals": true,
  "safetyNumericLiterals": true,
  "safetyOnFailure": "throw",
  "maxFileSizeKb": 8192,
  "parseTimeoutMs": 15000
}
```
