# Extraction evidence notes

Use for a new extraction or when adding provenance to a document. For a focused audit or refresh, record only the inspected areas and identify that scope; do not imply a full-system review. Put the notes in DESIGN.md, a requested sidecar, or the response according to the requested output.

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
