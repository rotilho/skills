# Research Pack Template

Use this when deep research should leave resumable artifacts under `.workbench/deep-research/`.

## Suggested layout

```text
.workbench/deep-research/
├── README.md
├── 00-brief.md
├── 01-knowledge-map.md
├── 02-gap-map.md
├── 03-plan.md
├── 04-source-log.md
├── 05-citation-registry.md
├── 06-task-notes.md
├── 07-evidence-register.md
├── 08-raw-notes.md
├── 09-executive-summary.md
├── 10-key-findings.md
├── 11-risks-open-questions.md
└── 12-sources.md
```

## File roles

- `00-brief.md`: question, decision target, audience, constraints, as-of date
- `01-knowledge-map.md`: what is already known, how strong it is, and what can be reused
- `02-gap-map.md`: unresolved questions ranked by importance and impact
- `03-plan.md`: tasks created only for unresolved high-priority gaps
- `04-source-log.md`: source inventory with URL/path, type, date, and status
- `05-citation-registry.md`: approved and dropped sources with stable IDs and citation-ready metadata
- `06-task-notes.md`: per-task distilled notes returned by subagents or sequential passes
- `claim-ledger.md` (optional): one claim ID per draftable claim with linked source IDs
- `07-evidence-register.md`: claim-level support, contradictions, confidence, follow-ups
- `08-raw-notes.md`: rough extracts, quotes, metrics, and observations
- `09-executive-summary.md`: concise synthesis for decision-makers
- `10-key-findings.md`: fuller findings organized by gap or stream
- `11-risks-open-questions.md`: unresolved issues, caveats, and what would change the answer
- `12-sources.md`: cleaned final source list

## Minimal templates

### `01-knowledge-map.md`

```md
## Topic / Claim
- Status: covered | partial | weak
- Current support: direct | indirect | unclear
- Existing artifact(s):
- Notes:
```

### `02-gap-map.md`

```md
## Gap
- Priority: critical | important | nice-to-have
- Why it matters:
- Best source types:
- Planned action:
- Status: open | in-progress | resolved | unresolved
```

### `03-plan.md`

```md
### Task T1
- Specialist role:
- Gap addressed:
- Objective:
- Best source types:
- Queries / source entry points:
- Depth: scan | deep
- Parallel group:
- Freshness risk:
- Output path:
```

### `05-citation-registry.md`

```md
## Approved
| ID | Source | Type | Accessibility | Date | Reliability | Why it matters |
|----|--------|------|---------------|------|-------------|----------------|
| S1 |        | official | public        |      | high        |                |

## Dropped
| Source | Type | Accessibility | Reason dropped |
|--------|------|---------------|----------------|
|        |      |               |                |
```

### `06-task-notes.md`

```md
## Task T1
- Specialist role:
- Gap addressed:
- Objective:
- Sources consulted: [S1], [S2]
- Source tags:
- Key findings:
  - C1: ... [S1][S2]
- Deep-read notes:
- Gaps / what was not found:
- Confidence:
- Output artifacts:
```

### `07-evidence-register.md`

```md
### Claim / Topic
- Claim ID:
- Source IDs:
- Observation:
- Inference:
- Contradiction / alternative view:
- Claim status: observed | inferred | unverified
- Evidence strength: weak | moderate | strong
- Follow-up needed:
```

### `08-raw-notes.md`

```md
## Source ID: S1
- URL / path:
- Why it matters:
- Raw observations:
- Useful quote or metric:
- Caveats:
```

## Operating rule

Capture existing knowledge before new search. Then build a gap map. Final reports should be derived from `knowledge-map`, `gap-map`, `citation-registry`, `task-notes`, `evidence-register`, and `raw-notes`, not from memory alone or raw search dumps.
