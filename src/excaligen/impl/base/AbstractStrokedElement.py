"""
Description: Base class for stroked elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from .AbstractElement import AbstractElement
from ...defaults.Defaults import Defaults
from ..colors.Color import Color

from ..inputs.Sloppiness import Sloppiness
from ..inputs.Stroke import Stroke
from ..inputs.Thickness import Thickness

from typing import Self


class AbstractStrokedElement(AbstractElement):
    def __init__(self, type: str, defaults: Defaults):
        super().__init__(type, defaults)
        self._stroke_color = getattr(defaults, "_stroke_color")
        self._stroke_width = getattr(defaults, "_stroke_width")
        self._stroke_style = getattr(defaults, "_stroke_style")
        self._roughness = getattr(defaults, "_roughness")

    def color(self, color: str | Color) -> Self:
        """Set the stroke (outline) color as #RRGGBB, color name or Color object.

        Args:
            color (str | Color): The color to set, specified as a hex string $RRGGBB, color name, or Color object.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        self._stroke_color = Color.from_(color)
        return self

    def thickness(self, thickness: int | str) -> Self:
        """Set the stroke thickness by int (1, 2, 3) or by string ('thin', 'bold', 'extra-bold').

        Args:
            thickness (int | str): The thickness to set, specified as an integer (1, 2, 3) or a string ('thin', 'bold', 'extra-bold').

        Raises:
            ValueError: If an invalid thickness value is provided.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        self._stroke_width = Thickness.from_(thickness)
        return self

    def sloppiness(self, value: int | str) -> Self:
        """Set the stroke sloppiness by int (0, 1, 2) or by string ('architect', 'artist', 'cartoonist').

        Args:
            value (int | str): The sloppiness value to set, specified as an integer (0, 1, 2) or a string ('architect', 'artist', 'cartoonist').

        Raises:
            ValueError: If an invalid sloppiness value is provided.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        self._roughness = Sloppiness.from_(value)
        return self

    def stroke(self, style: str) -> Self:
        """Set the stroke style (solid, dotted, dashed).

        Args:
            style (str): The stroke style to set, specified as 'solid', 'dotted', or 'dashed'.

        Raises:
            ValueError: If an invalid stroke style is provided.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        self._stroke_style = Stroke.from_(style)
        return self
