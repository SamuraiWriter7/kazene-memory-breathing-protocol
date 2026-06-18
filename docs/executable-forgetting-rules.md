# Executable Forgetting Rules

## Kazene Memory Breathing Protocol v0.2

**Version:** v0.2.0-candidate
**Status:** Draft
**Repository:** `kazene-memory-breathing-protocol`

---

## 1. Overview

Executable Forgetting Rules extend Kazene Memory Breathing Protocol by defining how AI systems decide what to forget, compress, archive, downgrade, promote, or return to human review.

In v0.1, the protocol defined the Four-Layer Memory Breathing Core:

* Short-Term Memory
* Working Memory
* Long-Term Memory
* Implicit Breathing Layer

v0.2 adds executable decision logic for memory metabolism.

The goal is to make forgetting explicit, auditable, and safe.

---

## 2. Core Idea

AI systems should not treat memory as permanent by default.

Every memory item should be evaluated according to:

* relevance,
* recurrence,
* safety impact,
* project usefulness,
* human preference,
* trace value,
* governance sensitivity,
* and future action value.

Forgetting is not deletion alone.

Forgetting may include:

```text
forget
compress
archive
downgrade_weight
promote_to_long_term
move_to_implicit_layer
convert_to_recurrence_rule
return_to_human_review
```

This transforms memory from passive storage into active metabolism.

---

## 3. Why Executable Forgetting Is Needed

Without executable forgetting rules, AI systems may accumulate:

* outdated assumptions,
* redundant conversation history,
* low-value logs,
* stale project states,
* obsolete implementation paths,
* repeated explanations,
* and unresolved temporary traces.

This increases:

* token load,
* computational cost,
* reasoning noise,
* hallucination risk,
* cognitive burden,
* and schema-example drift.

Executable Forgetting Rules prevent memory from becoming an unbounded warehouse.

They allow AI systems to breathe.

---

## 4. Forgetting Is Not Erasure

This protocol treats forgetting as a set of controlled transformations.

### 4.1 Forget

Remove or release low-value memory that has no future action value.

Example targets:

* one-time noise,
* redundant phrasing,
* obsolete assumptions,
* temporary conversational residue.

---

### 4.2 Compress

Reduce a memory item into a smaller reusable form.

Example:

```text
Long raw failure discussion
  → short recurrence rule
```

---

### 4.3 Archive

Move memory out of active working memory while preserving it for reference.

Example:

```text
resolved release thread
  → archived project note
```

---

### 4.4 Downgrade Weight

Reduce the influence of a memory item without fully removing it.

Example:

```text
active implementation assumption
  → low-weight historical note
```

---

### 4.5 Promote to Long-Term Memory

Elevate a recurring or durable pattern into long-term memory.

Example:

```text
repeated GitHub Actions indentation failure
  → long-term recurrence pattern
```

---

### 4.6 Move to Implicit Layer

Transform explicit memory into a behavioral tendency.

Example:

```text
The user prefers reduced cognitive burden
  → implicit influence: reduce_cognitive_load
```

---

### 4.7 Convert to Recurrence Rule

Transform a failure, drift, or repeated correction into a reusable prevention rule.

Example:

```text
Python dunder identifiers corrupted by Markdown
  → recurrence rule: verify __future__, __file__, __name__
```

---

### 4.8 Return to Human Review

Pause automation when memory affects high-impact judgment.

Example targets:

* legal judgment,
* safety boundary change,
* identity-sensitive decision,
* irreversible action,
* external system action,
* value allocation,
* political or military interpretation.

---

## 5. Forgetting Decision Model

An executable forgetting rule should answer five questions:

```text
1. What memory item is being evaluated?
2. Why is it being evaluated now?
3. What action should be applied?
4. What must be preserved?
5. Does this require human review?
```

---

## 6. Forgetting Rule Structure

A forgetting rule should include:

* rule ID,
* trigger condition,
* target memory type,
* evaluation criteria,
* action,
* preservation requirements,
* discard or compression targets,
* human review requirement,
* and resulting memory layer.

Example:

```yaml
forgetting_rule:
  id: "forget-rule-001"
  protocol_version: "0.2.0-candidate"
  name: "Compress resolved validation failure into recurrence rule"

  trigger:
    event: "validation_error_resolved"
    conditions:
      - "error_has_clear_recurrence_pattern"
      - "raw_log_is_no_longer_needed_for_current_task"

  target:
    memory_type: "raw_trace"
    description: "Resolved GitHub Actions validation failure log"
    current_layer: "working_memory"

  evaluation:
    relevance: "medium"
    recurrence: "high"
    safety_impact: "medium"
    future_action_value: "high"

  action:
    type: "convert_to_recurrence_rule"
    resulting_layer: "long_term_memory"

  preserve:
    - "failure_pattern"
    - "correction"
    - "prevention_rule"
    - "validation_boundary"

  release:
    - "redundant_log_lines"
    - "temporary_debug_context"

  human_review:
    required: false
```

---

## 7. Memory Retention Decision

A memory retention decision records the outcome of applying one or more forgetting rules.

It should document:

* what was evaluated,
* which rule was applied,
* what action was taken,
* what was preserved,
* what was released,
* and where the result was moved.

Example:

