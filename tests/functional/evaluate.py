"""
Description: Evaluate the generated JSON against the reference JSON.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
import json
import os

from src.Excaligen import Excaligen
from .ExcalidrawComparator import ExcalidrawComparator
from pytest import FixtureRequest

@pytest.fixture
def reference_json(request: FixtureRequest) -> dict[str, any]:
    """
    Load the reference JSON file for the test.
    The name of the reference file is derived from the test name.
    """
    test_name = request.node.name
    fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
    reference_file = os.path.join(fixture_dir, f"{test_name}.excalidraw")
    with open(reference_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluate(reference_json: dict[str, any], xg: Excaligen, request: FixtureRequest) -> None:
    generated_json = json.loads(xg.json())
    comparator = ExcalidrawComparator(
        ignore_fields={'version', 'versionNonce', 'seed', 'groupIds', 'frameId', 'containerId'}
    )

    # Compare the generated JSON with the reference JSON
    if not comparator.compare(reference_json, generated_json):
        # Write the generated JSON to a file
        test_name = request.node.name
        generated_dir = os.path.join(os.path.dirname(__file__), 'generated')
        os.makedirs(generated_dir, exist_ok=True)
        generated_file = os.path.join(generated_dir, f"{test_name}_generated_bad.excalidraw")
        with open(generated_file, 'w', encoding='utf-8') as f:
            f.write(xg.json())
        assert False, f"Generated JSON does not match the reference JSON. See '{generated_file}' for details."
