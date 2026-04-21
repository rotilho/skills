---
name: "deep-research"
description: "Run thorough, evidence-backed research or audit and refresh existing research artifacts with a gap-first workflow: inventory existing knowledge, identify only the missing high-impact gaps, verify important claims with primary sources, and synthesize a decision-useful answer with traceable evidence. Use for research-heavy comparisons, validation, or evidence-backed audits, not routine local code or prompt review."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "research"
  artifact_persistence: "preferred"
  capabilities_required: "web search or web fetch access for current/public research; ability to read source content, not only snippets"
  capabilities_optional: "parallel agents or subagents for independent research streams; file writing for research artifacts and resumable outputs; browser or API inspection for live verification"
---

# Deep Research

Use this skill when the user needs multi-source, evidence-backed research or validation.

Trigger for work like:
- market research
- competitor mapping
- technical due diligence
- tool or vendor comparison
- literature review
- strategy memo creation
- investigative question answering with evidence
- current or ecosystem research that needs live web data

## Core promise

Produce research that is:
- source-grounded
- explicit about what is already known
- focused on the highest-value unknowns
- clear about uncertainty
- traceable back to evidence
- organized enough to reuse later

Do not stop at link collection or surface summaries.

## Operating principle

Research is not "search everything, summarize later".

Use this loop:
1. inventory existing knowledge
2. identify real gaps
3. investigate only the highest-value gaps
4. stop when the answer is good enough for the decision

Hard rules:
- check what is already known before new search
- do not redo good existing work
- draft from notes and evidence, never raw search dumps
- if a gap stays unresolved, say so instead of guessing

## Architecture

Prefer a lead-agent plus subagent pattern when supported.

Lead agent:
- frame the job
- inventory existing knowledge
- build the knowledge map and gap map
- create only gap-closing tasks
- merge notes into outline, draft, review, and final answer

Subagents:
- investigate one gap or one tight gap cluster
- return distilled notes, not raw search logs
- tag sources, dates, and unresolved gaps
- emit claim-ready findings with source IDs

Hard rule: the lead agent should read subagent notes and registries, not raw search transcripts.

## When not to use

Do not use this skill for:
- simple factual questions answerable without multi-source research
- straightforward code edits with no research component
- routine local code, prompt, or skill review with no evidence-gathering requirement
- speculative brainstorming the user wants kept fast and loose
- pure rewriting or formatting with no investigation

## Capability check

Before researching, state:

```md
Research mode: web-enabled | local-only | hybrid
Can search web: yes/no
Can fetch full sources: yes/no
Can inspect live products/APIs: yes/no
Can write files: yes/no
Known limitations:
```

If web search is unavailable, do not imply current external research.

If subagent dispatch is unavailable, work the gaps sequentially.

## Source policy

Classify source accessibility:
- `public`: open without authentication
- `semi-public`: registration or limited access required; allowed with disclosure
- `exclusive-user-provided`: paid or private third-party material the user explicitly provides; allowed with disclosure
- `private-user-owned`: the user's own private accounts or records; do not use these to pretend you independently discovered what the user already knows

Rules:
- if only `private-user-owned` evidence exists, say the claim is not externally verified
- if the user provides private or paid sources for third-party research, disclose that they are `exclusive-user-provided`
- if no public equivalent exists, do not overstate verification strength

Also classify source type:
- `official`
- `academic`
- `secondary-industry`
- `journalism`
- `community`
- `other`

## Gap-first workflow

### Step 0 - Frame the job

Define or infer:
- research question
- decision target
- audience
- time horizon
- constraints
- out of scope
- output format
- as-of date

Compact template:

```md
Research question:
Decision target:
Audience:
Constraints:
Out of scope:
Output format:
As-of date:
```

### Step 1 - Inventory existing knowledge first

Before new searching, inspect what already exists.

Look for:
- user-provided notes, spreadsheets, docs, or prior memos
- existing `research/`, `notes/`, `analysis/`, `docs/`, or similar folders
- earlier source lists, evidence registers, raw exports, or draft reports
- earlier turns or agent outputs that already resolved part of the question

Classify each artifact:
- **Reusable**: strong enough to build on now
- **Needs refresh**: useful but stale, incomplete, or weakly sourced
- **Superseded**: contradicted, outdated, or lower quality than newer evidence

