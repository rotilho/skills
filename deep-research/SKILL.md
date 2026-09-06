---
name: "deep-research"
version: "1.1.0"
description: "Run evidence-backed research, comparisons, or audits and refresh existing research by identifying decision-critical gaps, verifying important claims with primary sources, and producing a traceable answer. Use for multi-source investigation, not routine local code or prompt review."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "research"
---

# Deep Research

Answer a research question with evidence strong enough for the decision. Reuse sound prior work, investigate what is missing, and make uncertainty visible.

## When to use

Use for literature reviews, technical due diligence, market or competitor research, tool comparisons, investigative questions, and refreshing substantial research artifacts.

Do not use for simple facts, routine local reviews or edits, pure rewriting, or brainstorming that needs no investigation.

## Prerequisites

- Read source content, not only search snippets. Current public research needs web search or fetch access; local-only work can use supplied documents and repositories.
- Disclose access limits when they affect the answer. Do not imply live or external verification from local notes alone.

## Workflow

### 1. Frame the decision and inventory existing evidence

Infer the question, audience, constraints, time horizon, and requested output. Inspect provided notes, prior reports, source lists, and relevant earlier results before searching.

Separate what is already supported from what is stale, conflicting, or missing. Reuse prior work only after checking its support and freshness. Rank unresolved questions by how much they could change the answer.

### 2. Investigate the consequential gaps

- Start with the gaps that block the decision, then those that materially affect confidence or tradeoffs.
- Search broadly enough to find terminology, primary sources, and competing explanations; read deeply where the result matters.
- Prefer official documentation, original papers and datasets, filings, source code, and direct product evidence. Use secondary reporting and community discussion as appropriate to the question, checking important claims against original evidence when available.
- Judge coverage by the claims supported, not a quota of domains, sources, tasks, or official-source percentages. Several sites repeating one claim are not independent confirmation.
- If useful and supported, delegate independent gaps. Give each worker the question, existing evidence, constraints, and output scope. Request findings with sources, dates, and unresolved questions. Inspect underlying sources when needed to verify a material finding.

### 3. Connect claims to sources

For each consequential claim, retain its source URL or path, the relevant evidence, publication/update date when available, and the date checked for time-sensitive material. Use stable source or claim IDs when they make a substantial report easier to audit.

Distinguish:
- **Observed fact**: directly supported by the inspected evidence.
- **Inference**: a conclusion drawn from evidence, with the reasoning visible.
- **Unverified claim**: plausible or reported, but not established.

Disclose when evidence requires registration, is paid or user-provided, or comes from the user's private records. Private records may support facts about the user's own system; they do not establish independent public confirmation.

Do not invent citations, rely on snippets as proof, or quietly reuse a source rejected as unreliable. Keep enough of the rejection reason to avoid repeating the mistake.

### 4. Challenge the answer

- Look for contradictory evidence, stale claims, missing context, and stronger alternative explanations.
- Cross-check high-impact conclusions independently where feasible. If one authoritative source is all that exists, say what that limits.
- Resolve contradictions or report both interpretations and what would settle them.
- Do not manufacture review issues to meet a count. Reopen research when drafting reveals a material evidence gap.

### 5. Synthesize and stop

Organize the answer around the user's decision, with sources beside the claims they support. Explain relevant tradeoffs, uncertainty, and what would change the conclusion. Include an as-of date for time-sensitive findings.

Stop when critical gaps are resolved and further research is unlikely to change the answer. If access, time, or missing evidence leaves a critical gap open, identify it and give the supported partial conclusion.

## Working artifacts

For substantial or resumable work, use `.workbench/deep-research/` unless the user or repo specifies another location. Start with one notes file containing the question, known evidence, open gaps, and claim-to-source links. Keep raw extracts distinguishable from conclusions within it.

Split out sources, worker notes, or the final report only when their size, ownership, or reuse warrants separate files. Do not create empty registries or a fixed document pack. Preserve enough provenance that another agent can check the answer and resume unresolved work.

## Verification

- The answer addresses the original question and builds on verified prior work.
- Important claims link to inspected sources and distinguish evidence from inference.
- Dates, access limits, contradictions, and decision-relevant gaps are visible.
- Recommendations follow from evidence and include material tradeoffs.
- The output is as small as the question allows while remaining traceable.
