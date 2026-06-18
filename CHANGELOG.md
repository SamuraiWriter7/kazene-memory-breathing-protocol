# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-release style during early protocol development.

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

* Defined `Structural Rumination Record` fields:

  * source event,
  * failure observation,
  * affected layer,
  * structural cause,
  * rumination,
  * recurrence pattern,
  * reusable lesson,
  * correction,
  * output,
  * release,
  * human review.

* Defined `Trace Compaction Record` fields:

  * source trace,
  * preserved elements,
  * transformed structures,
  * released elements,
  * compaction result,
  * active context reduction,
  * recurrence prevention value,
  * recommended memory weight,
  * human review.

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

* Validation now checks:

  * `memory-breathing-record.example.yaml`
  * `forgetting-rule.example.yaml`
  * `memory-retention-decision.example.yaml`
  * `memory-weight-record.example.yaml`
  * `structural-rumination-record.example.yaml`
  * `trace-compaction-record.example.yaml`

* Confirmed GitHub Actions validation passes with v0.4 schema-example integration.

---

### Structural Notes

This release strengthens the protocol’s ability to metabolize failure.

The protocol now supports the following flow:

```text
failure observation
  → structural cause extraction
  → recurrence pattern extraction
  → reusable lesson
  → confirmed correction
  → trace compaction
  → long-term prevention structure
```

This allows validation errors, YAML hierarchy failures, schema-example drift, Python syntax corruption, and workflow breakdowns to become reusable memory structures instead of repeated debugging burden.

---

### Status

`v0.4.0-candidate` establishes Structural Rumination / Trace Compaction Integration as the fourth core layer of Kazene Memory Breathing Protocol.

`v0.1.0-candidate` defined memory breathing.

`v0.2.0-candidate` made forgetting executable.

`v0.3.0-candidate` gave memory weight.

`v0.4.0-candidate` turns failure into structure.

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

* Defined memory routing fields:

  * retention priority,
  * destination layer,
  * recommended action,
  * review cycle,
  * created structures.

* Defined retention priorities:

  * `release`
  * `temporary`
  * `retain`
  * `promote`
  * `protect`
  * `review_required`

* Defined review cycles:

  * `none`
  * `daily`
  * `weekly`
  * `monthly`
  * `quarterly`
  * `release_cycle`
  * `on_major_change`
  * `human_requested`

---

### Validation

* Added validation target:

  * `Memory Weight Record`

* Validation now checks:

  * `memory-breathing-record.example.yaml`
  * `forgetting-rule.example.yaml`
  * `memory-retention-decision.example.yaml`
  * `memory-weight-record.example.yaml`

* Confirmed GitHub Actions validation passes with v0.3 schema-example integration.

---

### Structural Notes

This release connects memory weighting with executable forgetting.

The protocol now supports the following flow:

```text
memory item
  → weight evaluation
  → retention priority
  → memory layer routing
  → recommended action
  → review cycle
  → forgetting or preservation decision
```

This allows recurring technical failures, durable preferences, trace-sensitive records, and safety boundaries to receive different memory treatment.

---

### Status

`v0.3.0-candidate` establishes Memory Weight Architecture Integration as the third core layer of Kazene Memory Breathing Protocol.

`v0.1.0-candidate` defined memory breathing.

`v0.2.0-candidate` made forgetting executable.

`v0.3.0-candidate` gives memory weight.

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

* Defined how raw traces can be transformed into:

  * recurrence rules,
  * validation gates,
  * safety boundaries,
  * implicit behavioral influences,
  * archive records,
  * or human review records.

---

### Validation

* Added validation targets for:

  * `Forgetting Rule`
  * `Memory Retention Decision`

* Validation now checks:

  * `memory-breathing-record.example.yaml`
  * `forgetting-rule.example.yaml`
  * `memory-retention-decision.example.yaml`

* Confirmed GitHub Actions validation passes with v0.2 schema-example integration.

---

### Fixed During Candidate Formation

* Fixed YAML parent-key null issue where nested fields leaked outside `forgetting_rule`.

* Fixed schema-example hierarchy mismatch in `examples/forgetting-rule.example.yaml`.

* Confirmed that many simultaneous `additionalProperties` errors usually indicate YAML indentation or parent-child hierarchy collapse.

* Reinforced recurrence pattern:

  * parent keys must contain their intended child fields,
  * nested YAML objects must remain indented under their parent,
  * schema-required fields must map directly to example structure.

---

### Structural Notes

This release strengthens the protocol’s own memory metabolism.

The candidate process produced useful recurrence patterns:

* GitHub Actions hierarchy must remain strict:

  * `on`
  * `jobs`
  * `job`
  * `steps`

* Python dunder identifiers must be protected:

  * `__future__`
  * `__file__`
  * `__name__`

* Schema and example files must evolve together.

* If JSON Schema reports many unexpected root-level fields, inspect YAML indentation first.

* If parent keys are parsed as `null`, child fields have likely leaked out of the intended object.

---

### Status

`v0.2.0-candidate` established executable forgetting as the second core layer of Kazene Memory Breathing Protocol.

`v0.1.0-candidate` defined memory breathing.

`v0.2.0-candidate` made forgetting executable.

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

* Defined the transition from:

  * accumulative intelligence,
  * to breathing intelligence.

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

* Aligned example YAML with schema-required fields:

  * `influences`
  * `expression_mode`
  * `constraints`

---

### Structural Notes

This release produced several useful recurrence patterns for future protocol work:

* GitHub Actions requires strict hierarchy:

  * `on`
  * `jobs`
  * `job`
  * `steps`

* Python scripts copied through rendered Markdown must preserve dunder identifiers.

* Schema and example files must evolve together.

* Conceptually valid examples should not be weakened to fit an outdated schema when the schema should evolve instead.

---

### Status

`v0.1.0-candidate` established the first working core of Kazene Memory Breathing Protocol.

This release focused on the minimum viable memory breathing record and validation path.

