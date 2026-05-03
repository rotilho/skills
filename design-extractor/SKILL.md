---
name: "design-extractor"
description: "Create, audit, or refresh a DESIGN.md design-system file from visual and product references such as screenshots, Figma exports, existing CSS, Tailwind configs, design tokens, brand notes, sample pages, or app UI. Use when the task asks for DESIGN.md, design extraction, design-system inference, or converting scattered design evidence into structured tokens and guidance. Count the source references used for each section or major token group, and surface conflicts, inconsistencies, and inferred decisions instead of hiding uncertainty."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "design"
  style: "concise"
---

# Design Extractor

Use this skill to turn existing design evidence into a compliant `DESIGN.md`.

## Reference files

- Read `references/docs/spec.md` when exact `DESIGN.md` schema, section order, token rules, or consumer behavior matters.
- Read `references/examples/*/DESIGN.md` when you need examples of the expected tone, token shape, and section density.
- Do not load the bundled CLI source unless debugging validation behavior or parser/linter details.

## When to use

Trigger for work like:
- create `DESIGN.md` from screenshots, Figma frames, CSS, Tailwind config, tokens, or brand notes
- extract a design system from an existing app or website
- audit whether a `DESIGN.md` matches the provided references
- merge multiple design references into one coherent design-system source of truth
- identify conflicts between visual references, implementation tokens, and written design guidance

Do not use this skill for ordinary frontend implementation when no durable `DESIGN.md` or design-system extraction is requested.

## Core promise

Produce a `DESIGN.md` that:
- follows the bundled `DESIGN.md` spec
- separates normative tokens from explanatory prose
- is grounded in inspected references
- counts source support for the extracted design choices
- names conflicts, inconsistencies, weak evidence, and inferred decisions
- remains useful to future coding agents building UI from the design system

## Hard constraints

- Treat YAML frontmatter tokens as normative values; treat markdown prose as application guidance.
- Use only one `##` heading per section name; duplicate section headings are invalid.
- Keep known sections in this order when present: `Overview` or `Brand & Style`, `Colors`, `Typography`, `Layout` or `Layout & Spacing`, `Elevation & Depth` or `Elevation`, `Shapes`, `Components`, `Do's and Don'ts`.
- Use frontmatter only for the spec-supported token groups: `version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, and `components`.
- Use valid hex colors in the `colors` map. Put alpha, gradients, blur, shadows, and CSS literals in component tokens or prose unless the spec supports them directly.
- Use spec component property names where possible: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, and `width`. Map platform names such as `radius`, `padding-x`, `background`, or `text` into those names instead of copying them directly unless preserving an unknown property is intentional.
- Prefer token references such as `{colors.primary}` and `{typography.body-md}` inside `components` when a value maps to an existing token.
- Do not silently average conflicting values. Choose the strongest supported value, then record the conflict.
- Do not invent source support. Mark low-confidence choices as inferred.

## Workflow

### Step 1 - Inventory references

Assign stable source IDs before drafting:

```md
R1: <path, URL, screenshot, Figma frame, CSS file, token file, or note> - <source type>
R2: ...
```

Use these source types:
- visual reference
- implementation file
- token file
- brand or product note
- generated or prior design artifact
- user instruction

Count distinct references, not repeated observations inside one source. Multiple screenshots of materially different screens or states may count separately. A source supports a token or section only when it directly states, implements, or clearly displays the relevant choice.

Do not count this skill's own `references/docs/spec.md` or example `DESIGN.md` files as design evidence for the target product. You may list them as format references if useful, but exclude them from inspected/used design-reference counts.

When the target repo already contains generated extraction artifacts such as `DESIGN.md`, `evidence-matrix.md`, `final-report.md`, or prior workbench outputs, classify them as generated/prior design artifacts before using them. For isolated reruns or tests against raw product sources, exclude those artifacts from design evidence by default and mention that exclusion. Use an existing target `DESIGN.md` as evidence only when the task is to audit, refresh, migrate, or intentionally compare against that prior artifact.

If you inspect inactive components, unused assets, or older source files only to classify them as legacy or not rendered, list them as legacy/unused evidence separately. Do not include them in used-reference counts unless they materially explain a conflict or migration risk.

### Step 2 - Build an evidence matrix

Before writing `DESIGN.md`, create a compact working matrix. Persist it as `evidence-matrix.md` for non-trivial extractions, isolated skill tests, audits, or refreshes where future reviewers need to see the raw support trail. For small one-off extractions, it may live inside `## Extraction Notes` or the final response instead.

```md
| Area | Candidate choice | Supporting refs | Count | Conflicts / inconsistencies | Confidence |
|---|---|---:|---:|---|---|
| Colors.primary | #... | R1, R3 | 2 | R2 uses #... | high |
```

Track at least:
- brand personality and target feel
- color palettes and semantic roles
- typography families, levels, weights, line heights, and letter spacing
- spacing, layout grid, margins, density, and responsive behavior
- elevation, shadows, blur, borders, and layering
- radius and shape language
- component styles and interaction states
- practical do's and don'ts

### Step 3 - Resolve conflicts explicitly

