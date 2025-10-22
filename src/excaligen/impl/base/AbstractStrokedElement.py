"""
Description: Base class for stroked elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from .AbstractElement import AbstractElement
from ..elements.Text import Text
from ..colors.Color import Color
from .AbstractPlainLabelListener import AbstractPlainLabelListener
from ...defaults.Defaults import Defaults

from ..inputs.Sloppiness import Sloppiness
from ..inputs.Stroke import Stroke
from ..inputs.Thickness import Thickness

from typing import Self

class AbstractStrokedElement(AbstractElement):
    def __init__(self, type: str, defaults: Defaults, listener: AbstractPlainLabelListener):
        super().__init__(type, defaults)
        self._stroke_color = getattr(defaults, "_strokeColor")
        self._stroke_width = getattr(defaults, "_strokeWidth")
        self._stroke_style = getattr(defaults, "_strokeStyle")
        self._roughness = getattr(defaults, "_roughness")
        self.__listener = listener
        self.__label: Text | None = None

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

    def label(self, text: Text | str) -> Self:
        """Set the label text for the element.

        Args:
            text (Text | str): The text element to set as the label or plain text.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        match text:
            case Text():
                self.__label = text
            case str():
                self.__label = self.__listener._on_text(text)
            case _:
                raise ValueError("Invalid type for label. Use Text or str.")

        self.__label._x = self._x + (self._width - self.__label._width) / 2  # Center horizontally
        self.__label._y = self._y + (self._height - self.__label._height - self.__label._line_height) / 2  # Center vertically

        self._add_bound_element(self.__label)
        self.__label._container_id = self._id
        return self

    def _add_group_id(self, id: str) -> None:
        """Add a group ID to the element.

        Args:
            id (str): The group ID to add.
        """
        self._group_ids.append(id)
        if self.__label:
            self.__label._group_ids.append(id)
