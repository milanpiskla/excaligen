"""
Description: Functional tests for various elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from .evaluate import *
from typing import Any

from pytest import FixtureRequest

def test_text_justify(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    xg = SceneBuilder()
    
    y = 0
    for baseline in ['top', 'middle', 'bottom']:
        x = -300
        for align in ['left', 'center', 'right']:
            xg.rectangle(xg.text(f'{align}-{baseline}').align(align).baseline(baseline)).size(200, 120).center(x, y)
            x += 300
        y += 150

    evaluate(reference_json, xg, request)

def test_text_anchors(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    def cross(center: tuple[float, float], color: str) -> None:
        x, y = center
        scene.line().points([[x - 20, y], [x + 20, y]]).color(color)
        scene.line().points([[x, y - 20], [x, y + 20]]).color(color)

    scene = SceneBuilder()
    x = 42.0
    y = 0.0

    for h_align in ["left", "center", "right"]:
        for v_align in ["top", "middle", "bottom"]:
            cross((x, y), 'red')
            scene.text().anchor(x, y, h_align, v_align).content(f"{h_align}-{v_align}").fontsize("M").font("Hand-drawn").color("black")
            y += 60.0

    evaluate(reference_json, scene, request)

def test_text_fonts(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()
    
    for i, font in enumerate(['Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code']):
        scene.text(f"{font}").center(0, i * 20).font(font)

    evaluate(reference_json, scene, request)

def test_text_font_size(reference_json: dict[str, Any], request: FixtureRequest) -> None:
    scene = SceneBuilder()
    
    for column, font in enumerate(['Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code']):
        y = 0
        for size in ['S', 'M', 'L', 'XL']:
            text = scene.text(f"{font} ({size})").font(font).center(column * 300, y).fontsize(size)
            w, h = text.size()
            y += h

    evaluate(reference_json, scene, request)