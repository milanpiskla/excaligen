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
    element_1 = xg.ellipse().center(200, -100).size(130, 50).label(xg.text().content('UR'))

    xg.arrow().curve(0, 3.14).bind(center_element, element_1).arrowheads('none', 'arrow')
    
    evaluate(reference_json, xg, request)