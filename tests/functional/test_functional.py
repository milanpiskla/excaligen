import pytest
import json
import os
from typing import Dict, Any
from src.Excaligen import Excaligen
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

def evaluate(reference_json: Dict[str, Any], xg: Excaligen, request: FixtureRequest) -> None:
    generated_json = json.loads(xg.json())
    comparator = ExcalidrawComparator(
        ignore_fields={'version', 'versionNonce', 'seed', 'groupIds'}
    )

    # Compare the generated JSON with the reference JSON
    if not comparator.compare(reference_json, generated_json):
        # Write the generated JSON to a file
        test_name = request.node.name
        generated_dir = os.path.join(os.path.dirname(__file__), 'generated')
        os.makedirs(generated_dir, exist_ok=True)
        generated_file = os.path.join(generated_dir, f"{test_name}_generated_bad.json")
        with open(generated_file, 'w', encoding='utf-8') as f:
            f.write(xg.json())
        assert False, f"Generated JSON does not match the reference JSON. See '{generated_file}' for details."

def test_arrow_star(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()

    start_element = xg.ellipse().center(0, 0).size(100, 100).label(xg.text().content("center"))

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = 300 * math.cos(radians)
        y = 300 * math.sin(radians)
        end_element = xg.rectangle().center(x, y).size(100, 50).label(xg.text().content(str(angle))).roudness('round')
        xg.arrow().bind(start_element, end_element)

    evaluate(reference_json, xg, request)

def test_texts(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()
    xg.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000")
    xg.text().position(100, 100).content("Hello, Excalifont!").fontsize(40).font("excalifont").align("center").baseline("top").spacing(1.5).color("#0000FF").autoresize(True)

    evaluate(reference_json, xg, request)

def test_labels(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()
    label = xg.text().content("Hello, World!").fontsize("M").font("Hand-drawn").spacing(1.5).color("#FF0000")
    xg.rectangle().position(10, 20).size(300, 100).label(label)

    evaluate(reference_json, xg, request)

def test_sandbox(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()

    def cross(center: tuple[float, float], color: str) -> None:
        x, y = center
        xg.line().points([[x - 20, y], [x + 20, y]]).color(color)
        xg.line().points([[x, y - 20], [x, y + 20]]).color(color)

    cross([0, 0], '#ff0000')
    cross([100, 50], '#00ff00')

    xg.ellipse().position(0, 0).size(50, 50)
    xg.ellipse().position(0, 0).size(100, 100).opacity(50)

    xg.text().position(0, 0).content('Center').fontsize('L').align('center').baseline('middle').rotate(3.14 / 4)

    evaluate(reference_json, xg, request)

def test_lines(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()

    xg.line().color('#00FF00').points([(0, 0), (100, 50)]).sloppiness(2).stroke('solid')
    xg.line().color('#0000FF').points([(0, 0), (100, -50)]).sloppiness(0).stroke('dotted')
    xg.line().color('#FF0000').points([(0, 0), (-100, -50), (-100, 50)]).sloppiness(0).stroke('dashed').roundness('round')

    evaluate(reference_json, xg, request)

def test_arrow_arc(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()

    RADIUS = 300
    elements = []

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = RADIUS * math.cos(radians)
        y = RADIUS * math.sin(radians)

        #rect = xg.rectangle().center(x, y).size(80, 60)
        rect = xg.ellipse().center(x, y).size(80, 60)
        elements.append(rect)

    start_element = elements[0]
    for i in range(1, len(elements)):
        xg.arrow().arc(radius=RADIUS).bind(start_element, elements[i])
        start_element = elements[i]

    evaluate(reference_json, xg, request)

def test_arrow_hspline(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()
    start_element = xg.rectangle().center(-150, -150).size(100, 100).label(xg.text().content("center 1"))
    end_element = xg.rectangle().center(150, 150).size(100, 100).label(xg.text().content("center 2"))
    xg.arrow().hspline().bind(start_element, end_element)
    
    evaluate(reference_json, xg, request)

def test_group(reference_json: Dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()
    rect = xg.rectangle().center(0, 0).size(100, 100).label(xg.text().content("Group part"))
    ellipse = xg.ellipse().center(150, 150).size(100, 100).label(xg.text().content("Group part"))
    diamond = xg.diamond().center(-150, -150).size(100, 100).label(xg.text().content("Not Group"))
    xg.group(rect, ellipse)
    
    evaluate(reference_json, xg, request)
