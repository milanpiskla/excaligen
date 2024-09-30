import pytest
from src.impl.elements.Rectangle import Rectangle
from src.impl.elements.Diamond import Diamond
from src.impl.elements.Ellipse import Ellipse
from src.impl.elements.Text import Text
from src.impl.elements.Line import Line
from src.impl.elements.Arrow import Arrow
from src.config.Config import DEFAULT_CONFIG

def test_rectangle_init():
    rect = Rectangle(DEFAULT_CONFIG)
    assert rect.type == "rectangle"
    assert rect.width == DEFAULT_CONFIG['width']
    assert rect.height == DEFAULT_CONFIG['height']

def test_rectangle_size():
    rect = Rectangle(DEFAULT_CONFIG).size(150, 80)
    assert rect.width == 150
    assert rect.height == 80

def test_rectangle_color():
    rect = Rectangle(DEFAULT_CONFIG).color("#FF5733")
    assert rect.strokeColor == "#FF5733"

def test_rectangle_thickness_valid():
    rect = Rectangle(DEFAULT_CONFIG)
    rect.thickness(2)
    assert rect.strokeWidth == 2

    rect.thickness("bold")
    assert rect.roughness == 1

def test_rectangle_thickness_invalid():
    rect = Rectangle(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid thickness 'invalid'. Use 1, 2, 3 or 'thin', 'bold', 'extra-bold'."):
        rect.thickness("invalid")

def test_rectangle_sloppiness_valid():
    rect = Rectangle(DEFAULT_CONFIG)
    rect.sloppiness("artist")
    assert rect.roughness == 1

    rect.sloppiness(2)
    assert rect.roughness == 2

def test_rectangle_sloppiness_invalid():
    rect = Rectangle(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid value 'sloppy' for sloppiness. Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'."):
        rect.sloppiness("sloppy")

def test_rectangle_stroke_valid():
    rect = Rectangle(DEFAULT_CONFIG)
    rect.stroke("dotted")
    assert rect.strokeStyle == "dotted"

def test_rectangle_stroke_invalid():
    rect = Rectangle(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid style 'striped' for stroke. Use 'solid', 'dotted', 'dashed'."):
        rect.stroke("striped")

def test_rectangle_fill_valid():
    rect = Rectangle(DEFAULT_CONFIG)
    rect.fill("solid")
    assert rect.fillStyle == "solid"

def test_rectangle_fill_invalid():
    rect = Rectangle(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid style 'gradient' for fill. Use 'hatchure', 'cross-hatch', 'solid'."):
        rect.fill("gradient")

def test_rectangle_background():
    rect = Rectangle(DEFAULT_CONFIG).background("#00FF00")
    assert rect.backgroundColor == "#00FF00"

def test_rectangle_label():
    rect = Rectangle(DEFAULT_CONFIG).size(200, 100)
    text = Text(DEFAULT_CONFIG).content("Label")
    rect.label(text)
    assert rect.boundElements is not None
    assert len(rect.boundElements) == 1
    assert rect.boundElements[0]['id'] == text.id
    # Check that the text is centered within the rectangle
    assert text.x == rect.x + (rect.width - text.width) / 2
    assert text.y == rect.y + (rect.height - text.height - text.lineHeight) / 2

def test_rectangle_edges_valid():
    rect = Rectangle(DEFAULT_CONFIG)
    rect.edges("round")
    assert rect.roundness == {"type": 3}

def test_rectangle_edges_invalid():
    rect = Rectangle(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid edges 'curved'. Use 'sharp', 'round'"):
        rect.edges("curved")

def test_text_content():
    text = Text(DEFAULT_CONFIG).content("Sample Text")
    assert text.text == "Sample Text"
    assert text.width > 0
    assert text.height > 0

def test_text_font_size():
    text = Text(DEFAULT_CONFIG)
    text.fontsize(20)
    assert text.fontSize == 20
    text.fontsize("L")
    assert text.fontSize == 24

def test_text_font_size_invalid():
    text = Text(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid size 'XXL'. Use 'S', 'M', 'L', 'XL'."):
        text.fontsize("XXL")

def test_text_font_family_valid():
    text = Text(DEFAULT_CONFIG)
    text.font("comic-shaans")
    assert text.fontFamily == 8

def test_text_font_family_invalid():
    text = Text(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid font 'unknown-font'. Use 'Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code'."):
        text.font("unknown-font")

def test_text_align_valid():
    text = Text(DEFAULT_CONFIG)
    text.align("left")
    assert text.textAlign == "left"

def test_text_align_invalid():
    text = Text(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid alignment 'justify'. Use 'left', 'center', 'right'."):
        text.align("justify")

def test_text_baseline_valid():
    text = Text(DEFAULT_CONFIG)
    text.baseline("top")
    assert text.verticalAlign == "top"

def test_text_baseline_invalid():
    text = Text(DEFAULT_CONFIG)
    with pytest.raises(ValueError, match="Invalid vertical alignment 'middle-ish'. Use 'top', 'middle', 'bottom'."):
        text.baseline("middle-ish")

def test_text_color():
    text = Text(DEFAULT_CONFIG).color("#123456")
    assert text.strokeColor == "#123456"

def test_text_autoresize():
    text = Text(DEFAULT_CONFIG).autoresize(False)
    assert text.autoResize is False

def test_arrow_plot():
    arrow = Arrow(DEFAULT_CONFIG)
    arrow.plot([(0, 0), (100, 100)])
    assert arrow.points == [(0, 0), (100, 100)]

def test_arrow_bind():
    rect1 = Rectangle(DEFAULT_CONFIG).position(0, 0).size(100, 100)
    rect2 = Rectangle(DEFAULT_CONFIG).position(200, 200).size(100, 100)
    arrow = Arrow(DEFAULT_CONFIG)
    arrow.bind(rect1, rect2)
    assert arrow.startBinding['elementId'] == rect1.id
    assert arrow.endBinding['elementId'] == rect2.id
    assert rect1.boundElements is not None
    assert rect2.boundElements is not None

def test_arrow_bind_correct_points():
    rect1 = Rectangle(DEFAULT_CONFIG).position(0, 0).size(100, 100)
    rect2 = Rectangle(DEFAULT_CONFIG).position(200, 200).size(100, 100)
    arrow = Arrow(DEFAULT_CONFIG)
    arrow.bind(rect1, rect2)
    
    # Expected start and end points using the same calculations as in _calculate_edge_point
    start_center_x = rect1.x + rect1.width / 2
    start_center_y = rect1.y + rect1.height / 2
    end_center_x = rect2.x + rect2.width / 2
    end_center_y = rect2.y + rect2.height / 2

    # Calculate expected start edge point
    dx = end_center_x - start_center_x
    dy = end_center_y - start_center_y
    if dx != 0:
        t_x = (rect1.width / 2) / abs(dx)
    else:
        t_x = float('inf')
    if dy != 0:
        t_y = (rect1.height / 2) / abs(dy)
    else:
        t_y = float('inf')
    t = min(t_x, t_y)
    start_x = start_center_x + t * dx
    start_y = start_center_y + t * dy

    # Calculate expected end edge point
    dx = start_center_x - end_center_x
    dy = start_center_y - end_center_y
    if dx != 0:
        t_x = (rect2.width / 2) / abs(dx)
    else:
        t_x = float('inf')
    if dy != 0:
        t_y = (rect2.height / 2) / abs(dy)
    else:
        t_y = float('inf')
    t = min(t_x, t_y)
    end_x = end_center_x + t * dx
    end_y = end_center_y + t * dy

    # Verify arrow position
    assert arrow.x == start_x
    assert arrow.y == start_y

    # Verify arrow points
    expected_end_x = end_x - start_x
    expected_end_y = end_y - start_y
    assert arrow.points[0] == [0, 0]
    assert arrow.points[1] == [expected_end_x, expected_end_y]

def test_arrow_invalid_bind():
    rect = Rectangle(DEFAULT_CONFIG).position(0, 0).size(100, 100)
    text = Text(DEFAULT_CONFIG).position(200, 200)
    arrow = Arrow(DEFAULT_CONFIG)
    arrow.bind(rect, text)
    assert arrow.startBinding['elementId'] == rect.id
    assert arrow.endBinding['elementId'] == text.id
    assert rect.boundElements is not None
    assert text.boundElements is not None

def test_ellipse():
    ellipse = Ellipse(DEFAULT_CONFIG).size(100, 150)
    assert ellipse.type == "ellipse"
    assert ellipse.width == 100
    assert ellipse.height == 150

def test_diamond():
    diamond = Diamond(DEFAULT_CONFIG).size(80, 80)
    assert diamond.type == "diamond"
    assert diamond.width == 80
    assert diamond.height == 80

def test_line_plot():
    line = Line(DEFAULT_CONFIG)
    line.plot([(0, 0), (50, 50), (100, 0)])
    assert line.points == [(0, 0), (50, 50), (100, 0)]

def test_line_color():
    line = Line(DEFAULT_CONFIG).color("#ABCDEF")
    assert line.strokeColor == "#ABCDEF"
