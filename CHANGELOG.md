# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-release style during early protocol development.

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

`v0.1.0-candidate` establishes the first working core of Kazene Memory Breathing Protocol.

This release is focused on the minimum viable memory breathing record and validation path.

Future versions may expand toward executable forgetting rules, trace layer integration, Mythos tuning, and multi-agent memory circulation.
