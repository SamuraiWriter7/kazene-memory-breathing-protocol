# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-release style during early protocol development.

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

`v0.2.0-candidate` establishes executable forgetting as the second core layer of Kazene Memory Breathing Protocol.

`v0.1.0-candidate` defined memory breathing.

`v0.2.0-candidate` makes forgetting executable.

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
