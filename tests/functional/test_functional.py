"""
Description: Functional tests for various elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.DiagramBuilder import DiagramBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_grid(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    xg.grid(50, 10, True)
    xg.rectangle().center(0, 0).size(100, 100)
    
    evaluate(reference_json, xg, request)

def test_view_background(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    xg.grid(50, 10, True)
    xg.background('#0000FF')
    xg.rectangle().center(0, 0).size(100, 100)
    
    evaluate(reference_json, xg, request)

def test_texts(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    xg.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000")
    xg.text().position(100, 100).content("Hello, Excalifont!").fontsize(40).font("excalifont").align("center").baseline("top").spacing(1.5).color("#0000FF").autoresize(True)

    evaluate(reference_json, xg, request)

def test_text_anchors(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    def cross(center: tuple[float, float], color: str) -> None:
        x, y = center
        xg.line().points([[x - 20, y], [x + 20, y]]).color(color)
        xg.line().points([[x, y - 20], [x, y + 20]]).color(color)

    xg = DiagramBuilder()
    x = 42.0
    y = 0.0

    for h_align in ["left", "center", "right"]:
        for v_align in ["top", "middle", "bottom"]:
            cross((x, y), 'red')
            xg.text().anchor(x, y, h_align, v_align).content(f"{h_align}-{v_align}").fontsize("M").font("Hand-drawn").color("black")
            y += 60.0

    evaluate(reference_json, xg, request)

def test_labels(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    label = xg.text().content("Hello, World!").fontsize("M").font("Hand-drawn").spacing(1.5).color("#FF0000")
    xg.rectangle().position(10, 20).size(300, 100).label(label)

    evaluate(reference_json, xg, request)

def test_plain_label(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    xg.rectangle().label("Hello")

    evaluate(reference_json, xg, request)

def test_sandbox(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()

    def cross(center: tuple[float, float], color: str) -> None:
        x, y = center
        xg.line().points([[x - 20, y], [x + 20, y]]).color(color)
        xg.line().points([[x, y - 20], [x, y + 20]]).color(color)

    cross((0, 0), '#ff0000')
    cross((100, 50), '#00ff00')

    xg.ellipse().position(0, 0).size(50, 50)
    xg.ellipse().position(0, 0).size(100, 100).opacity(50)

    xg.text().position(0, 0).content('Center').fontsize('L').align('center').baseline('middle').rotate(3.14 / 4)

    evaluate(reference_json, xg, request)

def test_lines(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()

    xg.line().color('#00FF00').points([(0, 0), (100, 50)]).sloppiness(2).stroke('solid')
    xg.line().color('#0000FF').points([(0, 0), (100, -50)]).sloppiness(0).stroke('dotted')
    xg.line().color('#FF0000').points([(0, 0), (-100, -50), (-100, 50)]).sloppiness(0).stroke('dashed').roundness('round')

    evaluate(reference_json, xg, request)

def test_closed_lines_background(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()

    xg.line().color('black').points([(0, 0), (100, 50), (50, 100)]).close().background('green').fill('solid')

    evaluate(reference_json, xg, request)

def test_closed_lines_fill(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()

    xg.line().color('black').points([(0, 0), (100, 50), (50, 100)]).close().background('red').fill('cross-hatch')
    
    evaluate(reference_json, xg, request)

def test_group(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    rect = xg.rectangle().center(0, 0).size(100, 100).label(xg.text().content("Group part"))
    ellipse = xg.ellipse().center(150, 150).size(100, 100).label(xg.text().content("Group part"))
    diamond = xg.diamond().center(-150, -150).size(100, 100).label(xg.text().content("Not Group"))
    xg.group().elements(rect, ellipse)
    
    evaluate(reference_json, xg, request)

def test_frame_default_inset(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    rect = xg.rectangle().center(0, 0).size(100, 100).label(xg.text().content("In frame"))
    ellipse = xg.ellipse().center(150, 150).size(100, 100).label(xg.text().content("In frame"))
    diamond = xg.diamond().center(-150, -150).size(100, 100).label(xg.text().content("Not in frame"))
    xg.frame().title('Test frame').elements(rect, ellipse)
    
    evaluate(reference_json, xg, request)

def test_frame(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    rect = xg.rectangle().center(0, 0).size(100, 100).label(xg.text().content("In frame"))
    ellipse = xg.ellipse().center(150, 150).size(100, 100).label(xg.text().content("In frame"))
    diamond = xg.diamond().center(-150, -150).size(100, 100).label(xg.text().content("Not in frame"))
    xg.frame().center(10, 100).size(400, 500).title('Test frame').elements(rect, ellipse)
    
    evaluate(reference_json, xg, request)
