"""
Description: Functional tests for various elements.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_shapes(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.rectangle('Rectangle').center(-150, 0)
    scene.ellipse('Ellipse').center(0, 0)
    scene.diamond('Diamond').center(150, 0)

    evaluate(reference_json, scene, request)

def test_strokes(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.ellipse().center(-150, 0).stroke('solid')
    scene.ellipse().center(0, 0).stroke('dashed')
    scene.ellipse().center(150, 0).stroke('dotted')

    evaluate(reference_json, scene, request)

def test_fills(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.ellipse().center(-150, 0).background('gray').fill('solid')
    scene.ellipse().center(0, 0).background('gray').fill('hachure')
    scene.ellipse().center(150, 0).background('gray').fill('cross-hatch')

    evaluate(reference_json, scene, request)

def test_sloppiness(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.ellipse().center(-150, 0).sloppiness('architect')
    scene.ellipse().center(0, 0).sloppiness('artist')
    scene.ellipse().center(150, 0).sloppiness('cartoonist')

    evaluate(reference_json, scene, request)

def test_thickness(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.ellipse().center(-150, 0).thickness('thin')
    scene.ellipse().center(0, 0).thickness('bold')
    scene.ellipse().center(150, 0).thickness('extra-bold')

    evaluate(reference_json, scene, request)

def test_shape_colors(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    # Add a rectangle with a named color
    (
        scene.rectangle('Action')
        .position(0, 0)
        .color("BlueViolet")
        .background("Lavender")
    )

    # Add an ellipse with RGB color as string
    (
        scene.ellipse('Start')
        .position(150, 0)
        .color('#FF5733')
        .background('#FFBD33')
    )

    # Add a diamond with HSL color
    (
        scene.diamond('Decision')
        .position(300, 0)
        .color(scene.color().hsl(120, 100, 25))
        .background(scene.color().hsl(120, 100, 85))
    )

    evaluate(reference_json, scene, request)

def test_shape_center(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.ellipse().center(0, 0)
    scene.rectangle().center(0, -120)
    scene.diamond().center(150, 0)

    evaluate(reference_json, scene, request)

def test_shape_position(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.rectangle('Rectangle 1').position(0, 0)
    scene.rectangle('Rectangle 2').position(150, 0)
    scene.rectangle('Rectangle 3').position(0, 120)

    evaluate(reference_json, scene, request)


def test_shape_size(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.rectangle('Small').size(80, 64).center(0, 0)    
    scene.rectangle('Medium').size(100, 80).center(100, 0)
    scene.rectangle('Large').size(150, 120).center(235, 0)

    evaluate(reference_json, scene, request)

def test_shape_roundness(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    scene.rectangle('Rounded').roundness('round').center(0, 0)
    scene.rectangle('Sharp').roundness('sharp').center(150, 0)
    scene.diamond('Rounded').roundness('round').center(0, 100)
    scene.diamond('Sharp').roundness('sharp').center(150, 100)
    
    evaluate(reference_json, scene, request)

def test_shape_styled_label(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    label = scene.text('Styled Label').color('SkyBlue')
    scene.rectangle(label)

    evaluate(reference_json, scene, request)
