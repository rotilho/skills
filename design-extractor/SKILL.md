---
name: "design-extractor"
version: "1.1.0"
description: "Create, audit, or refresh DESIGN.md from product visuals, source code, design tokens, or brand references. Use for design-system extraction, not ordinary frontend implementation."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "design"
---

# Design Extractor

Turn product evidence into a compliant `DESIGN.md`, with traceable source counts and visible conflicts or inferences.

## Choose the requested operation

- **Create/extract:** inspect the relevant product surfaces, build an evidence matrix, and write a complete document. Use the [starting structure](templates/design.md) when a new document needs it.
- **Audit:** compare the specified document or areas with the supplied evidence and report discrepancies. An audit alone does not authorize rewriting the target document.
- **Focused refresh:** update the requested areas and their dependent tokens or prose. Recheck their evidence and references; preserve unaffected content and provenance. Do not rebuild the entire extraction unless the change requires it.

For isolated tests, write artifacts outside the target repo in the requested scratch/workbench directory unless target edits are explicitly authorized.

## Load relevant format guidance

- Read [the format spec](references/docs/spec.md) when writing or validating schema, section order, tokens, or consumer behavior.
- Consult a relevant `references/examples/*/DESIGN.md` only when tone or token shape is unclear.
- Use the [extraction-note template](templates/extraction-notes.md) when adding provenance. It is not a required separate artifact.
- Load bundled CLI source only when debugging parser or linter behavior. `references/` is an external submodule; place user-owned templates outside it.

## Establish evidence for the requested scope

Assign stable IDs to inspected sources, with their path/URL and type: visual reference, implementation file, token file, brand/product note, generated/prior artifact, or user instruction. For a focused review, identify the reviewed areas so its counts cannot be mistaken for a full-system audit.

Count distinct references, not repeated observations within one file. Materially different screenshots may count separately. A source supports a choice only when it directly states, implements, or clearly displays that choice.

- Exclude this skill's format spec and examples from product-reference counts.
- Classify generated `DESIGN.md`, evidence matrices, reports, and workbench output before use. Exclude prior extraction artifacts when extracting afresh from raw product sources; use an existing document when auditing, refreshing, migrating, or deliberately comparing it.
- Classify UI evidence as active, legacy, or unused. Prefer active entrypoints and currently rendered components. Exclude unused material from used-reference counts unless it explains a conflict or migration risk.

Track candidate values, supporting IDs, counts, conflicts, and confidence in a compact matrix. Keep it in extraction notes or the response; use a sidecar only when requested or needed for a large evidence trail. Full extractions should consider the supported brand, colors, typography, layout/spacing, elevation, shapes, components/states, and practical usage rules. Focused work covers the affected areas without inventing evidence for absent ones.

## Resolve differences and choose tokens

Check for inconsistent values, semantic roles, interaction states, inaccessible color combinations, and mismatches between tokens, prose, and rendered UI. Prefer the current source of truth named by the user, then active tokens/theme config, repeated current implementation, repeated visual evidence, brand notes, and finally labeled inference. If strong sources disagree, show both and explain the choice; never silently average values or invent support.

Create the smallest reusable token set supported by the evidence. Keep one-off decoration in prose. Map platform dimensions into spec-valid values and disclose conversions such as Compose `sp` to `px`. Omit or label inferred line heights, weights, and letter spacing instead of silently guessing.

Preserve these format constraints:

- Frontmatter tokens are normative; Markdown explains their application. Use the supported groups: `version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, and `components`.
- Use each `##` section name once, with known sections in spec order. Include only relevant sections.
- Use valid hex values for the colors map. Put unsupported alpha, gradient, blur, shadow, or CSS literals in component tokens or prose.
- Prefer spec component properties (`backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`) and references such as `{colors.primary}`. Translate platform property names; preserve unknown properties only intentionally.

## Deliver and validate

Complete the requested document, patch, or audit findings. Include inspected/used source counts, support per affected section or token group, conflicts, and inferred choices. By default use `## Extraction Notes`; for a clean production document put the evidence in the response or a requested sidecar. Do not remove existing provenance merely to shorten the output.

For created or changed documents, check frontmatter delimiters, unique headings and section order, color/dimension values, and token-reference resolution, including dependents of changed tokens. Audit findings should state which areas were actually checked.

Run `npx @google/design.md lint DESIGN.md` when the package is available and full format validation is relevant. Fix real reference errors; document intentional warnings. Unused semantic tokens expressed in prose can produce valid warning-only output. If tooling is unavailable, blocked, or unnecessary for a focused audit, report that the linter did not run and describe the manual checks. Never imply linter execution from manual review.

Report the artifact paths, evidence scope/counts, unresolved conflicts or inferences, and validation results. A separate final report is needed only when requested.