Look for:
- token values that differ from CSS, Tailwind, screenshots, or prose
- screenshots that show different radii, spacing, density, shadows, or typography for the same component
- brand notes that describe a mood the implemented UI does not express
- inconsistent semantic color usage, especially primary actions, errors, surfaces, and text colors
- component prose that cannot be represented by current tokens
- missing evidence for required or expected token groups
- accessibility issues such as linter-reported color contrast failures, especially for buttons, badges, links, text on accents, and data states

Resolve by preferring, in order:
1. user-provided current source of truth
2. existing design tokens or theme config
3. repeated implementation values
4. repeated visual evidence across screens
5. brand/product notes
6. clearly labeled inference

If the strongest source conflicts with repeated visual evidence, surface both and explain the chosen direction.

When a repo contains multiple generations of UI, classify evidence as active, legacy, or unused before choosing. Prefer active entrypoints, currently rendered screens, shared components imported by those screens, and repeated current values. Treat older theme files, unused assets, or superseded components as conflicts or legacy notes rather than equal-weight evidence.

### Step 4 - Draft tokens

Create the smallest token set that can reproduce the observed system:
- colors: semantic roles, surfaces, text colors, outlines, error states, and repeated accents
- typography: usually 5-12 levels unless the references clearly support more
- rounded: named scale values used by real components
- spacing: base unit, gaps, margins, container widths, and repeated component padding
- components: buttons, inputs, cards, lists, badges, navigation, and domain-specific components with variants as separate keys

Translate platform units into spec-valid dimensions. For example, Compose `dp` and web `px` can become `px`; Compose `sp` may become `px` only when you record that it is a platform-to-spec conversion. If line height, letter spacing, or font weight is implicit in the source, omit it or mark it inferred instead of guessing silently.

Prefer reference-friendly token names. If a source scale uses keys that are awkward in `{path.to.token}` references, such as `2xl` or `3xl`, map them to clear aliases like `xxl` or `xxxl` and document the mapping in extraction notes.

Keep one-off decoration in prose unless it appears as a reusable system rule.

### Step 5 - Write DESIGN.md

Use this structure by default:

```md
---
version: alpha
name: <Design system name>
description: <optional short description>
colors:
  ...
typography:
  ...
rounded:
  ...
spacing:
  ...
components:
  ...
---

## Brand & Style

## Colors

## Typography

## Layout & Spacing

## Elevation & Depth

## Shapes

## Components

## Do's and Don'ts

## Extraction Notes
```

Use `## Extraction Notes` unless the user requests a clean production-only `DESIGN.md`. This unknown section is allowed by the spec and should include:

```md
## Extraction Notes

- References inspected: <total>
- References used in tokens or prose: <count>
- Low-confidence or inferred decisions: <count>

### Reference IDs

- R1: <path or source> - <source type>
- R2: <path or source> - <source type>

| Area | Supporting refs | Count | Confidence |
|---|---|---:|---|
| Colors | R1, R2 | 2 | high |

### Conflicts and Inconsistencies

- <area>: <conflict>, chosen <value/rule> because <source reason>.

### Inferred Decisions

- <area>: <decision> inferred from <refs or pattern>.
```

If the user wants no extraction notes inside `DESIGN.md`, put the same counts and conflicts in a sidecar note or final response.

### Step 5.5 - Write sidecar artifacts when useful

Use sidecar artifacts when the extraction is a test run, audit, rerun, or large enough that embedding every detail in `DESIGN.md` would make it noisy:

- `evidence-matrix.md`: full source ID inventory, active/legacy/unused classification, candidate choices, support counts, conflicts, confidence, and inferred decisions.
- `final-report.md`: files written, inspected/used reference counts, conflicts and inconsistencies found, linter/manual validation results, target repo git status when applicable, and any skill ambiguity or missing instruction discovered during the run.

For isolated skill tests, write sidecars to the requested scratch or workbench directory and do not modify the target repo unless the user explicitly asks. For production repo updates, write sidecars next to `DESIGN.md` only when the user asked for traceability or the extraction has meaningful uncertainty.

### Step 6 - Validate

Before finishing:
- confirm YAML frontmatter starts and ends with `---`
- confirm no duplicate `##` section headings exist
- confirm known sections are in spec order
- confirm color tokens are valid hex values
- confirm typography values use valid dimensions or numbers
- confirm component token references resolve
- run `npx @google/design.md lint DESIGN.md` when the package is available
- if the linter reports warnings, either fix warnings that indicate real broken references or document intentional warning-only tradeoffs in the final response
- do not treat warning-only lint output as a failed extraction when the warnings are caused by deliberate semantic tokens that are used in prose but not directly referenced by component tokens
- if validation tooling is unavailable, blocked by sandbox/network/package resolution, or intentionally skipped, report that the linter did not run and perform the manual checks above
- never claim linter results unless the linter command actually ran; keep manual validation and linter validation as separate report items

## Verification checklist

Before finishing, confirm that you:
- read the spec or relied on a freshly read relevant excerpt
- assigned source IDs to references
- counted inspected and used references
- included support counts by section or major token group
- surfaced conflicts and inconsistencies
- labeled inferred or low-confidence decisions
- persisted or summarized the evidence matrix
- produced a final report for test, audit, or rerun workflows
- wrote valid `DESIGN.md` frontmatter and section structure
- validated manually or with the DESIGN.md linter
- stated whether generated/prior target artifacts were used, compared, or excluded
