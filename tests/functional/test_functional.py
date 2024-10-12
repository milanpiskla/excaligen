import pytest
import json
import os
from typing import Dict, Any
from src.Excalidraw import Excalidraw
from tests.functional.ExcalidrawComparator import ExcalidrawComparator
from pytest import FixtureRequest

import math

@pytest.fixture
def reference_json(request: FixtureRequest) -> Dict[str, Any]:
    """
    Load the reference JSON file for the test.
    The name of the reference file is derived from the test name.
    """
    test_name = request.node.name
    fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
    reference_file = os.path.join(fixture_dir, f"{test_name}.excalidraw")
    with open(reference_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluate(reference_json: Dict[str, Any], xd: Excalidraw, request: FixtureRequest) -> None:
    generated_json = json.loads(xd.json())
    comparator = ExcalidrawComparator(
        ignore_fields={'version', 'versionNonce', 'seed'}
    )

    # Compare the generated JSON with the reference JSON
    if not comparator.compare(reference_json, generated_json):
        # Write the generated JSON to a file
        test_name = request.node.name
        generated_dir = os.path.join(os.path.dirname(__file__), 'generated')
        os.makedirs(generated_dir, exist_ok=True)
        generated_file = os.path.join(generated_dir, f"{test_name}_generated_bad.json")
        with open(generated_file, 'w', encoding='utf-8') as f:
            f.write(xd.json())
        assert False, f"Generated JSON does not match the reference JSON. See '{generated_file}' for details."

def test_arrow_star(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xd = Excalidraw()

    start_element = xd.ellipse().center(0, 0).size(100, 100).label(xd.text().content("center"))

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = 300 * math.cos(radians)
        y = 300 * math.sin(radians)
        end_element = xd.rectangle().center(x, y).size(100, 50).label(xd.text().content(str(angle))).roudness('round')
        xd.arrow().bind(start_element, end_element)

    evaluate(reference_json, xd, request)

def test_texts(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xd = Excalidraw()
    xd.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000")
    xd.text().position(100, 100).content("Hello, Excalifont!").fontsize(40).font("excalifont").align("center").baseline("top").spacing(1.5).color("#0000FF").autoresize(True)

    evaluate(reference_json, xd, request)

def test_labels(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xd = Excalidraw()
    label = xd.text().content("Hello, World!").fontsize("M").font("Hand-drawn").spacing(1.5).color("#FF0000")
    xd.rectangle().position(10, 20).size(300, 100).label(label)

    evaluate(reference_json, xd, request)

def test_sandbox(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xd = Excalidraw()

    def cross(center: tuple[float, float], color: str) -> None:
        x, y = center
        xd.line().points([[x - 20, y], [x + 20, y]]).color(color)
        xd.line().points([[x, y - 20], [x, y + 20]]).color(color)

    cross([0, 0], '#ff0000')
    cross([100, 50], '#00ff00')

    xd.ellipse().position(0, 0).size(50, 50)
    xd.ellipse().position(0, 0).size(100, 100).opacity(50)

    xd.text().position(0, 0).content('Center').fontsize('L').align('center').baseline('middle').rotate(3.14 / 4)

    evaluate(reference_json, xd, request)

def test_lines(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xd = Excalidraw()

    xd.line().color('#00FF00').points([(0, 0), (100, 50)]).sloppiness(2).stroke('solid')
    xd.line().color('#0000FF').points([(0, 0), (100, -50)]).sloppiness(0).stroke('dotted')
    xd.line().color('#FF0000').points([(0, 0), (-100, -50), (-100, 50)]).sloppiness(0).stroke('dashed').roundness('round')

    evaluate(reference_json, xd, request)
