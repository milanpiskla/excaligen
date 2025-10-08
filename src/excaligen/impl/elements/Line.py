"""
Description: Line element.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractLine import AbstractLine
from ..colors.Color import Color
from ...config.Config import Config, DEFAULT_CONFIG
from typing import Self

class Line(AbstractLine):
    """A line element that draws a straight or curved line segments between the given points.

    This class represents a line element in the drawing canvas.
    It provides functionality for creating and manipulating straight pr curved lines with specified 
    configurations for styling and positioning.
    """
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
        self._background_color = config.get("backgroundColor", "transparent")

    def background(self, color: str | Color) -> Self:
        """
        Set the background (fill) color.
        Args:
            color (str | Color): The background color, specified as a hex string (#RRGGBB), 
                     a color name, or a Color object.
        
        Returns:
            Self: The instance of the class for method chaining.
        """
        self._background_color = Color.from_input(color)
        return self

    def close(self):
        """Close the line by connecting the last point to the first point."""
        if len(self._points) > 2:
            self._points.append(self._points[0])
        return self

