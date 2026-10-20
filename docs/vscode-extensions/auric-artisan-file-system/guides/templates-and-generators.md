---
title: Auric Artisan File System — templates, presets and generators
description: Create files from templates, use the ten framework presets, and write your own templates and generators with variables, filters and conditions.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Templates and generators

A *template* is a file pattern: a file name and a body with placeholders that are filled in when you create a file. A *framework preset* is a ready-made set of templates and file relationships for one ecosystem. A *generator* is a template that can also create companion files in the same step.

## Create from a template

1. Run **Auric Files: New File from Template…** (**Create** group, or `Ctrl` + `Alt` + `A`, then `T` with the shortcut deck).
2. **Choose a template.** The list includes the active preset's built-in templates, your generators and any templates in your template folders.
3. **Choose the destination folder.**
4. Answer the template's questions, such as the name.
5. The file (and any companions the template defines) is created, and the first file opens with the cursor where the template placed it.

## Create from a framework preset

1. Run **Auric Files: New from Framework Preset…** (`Ctrl` + `Alt` + `A`, then `P` with the deck).
2. **Choose a framework preset or custom generator.**
3. **Choose what to create** from that preset's templates.
4. **Choose the destination folder** and answer its questions.

### The ten presets

| Preset | What it covers |
| --- | --- |
| **React** | Components, hooks, contexts, tests, styles and stories |
| **Vue** | Single file components, composables, Pinia stores and specs |
| **Angular** | Standalone components with their template, style and spec |
| **Svelte** | Runes components, stores, tests and stories |
| **Node.js** | CommonJS and ES modules, CLI entry points, tests and declarations |
| **Python** | Dataclass modules, pytest suites, package markers and CLI entry points |
| **Java** | Classes, records, interfaces and JUnit 5 tests with derived packages |
| **Go** | Package files, table tests, command entry points and doc comments |
| **Rust** | Modules with inline test blocks, crate roots and error types |
| **Generic** | Plain modules, documents and data files for any workspace |

The templates in each preset:

- **React:** React Component, React Component (JavaScript), React Hook, React Context Provider, React Component Test, Component Stylesheet, Storybook Story, Barrel Index, Component Types.
- **Vue:** Vue Single File Component, Vue Composable, Pinia Store, Vue Component Test, Component Stylesheet, Storybook Story, Barrel Index, Component Types.
- **Angular:** Angular Component, Component Template, Component Stylesheet, Component Spec, Angular Service, Barrel Index, Model.
- **Svelte:** Svelte Component, Svelte Store, Svelte Component Test, Component Stylesheet, Storybook Story, Barrel Index, Component Types.
- **Node.js:** CommonJS Module, ES Module, TypeScript Module, Module Test, CLI Entry Point, Barrel Index, Type Declarations.
- **Python:** Python Module, Pytest Test, Package Init, Python CLI, Python Types.
- **Java:** Java Class, Java Record, Java Interface, JUnit Test, Package Info.
- **Go:** Go Source File, Go Test, Go Main, Package Documentation, Go Interfaces.
- **Rust:** Rust Module, Rust Integration Test, Module Index, Crate Root, Error Type.
- **Generic:** JavaScript Module, Module Test, Stylesheet, Barrel Index, Type Declarations, Markdown Document, Documentation Page, JSON File, YAML File, Text File.

### Choosing the preset

`auricFiles.create.preset` is `auto` by default: Auric Files reads the workspace's dependencies and configuration files and picks the best match. Set it to `react`, `vue`, `angular`, `svelte`, `node`, `python`, `java`, `go`, `rust` or `generic` to fix it.

Three settings shape what the presets generate:

| Setting | Default | Values |
| --- | --- | --- |
| `auricFiles.create.componentStyleLanguage` | `css` | `css`, `scss`, `less`, `styled`, `module-css`, `module-scss` |
| `auricFiles.create.testFramework` | `auto` | `auto`, `jest`, `vitest`, `mocha`, `node`, `pytest`, `junit`, `gotest`, `cargo` |
| `auricFiles.create.indent` | `space2` | `space2`, `space4`, `tab` |

Java and Kotlin templates derive the package from the folder, recognising source roots such as `src/main/java`.

## Write your own templates

### Where templates live

| Scope | Where | Setting |
| --- | --- | --- |
| Workspace | `.auric/templates` and `.vscode/templates` in each workspace folder | `auricFiles.templates.directories` |
| Global | Absolute folders you choose, shared across all workspaces | `auricFiles.templates.global` |
| Generator | Defined in settings | `auricFiles.create.generatorProfiles` |
| Built-in | The active preset | `auricFiles.create.preset` |

Every file in a template folder is read as one template. When two templates share an id, a workspace template replaces a global one, which replaces a generator, which replaces a built-in template. So you can override a built-in template by giving yours the same id.

Template folders are workspace configuration, so they only apply in a trusted workspace.

### The file format

A template file has optional *front matter* between two `---` lines, followed by the body:

