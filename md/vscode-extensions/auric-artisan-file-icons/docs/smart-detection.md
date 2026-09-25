---
title: Auric Artisan File Icons — Smart detection
description: Content-aware badges, colours and explanations in the Explorer, the built-in rules, custom rules and workspace scans.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Smart detection

Smart detection looks at a folder's direct contents, its package dependencies, or the start of a small text file, and adds an Explorer **decoration**: a badge of up to two characters, a category colour and a hover explanation. For example, a folder containing `Cargo.toml` gets the badge **RS** and the explanation "Rust project".

Decorations sit on top of the base icon; they do not replace its SVG. They run only while one of the Auric Artisan File Icons themes is active.

## Turn it on or off

- On the **Workspace** tab, tick or clear **Enable smart detection**.
- Run **Auric Artisan File Icons: Toggle Smart Icon Detection**. VS Code confirms "Smart icon detection enabled" or "disabled".
- Set `auricFileIcons.smart.enabled`.

Folder detection and file detection can be switched separately with `auricFileIcons.smart.folders` and `auricFileIcons.smart.files`.

## Choose how matches appear

Run **Auric Artisan File Icons: Configure Smart Icon Detection** (or **Configure** on the Workspace tab). The menu offers:

| Item | Effect |
| --- | --- |
| **Enable / Disable smart detection** | Toggles detection for this workspace. |
| **Badge and color** | Badge plus category colour (default). |
| **Badge only** | Badge without colour. |
| **Color only** | Category colour without a badge. |
| **Tooltip only** | Only the hover explanation. |
| **Refresh smart matches** | Clears cached results. |
| **Edit custom rules** | Opens `settings.json` at `auricFileIcons.smart.rules`. |

Choices made in this menu are saved in the workspace settings.

## Explain, refresh and apply

| Action | How | Result |
| --- | --- | --- |
| Explain a match | Right-click › **Auric File Icons** › **Explain Smart Icon Match**, or the command | A message naming the rule that matched. |
| Refresh | **Refresh Smart Icon Matches**, or **Refresh** on the Workspace tab | Clears the cache: "Smart icon matches refreshed." |
| Apply a detected icon | Right-click a folder › **Apply Detected Folder Icon** | Saves the matching folder icon as an association. |

## Built-in folder rules

Checked highest priority first. A folder matches when it contains one of the listed names, or when its `package.json` lists one of the dependencies.

| Badge | Explanation | Recognised by |
| --- | --- | --- |
| AL | Auric Live project | `.auric-live`, `auric.live.json`, `.auricignore-live` |
| AS | Auric Studio project | `.auric-artisan` |
| AF | Auric Formatter project | `.auricformatrc*`, `.auricformatignore`, `auric.format.json` |
| AU | Auric workspace | `.auric`, `.auricignore` |
| NG | Angular project | `angular.json` or `@angular/core` |
| NX | Next.js project | `next.config.*` or `next` |
| NU | Nuxt project | `nuxt.config.*` or `nuxt` |
| SV | Svelte project | `svelte.config.*`, `svelte` or `@sveltejs/kit` |
| VU | Vue project | `vue` |
| RE | React project | `react` or `react-dom` |
| NS | NestJS project | `@nestjs/core` |
| VT | Vite project | `vite.config.*` or `vite` |
| RM | Remix project | `remix.config.*` or `@remix-run/*` |
| QW | Qwik project | `qwik.config.*` or `@builder.io/qwik` |
| SO | SolidJS project | `solid-js` or `@solidjs/start` |
| DN | Deno project | `deno.json`, `deno.jsonc`, `deno.lock` |
| BN | Bun project | `bun.lock`, `bun.lockb`, `bunfig.toml` |
| NT | .NET project | `*.sln`, `*.csproj`, `*.fsproj`, `*.vbproj` |
| FL | Flutter or Dart project | `pubspec.yaml`, `pubspec.yml` |
| RS | Rust project | `Cargo.toml` |
| GO | Go project | `go.mod` |
| PY | Python project | `pyproject.toml`, `requirements*.txt`, `setup.py`, `Pipfile` |
| JV | Java or JVM project | `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle`, `settings.gradle.kts` |
| BZ | Bazel workspace | `WORKSPACE`, `WORKSPACE.bazel`, `MODULE.bazel`, `BUILD.bazel` |
| PM | Pulumi project | `Pulumi.yaml` |
| SS | Serverless project | `serverless.yml`, `serverless.yaml` |
| DC | Dev Container workspace | `.devcontainer`, `devcontainer.json`, `.devcontainer.json` |
| PR | Prisma data project | `prisma`, or `prisma` or `@prisma/client` |
| DZ | Drizzle data project | `drizzle`, or `drizzle-orm` or `drizzle-kit` |
| SB | Supabase project | `supabase` or `@supabase/*` |
| TW | Tailwind CSS project | `tailwind.config.*` or `tailwindcss` |
| MR | Monorepo workspace | `pnpm-workspace.yaml`, `lerna.json`, `nx.json`, `turbo.json` |
| TS | TypeScript project | `tsconfig.json` |
| ND | JavaScript or Node project | `package.json` |
| HM | Helm chart | `Chart.yaml` |
| TF | Terraform project | `*.tf` |
| DK | Container project | `Dockerfile`, `docker-compose.*`, `compose.yml`, `compose.yaml` |
| T | Test workspace | `jest.config.*`, `vitest.config.*`, `playwright.config.*`, `pytest.ini` |
| DC | Documentation workspace | `README*` together with `mkdocs.yml`, `docusaurus.config.*` or `docs` |
| DB | Database workspace | `prisma`, `migrations`, `schema.sql` |

