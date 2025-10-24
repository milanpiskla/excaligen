"""
Description: Unit tests for inputs.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
from pytest import approx
from excaligen.defaults.Defaults import Defaults
from excaligen.impl.inputs.Align import Align
from excaligen.impl.inputs.Arrowheads import Arrowheads
from excaligen.impl.inputs.Baseline import Baseline
from excaligen.impl.inputs.Fill import Fill
from excaligen.impl.inputs.Font import Font
from excaligen.impl.inputs.Fontsize import Fontsize
from excaligen.impl.inputs.Opacity import Opacity
from excaligen.impl.inputs.Roundness import Roundness
from excaligen.impl.inputs.Sloppiness import Sloppiness
from excaligen.impl.inputs.Stroke import Stroke
from excaligen.impl.inputs.Thickness import Thickness

def test_align_valid_values():
    """Test that valid alignment values are accepted."""
    assert Align.from_("left") == "left"
    assert Align.from_("center") == "center"
    assert Align.from_("right") == "right"

@pytest.mark.parametrize("invalid_align", [
    "",                  # empty string
    "LEFT",             # wrong case
    "Centre",           # wrong spelling
    "middle",           # invalid value
    "top",             # invalid value
    "bottom",          # invalid value
    None,              # None value
    123,               # wrong type
])
def test_align_invalid_values(invalid_align):
    """Test that invalid alignment values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Align.from_(invalid_align)
    assert "Invalid horizontal text alignment" in str(exc_info.value)
    assert "Use 'left', 'center', or 'right'" in str(exc_info.value)

def test_arrowheads_default_values():
    """Test default values for arrowheads."""
    start, end = Arrowheads.from_()
    assert start is None
    assert end == "arrow"

@pytest.mark.parametrize("head", [
    "arrow",
    "bar",
    "dot", 
    "triangle",
    None
])
def test_arrowheads_valid_values(head):
    """Test valid arrowhead values."""
    assert Arrowheads._convert(head) == (head.lower() if head else None)

@pytest.mark.parametrize("head", [
    "ARROW",
    "BAR",
    "DOT",
    "TRIANGLE"
])
def test_arrowheads_case_insensitive(head):
    """Test case insensitivity of arrowhead values."""
    assert Arrowheads._convert(head) == head.lower()

@pytest.mark.parametrize("invalid_head", [
    "",
    "invalid",
    "square",
    "circle",
    123,
    True
])

def test_arrowheads_invalid_values(invalid_head):
    """Test invalid arrowhead values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Arrowheads._convert(invalid_head)
    assert "Invalid arrowhead" in str(exc_info.value)

@pytest.mark.parametrize("start,end,expected", [
    ("arrow", "bar", ("arrow", "bar")),
    (None, "dot", (None, "dot")),
    ("triangle", None, ("triangle", None)),
    ("bar", "arrow", ("bar", "arrow")),
    (None, None, (None, None))
])
def test_arrowheads_combinations(start, end, expected):
    """Test various combinations of start and end arrowheads."""
    assert Arrowheads.from_(start, end) == expected

@pytest.mark.parametrize("align", [
    "top",
    "middle", 
    "bottom"
])
def test_baseline_valid_values(align):
    """Test valid baseline alignments."""
    assert Baseline.from_(align) == align

@pytest.mark.parametrize("invalid_align", [
    "",                 # empty string
    "TOP",             # wrong case
    "Middle",          # wrong case
    "center",          # invalid value
    "baseline",        # invalid value
    None,              # None value
    123,               # wrong type
    True,              # wrong type
])
def test_baseline_invalid_values(invalid_align):
    """Test invalid baseline values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Baseline.from_(invalid_align)
    assert "Invalid vertical text alignment" in str(exc_info.value)
    assert "Use 'top', 'middle', or 'bottom'" in str(exc_info.value)

@pytest.mark.parametrize("style", [
    "hatchure",
    "cross-hatch",
    "solid"
])
def test_fill_valid_styles(style):
    """Test valid fill styles."""
    assert Fill.from_(style) == style

@pytest.mark.parametrize("invalid_style", [
    "",                    # empty string
    "SOLID",              # wrong case
    "Hatchure",           # wrong case
    "Cross-Hatch",        # wrong case
    "none",               # invalid value
    "hatched",           # similar but invalid
    "crosshatch",        # similar but invalid
    None,                # None value
    123,                 # wrong type
    True                 # wrong type
])
def test_fill_invalid_styles(invalid_style):
    """Test invalid fill styles raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Fill.from_(invalid_style)
    assert "Invalid fill style" in str(exc_info.value)
    assert "Use 'hatchure', 'cross-hatch', or 'solid'" in str(exc_info.value)

@pytest.mark.parametrize("font,expected", [
    ("hand-drawn", 1),
    ("normal", 2),
    ("code", 3),
    ("excalifont", 5),
    ("comic-shaans", 8),
    ("lilita-one", 7),
    ("nunito", 6)
])
def test_font_valid_values(font, expected):
    """Test valid font values return correct mapping."""
    assert Font.from_(font) == expected

@pytest.mark.parametrize("input_font,expected", [
    ("HAND-DRAWN", 1),     # uppercase
    ("Normal", 2),         # capitalized
    ("hand drawn", 1),     # with space
    ("COMIC SHAANS", 8),   # uppercase with space
    ("Lilita One", 7)      # mixed case with space
])
def test_font_case_and_spaces(input_font, expected):
    """Test font names are case insensitive and handle spaces."""
    assert Font.from_(input_font) == expected

@pytest.mark.parametrize("invalid_font", [
    "",                    # empty string
    "invalid",             # non-existent font
    "arial",               # unsupported font
    "times-new-roman",     # unsupported font
    None,                  # None value
    123,                   # wrong type
    True                   # wrong type
])
def test_font_invalid_values(invalid_font):
    """Test invalid font values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Font.from_(invalid_font)
    assert "Invalid font" in str(exc_info.value)

