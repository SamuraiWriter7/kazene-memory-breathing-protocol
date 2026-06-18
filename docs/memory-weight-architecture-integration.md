# Memory Weight Architecture Integration

## Kazene Memory Breathing Protocol v0.3

**Version:** v0.3.0-candidate
**Status:** Draft
**Repository:** `kazene-memory-breathing-protocol`

---

## 1. Overview

Memory Weight Architecture Integration extends Kazene Memory Breathing Protocol by defining how AI memory items receive weight, priority, retention level, review cycle, and action routing.

In earlier versions:

* `v0.1` defined the Four-Layer Memory Breathing Core.
* `v0.2` defined Executable Forgetting Rules.

`v0.3` adds memory weighting as an operational layer.

The goal is to make AI memory selective, weighted, reviewable, and metabolically efficient.

AI should not treat all memory equally.

Some memory should be released immediately.
Some should remain active for a project cycle.
Some should be promoted to long-term memory.
Some should become implicit behavioral influence.
Some should require human review before retention or forgetting.

---

## 2. Core Idea

Memory weight defines how strongly a memory item should influence future AI behavior.

A memory item may be evaluated by:

* importance,
* recurrence,
* future action value,
* safety impact,
* human preference relevance,
* trace or attribution value,
* project relevance,
* freshness,
* and review requirement.

Memory weight is not only a label.

It determines memory routing.

```text
memory item
  → weight evaluation
  → retention priority
  → memory layer decision
  → review cycle
  → forgetting or preservation action
```

---

## 3. Why Memory Weight Matters

Without memory weighting, AI systems may:

* over-retain low-value context,
* forget important recurrence patterns,
* treat temporary details as durable truth,
* repeat old assumptions,
* overload context windows,
* increase computational cost,
* and burden humans with irrelevant memory residue.

Memory weighting allows AI systems to remember less but better.

It supports:

* lower token load,
* better context selection,
* safer long-term behavior,
* clearer human review boundaries,
* stronger trace compaction,
* and more efficient agent workflows.

---

## 4. Weight Levels

Kazene Memory Breathing Protocol defines four default memory weight levels.

```text
low
medium
high
critical
```

---

## 5. Low Weight Memory

### Definition

Low weight memory has little future action value.

It is usually temporary, local, redundant, or already resolved.

### Examples

* one-time phrasing,
* temporary debugging chatter,
* resolved intermediate comments,
* duplicate log lines,
* obsolete assumptions,
* low-value conversational residue.

### Default action

```text
forget
compress
release
```

### Typical layer

```text
short_term_memory
released
```

---

## 6. Medium Weight Memory

### Definition

Medium weight memory has project-level value but may not need long-term retention.

It is useful during an active release, task, repository, or design cycle.

### Examples

* current repository state,
* active schema design,
* release candidate status,
* recent validation result,
* unresolved issue,
* implementation note.

### Default action

```text
keep temporarily
archive after resolution
compress if repeated
```

### Typical layer

```text
working_memory
archive
```

---

## 7. High Weight Memory

### Definition

High weight memory has repeated future action value.

It should influence future work, validation, or behavior.

### Examples

* recurring error pattern,
* confirmed prevention rule,
* durable user preference,
* core architecture decision,
* release validation boundary,
* repeated schema-example mismatch pattern.

### Default action

```text
promote_to_long_term
convert_to_recurrence_rule
create_validation_gate
```

### Typical layer

```text
long_term_memory
implicit_breathing_layer
```

---

## 8. Critical Weight Memory

### Definition

Critical weight memory affects safety, governance, authorship, attribution, value allocation, or high-impact decisions.

It must not be silently forgotten or transformed without review.

### Examples

* human review boundary,
* safety boundary,
* authorship attribution,
* royalty or value allocation trace,
* identity-sensitive decision,
* legal or political interpretation,
* irreversible external system action.

### Default action

```text
preserve
return_to_human_review
create_review_record
```

### Typical layer

```text
long_term_memory
human_review
archive
```

---

## 9. Weight Evaluation Criteria

A memory weight record should evaluate at least the following dimensions.

### 9.1 Importance

How important is this memory to future behavior?

Suggested values:

```text
low
medium
high
critical
```

---

### 9.2 Recurrence

How likely is this memory pattern to recur?

Suggested values:

```text
none
low
medium
high
systemic
```

---

### 9.3 Future Action Value

Will this memory guide future useful action?

Suggested values:

```text
low
medium
high
critical
```

---

### 9.4 Safety Impact

Could retaining, forgetting, or misusing this memory affect safety?

Suggested values:

```text
low
medium
high
critical
```

---

### 9.5 Human Preference Relevance

Does this memory reflect a durable human preference?

Suggested values:

```text
none
low
medium
high
critical
```

---

### 9.6 Trace Value

Does this memory preserve origin, contribution, authorship, accountability, or value circulation?

Suggested values:

```text
none
low
medium
high
critical
```

---

### 9.7 Freshness

How fresh or stale is this memory?

Suggested values:

```text
fresh
active
aging
stale
obsolete
```

---

## 10. Memory Weight Record

