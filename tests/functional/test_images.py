"""
Description: Functional tests for various elements.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any
import math

from pytest import FixtureRequest

def test_image_from_data(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    IMAGE_DATA = '''
        <svg xmlns="http://www.w3.org/2000/svg" width="467" height="462" stroke="#000" stroke-width="2">
            <rect x="80" y="60" width="250" height="250" rx="20" fill="#F80"/>
            <circle cx="310" cy="290" r="120" fill="#00F" fill-opacity=".7"/>
        </svg>'''

    scene.image().data(IMAGE_DATA)

    evaluate(reference_json, scene, request)

