"""
Description: Unit tests for colors.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest

from excaligen.impl.colors.Color import Color

def test_color_rgb_from_hex_str():
    c = Color().rgb("#FF8000")
    assert c.rgb() == (255, 128, 0)
    assert str(c) == "#FF8000"

    c = Color().rgb("#003264")
    assert c.rgb() == (0, 50, 100)
    assert str(c) == "#003264"
    
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
    color = Color.from_("#FF8000")
    assert color == "#FF8000"

    color = Color.from_("#003264")
    assert color == "#003264"

    color = Color.from_("orange")
    assert color == "Orange"

    color = Color.from_("BLUE")
    assert color == "Blue"

    with pytest.raises(ValueError):
        Color.from_("invalid")

    with pytest.raises(ValueError):
        Color.from_("#12345")

    with pytest.raises(ValueError):
        Color.from_("#1234567")

def test_static_rgb_to_hsl():
    assert Color.rgb_to_hsl(255, 0, 0) == (0, 100, 50)
    assert Color.rgb_to_hsl(0, 255, 0) == (120, 100, 50)
    assert Color.rgb_to_hsl(0, 0, 255) == (240, 100, 50)
    assert Color.rgb_to_hsl(255, 255, 255) == (0, 0, 100)
    assert Color.rgb_to_hsl(0, 0, 0) == (0, 0, 0)

def test_static_hsl_to_rgb():
    assert Color.hsl_to_rgb(0, 100, 50) == (255, 0, 0)
    assert Color.hsl_to_rgb(120, 100, 50) == (0, 255, 0)
    assert Color.hsl_to_rgb(240, 100, 50) == (0, 0, 255)

def test_rgb_getter():
    c = Color().rgb(1, 2, 3)
    assert c.rgb() == (1, 2, 3)

def test_hsl_getter():
    c = Color().hsl(0, 100, 50)
    # Allow small rounding differences if necessary, but integers should match for simple cases
    assert c.hsl() == (0, 100, 50)
    
    c.rgb(0, 0, 0)
    assert c.hsl() == (0, 0, 0)

def test_rgb_to_hsl_roundtrip():
    c = Color().rgb(255, 0, 0)
    assert c.hsl_to_rgb(*c.rgb_to_hsl(*c.rgb())) == c.rgb()

    c = Color().rgb(0, 255, 0)
    assert c.hsl_to_rgb(*c.rgb_to_hsl(*c.rgb())) == c.rgb()

    c = Color().rgb(0, 0, 255)
    assert c.hsl_to_rgb(*c.rgb_to_hsl(*c.rgb())) == c.rgb()

    c = Color().rgb(255, 255, 255)
    assert c.hsl_to_rgb(*c.rgb_to_hsl(*c.rgb())) == c.rgb()

    c = Color().rgb(0, 0, 0)
    assert c.hsl_to_rgb(*c.rgb_to_hsl(*c.rgb())) == c.rgb()

def test_hsl_to_rgb_roundtrip():
    c = Color().hsl(0, 100, 50)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

    c = Color().hsl(120, 100, 50)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

    c = Color().hsl(240, 100, 50)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

    c = Color().hsl(0, 0, 100)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

    c = Color().hsl(0, 0, 0)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

    c = Color().hsl(30, 75, 50)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

    c = Color().hsl(60, 100, 25)
    assert c.rgb_to_hsl(*c.hsl_to_rgb(*c.hsl())) == c.hsl()

def test_invalid_args():
    c = Color()
    with pytest.raises(TypeError):
        c.rgb(1, 2)
    
    with pytest.raises(TypeError):
        c.hsl(1, 2)


        
    