Treat prior research as input, not truth. Reuse what earns reuse.

Compact template:

```md
Existing research checked: yes/no
Prior artifacts found:
- <path or source> - reusable | needs refresh | superseded
What is already known with reasonable confidence:
-
```

### Step 2 - Build a knowledge map and gap map

Before searching, write two lists.

1. **Knowledge map**
   - what is already covered
   - confidence level
   - whether support is direct or weak

2. **Gap map**
   - what is missing, stale, conflicting, or decision-critical
   - ranked by impact on the final answer

Classify each gap:
- **Critical**: blocks the answer or recommendation
- **Important**: materially affects confidence or tradeoffs
- **Nice to have**: useful context, not decision-changing

Default rule: research `Critical` and `Important` gaps first.

Compact template:

```md
## Knowledge map
- Topic / claim:
  - Status: covered | partial | weak
  - Support: direct | indirect | unclear

## Gap map
- Gap:
  - Priority: critical | important | nice-to-have
  - Why it matters:
  - Best source types:
  - Planned action:
```

### Step 3 - Plan only the gap-closing work

Turn the top gaps into tasks.

Each task should include:
- task ID
- specialist role
- gap addressed
- objective
- best source types
- starting queries or entry points
- expected depth: scan | deep
- parallel group if using subagents
- freshness risk for time-sensitive claims
- output path if files are available

Only create tasks for unresolved gaps.

Compact template:

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

Default sizing:
- lightweight: 3-4 tasks
- standard: 4-6 tasks
- max 3 concurrent subagents per wave unless the environment clearly supports more

### Step 4 - Breadth pass on unresolved gaps

For each active gap:
- identify candidate sources and terminology
- note repeated claims that need verification
- keep rough notes with stable source IDs
- stop broad search once the gap landscape is clear

Breadth outputs:
- candidate source set
- terminology list
- competing hypotheses
- updated gap map

### Step 5 - Depth and verification pass

Go deep only where it changes the answer.

For important conclusions, verify with one or more of:
- official docs or sites
- live product or API behavior
- original papers or reports
- pricing pages
- repo or package inspection
- public filings or canonical announcements
- user-provided primary materials

For high-value claims, prefer two independent checks when possible.

Label conclusions as:
- **Observed fact**
- **Inference**
- **Unverified claim**

Record evidence strength:
- weak
- moderate
- strong

Build a citation registry during this phase.

Registry rules:
- assign stable source IDs on first approved use
- record source type, accessibility, date, reliability, and why it matters
- keep two buckets: `Approved` and `Dropped`
- only approved sources may appear in the final draft
- do not reuse dropped sources unless you explicitly re-evaluate and promote them

Quality gates for approved sources:
- standard mode: at least 5 unique domains and at least 30% official sources when the domain allows it
- lightweight mode: at least 3 unique domains and at least 20% official sources when the domain allows it
- avoid over-reliance on one source for key claims
- if strong public evidence does not exist, say so plainly

### Step 6 - Counter-review and contradiction pass

Before synthesis, look for:
- conflicts between sources
- missing context
- edge cases
- stale information
- stronger competing interpretations
- high-impact claims still resting on weak evidence

If a contradiction remains unresolved, surface both interpretations and say what would settle it.

Minimum review standard:
- challenge the main conclusion directly
- identify high-impact claims that rely on one source
- check recency-sensitive claims for staleness
- find at least 3 review issues, or say why fewer were possible

### Step 7 - Stop or continue

Stop when:
- critical gaps are resolved
- remaining gaps are only nice-to-have
- new searches mostly repeat existing findings
- remaining uncertainty does not materially change the answer

If critical gaps remain, say so clearly.

### Step 8 - Evidence-mapped outline and drafting

Before final drafting, map sections to supported claims and source IDs.

Rules:
- organize by topic or decision dimension, not task order
- every factual claim should trace to approved source IDs
- for substantial reports, use claim IDs in notes or evidence registers so spot-checking is mechanical
- do not introduce new sources during drafting
- if evidence conflicts, add a caveat or counter-claim
- if support is missing, mark the claim unverified or remove it

### Step 9 - Final verification

Before delivery:
- cross-check every cited source ID against the approved registry
- spot-check at least 5 important claims when the report is substantial
- remove or fix non-traceable claims
- confirm no dropped source was resurrected
- confirm major time-sensitive claims use current-enough dates

