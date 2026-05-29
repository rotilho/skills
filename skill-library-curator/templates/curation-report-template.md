# Skill Library Curation Report

Date: [YYYY-MM-DD]
Scope: [global | repo-local | mixed]
Roots:
- Global: `~/IdeaProjects/skills`
- Repo-local: `[<target-repo>/.agents/skills or not inspected]`

## Summary

- Inspected: [count] active candidate skills
- Patched: [count]
- Merged: [count]
- Promoted: [count]
- Embedded: [count]
- Archived: [count]
- Excluded: [count]
- Install result: [`npx skills add ~/IdeaProjects/skills/ -g --all -y` succeeded, failed with short reason, or not needed]

## Inspected Skills

| Skill | Classification | Reason |
|---|---|---|
| [skill-name] | [keep/patch/merge/promote/embed/archive/exclude] | [short reason] |

## Changes Made

| Skill | Change | Files |
|---|---|---|
| [skill-name] | [patched/merged/promoted/embedded/archived] | [paths] |

## Merges

| Target Skill | Archived Skill | Reason | Archive Path |
|---|---|---|---|
| [target-skill] | [superseded-skill] | [why merge was safe] | `.archive/[YYYY-MM-DD]/[skill-name]/` |

## Promotions

| Source Skill | Global Target | Reason | Archive Path |
|---|---|---|---|
| [repo-local-skill] | [global-skill] | [why promotion was safe] | `[repo]/.agents/skills/.archive/[YYYY-MM-DD]/[skill-name]/` |

## Embeddings

| Source Skill | Target Skill | Scope | Reason | Archive Path |
|---|---|---|---|---|
| [source-skill] | [target-skill] | [global/repo-local] | [why embedding was safe] | `.archive/[YYYY-MM-DD]/[skill-name]/` |

## Archives

| Skill | Archive Path | Reason |
|---|---|---|
| [skill-name] | `.archive/[YYYY-MM-DD]/[skill-name]/` | [reason] |

## Exclusions

| Path | Reason |
|---|---|
| [path] | [vendor/package-managed/submodule/generated/unclear ownership] |

## Verification

- [frontmatter checked]
- [support links checked]
- [duplicates checked]
- [global install command result recorded, or repo-local-only change noted]

## Residual Risks

- [risk or "None noted"]
