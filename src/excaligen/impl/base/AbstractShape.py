"""
Description: Base class for shapes.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from .AbstractElement import AbstractElement
from ..colors.Color import Color
from ...defaults.Defaults import Defaults
from ..inputs.Fill import Fill
from typing import Self

class AbstractShape(AbstractElement):
    def __init__(self, type: str, defaults: Defaults):
        super().__init__(type, defaults)
        self._width = getattr(defaults, "_width")
        self._height = getattr(defaults, "_height")
        self._background_color = getattr(defaults, "_background_color")
        self._fill_style = getattr(defaults, "_fill_style")

    def size(self, width: float, height: float) -> Self:
        """
        Set the size of the shape.

        Parameters:
        width (float): The width of the shape.
        height (float): The height of the shape.

        Returns:
        Self: The instance of the shape with the updated size.
        """
        return self._size(width, height)

    def background(self, color: str | Color) -> Self:
        """
        Set the background (fill) color.
        Args:
            color (str | Color): The background color, specified as a hex string (#RRGGBB), 
                     a color name, or a Color object.
        
        Returns:
            Self: The instance of the class for method chaining.
        """
        self._background_color = Color.from_(color)
        return self

    def fill(self, style: str) -> Self:
        """
        Set the fill style for the shape.

        Parameters:
        style (str): The fill style to be applied. Must be one of 'hachure', 'cross-hatch', or 'solid'.

        Returns:
        Self: The instance of the shape with the updated fill style.

        Raises:
        ValueError: If the provided style is not one of 'hachure', 'cross-hatch', or 'solid'.
        """
        self._fill_style = Fill.from_(style)
        return self