## Parallelism guidance

If subagents are available, split by unresolved high-priority gaps, not arbitrary themes.

Good splits:
- canonical docs or primary sources
- market or competitor evidence
- technical or implementation verification
- risks, regulation, or counter-evidence

Preferred subagent handoff:

```md
## Task <id>
- Specialist role:
- Gap addressed:
- Objective:
- Sources consulted: [S1], [S2]
- Source tags:
- Key findings:
- Deep-read notes:
- Gaps / what was not found:
- Confidence:
- Output artifacts:
```

The lead agent should synthesize from notes and evidence artifacts, not raw search logs.

## Source governance

Prefer sources in this order:
1. official docs, official sites, original papers, original datasets, filings
2. live APIs, product behavior, package contents, source code, changelogs
3. reputable third-party analysis
4. community discussion, forums, social posts, marketing summaries

Use lower-tier sources to discover leads, not anchor key conclusions.

For each important source, track:
- source type
- source accessibility
- publication or update date if available
- date researched
- why the source matters

For time-sensitive topics, mark claims with an as-of date.

## Working memory and artifacts

When file output is available and the task is substantial, maintain lightweight artifacts under `.research/`.

Recommended artifacts in `.research/`:
- `brief`: question, decision target, constraints, as-of date
- `knowledge-map`: what is already known and how strong it is
- `gap-map`: unresolved questions ranked by importance
- `plan`: tasks created only for active gaps
- `source-log`: source inventory with stable source IDs
- `citation-registry`: approved and dropped sources, citation-ready metadata, and why each source matters
- `task-notes`: per-task distilled notes
- `claim-ledger`: optional but recommended for substantial multi-agent research; one claim ID per draftable claim with linked source IDs
- `evidence-register`: claim-level support, contradictions, and confidence
- `raw-notes`: rough extracts, quotes, metrics, observations
- `synthesis`: working conclusions and draft answer

Default rules:
- keep raw evidence separate from synthesis
- keep open gaps visible until resolved or explicitly left open
- do not compress away provenance too early

## Core note formats

### Citation registry

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

### Evidence register

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

## Deliverable modes

### Short answer mode

Include:
- direct answer
- supporting findings
- major caveats
- recommendation
- source list
- as-of date

### Memo mode

Suggested sections:
1. Executive summary
2. Scope and method
3. Research mode and limitations
4. What was already known
5. Gap-focused findings
6. Recommendation or answer
7. Risks, contradictions, and open questions
8. Sources

### Doc-pack mode

Suggested file set:
- `README.md`
- `00-brief.md`
- `01-knowledge-map.md`
- `02-gap-map.md`
- `03-plan.md`
- `04-source-log.md`
- `05-citation-registry.md`
- `06-task-notes.md`
- `07-evidence-register.md`
- `08-raw-notes.md`
- `09-executive-summary.md`
- `10-key-findings.md`
- `11-risks-open-questions.md`
- `12-sources.md`

For smaller tasks, combine files, but keep distinct:
- existing knowledge
- open gaps
- raw evidence
- final synthesis

## Pitfalls to avoid

- starting web search before inventorying existing knowledge
- treating prior memos as proof without checking support
- researching every angle instead of decision-relevant gaps
- collecting links without synthesis
- relying on snippets as evidence
- mixing speculation with fact
- ignoring contradictory evidence
- having the lead agent read raw search outputs instead of task notes
- inventing URLs or citations
- resurrecting dropped sources without explicit re-evaluation
- giving recommendations without tradeoffs
- hiding capability limits that reduce confidence
- merging raw evidence and conclusions so tightly that the work cannot be resumed or audited

## Final verification checklist

Before finishing, confirm that you:
- stated research mode and capability limits
- inventoried existing research first
- wrote a knowledge map and gap map
- prioritized only the gaps that matter
- verified the most important claims
- separated facts from inference
- kept enough evidence to trace major claims
- documented contradictions or unresolved gaps
- marked time-sensitive claims with an as-of date
- answered the original question directly
- included sources

## Default final-answer structure

```md
## Executive summary

## Scope and method

## Research mode and limitations

## What was already known

## Gap-focused findings

## Recommendation / answer

## Risks, contradictions, caveats, and open questions

## Sources

## As-of date
```
