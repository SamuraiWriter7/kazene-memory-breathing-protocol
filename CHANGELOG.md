# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-release style during early protocol development.

---

## [v0.5.0-candidate] - 2026-06-18

### Added

* Added v0.5 documentation:

  * `docs/multi-wing-memory-wing-integration.md`

* Added multi-wing memory route schema:

  * `schemas/multi-wing-memory-route.schema.json`

* Added memory wing boundary schema:

  * `schemas/memory-wing-boundary.schema.json`

* Added multi-wing memory route example:

  * `examples/multi-wing-memory-route.example.yaml`

* Added memory wing boundary example:

  * `examples/memory-wing-boundary.example.yaml`

* Updated validation script to include v0.5 targets:

  * `scripts/validate_examples.py`

---

### Defined

* Defined **Multi-Wing Memory Wing Integration** as the fifth core layer of Kazene Memory Breathing Protocol.

* Defined multi-wing memory routing as a structured event for moving memory between specialized AI wings.

* Defined `Multi-Wing Memory Route` fields:

  * source wing,
  * destination wing,
  * memory item,
  * routing reason,
  * memory weight,
  * trace sensitivity,
  * allowed action,
  * routing purpose,
  * constraints,
  * human review,
  * routing result.

* Defined `Memory Wing Boundary` fields:

  * wing,
  * role,
  * allowed inputs,
  * allowed outputs,
  * routing permissions,
  * forgetting permissions,
  * prohibited actions,
  * human review triggers,
  * default boundary action,
  * memory scope.

* Defined supported wing types:

  * `human_interface_wing`
  * `planning_wing`
  * `research_wing`
  * `coding_wing`
  * `validation_wing`
  * `structural_rumination_wing`
  * `trace_compaction_wing`
  * `memory_weight_wing`
  * `forgetting_wing`
  * `safety_review_wing`
  * `governance_wing`
  * `royalty_trace_wing`
  * `implicit_breathing_wing`
  * `archive_wing`

* Defined multi-wing memory circulation flow:

```text
validation_wing
  → structural_rumination_wing
  → trace_compaction_wing
  → memory_weight_wing
  → forgetting_wing
  → long_term_memory / human_review
```

---

### Validation

* Added validation targets:

  * `Multi-Wing Memory Route`
  * `Memory Wing Boundary`

* Validation now checks:

  * `memory-breathing-record.example.yaml`
  * `forgetting-rule.example.yaml`
  * `memory-retention-decision.example.yaml`
  * `memory-weight-record.example.yaml`
  * `structural-rumination-record.example.yaml`
  * `trace-compaction-record.example.yaml`
  * `multi-wing-memory-route.example.yaml`
  * `memory-wing-boundary.example.yaml`

* Confirmed GitHub Actions validation passes with v0.5 schema-example integration.

---

### Structural Notes

This release extends the protocol from single-agent memory metabolism into multi-wing memory circulation.

The protocol now supports the following flow:

```text
memory item
  → wing-specific boundary check
  → memory weight evaluation
  → trace sensitivity check
  → declared routing purpose
  → cross-wing route
  → destination wing action
  → human review if boundary is crossed
```

This prevents memory from becoming one uncontrolled shared context across multiple AI agents.

Each wing can remember only what it needs, route only with purpose, and return high-impact boundary cases to human review.

---

### Status

`v0.5.0-candidate` establishes Multi-Wing Memory Wing Integration as the fifth core layer of Kazene Memory Breathing Protocol.

`v0.1.0-candidate` defined memory breathing.

`v0.2.0-candidate` made forgetting executable.

`v0.3.0-candidate` gave memory weight.

`v0.4.0-candidate` turned failure into structure.

`v0.5.0-candidate` lets memory circulate across wings.

---

## [v0.4.0-candidate] - 2026-06-18

### Added

* Added v0.4 documentation:

  * `docs/structural-rumination-trace-compaction-integration.md`

* Added structural rumination record schema:

  * `schemas/structural-rumination-record.schema.json`

* Added trace compaction record schema:

  * `schemas/trace-compaction-record.schema.json`

* Added structural rumination record example:

  * `examples/structural-rumination-record.example.yaml`

* Added trace compaction record example:

  * `examples/trace-compaction-record.example.yaml`

* Updated validation script to include v0.4 targets:

  * `scripts/validate_examples.py`

---

### Defined

* Defined **Structural Rumination / Trace Compaction Integration** as the fourth core layer of Kazene Memory Breathing Protocol.

* Defined structural rumination as a process for turning failure into reusable structure.

* Defined trace compaction as a process for reducing raw traces while preserving recurrence prevention value.

* Defined failure-to-structure transformation flow:

```text
raw failure
  → structural rumination
  → trace compaction
  → memory weight evaluation
  → forgetting or retention decision
  → recurrence prevention
```

