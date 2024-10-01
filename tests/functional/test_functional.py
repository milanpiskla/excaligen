import pytest
import json
import os
from typing import Dict, Any
from src.Excalidraw import Excalidraw
from tests.functional.ExcalidrawComparator import ExcalidrawComparator

import math

@pytest.fixture
def reference_json(request) -> Dict[str, Any]:
    """
    Load the reference JSON file for the test.
    The name of the reference file is derived from the test name.
    """
    test_name = request.node.name
    fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
    reference_file = os.path.join(fixture_dir, f"{test_name}.excalidraw")
    with open(reference_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def test_arrow_star(reference_json: Dict[str, Any]) -> None:
    """
    Functional test comparing generated Excalidraw JSON to a reference JSON.
    """
    xd = Excalidraw()

    start_element = xd.ellipse().position(-50, -50).size(100, 100).label(xd.text().content("center"))

    for angle in range(0, 360, 30):
        x = 300 * math.cos(angle * math.pi / 180)
        y = 300 * math.sin(angle * math.pi / 180)
        end_element = xd.rectangle().position(x - 50, y - 25).size(100, 50).label(xd.text().content(str(angle))).edges('round')
        xd.arrow().bind(start_element, end_element)

    # Generate JSON from the Excalidraw object
    generated_json = json.loads(xd.json())

    # Create a comparator instance with fields to ignore
    comparator = ExcalidrawComparator(
        ignore_fields={'version', 'versionNonce', 'seed'}
    )

    # Compare the generated JSON with the reference JSON
    assert comparator.compare(
        reference_json,
        generated_json
    ), "Generated JSON does not match the reference JSON"

def test_texts(reference_json: Dict[str, Any]) -> None:
    xd = Excalidraw()
    xd.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000")
    xd.text().position(100, 100).content("Hello, Excalifont!").fontsize(40).font("excalifont").align("center").baseline("top").spacing(1.5).color("#0000FF").autoresize(True)
    xd.save('texts.excalidraw')

    generated_json = json.loads(xd.json())
    comparator = ExcalidrawComparator(
        ignore_fields={'version', 'versionNonce', 'seed'}
    )
    assert comparator.compare(
        reference_json,
        generated_json
    ), "Generated JSON does not match the reference JSON"