```text
---
id: react-card
label: Card component
description: A card with an optional stylesheet
filename: "{{name|pascal}}/{{name|pascal}}.tsx"
variables: [{"name": "withStyles", "type": "boolean", "default": true, "label": "Include styles"}]
companions: [{"when": "{{withStyles}}", "filename": "{{name|pascal}}/{{name|pascal}}.css", "body": ".{{name|kebab}} {}\n"}]
---
export function {{name|pascal}}() {
  return <div className="{{name|kebab}}">$CURSOR</div>;
}
```

| Key | Required | Meaning |
| --- | --- | --- |
| `id` | Defaults to the file name | Letters and numbers, with `.`, `_` or `-` between them |
| `label` | Defaults from the id | Name shown in the template list |
| `description` | No | Extra text in the list |
| `filename` | Defaults to `{{name}}` | Output path, with placeholders; may include folders |
| `variables` | No | Questions to ask, as inline JSON (see below) |
| `companions` | No | Extra files, as inline JSON: `when`, `filename`, `body` |
| `match` | No | Globs that narrow where the template is offered |
| `preset` | No | The ecosystem the template belongs to |

Front matter lines are `key: value`. A key with a list below it uses `- item` lines. Anything nested (`variables`, `companions`) is written as inline JSON on one line. The whole front matter can also be a single JSON object.

### Variables you define

Each variable has a `name` and optionally:

| Field | Meaning |
| --- | --- |
| `label` | The question shown |
| `description` | Extra help |
| `type` | `string` (default), `boolean`, `number` or `choice` |
| `choices` | The options for a `choice` variable |
| `default` | The pre-filled answer |
| `required` | `true` to insist on an answer |

`auricFiles.templates.variables` supplies values to every template, such as an author or a licence header. An answer you type wins over it.

### Built-in variables

| Variable | Value for `src/components/Button.test.tsx` |
| --- | --- |
| `name`, `basename` | `Button` (compound extensions such as `.test.tsx` removed) |
| `fileName` | `Button.test.tsx` |
| `stem` | the file name without its last extension |
| `ext` | the extension |
| `dir` | `src/components` |
| `parentDir` | `components` |
| `relativePath` | `src/components/Button.test.tsx` |
| `absolutePath` | the full path on disk |
| `workspace` | the workspace name |
| `date`, `time`, `year`, `isoDate` | the current local date, time, year and ISO timestamp |
| `uuid` | a new random identifier |
| `className`, `pascalName` | `Button` |
| `camelName`, `kebabName`, `snakeName`, `upperName` | `button`, `button`, `button`, `BUTTON` |
| `indent` | the indentation from `auricFiles.create.indent` |
| `javaPackage`, `pythonPackage` | the package derived from the folder |
| `goPackage` | the package name from the parent folder, or `main` |

### Template language

| Syntax | Meaning |
| --- | --- |
| `{{name}}` | Insert a value; an unknown name inserts nothing |
| `{{#if withStyles}} … {{else}} … {{/if}}` | Include text when a value is true (non-empty, not `false`, not `0`) |
| `{{#unless flag}} … {{/unless}}` | Include text when a value is false |
| `{{#each items}} … {{/each}}` | Repeat for each item; inside, use `{{this}}`, `{{@index}}` and `{{@key}}` |
| `{{> other-template-id}}` | Insert another template (a partial), up to 8 levels deep |
| `$CURSOR` | Where the cursor goes when the file opens |

To apply a *filter*, write a vertical bar and the filter name after the value inside the braces: `{{name|pascal}}` turns `my button` into `MyButton`. Filters can be chained, as in `{{name|kebab|upper}}`.

`{{#each}}` also accepts a comma-separated string.

Filters: `upper`, `lower`, `kebab`, `camel`, `pascal`, `snake`, `title`, `trim`, `basename`, `dirname`, `stem`, `ext`, `plural`, `singular`, `date`, `isoDate`, `year`. An unknown filter does nothing, and template validation reports it.

The language is deliberately small: there is no code execution. A broken template renders nothing rather than running anything.

## Generator profiles

A generator is a template defined in settings, shown beside the framework presets. Add them to `auricFiles.create.generatorProfiles`:

```json
{
  "auricFiles.create.generatorProfiles": [
    {
      "id": "repository",
      "label": "Repository class",
      "description": "Data access class with its test",
      "match": ["src/**"],
      "filename": "src/data/{{name|pascal}}Repository.ts",
      "body": "export class {{name|pascal}}Repository {\n  $CURSOR\n}\n",
      "variables": [{ "name": "name", "label": "Entity name", "required": true }],
      "companions": [
        {
          "filename": "src/data/{{name|pascal}}Repository.test.ts",
          "body": "import { {{name|pascal}}Repository } from './{{name|pascal}}Repository';\n"
        }
      ]
    }
  ]
}
```

Required fields are `id`, `label`, `filename` and `body`. A companion is created only when its `when` expression renders to something true; leave `when` out to always create it.

When a template runs, the files it describes appear in the Explorer, and the first opens with the cursor at `$CURSOR`.
