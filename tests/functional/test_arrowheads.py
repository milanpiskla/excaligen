"""
Description: Functional tests for arrowheads.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_arrowheads(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    xg.defaults().color('gray').size(100, 50).roundness('round')
    y = 0

    for start_head in [None, 'arrow', 'bar', 'dot', 'triangle']:
        x = -400
        for end_head in [None, 'arrow', 'bar', 'dot', 'triangle']:
            start_element = xg.rectangle().center(x, y).label(f"SH: {start_head}")
            end_element = xg.rectangle().center(x + 200, y).label(f"EH: {end_head}")

            xg.arrow().bind(start_element, end_element).arrowheads(start_head, end_head).color('blue')
            x += 320
        y += 150

    evaluate(reference_json, xg, request)