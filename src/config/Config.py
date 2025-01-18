"""
Description: Default configuration for elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from typing import Any
type Config = dict[str, Any]

DEFAULT_CONFIG: Config = {
    "x" : 0,
    "y" : 0,
    "width": 130,
    "height": 80,
    "opacity": 100,
    "angle": 0,
    "roughness": 1,
    "strokeStyle": "solid", 
    "strokeWidth": 1,
    "strokeColor": "#000000",
    "backgroundColor": "transparent",
    "fillStyle": "hachure",
    "roundness": { "type": 3 },
    "fontSize": 16,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "autoResize": True,
    "lineHeight": 1.25,
    "link": None
}