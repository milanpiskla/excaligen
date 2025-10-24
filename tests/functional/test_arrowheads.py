"""
Description: Functional tests for arrowheads.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.DiagramBuilder import DiagramBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_arrowheads(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = DiagramBuilder()
    xg.defaults().color('gray')
    y = 0

    for start_head in [None, 'arrow', 'bar', 'dot', 'triangle']:
        x = -400
        for end_head in [None, 'arrow', 'bar', 'dot', 'triangle']:
            start_element = xg.rectangle().center(x, y).size(100, 50).roundness('round').label(xg.text().content(f"SH: {start_head}"))
            end_element = xg.rectangle().center(x + 200, y).size(100, 50).roundness('round').label(xg.text().content(f"EH: {end_head}"))

            xg.arrow().bind(start_element, end_element).arrowheads(start_head, end_head).color('blue')
            x += 320
        y += 150

    evaluate(reference_json, xg, request)