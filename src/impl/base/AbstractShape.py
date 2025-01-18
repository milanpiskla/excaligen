"""
Description: Base class for shapes.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

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
        self._background_color = Color.from_input(color)
        return self

    def fill(self, style: str) -> Self:
        """
        Set the fill style for the shape.

        Parameters:
        style (str): The fill style to be applied. Must be one of 'hatchure', 'cross-hatch', or 'solid'.

        Returns:
        Self: The instance of the shape with the updated fill style.

        Raises:
        ValueError: If the provided style is not one of 'hatchure', 'cross-hatch', or 'solid'.
        """
        match style:
            case "hatchure" | "cross-hatch" | "solid":
                self._fill_style = style
            case _:
                raise ValueError(f"Invalid style '{style}' for fill. Use 'hatchure', 'cross-hatch', 'solid'.")
        return self

