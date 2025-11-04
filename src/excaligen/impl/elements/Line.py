"""
Description: Line element.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractLine import AbstractLine
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..elements.Text import Text
from ..colors.Color import Color
from ..inputs.Fill import Fill
from ...defaults.Defaults import Defaults
from typing import Self

class Line(AbstractLine):
    """A line element that draws a straight or curved line segments between the given points.

    This class represents a line element in the drawing canvas.
    It provides functionality for creating and manipulating straight pr curved lines with specified 
    configurations for styling and positioning.
    """
    def __init__(self, defaults: Defaults):
        class DummyListener(AbstractPlainLabelListener):
            def _on_text(self, text: str) -> Text:
                return Text(defaults)

        super().__init__("line", defaults, DummyListener())
        self._background_color = getattr(defaults, "_background_color")
        self._fill_style = getattr(defaults, "_fill_style")

    def background(self, color: str | Color) -> Self:
        """
        Set the background (fill) color of the shape created by a closed line segments.
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
        Set the fill style for the shape created by a closed line segments.

        Parameters:
        style (str): The fill style to be applied. Must be one of 'hatchure', 'cross-hatch', or 'solid'.

        Returns:
        Self: The instance of the shape with the updated fill style.

        Raises:
        ValueError: If the provided style is not one of 'hatchure', 'cross-hatch', or 'solid'.
        """
        self._fill_style = Fill.from_(style)
        return self
    
    def close(self):
        """Close the line by connecting the last point to the first point."""
        if len(self._points) > 2:
            self._points.append(self._points[0])
        return self

