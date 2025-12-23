"""
Description: Functional tests for various elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_text_justify(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    
    y = 0
    for baseline in ['top', 'middle', 'bottom']:
        x = -300
        for align in ['left', 'center', 'right']:
            xg.rectangle(xg.text(f'{align}-{baseline}').align(align).baseline(baseline)).size(200, 120).center(x, y)
            x += 300
        y += 150

    evaluate(reference_json, xg, request)