---

### Validation

* Added validation targets:

  * `Structural Rumination Record`
  * `Trace Compaction Record`

* Confirmed GitHub Actions validation passes with v0.4 schema-example integration.

---

### Status

`v0.4.0-candidate` establishes Structural Rumination / Trace Compaction Integration as the fourth core layer of Kazene Memory Breathing Protocol.

---

## [v0.3.0-candidate] - 2026-06-18

### Added

* Added v0.3 documentation:

  * `docs/memory-weight-architecture-integration.md`

* Added memory weight record schema:

  * `schemas/memory-weight-record.schema.json`

* Added memory weight record example:

  * `examples/memory-weight-record.example.yaml`

* Updated validation script to include v0.3 target:

  * `scripts/validate_examples.py`

---

### Defined

* Defined **Memory Weight Architecture Integration** as an operational layer for AI memory routing.

* Defined memory weight as a routing mechanism rather than a passive label.

* Defined memory weight levels:

  * `low`
  * `medium`
  * `high`
  * `critical`

* Defined memory evaluation criteria:

  * importance,
  * recurrence,
  * future action value,
  * safety impact,
  * human preference relevance,
  * trace value,
  * freshness.

---

### Validation

* Added validation target:

  * `Memory Weight Record`

* Confirmed GitHub Actions validation passes with v0.3 schema-example integration.

---

### Status

`v0.3.0-candidate` establishes Memory Weight Architecture Integration as the third core layer of Kazene Memory Breathing Protocol.

---

## [v0.2.0-candidate] - 2026-06-18

### Added

* Added v0.2 documentation:

  * `docs/executable-forgetting-rules.md`

* Added executable forgetting rule schema:

  * `schemas/forgetting-rule.schema.json`

* Added memory retention decision schema:

  * `schemas/memory-retention-decision.schema.json`

* Added executable forgetting rule example:

  * `examples/forgetting-rule.example.yaml`

* Added memory retention decision example:

  * `examples/memory-retention-decision.example.yaml`

* Updated validation script to include v0.2 targets:

  * `scripts/validate_examples.py`

---

### Defined

* Defined **Executable Forgetting Rules** as structured, auditable rules for AI memory metabolism.

* Defined forgetting as controlled transformation rather than simple deletion.

* Defined supported forgetting actions:

  * `forget`
  * `compress`
  * `archive`
  * `downgrade_weight`
  * `promote_to_long_term`
  * `move_to_implicit_layer`
  * `convert_to_recurrence_rule`
  * `return_to_human_review`

* Defined **Memory Retention Decision** records as outcomes of applying executable forgetting rules.

---

### Validation

* Added validation targets:

  * `Forgetting Rule`
  * `Memory Retention Decision`

* Confirmed GitHub Actions validation passes with v0.2 schema-example integration.

---

### Fixed During Candidate Formation

* Fixed YAML parent-key null issue where nested fields leaked outside `forgetting_rule`.

* Fixed schema-example hierarchy mismatch in `examples/forgetting-rule.example.yaml`.

* Confirmed that many simultaneous `additionalProperties` errors usually indicate YAML indentation or parent-child hierarchy collapse.

---

### Status

`v0.2.0-candidate` established executable forgetting as the second core layer of Kazene Memory Breathing Protocol.

---

## [v0.1.0-candidate] - 2026-06-18

### Added

* Added initial documentation:

  * `docs/kazene-memory-breathing-protocol.md`

* Added initial JSON Schema:

  * `schemas/memory-breathing-record.schema.json`

* Added initial YAML example:

  * `examples/memory-breathing-record.example.yaml`

* Added validation script:

  * `scripts/validate_examples.py`

* Added GitHub Actions workflow:

  * `.github/workflows/validate-examples.yml`

---

### Defined

* Defined the core concept of AI memory metabolism.

* Defined the Four-Layer Memory Breathing Model:

  * Short-Term Memory
  * Working Memory
  * Long-Term Memory
  * Implicit Breathing Layer

* Defined core protocol functions:

  * memory weighting,
  * forgetting policy,
  * trace compaction,
  * implicit behavioral influence,
  * human review boundary.

---

### Validation

* Added YAML example validation against JSON Schema.

* Added GitHub Actions validation for changes under:

  * `schemas/**`
  * `examples/**`
  * `scripts/validate_examples.py`
  * `.github/workflows/validate-examples.yml`

---

### Fixed During Candidate Formation

* Fixed GitHub Actions workflow hierarchy issue where `steps` could be placed outside the job definition.

* Fixed Python script corruption risks involving dunder identifiers:

  * `__future__`
  * `__file__`
  * `__name__`

* Fixed schema-example mismatch around `implicit_breathing_layer`.

---

### Status

`v0.1.0-candidate` established the first working core of Kazene Memory Breathing Protocol.
