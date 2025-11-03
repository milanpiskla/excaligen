"""
Description: Unit tests for texts.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
from pytest import approx

from src.excaligen.impl.elements.Text import Text
from src.excaligen.defaults.Defaults import Defaults

def test_text_content():
    text = Text(Defaults()).content("Sample Text")
    assert text._text == "Sample Text"
    assert text._width > 0
    assert text._height > 0

def test_text_font_size():
    text = Text(Defaults())
    text.fontsize(20)
    assert text._font_size == 20
    text.fontsize("L")
    assert text._font_size == 24

def test_text_font_size_invalid():
    text = Text(Defaults())
    with pytest.raises(ValueError, match="Invalid size 'XXL'. Use 'S', 'M', 'L', or 'XL'."):
        text.fontsize("XXL")

def test_text_font_family_valid():
    text = Text(Defaults())
    text.font("comic-shaans")
    assert text._font_family == 8

def test_text_font_family_invalid():
    text = Text(Defaults())
    with pytest.raises(ValueError, match=r"Invalid font 'unknown-font'. Use one of \['hand-drawn', 'normal', 'code', 'excalifont', 'comic-shaans', 'lilita-one', 'nunito'\]."):
        text.font("unknown-font")

def test_text_align_valid():
    text = Text(Defaults())
    text.align("left")
    assert text._text_align == "left"

def test_text_align_invalid():
    text = Text(Defaults())
    with pytest.raises(ValueError, match="Invalid horizontal text alignment 'justify'. Use 'left', 'center', or 'right'."):
        text.align("justify")

def test_text_baseline_valid():
    text = Text(Defaults())
    text.baseline("top")
    assert text._vertical_align == "top"

def test_text_baseline_invalid():
    text = Text(Defaults())
    with pytest.raises(ValueError, match="Invalid vertical text alignment 'middle-ish'. Use 'top', 'middle', or 'bottom'."):
        text.baseline("middle-ish")

def test_text_color():
    text = Text(Defaults()).color("#123456")
    assert text._stroke_color == "#123456"

def test_text_autoresize():
    text = Text(Defaults()).autoresize(False)
    assert text._auto_resize is False

def test_text_anchor_left_top():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'left', 'top')
    assert text._x == approx(21)
    assert text._y == approx(42)

def test_text_anchor_left_middle():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'left', 'middle')
    assert text._x == approx(21)
    assert text._y == approx(32)

def test_text_anchor_left_bottom():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'left', 'bottom')
    assert text._x == approx(21)
    assert text._y == approx(22)

def test_text_anchor_center_top():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'center', 'top')
    assert text._x == approx(-3)
    assert text._y == approx(42)

def test_text_anchor_center_middle():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'center', 'middle')
    assert text._x == approx(-3)
    assert text._y == approx(32)

def test_text_anchor_center_bottom():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'center', 'bottom')
    assert text._x == approx(-3)
    assert text._y == approx(22)

def test_text_anchor_right_top():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'right', 'top')
    assert text._x == approx(-27)
    assert text._y == approx(42)

def test_text_anchor_right_middle():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'right', 'middle')
    assert text._x == approx(-27)
    assert text._y == approx(32)

def test_text_anchor_right_bottom():
    text = Text(Defaults()).content('Hello').anchor(21, 42, 'right', 'bottom')
    assert text._x == approx(-27)
    assert text._y == approx(22)

