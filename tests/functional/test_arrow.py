from src.Excaligen import Excaligen
from .evaluate import *

from pytest import FixtureRequest
import math

def test_arrow_star(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()

    start_element = xg.ellipse().center(0, 0).size(100, 100).label(xg.text().content("center"))

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = 300 * math.cos(radians)
        y = 300 * math.sin(radians)
        end_element = xg.rectangle().center(x, y).size(100, 50).label(xg.text().content(str(angle))).roudness('round')
        xg.arrow().bind(start_element, end_element)

    evaluate(reference_json, xg, request)

def test_arrow_curve(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    center_element = xg.rectangle().center(0, 0).size(160, 70).roudness('round').label(xg.text().content("center"))
    element_1 = xg.ellipse().center(400, -200).size(130, 50).label(xg.text().content('UR'))
    xg.arrow().curve(0, 3.14).bind(center_element, element_1).arrowheads('none', 'arrow')
    
    evaluate(reference_json, xg, request)

def test_arrow_curve_narrow(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    start_element = xg.ellipse().center(-150, -150).size(120, 80).label(xg.text().content("center 1"))
    end_element = xg.ellipse().center(150, 150).size(120, 80).label(xg.text().content("center 2"))
    xg.arrow().curve(0.0, 3.14 * 0.75).bind(start_element, end_element)

    evaluate(reference_json, xg, request)

def test_arrow_curve_complex(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    RADIUS = 700
    XOFFSET = -200
    center_element = xg.rectangle().center(0, 0).size(120, 80).roudness('round').label(xg.text().content("Center"))

    for i in range(-3, 4):
        angle = i * math.pi / 14
        xr = RADIUS * math.cos(angle) + XOFFSET
        yr = RADIUS * math.sin(angle)
        relement = xg.rectangle().center(xr, yr).size(120, 80).roudness('round').label(xg.text().content(f"Right {i}"))
        xg.arrow().curve(0, math.pi).bind(center_element, relement).arrowheads('none', 'arrow')
        
        xl = RADIUS * math.cos(angle + math.pi) - XOFFSET
        yl = RADIUS * math.sin(angle + math.pi)
        lelement = xg.rectangle().center(xl, yl).size(120, 80).roudness('round').label(xg.text().content(f"Left {i}"))
        xg.arrow().curve(math.pi, 0).bind(center_element, lelement).arrowheads('none', 'arrow')

    evaluate(reference_json, xg, request)

def test_arrow_curve_str_directions(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    center_element = xg.rectangle().center(0, 0).size(160, 70).roudness('round').label(xg.text().content("center"))
    element_1 = xg.ellipse().center(400, -200).size(130, 50).label(xg.text().content('UR'))
    xg.arrow().curve('R', 'L').bind(center_element, element_1).arrowheads('none', 'arrow')
    xg.arrow().curve('U', 'U').bind(center_element, element_1).arrowheads('none', 'arrow')
    xg.arrow().curve('D', 'D').bind(center_element, element_1).arrowheads('none', 'arrow')
    xg.arrow().curve('L', 'R').bind(center_element, element_1).arrowheads('none', 'arrow')
    
    evaluate(reference_json, xg, request)

def test_arrow_curve_diff_calling_order(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    center_element = xg.rectangle().center(0, 0).size(160, 70).roudness('round').label(xg.text().content("center"))
    element_1 = xg.ellipse().center(400, -200).size(130, 50).label(xg.text().content('UR'))
    xg.arrow().bind(center_element, element_1).arrowheads('none', 'arrow').curve(0, 3.14)
    
    evaluate(reference_json, xg, request)

def test_arrow_elbows(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    center_element = xg.rectangle().center(0, 0).size(160, 70).roudness('round').label(xg.text().content("center"))
    element_1 = xg.ellipse().center(400, -200).size(130, 50).label(xg.text().content('UR'))
    xg.arrow().elbow('R', 'L').bind(center_element, element_1).arrowheads('none', 'arrow')
    xg.arrow().elbow('U', 'U').bind(center_element, element_1).arrowheads('none', 'arrow')
    xg.arrow().elbow('D', 'D').bind(center_element, element_1).arrowheads('none', 'arrow')
    xg.arrow().elbow('L', 'R').bind(center_element, element_1).arrowheads('none', 'arrow')
    
    evaluate(reference_json, xg, request)

def test_arrow_elbows_diff_calling_order(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    center_element = xg.rectangle().center(0, 0).size(160, 70).roudness('round').label(xg.text().content("center"))
    element_1 = xg.ellipse().center(400, -200).size(130, 50).label(xg.text().content('UR'))
    xg.arrow().bind(center_element, element_1).arrowheads('none', 'arrow').elbow('R', 'L')
    xg.arrow().bind(center_element, element_1).arrowheads('none', 'arrow').elbow('U', 'U')
    xg.arrow().bind(center_element, element_1).arrowheads('none', 'arrow').elbow('D', 'D')
    xg.arrow().bind(center_element, element_1).arrowheads('none', 'arrow').elbow('L', 'R')
    
    evaluate(reference_json, xg, request)

def test_arrow_arc(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()

    RADIUS = 300
    elements = []

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = RADIUS * math.cos(radians)
        y = RADIUS * math.sin(radians)

        rect = xg.ellipse().center(x, y).size(80, 60).label(xg.text().content(f"{angle}°"))
        elements.append(rect)

    start_element = elements[0]
    for i in range(1, len(elements)):
        xg.arrow().arc(radius=RADIUS).bind(start_element, elements[i])
        start_element = elements[i]

    evaluate(reference_json, xg, request)

def test_arrow_label(reference_json: dict[str, any], request: FixtureRequest) -> None:
    xg = Excaligen()
    center_element = xg.rectangle().center(0, 0).size(160, 70).roudness('round').label(xg.text().content("center"))
    element_1 = xg.ellipse().center(400, -200).size(130, 50).label(xg.text().content('UR'))
    label = xg.text().content('Label')
    xg.arrow().curve(0, 3.14).bind(center_element, element_1).arrowheads('none', 'arrow').label(label)
    
    evaluate(reference_json, xg, request)
