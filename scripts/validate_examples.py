#!/usr/bin/env python3
"""
Validate YAML examples against JSON Schemas for
Kazene Memory Breathing Protocol.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Memory Breathing Record",
        "schema": ROOT / "schemas" / "memory-breathing-record.schema.json",
        "example": ROOT / "examples" / "memory-breathing-record.example.yaml",
    },
    {
        "name": "Forgetting Rule",
        "schema": ROOT / "schemas" / "forgetting-rule.schema.json",
        "example": ROOT / "examples" / "forgetting-rule.example.yaml",
    },
    {
        "name": "Memory Retention Decision",
        "schema": ROOT / "schemas" / "memory-retention-decision.schema.json",
        "example": ROOT / "examples" / "memory-retention-decision.example.yaml",
    },
    {
        "name": "Memory Weight Record",
        "schema": ROOT / "schemas" / "memory-weight-record.schema.json",
        "example": ROOT / "examples" / "memory-weight-record.example.yaml",
    },
    {
        "name": "Structural Rumination Record",
        "schema": ROOT / "schemas" / "structural-rumination-record.schema.json",
        "example": ROOT / "examples" / "structural-rumination-record.example.yaml",
    },
    {
        "name": "Trace Compaction Record",
        "schema": ROOT / "schemas" / "trace-compaction-record.schema.json",
        "example": ROOT / "examples" / "trace-compaction-record.example.yaml",
    },
    {
        "name": "Multi-Wing Memory Route",
        "schema": ROOT / "schemas" / "multi-wing-memory-route.schema.json",
        "example": ROOT / "examples" / "multi-wing-memory-route.example.yaml",
    },
    {
        "name": "Memory Wing Boundary",
        "schema": ROOT / "schemas" / "memory-wing-boundary.schema.json",
        "example": ROOT / "examples" / "memory-wing-boundary.example.yaml",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> Any:
    """Load a YAML file."""
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_target(name: str, schema_path: Path, example_path: Path) -> None:
    """Validate one YAML example against one JSON Schema."""
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    if not example_path.exists():
        raise FileNotFoundError(f"Example file not found: {example_path}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    jsonschema.validate(instance=example, schema=schema)

    print(f"[ok] {name} example is valid")


def main() -> None:
    """Run all validations."""
    for target in VALIDATION_TARGETS:
        validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )


if __name__ == "__main__":
    main()

