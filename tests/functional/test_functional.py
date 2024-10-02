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

def evaluate(reference_json: Dict[str, Any], xd: Excalidraw) -> None:
    generated_json = json.loads(xd.json())
    comparator = ExcalidrawComparator(
        ignore_fields={'version', 'versionNonce', 'seed'}
    )

    assert comparator.compare(
        reference_json,
        generated_json
    ), "Generated JSON does not match the reference JSON"

def test_arrow_star(reference_json: Dict[str, Any]) -> None:
    xd = Excalidraw()

    start_element = xd.ellipse().position(-50, -50).size(100, 100).label(xd.text().content("center"))

    for angle in range(0, 360, 30):
        x = 300 * math.cos(angle * math.pi / 180)
        y = 300 * math.sin(angle * math.pi / 180)
        end_element = xd.rectangle().position(x - 50, y - 25).size(100, 50).label(xd.text().content(str(angle))).edges('round')
        xd.arrow().bind(start_element, end_element)

    evaluate(reference_json, xd)

def test_texts(reference_json: Dict[str, Any]) -> None:
    xd = Excalidraw()
    xd.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000")
    xd.text().position(100, 100).content("Hello, Excalifont!").fontsize(40).font("excalifont").align("center").baseline("top").spacing(1.5).color("#0000FF").autoresize(True)

    evaluate(reference_json, xd)

def test_labels(reference_json: Dict[str, Any]) -> None:
    xd = Excalidraw()
    label = xd.text().content("Hello, World!").fontsize("M").font("Hand-drawn").spacing(1.5).color("#FF0000")
    xd.rectangle().position(10, 20).size(300, 100).label(label)

    evaluate(reference_json, xd)


def test_sandbox(reference_json: Dict[str, Any]) -> None:
    xd = Excalidraw()

    def cross(center: tuple[float, float], color: str) -> None:
        x, y = center
        xd.line().plot([[x - 20, y], [x + 20, y]]).color(color)
        xd.line().plot([[x, y - 20], [x, y + 20]]).color(color)

    cross([0, 0], '#ff0000')
    cross([100, 50], '#00ff00')

    xd.ellipse().position(0, 0).size(50, 50)
    xd.ellipse().position(0, 0).size(100, 100).fade(50)

    xd.text().position(0, 0).content('Center').fontsize('L').align('center').baseline('middle').rotate(3.14 / 4)

    evaluate(reference_json, xd)
