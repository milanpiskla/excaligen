"""
Description: Functional tests for colors.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_rgb_colors(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    for i in range(0, 256, 8):
        red_color = scene.color().rgb(i, 0, 0)
        green_color = scene.color().rgb(0, i, 0)
        blue_color = scene.color().rgb(0, 0, i)
        
        (
            scene.rectangle()
            .size(8,100)
            .center(i, 0)
            .sloppiness('architect')
            .roundness('sharp')
            .color(red_color)
            .background(red_color)
            .fill('solid')
        )
        (
            scene.rectangle()
            .size(8,100)
            .center(i, 100)
            .sloppiness('architect')
            .roundness('sharp')
            .color(green_color)
            .background(green_color)
            .fill('solid')
        )
        (
            scene.rectangle()
            .size(8,100)
            .center(i, 200)
            .sloppiness('architect')
            .roundness('sharp')
            .color(blue_color)
            .background(blue_color)
            .fill('solid')
        )
    
    evaluate(reference_json, scene, request)

def test_hsl_colors(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()

    for i in range(0, 360, 10):
        color = scene.color().hsl(i, 100, 50)
        (
            scene.rectangle()
            .size(10,100)
            .center(i, 0)
            .sloppiness('architect')
            .roundness('sharp')
            .color(color)
            .background(color)
            .fill('solid')
        )
    
    evaluate(reference_json, scene, request)

def test_color_names(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    _COLOR_NAMES = [
        "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood",
        "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey",
        "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey",
        "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite",
        "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen",
        "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen",
        "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue",
        "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose",
        "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed",
        "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown",
        "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato",
        "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"
    ]

    COUNT_PER_ROW = 10
    REC_WIDTH = 120
    REC_HEIGHT = 60
    
    scene = SceneBuilder()
    counter = 0
    for name in _COLOR_NAMES:
        x = counter % COUNT_PER_ROW * REC_WIDTH
        y = counter // COUNT_PER_ROW * REC_HEIGHT
        (
            scene.rectangle(name)
            .size(REC_WIDTH, REC_HEIGHT)
            .position(x, y)
            .sloppiness('architect')
            .roundness('sharp')
            .color(name)
            .background(name)
            .fill('solid')
        )
        counter += 1

    evaluate(reference_json, scene, request)        
    
def test_colors_hex(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()
    
    for i in range(0, 256, 8):
        red_color = f"#{i:02x}0000"
        green_color = f"#00{i:02x}00"
        blue_color = f"#0000{i:02x}"
        
        (
            scene.rectangle()
            .size(8,100)
            .center(i, 0)
            .sloppiness('architect')
            .roundness('sharp')
            .color(red_color)
            .background(red_color)
            .fill('solid')
        )
        (
            scene.rectangle()
            .size(8,100)
            .center(i, 100)
            .sloppiness('architect')
            .roundness('sharp')
            .color(green_color)
            .background(green_color)
            .fill('solid')
        )
        (
            scene.rectangle()
            .size(8,100)
            .center(i, 200)
            .sloppiness('architect')
            .roundness('sharp')
            .color(blue_color)
            .background(blue_color)
            .fill('solid')
        )
    
    evaluate(reference_json, scene, request)