```yaml
memory_retention_decision:
  id: "mrd-2026-06-18-001"
  protocol_version: "0.2.0-candidate"
  source_rule: "forget-rule-001"

  evaluated_memory:
    type: "raw_trace"
    summary: "GitHub Actions steps indentation failure"
    source_layer: "working_memory"

  decision:
    action: "convert_to_recurrence_rule"
    destination_layer: "long_term_memory"
    reason:
      - "The failure pattern is likely to recur."
      - "Raw log lines are no longer needed."
      - "The prevention rule is useful for future workflow editing."

  preserved:
    - "steps must be nested under jobs.<job_id>"
    - "runs-on and steps must be sibling keys inside the same job"

  released:
    - "full CI traceback"
    - "temporary troubleshooting chatter"

  human_review:
    required: false
```

---

## 8. Evaluation Criteria

Executable forgetting rules should evaluate memory using the following criteria.

### 8.1 Relevance

How relevant is the memory item to the current or future task?

Suggested values:

```text
low
medium
high
critical
```

---

### 8.2 Recurrence

How likely is this pattern to appear again?

Suggested values:

```text
none
low
medium
high
systemic
```

---

### 8.3 Safety Impact

Could forgetting or retaining this memory affect safety, governance, or human responsibility?

Suggested values:

```text
low
medium
high
critical
```

---

### 8.4 Future Action Value

Will this memory guide future useful action?

Suggested values:

```text
low
medium
high
critical
```

---

### 8.5 Human Sensitivity

Does this memory involve identity, legal, political, financial, medical, or safety-critical judgment?

Suggested values:

```text
none
low
medium
high
critical
```

---

## 9. Default Action Matrix

The following matrix gives default guidance.

| Condition                                 | Recommended Action         |
| ----------------------------------------- | -------------------------- |
| Low relevance + low recurrence            | forget                     |
| Low relevance + possible historical value | archive                    |
| Medium recurrence + low raw value         | compress                   |
| High recurrence + clear prevention value  | convert_to_recurrence_rule |
| Durable preference or core architecture   | promote_to_long_term       |
| Repeated behavioral preference            | move_to_implicit_layer     |
| High-impact or sensitive judgment         | return_to_human_review     |
| Obsolete assumption                       | downgrade_weight or forget |
| Resolved temporary detail                 | compress or release        |

---

## 10. Human Review Boundary

Executable forgetting must not silently erase memory that affects high-impact judgment.

Human review is required when a memory item relates to:

* irreversible decisions,
* safety boundary changes,
* legal interpretation,
* financial consequences,
* identity-sensitive judgment,
* political or military interpretation,
* value allocation,
* authorship or attribution,
* external system action,
* or governance-level decisions.

Example:

```yaml
human_review:
  required: true
  required_for:
    - "value_allocation"
    - "authorship_attribution"
    - "irreversible_decision"
  default_action: "pause_and_return_to_human"
```

---

## 11. Relation to v0.1 Memory Layers

Executable Forgetting Rules operate across the four memory layers.

```text
Short-Term Memory
  → forget, compress, or archive after use

Working Memory
  → compress, archive, downgrade, or promote

Long-Term Memory
  → preserve, review, downgrade, or convert to principle

Implicit Breathing Layer
  → receive compressed behavioral tendencies
```

---

## 12. Relation to Trace Compaction

Trace Compaction is a special case of executable forgetting.

It turns raw traces into reusable structure.

```text
raw_trace
  → recurrence_rule
  → validation_gate
  → safety_boundary
```

This avoids preserving heavy logs while retaining future prevention value.

---

## 13. Relation to Memory Weight Architecture

Executable Forgetting Rules prepare the protocol for deeper memory weighting.

A memory item may be:

* promoted when recurrence and future action value are high,
* downgraded when relevance decreases,
* compressed when raw detail is excessive,
* or moved to implicit behavior when it should guide posture rather than explicit recall.

This makes memory weight operational rather than merely descriptive.

---

## 14. Minimal v0.2 Scope

Version `v0.2.0-candidate` introduces:

* forgetting rule schema,
* memory retention decision schema,
* example forgetting rule,
* example retention decision,
* validation integration,
* and documentation for executable memory metabolism.

This version does not yet define:

* distributed forgetting across multiple agents,
* cryptographic retention proofs,
* royalty-sensitive retention logic,
* or full multi-wing memory governance.

Those may be added in later versions.

---

## 15. Suggested Files

```text
docs/executable-forgetting-rules.md

schemas/forgetting-rule.schema.json
schemas/memory-retention-decision.schema.json

examples/forgetting-rule.example.yaml
examples/memory-retention-decision.example.yaml
```

Validation should be added to:

```text
scripts/validate_examples.py
```

---

## 16. Design Philosophy

```text
Forgetting is not disappearance.
Forgetting is transformation.

A memory item should not remain heavy forever.
It should breathe, compress, circulate, or return to human review.

Raw traces should not become permanent noise.
They should become recurrence prevention.

Implicit memory should not become hidden authority.
It should remain bounded by human review.
```

---

## 17. Summary

Executable Forgetting Rules make AI memory metabolism actionable.

They allow AI systems to decide:

* what to forget,
* what to compress,
* what to archive,
* what to promote,
* what to downgrade,
* what to move into implicit behavior,
* and what to return to human review.

This is the next step in Kazene Memory Breathing Protocol.

v0.1 defined memory breathing.

v0.2 makes forgetting executable.
