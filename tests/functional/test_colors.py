from src.Excaligen import Excaligen
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_shape_color(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = Excaligen()
    xg.rectangle().center(0, 0).size(100, 100).color('#FF0000').background('Blue')
    
    green = xg.color().rgb(0, 255, 0)
    xg.rectangle().center(100, 100).size(100, 100).color('Olive').background(green)
    
    evaluate(reference_json, xg, request)