A memory weight record documents how a memory item is weighted and routed.

Example:

```yaml
memory_weight_record:
  id: "mwr-2026-06-18-001"
  protocol_version: "0.3.0-candidate"
  memory_item:
    type: "recurring_error_pattern"
    summary: "YAML parent keys may become null when indentation collapses."
    source_layer: "working_memory"
  evaluation:
    importance: "high"
    recurrence: "high"
    future_action_value: "high"
    safety_impact: "medium"
    human_preference_relevance: "low"
    trace_value: "medium"
    freshness: "active"
  weight:
    level: "high"
    reason:
      - "The pattern is likely to recur during schema-example editing."
      - "Preserving the prevention rule reduces future debugging load."
      - "The raw log can be released after the structural rule is retained."
  routing:
    destination_layer: "long_term_memory"
    recommended_action: "convert_to_recurrence_rule"
    review_cycle: "monthly"
```

---

## 11. Retention Priority

Memory weight produces retention priority.

Suggested priority levels:

```text
release
temporary
retain
promote
protect
review_required
```

### Default mapping

| Weight   | Default Priority | Typical Action                            |
| -------- | ---------------- | ----------------------------------------- |
| low      | release          | forget or compress                        |
| medium   | temporary        | keep in working memory, archive after use |
| high     | promote          | promote to long-term or recurrence rule   |
| critical | review_required  | preserve and return to human review       |

---

## 12. Review Cycle

Memory should not remain fixed forever.

A memory weight record may include a review cycle.

Suggested values:

```text
none
daily
weekly
monthly
quarterly
release_cycle
on_major_change
human_requested
```

Examples:

* low weight memory may need no review,
* medium weight memory may be reviewed after a release,
* high weight memory may be reviewed monthly or per release cycle,
* critical memory may require human review on major changes.

---

## 13. Weight-Based Routing

Memory weight determines the route of a memory item.

```text
low
  → forget / compress / release

medium
  → keep temporarily / archive

high
  → promote / convert to recurrence rule / move to implicit layer

critical
  → preserve / human review / protected archive
```

This routing connects directly to v0.2 Executable Forgetting Rules.

---

## 14. Relation to Executable Forgetting Rules

Memory Weight Architecture does not replace forgetting rules.

It guides them.

```text
memory_weight_record
  → recommends action

forgetting_rule
  → defines executable transformation

memory_retention_decision
  → records what actually happened
```

Example:

```text
weight = high
recurrence = high
future_action_value = high
  → recommended action: convert_to_recurrence_rule
```

---

## 15. Relation to Implicit Breathing Layer

Some memories should not be retained as explicit long-form text.

If a memory is a repeated behavioral preference or response posture, it may be moved into the Implicit Breathing Layer.

Examples:

* reduce cognitive load,
* avoid redundant questions,
* preserve human review boundary,
* prefer structural clarity,
* validate before release.

This reduces explicit context load while preserving useful behavioral influence.

---

## 16. Relation to Trace and Royalty Layers

Some memory must remain durable because it affects traceability, origin, contribution, authorship, or value circulation.

Examples:

* attribution trace,
* authorship origin,
* royalty allocation event,
* contribution record,
* public return decision,
* human approval boundary.

These memories often require critical weight or human review.

Memory should not be compressed in a way that destroys attribution or value return.

---

## 17. Human Review Boundary

Memory weight must not become unchecked authority.

Human review is required when memory weight affects:

* value allocation,
* authorship attribution,
* legal judgment,
* political or military interpretation,
* safety boundary changes,
* financial consequence,
* identity-sensitive decision,
* irreversible external action,
* or human preference changes.

Example:

```yaml
human_review:
  required: true
  required_for:
    - "authorship_attribution"
    - "value_allocation"
    - "safety_boundary_change"
  default_action: "pause_and_return_to_human"
```

---

## 18. Minimal v0.3 Scope

Version `v0.3.0-candidate` introduces:

* memory weight record schema,
* memory weight example,
* weight evaluation criteria,
* retention priority,
* review cycle,
* weight-based memory routing,
* and integration with executable forgetting rules.

This version does not yet define:

* full multi-agent memory weighting,
* cryptographic memory proofs,
* distributed weight synchronization,
* or royalty allocation logic.

Those may be added in later versions.

---

## 19. Suggested Files

```text
docs/memory-weight-architecture-integration.md

schemas/memory-weight-record.schema.json

examples/memory-weight-record.example.yaml
```

Validation should be added to:

```text
scripts/validate_examples.py
```

---

## 20. Design Philosophy

```text
Not every memory deserves the same gravity.

A memory item should become heavy only when it guides future action,
protects safety,
preserves trace,
or prevents recurrence.

Low-value memory should flow away.
High-value memory should become structure.
Critical memory should return to human review.
```

---

## 21. Summary

Memory Weight Architecture Integration makes AI memory selective.

It allows AI systems to decide:

* what should remain light,
* what should become durable,
* what should be promoted,
* what should be downgraded,
* what should become implicit behavior,
* and what must return to human review.

`v0.1` defined memory breathing.
`v0.2` made forgetting executable.
`v0.3` gives memory weight.