@pytest.mark.parametrize("size,expected", [
    (12, 12),         # direct int
    (20, 20),         # matches 'M' value but as int
    (32, 32),         # matches 'XL' value but as int
    ("s", 16),        # small
    ("m", 20),        # medium
    ("l", 24),        # large
    ("xl", 32),       # extra large
    ("S", 16),        # uppercase
    ("M", 20),        # uppercase
    ("L", 24),        # uppercase
    ("XL", 32),       # uppercase
])
def test_fontsize_valid_values(size, expected):
    """Test valid font size values."""
    assert Fontsize.from_(size) == expected

@pytest.mark.parametrize("invalid_size", [
    "",               # empty string
    "xs",            # invalid size
    "xxl",           # invalid size
    "medium",        # invalid size
    "small",         # invalid size
    None,            # None value
    1.5,             # float
    True,            # bool
    [],              # list
])

def test_fontsize_invalid_values(invalid_size):
    """Test invalid font size values raise appropriate errors."""
    with pytest.raises((ValueError, TypeError)) as exc_info:
        Fontsize.from_(invalid_size)
    if isinstance(invalid_size, str):
        assert "Invalid size" in str(exc_info.value)
        assert "Use 'S', 'M', 'L', or 'XL'" in str(exc_info.value)
    else:
        assert "Font size must be an int or one of" in str(exc_info.value)

@pytest.mark.parametrize("roundness,expected", [
    ("sharp", None),
    ("round", {"type": 3})
])
def test_roundness_valid_values(roundness, expected):
    """Test valid roundness values."""
    assert Roundness.from_(roundness) == expected

@pytest.mark.parametrize("invalid_roundness", [
    "",                     # empty string
    "SHARP",               # wrong case
    "Round",               # wrong case
    "rounded",             # invalid value
    "square",              # invalid value
    None,                  # None value
    123,                   # wrong type
    True,                  # wrong type
    [],                    # wrong type
    {"wrong": "dict"}      # invalid dict structure
])
def test_roundness_invalid_values(invalid_roundness):
    """Test invalid roundness values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Roundness.from_(invalid_roundness)
    assert "Invalid roundness" in str(exc_info.value)
    assert "Use 'sharp', or 'round'" in str(exc_info.value)

@pytest.mark.parametrize("sloppiness,expected", [
    (0, 0),                    # numeric inputs
    (1, 1),
    (2, 2),
    ("architect", 0),          # string inputs
    ("artist", 1),
    ("cartoonist", 2)
])
def test_sloppiness_valid_values(sloppiness, expected):
    """Test valid sloppiness values."""
    assert Sloppiness.from_(sloppiness) == expected

@pytest.mark.parametrize("invalid_sloppiness", [
    -1,                    # below range
    3,                     # above range
    1.5,                   # float
    "",                    # empty string
    "rough",               # invalid string
    "sloppy",             # invalid string
    None,                  # None value
    [],                    # list
])
def test_sloppiness_invalid_values(invalid_sloppiness):
    """Test invalid sloppiness values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Sloppiness.from_(invalid_sloppiness)
    assert "Invalid value" in str(exc_info.value)
    assert "Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'" in str(exc_info.value)

@pytest.mark.parametrize("style", [
    "solid",
    "dashed",
    "dotted"
])
def test_stroke_valid_styles(style):
    """Test valid stroke styles."""
    assert Stroke.from_(style) == style

@pytest.mark.parametrize("invalid_style", [
    "",                 # empty string
    "SOLID",           # wrong case
    "Dashed",          # wrong case
    "DOTTED",          # wrong case
    "line",            # invalid value
    "dash",            # similar but invalid
    "dot",             # similar but invalid
    None,              # None value
    123,               # wrong type
    True,              # wrong type
])
def test_stroke_invalid_styles(invalid_style):
    """Test invalid stroke styles raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Stroke.from_(invalid_style)
    assert "Invalid style" in str(exc_info.value)
    assert "Use 'solid', 'dotted', or 'dashed'" in str(exc_info.value)

@pytest.mark.parametrize("thickness,expected", [
    (1, 1),                    # numeric inputs
    (2, 2),
    (3, 3),
    ("thin", 1),              # string inputs
    ("bold", 2),
    ("extra-bold", 4)
])
def test_thickness_valid_values(thickness, expected):
    """Test valid thickness values."""
    assert Thickness.from_(thickness) == expected

@pytest.mark.parametrize("invalid_thickness", [
    0,                      # below range
    4,                      # above range
    -1,                     # negative
    1.5,                    # float
    "",                     # empty string
    "medium",               # invalid string
    "thick",               # invalid string
    None,                  # None value
    [],                    # list
])
def test_thickness_invalid_values(invalid_thickness):
    """Test invalid thickness values raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Thickness.from_(invalid_thickness)
    assert "Invalid thickness" in str(exc_info.value)
    assert "Use 1, 2, 3 or 'thin', 'bold', or 'extra-bold'" in str(exc_info.value)