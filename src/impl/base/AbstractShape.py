"""
Description: Base class for shapes.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from .AbstractElement import AbstractElement
from ..colors.Color import Color
from ...config.Config import Config
from typing import Self

class AbstractShape(AbstractElement):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self._width = config.get("width", 100)
        self._height = config.get("height", 100)
        self._background_color = config.get("backgroundColor", "transparent")
        self._fill_style = config.get("fillStyle", "hachure")

    def size(self, width: float, height: float) -> Self:
        """Set the shape size."""
        return self._size(width, height)

    def background(self, color: str | Color) -> Self:
        """Set the background (fill) color as #RRGGBB, color name or Color object.."""
        self._background_color = Color.from_input(color)
        return self

    def fill(self, style: str) -> Self:
        """Set the fill style (hatchure, cross-hatch, solid)."""
        match style:
            case "hatchure" | "cross-hatch" | "solid":
                self._fill_style = style
            case _:
                raise ValueError(f"Invalid style '{style}' for fill. Use 'hatchure', 'cross-hatch', 'solid'.")
        return self

