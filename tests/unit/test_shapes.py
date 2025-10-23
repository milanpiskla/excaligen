"""
Description: Unit tests for shapes.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
from pytest import approx
from src.excaligen.impl.elements.Rectangle import Rectangle
from src.excaligen.impl.elements.Diamond import Diamond
from src.excaligen.impl.elements.Ellipse import Ellipse
from src.excaligen.impl.elements.Text import Text
from src.excaligen.impl.elements.Line import Line
from src.excaligen.impl.elements.Arrow import Arrow
from excaligen.defaults.Defaults import Defaults
from src.excaligen.impl.base.AbstractPlainLabelListener import AbstractPlainLabelListener

class DummyListener(AbstractPlainLabelListener):
            def _on_text(self, text: str) -> Text:
                return Text(Defaults())

def test_rectangle_init():
    defaults = Defaults()
    rect = Rectangle(defaults, DummyListener())
    assert rect._type == "rectangle"
    assert rect._width == getattr(defaults, '_width')
    assert rect._height == getattr(defaults, '_height')

def test_rectangle_size():
    rect = Rectangle(Defaults(), DummyListener()).size(150, 80)
    assert rect._width == 150
    assert rect._height == 80

def test_rectangle_center_first():
    CX, CY = 100, 200
    W, H = 150, 80
    
    rect = Rectangle(Defaults(), DummyListener()).center(CX, CY).size(W, H)
    cx, cy = rect.get_center()
    assert cx == approx(CX)
    assert cy == approx(CY)
    assert rect._x == approx(CX - W / 2)
    assert rect._y == approx(CY - H / 2)

def test_rectangle_center_second():
    CX, CY = 100, 200
    W, H = 150, 80
    
    rect = Rectangle(Defaults(), DummyListener()).size(W, H).center(CX, CY)
    cx, cy = rect.get_center()
    assert cx == approx(CX)
    assert cy == approx(CY)
    assert rect._x == approx(CX - W / 2)
    assert rect._y == approx(CY - H / 2)

def test_rectangle_color():
    defaults = Defaults()
    rect = Rectangle(Defaults(), DummyListener()).color("#FF5733")
    assert rect._stroke_color == "#FF5733"

def test_rectangle_thickness_valid():
    rect = Rectangle(Defaults(), DummyListener())
    rect.thickness(2)
    assert rect._stroke_width == 2

    rect.thickness("thin")
    assert rect._stroke_width == 1

    rect.thickness("bold")
    assert rect._stroke_width == 2

    rect.thickness("extra-bold")
    assert rect._stroke_width == 4

def test_rectangle_thickness_invalid():
    rect = Rectangle(Defaults(), DummyListener())
    with pytest.raises(ValueError, match="Invalid thickness 'invalid'. Use 1, 2, 3 or 'thin', 'bold', or 'extra-bold'."):
        rect.thickness("invalid")

def test_rectangle_sloppiness_valid():
    rect = Rectangle(Defaults(), DummyListener())

    rect.sloppiness("architect")
    assert rect._roughness == 0

    rect.sloppiness("artist")
    assert rect._roughness == 1

    rect.sloppiness("cartoonist")
    assert rect._roughness == 2

    rect.sloppiness(2)
    assert rect._roughness == 2

def test_rectangle_sloppiness_invalid():
    rect = Rectangle(Defaults(), DummyListener())
    with pytest.raises(ValueError, match="Invalid value 'sloppy' for sloppiness. Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'."):
        rect.sloppiness("sloppy")

def test_rectangle_stroke_valid():
    rect = Rectangle(Defaults(), DummyListener())
    rect.stroke("dotted")
    assert rect._stroke_style == "dotted"

def test_rectangle_stroke_invalid():
    rect = Rectangle(Defaults(), DummyListener())
    with pytest.raises(ValueError, match="Invalid style 'striped' for stroke. Use 'solid', 'dotted', or 'dashed'."):
        rect.stroke("striped")

def test_rectangle_fill_valid():
    rect = Rectangle(Defaults(), DummyListener())
    rect.fill("solid")
    assert rect._fill_style == "solid"

def test_rectangle_fill_invalid():
    rect = Rectangle(Defaults(), DummyListener())
    with pytest.raises(ValueError, match="Invalid fill style 'gradient'. Use 'hatchure', 'cross-hatch', or 'solid'."):
        rect.fill("gradient")

def test_rectangle_background():
    rect = Rectangle(Defaults(), DummyListener()).background("#00FF00")
    assert rect._background_color == "#00FF00"

def test_rectangle_label():
    rect = Rectangle(Defaults(), DummyListener()).size(200, 100)
    text = Text(Defaults()).content("Label")
    rect.label(text)
    assert rect._bound_elements is not None
    assert len(rect._bound_elements) == 1
    assert rect._bound_elements[0]['id'] == text._id
    # Check that the text is centered within the rectangle
    assert text._x == rect._x + (rect._width - text._width) / 2
    assert text._y == rect._y + (rect._height - text._height - text._line_height) / 2

def test_rectangle_roundness_valid():
    rect = Rectangle(Defaults(), DummyListener())
    rect.roundness("round")
    assert rect._roundness == {"type": 3}

def test_rectangle_roundness_invalid():
    rect = Rectangle(Defaults(), DummyListener())
    with pytest.raises(ValueError, match="Invalid roundness 'curved'. Use 'sharp', or 'round'"):
        rect.roundness("curved")

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

def test_arrow_points():
    arrow = Arrow(Defaults(), DummyListener())
    arrow.points([(0, 0), (100, 100)])
    assert arrow._points == [(0, 0), (100, 100)]

def test_arrow_points_size():
    arrow = Arrow(Defaults(), DummyListener())
    arrow.points([(0, 0), (50, 100), (-25, -125)])
    assert arrow._width == 75
    assert arrow._height == 225
    
def test_arrow_bind():
    rect1 = Rectangle(Defaults(), DummyListener()).position(0, 0).size(100, 100)
    rect2 = Rectangle(Defaults(), DummyListener()).position(200, 200).size(100, 100)
    arrow = Arrow(Defaults(), DummyListener())
    arrow.bind(rect1, rect2)
    assert arrow._start_binding is not None
    assert arrow._start_binding['elementId'] == rect1._id
    assert arrow._end_binding is not None
    assert arrow._end_binding['elementId'] == rect2._id
    assert rect1._bound_elements is not None
    assert rect2._bound_elements is not None

def test_arrow_bind_correct_points():
    rect1 = Rectangle(Defaults(), DummyListener()).position(0, 0).size(100, 100)
    rect2 = Rectangle(Defaults(), DummyListener()).position(200, 200).size(100, 100)
    arrow = Arrow(Defaults(), DummyListener())
    arrow.bind(rect1, rect2)
    
    # Expected start and end points using the same calculations as in _calculate_edge_point
    start_center_x = rect1._x + rect1._width / 2
    start_center_y = rect1._y + rect1._height / 2
    end_center_x = rect2._x + rect2._width / 2
    end_center_y = rect2._y + rect2._height / 2

    # Calculate expected start edge point
    dx = end_center_x - start_center_x
    dy = end_center_y - start_center_y
    if dx != 0:
        t_x = (rect1._width / 2) / abs(dx)
    else:
        t_x = float('inf')
    if dy != 0:
        t_y = (rect1._height / 2) / abs(dy)
    else:
        t_y = float('inf')
    t = min(t_x, t_y)
    start_x = start_center_x + t * dx
    start_y = start_center_y + t * dy

    # Calculate expected end edge point
    dx = start_center_x - end_center_x
    dy = start_center_y - end_center_y
    if dx != 0:
        t_x = (rect2._width / 2) / abs(dx)
    else:
        t_x = float('inf')
    if dy != 0:
        t_y = (rect2._height / 2) / abs(dy)
    else:
        t_y = float('inf')
    t = min(t_x, t_y)
    end_x = end_center_x + t * dx
    end_y = end_center_y + t * dy

    # Verify arrow position
    assert arrow._x == start_x
    assert arrow._y == start_y

    # Verify arrow points
    expected_end_x = end_x - start_x
    expected_end_y = end_y - start_y
    assert arrow._points[0] == (0, 0)
    assert arrow._points[1] == (expected_end_x, expected_end_y)

def test_arrow_invalid_bind():
    rect = Rectangle(Defaults(), DummyListener()).position(0, 0).size(100, 100)
    text = Text(Defaults()).position(200, 200)
    arrow = Arrow(Defaults(), DummyListener())
    arrow.bind(rect, text)
    assert arrow._start_binding is not None
    assert arrow._start_binding['elementId'] == rect._id
    assert arrow._end_binding is not None
    assert arrow._end_binding['elementId'] == text._id
    assert rect._bound_elements is not None
    assert text._bound_elements is not None

def test_ellipse():
    ellipse = Ellipse(Defaults(), DummyListener()).size(100, 150)
    assert ellipse._type == "ellipse"
    assert ellipse._width == 100
    assert ellipse._height == 150

def test_diamond():
    diamond = Diamond(Defaults(), DummyListener()).size(80, 80)
    assert diamond._type == "diamond"
    assert diamond._width == 80
    assert diamond._height == 80

def test_line_points():
    line = Line(Defaults())
    line.points([(0, 0), (50, 50), (100, 0)])
    assert line._points == [(0, 0), (50, 50), (100, 0)]

def test_line_points_size():
    line = Line(Defaults())
    line.points([(0, 0), (-10, 50), (100, -20)])
    assert line._width == 110
    assert line._height == 70

def test_line_color():
    line = Line(Defaults()).color("#ABCDEF")
    assert line._stroke_color == "#ABCDEF"

def test_center():
    rect = Rectangle(Defaults(), DummyListener()).position(12, 23).center(10, 20).size(210, 108)
    assert rect._x == 10 - 0.5 * 210
    assert rect._y == 20 - 0.5 * 108

    rect = Rectangle(Defaults(), DummyListener()).position(12, 23).size(210, 108).center(10, 20)
    assert rect._x == 10 - 0.5 * 210
    assert rect._y == 20 - 0.5 * 108

    rect = Rectangle(Defaults(), DummyListener()).center(10, 20).size(210, 108)
    assert rect._x == 10 - 0.5 * 210
    assert rect._y == 20 - 0.5 * 108

def test_link_string():
    rect = Rectangle(Defaults(), DummyListener()).link("https://example.com")
    assert rect._link == "https://example.com"

def test_link_element():
    rect1 = Rectangle(Defaults(), DummyListener())
    rect2 = Rectangle(Defaults(), DummyListener()).link(rect1)
    assert rect2._link == f"https://excalidraw.com/?element={rect1._id}"

# def test_link_element_invalid():
#     rect = Rectangle(Defaults(), DummyListener())
#     with pytest.raises(ValueError, match="Link target must be a string or an AbstractElement."):
#         rect.link(42)
