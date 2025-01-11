"""
Description: Base class for stroked elements.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from .AbstractElement import AbstractElement
from ..elements.Text import Text
from ..colors.Color import Color
from .AbstractPlainLabelListener import AbstractPlainLabelListener
from ...config.Config import Config
from typing import Self

class AbstractStrokedElement(AbstractElement):
    def __init__(self, type: str, listener: AbstractPlainLabelListener, config: Config):
        super().__init__(type, config)
        self._stroke_color = config.get("strokeColor", "#000000")
        self._stroke_width = config.get("strokeWidth", 1)
        self._stroke_style = config.get("strokeStyle", "solid")
        self._roughness = config.get("roughness", 1)
        self.__listener = listener
        self.__label: Text | None = None

    def color(self, color: str | Color) -> Self:
        """Set the stroke (outline) color as #RRGGBB, color name or Color object.

        Args:
            color (str | Color): The color to set, specified as a hex string $RRGGBB, color name, or Color object.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        self._stroke_color = Color.from_input(color)
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
        match thickness:
            case 1 | 2 | 3:
                self._stroke_width = thickness
            case "thin":
                self._roughness = 0
            case "bold":
                self._roughness = 1
            case "extra-bold":
                self._roughness = 2
            case _:
                raise ValueError(f"Invalid thickness '{thickness}'. Use 1, 2, 3 or 'thin', 'bold', 'extra-bold'.")
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
        match value:
            case 0 | 1 | 2:
                self._roughness = value
            case "architect":
                self._roughness = 0
            case "artist":
                self._roughness = 1
            case "cartoonist":
                self._roughness = 2
            case _:
                raise ValueError(f"Invalid value '{value}' for sloppiness. Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'.")
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
        match style:
            case "solid" | "dotted" | "dashed":
                self._stroke_style = style
            case _:
                raise ValueError(f"Invalid style '{style}' for stroke. Use 'solid', 'dotted', 'dashed'.")
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
                self.__label = self.__listener.on_text(text)
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