## Built-in file rules

| Badge | Explanation | Recognised by |
| --- | --- | --- |
| ! | Sensitive key material | A private key header in the content |
| G | Generated file | `@generated`, `DO NOT EDIT` or `generated by` in the content |
| NG | Angular component | `@Component(` or `@NgModule(` |
| VU | Vue component | A `.vue` file with `<template` or `defineComponent(` |
| RE | React module | An import from `react`, `React.createElement(` or `use client` |
| T | Test source | `*.test.*`, `*.spec.*`, `test_*`, `*_test.*` |
| SC | Schema-bearing document | A `"$schema"` key |
| OA | OpenAPI document | `openapi` or `swagger` keys |
| MG | Database migration | A `.sql` file with `CREATE TABLE`, `ALTER TABLE` or `CREATE INDEX` |
| IN | Localization resource | `"translations"`, `"locale"`, `msgid` or `msgstr` |
| #! | Executable script | Content starting with `#!` |

## Category colours

Each rule has a category colour. You can change them in `workbench.colorCustomizations`.

| Colour ID | Category | Dark default | Light default |
| --- | --- | --- | --- |
| `auricFileIcons.smart.auric` | Auric projects | `#F0C15A` | `#946414` |
| `auricFileIcons.smart.framework` | Frameworks | `#70C7FF` | `#176E9F` |
| `auricFileIcons.smart.language` | Languages | `#B097FF` | `#6245B2` |
| `auricFileIcons.smart.infrastructure` | Infrastructure | `#63D8C4` | `#217B70` |
| `auricFileIcons.smart.test` | Tests | `#7DD58A` | `#2F7838` |
| `auricFileIcons.smart.docs` | Documentation | `#E28EE8` | `#873C95` |
| `auricFileIcons.smart.data` | Data | `#F2A665` | `#99521C` |
| `auricFileIcons.smart.generated` | Generated files | `#A9B4C2` | `#586473` |
| `auricFileIcons.smart.security` | Security | `#F2768D` | `#A3243E` |
| `auricFileIcons.smart.custom` | Custom rules (default) | `#F0C15A` | `#946414` |

High-contrast themes use lighter variants of each.

## Custom rules

Custom rules run before the built-in ones, highest priority first. Add them to `auricFileIcons.smart.rules`:

```json
{
  "auricFileIcons.smart.rules": [
    {
      "id": "design-system",
      "label": "Design system package",
      "target": "folder",
      "badge": "DS",
      "color": "custom",
      "priority": 950,
      "whenAll": ["package.json", "tokens"],
      "dependenciesAny": ["storybook", "@storybook/*"]
    }
  ]
}
```

| Field | Meaning |
| --- | --- |
| `badge` | Required. At most two characters (a VS Code limit). |
| `id`, `label` | Identify the rule; the label is shown in explanations. |
| `target` | `folder` (default) or `file`. |
| `color` | `auric`, `framework`, `language`, `infrastructure`, `test`, `docs`, `data`, `generated`, `security` or `custom`. |
| `priority` | Higher runs first. |
| `whenAll`, `whenAny` | Child names that must all, or any, be present (folders). |
| `dependenciesAny` | Package dependencies, any of which match (folders). |
| `fileNames`, `contentAny`, `contentAll`, `contentPrefix` | Name patterns and content checks (files). |

Patterns support `*` and `?` only, never regular expressions.

## Scan the workspace for folder icons

1. Run **Auric Artisan File Icons: Scan Workspace for Folder Icons**, or **Scan folders…** on the Workspace tab.
2. A progress notification ("Scanning project folders for Facet icons") inspects first-level folders, up to `auricFileIcons.smart.scanLimit` (80 by default). You can cancel it.
3. Detected folders get icon associations in the workspace settings. Existing manual associations are preserved. The result reads, for example, "Applied 4 detected folder icon(s); preserved 2 existing assignment(s)."

## Bounds and exclusions

| Setting | Default | Range | Meaning |
| --- | --- | --- | --- |
| `auricFileIcons.smart.maxFileSize` | 65536 bytes (64 KiB) | 1,024 to 262,144 | Largest text file inspected. |
| `auricFileIcons.smart.maxFolderEntries` | 250 | 25 to 2,000 | Direct child names considered per folder. |
| `auricFileIcons.smart.cacheSeconds` | 15 | 1 to 3,600 | How long a match is cached. |
| `auricFileIcons.smart.scanLimit` | 80 | 1 to 250 | Folders inspected by the workspace scan. |
| `auricFileIcons.smart.exclusions` | See below | List | Folder names or simple wildcards never inspected. |
| `auricFileIcons.smart.propagate` | false | On or off | Show child decorations on parent folders. |
| `auricFileIcons.smart.watch` | true | On or off | Watch project marker files and refresh matching folders. |

Default exclusions: `.git`, `node_modules`, `vendor`, `dist`, `build`, `out`, `coverage`, `.next`, `.nuxt`, `.cache`, `.turbo`, `target`, `__pycache__`. Binary, oversized and unavailable files are skipped.

Inspection uses VS Code's file system access, so it works in local, remote and virtual workspaces where the provider allows reading. It never runs project code.

## Result

Recognised folders and files carry badges, colours and explanations, and you can make any detected folder type a permanent icon.
