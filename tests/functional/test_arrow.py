"""
Description: Functional tests for arrows.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest
import math

def test_arrow_star(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()

    start_element = xg.ellipse('center').center(0, 0).size(100, 100)

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = 300 * math.cos(radians)
        y = 300 * math.sin(radians)
        end_element = xg.rectangle(str(angle)).center(x, y).size(100, 50).roundness('round')
        xg.arrow().bind(start_element, end_element)

    evaluate(reference_json, xg, request)

def test_arrow_curve(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()
    
    center = scene.rectangle('center').center(0, 0).size(160, 70)
    ur = scene.ellipse('up-right').center(400, -200).size(130, 50)
    ul = scene.ellipse('up-left').center(-400, -200).size(130, 50)
    dr = scene.ellipse('down-right').center(200, 300).size(130, 50)
    dl = scene.ellipse('down-left').center(-200, 300).size(130, 50)
   
    scene.arrow().curve('R', 'L').bind(center, ur).arrowheads(None, 'arrow')
    scene.arrow().curve('L', 'R').bind(center, ul).arrowheads(None, 'arrow')
    scene.arrow().curve('D', 'U').bind(center, dr).arrowheads(None, 'arrow')
    scene.arrow().curve('D', 'U').bind(center, dl).arrowheads(None, 'arrow')
    
    evaluate(reference_json, scene, request)

def test_arrow_curve_narrow(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    start_element = xg.ellipse('Begin').center(-150, -150).size(120, 80)
    end_element = xg.ellipse('End').center(150, 150).size(120, 80)
    xg.arrow().curve(0.0, 3.14 * 0.75).bind(start_element, end_element)

    evaluate(reference_json, xg, request)

def test_arrow_curve_complex(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    RADIUS = 700
    XOFFSET = -200
    center_element = xg.rectangle('center').center(0, 0).size(120, 80).roundness('round')

    for i in range(-3, 4):
        angle = i * math.pi / 14
        xr = RADIUS * math.cos(angle) + XOFFSET
        yr = RADIUS * math.sin(angle)
        relement = xg.rectangle(f'right {i}').center(xr, yr).size(120, 80).roundness('round')
        xg.arrow().curve(0, math.pi).bind(center_element, relement).arrowheads(None, 'arrow')
        
        xl = RADIUS * math.cos(angle + math.pi) - XOFFSET
        yl = RADIUS * math.sin(angle + math.pi)
        lelement = xg.rectangle(f'left {i}').center(xl, yl).size(120, 80).roundness('round')
        xg.arrow().curve(math.pi, 0).bind(center_element, lelement).arrowheads(None, 'arrow')

    evaluate(reference_json, xg, request)

def test_arrow_beams_as_curves(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()
    start_element = scene.ellipse('Center').center(0, 0).size(100, 100)
    
    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = 300 * math.cos(radians)
        y = 300 * math.sin(radians)
        end_element = scene.ellipse(str(angle)).center(x, y).size(80, 80)
        scene.arrow().curve(radians, radians -math.pi).bind(start_element, end_element)

    evaluate(reference_json, scene, request)

def test_arrow_curve_all_directions(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    center_element = xg.rectangle('Begin').center(0, 0).size(160, 70).roundness('round')
    element_1 = xg.ellipse('End').center(400, -200).size(130, 50)
    xg.arrow().curve('R', 'L').bind(center_element, element_1).arrowheads(None, 'arrow')
    xg.arrow().curve('U', 'U').bind(center_element, element_1).arrowheads(None, 'arrow')
    xg.arrow().curve('D', 'D').bind(center_element, element_1).arrowheads(None, 'arrow')
    xg.arrow().curve('L', 'R').bind(center_element, element_1).arrowheads(None, 'arrow')
    
    evaluate(reference_json, xg, request)

def test_arrow_curve_diff_calling_order(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()
    
    center = scene.rectangle('center').center(0, 0).size(160, 70)
    ur = scene.ellipse('up-right').center(400, -200).size(130, 50)
    ul = scene.ellipse('up-left').center(-400, -200).size(130, 50)
    dr = scene.ellipse('down-right').center(200, 300).size(130, 50)
    dl = scene.ellipse('down-left').center(-200, 300).size(130, 50)
   
    scene.arrow().bind(center, ur).arrowheads(None, 'arrow').curve('R', 'L')
    scene.arrow().bind(center, ul).arrowheads(None, 'arrow').curve('L', 'R')
    scene.arrow().bind(center, dr).arrowheads(None, 'arrow').curve('D', 'U')
    scene.arrow().bind(center, dl).arrowheads(None, 'arrow').curve('D', 'U')
    
    evaluate(reference_json, scene, request)

def test_arrow_elbows(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    center_element = xg.rectangle('Begin').center(0, 0).size(160, 70).roundness('round')
    element_1 = xg.ellipse('End').center(400, -200).size(130, 50)
    xg.arrow().elbow('R', 'L').bind(center_element, element_1).arrowheads(None, 'arrow').roundness('sharp')
    xg.arrow().elbow('U', 'U').bind(center_element, element_1).arrowheads(None, 'arrow').roundness('sharp')
    xg.arrow().elbow('D', 'D').bind(center_element, element_1).arrowheads(None, 'arrow').roundness('sharp')
    xg.arrow().elbow('L', 'R').bind(center_element, element_1).arrowheads(None, 'arrow').roundness('sharp')
    
    evaluate(reference_json, xg, request)

def test_arrow_elbows_diff_calling_order(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    center_element = xg.rectangle('Begin').center(0, 0).size(160, 70).roundness('round')
    element_1 = xg.ellipse('End').center(400, -200).size(130, 50)
    xg.arrow().bind(center_element, element_1).arrowheads(None, 'arrow').elbow('R', 'L').roundness('sharp')
    xg.arrow().bind(center_element, element_1).arrowheads(None, 'arrow').elbow('U', 'U').roundness('sharp')
    xg.arrow().bind(center_element, element_1).arrowheads(None, 'arrow').elbow('D', 'D').roundness('sharp')
    xg.arrow().bind(center_element, element_1).arrowheads(None, 'arrow').elbow('L', 'R').roundness('sharp')
    
    evaluate(reference_json, xg, request)

def test_arrow_arc(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()

    RADIUS = 300
    elements = []

    for angle in range(0, 360, 30):
        radians = angle * math.pi / 180
        x = RADIUS * math.cos(radians)
        y = RADIUS * math.sin(radians)

        rect = xg.ellipse(f'{angle}°').center(x, y).size(80, 60)
        elements.append(rect)

    start_element = elements[0]
    for i in range(1, len(elements)):
        xg.arrow().arc(radius=RADIUS).bind(start_element, elements[i])
        start_element = elements[i]

    evaluate(reference_json, xg, request)

def test_arrow_label(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    center_element = xg.rectangle('Begin').center(0, 0).size(160, 70).roundness('round')
    element_1 = xg.ellipse('End').center(400, -200).size(130, 50)
    label = xg.text().content('Label')
    xg.arrow(label).curve(0, 3.14).bind(center_element, element_1).arrowheads(None, 'arrow')
    
    evaluate(reference_json, xg, request)

def test_arrow_plain_label(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    center_element = xg.rectangle('Begin').center(0, 0).size(160, 70).roundness('round')
    element_1 = xg.ellipse('End').center(400, -200).size(130, 50)
    xg.arrow('Label').curve(0, 3.14).bind(center_element, element_1).arrowheads(None, 'arrow')
    
    evaluate(reference_json, xg, request)
