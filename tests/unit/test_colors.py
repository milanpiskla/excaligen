"""
Description: Unit tests for colors.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest

from excaligen.impl.colors.Color import Color

def test_color_hex():
    color = Color().rgb(255, 128, 0)
    assert str(color) == "#FF8000"

    color = Color().rgb(0, 50, 100)
    assert str(color) == "#003264"

def test_color_hsl():
    color = Color().hsl(30, 75, 50)
    assert str(color) == "#DF8020"

    color = Color().hsl(0, 100, 100)
    assert str(color) == "#FFFFFF"

    color = Color().hsl(0, 100, 50)
    assert str(color) == "#FF0000"

    color = Color().hsl(120, 100, 50)
    assert str(color) == "#00FF00"

    color = Color().hsl(60, 100, 25)
    assert str(color) == "#808000"

def test_color_string():
    color = Color.from_input("#FF8000")
    assert color == "#FF8000"

    color = Color.from_input("#003264")
    assert color == "#003264"

    color = Color.from_input("orange")
    assert color == "Orange"

    color = Color.from_input("BLUE")
    assert color == "Blue"

    with pytest.raises(ValueError):
        Color.from_input("invalid")

    with pytest.raises(ValueError):
        Color.from_input("#12345")

    with pytest.raises(ValueError):
        Color.from_input("#1234567")
