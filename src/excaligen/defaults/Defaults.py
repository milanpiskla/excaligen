"""
Description: Default values for elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..impl.inputs.Sloppiness import Sloppiness
from ..impl.inputs.Stroke import Stroke
from ..impl.inputs.Thickness import Thickness

from typing import Self

class Defaults:
    def __init__(self):
        self._x: float = 0,
        self._y: float = 0,
        self._width: float = 130,
        self._height: float = 80,
        self._opacity:int = 100,
        self._angle: float = 0,
        self._roughness: int | str = 1,
        self._strokeStyle: str = "solid", 
        self._strokeWidth: float = 1,
        self._strokeColor: str = "#000000",
        self._backgroundColor: str = "transparent",
        self._fillStyle: str = "hachure",
        self._roundness: any = { "type" : 3 },
        self._fontSize = 16,
        self._fontFamily:int = 1,
        self._textAlign: str = "center",
        self._verticalAlign: str = "middle",
        self._autoResize = True,
        self._lineHeight: float = 1.25,
        self._link = None

    def position(self, x: float, y: float) -> Self:
        """
        Sets the position of the element.

        Args:
            x (float): The x-coordinate of the element.
            y (float): The y-coordinate of the element.

        Returns:
            Self: The instance defaults with updated position.
        """
        self.x = x
        self.y = y
        return self
    
    def size(self, width: float, height: float) -> Self:
        """
        Sets the size of the element.

        Args:
            width (float): The width of the element.
            height (float): The height of the element.

        Returns:
            Self: The instance defaults with updated size.
        """
        self.width = width
        self.height = height
        return self
    
    def opacity(self, opacity: int) -> Self:
        """
        Sets the opacity of the element.

        Args:
            opacity (int): The opacity of the element (0-100).

        Returns:
            Self: The instance defaults with updated opacity.

                    Raises:
            ValueError: If the opacity value is not within the range 0-100.
        """
        if not (0 <= opacity <= 100):
            raise ValueError("Opacity values must be in the range: 0-100.")
        self._opacity = opacity
        return self

    def rotate(self, angle: float) -> Self:
        """
        Sets the rotation angle of the element.

        Args:
            angle (float): The rotation angle in radians.

        Returns:
            Self: The instance defaults with updated angle.
        """
        self._angle = angle
        return self
    
    def sloppiness(self, sloppiness: int | str) -> Self:
        """
        Sets the sloppiness of the element.

        Args:
            sloppiness (int | str): The sloppiness value to set, specified as an integer (0, 1, 2) or a string ('architect', 'artist', 'cartoonist').

        Returns:
            Self: The instance defaults with updated sloppiness.
        """
        self._roughness = Sloppiness.from_(sloppiness)
        return self
    
    def stroke(self, stroke: str) -> Self:
        """
        Sets the stroke style of the element.

        Args:
            stroke (str): The stroke style to set, specified as a string ('solid', 'dashed', 'dotted').

        Returns:
            Self: The instance defaults with updated stroke style.
        """
        self._strokeStyle = Stroke.from_(stroke)
        return self
    
    def thickness(self, thickness: int | str) -> Self:
        """
        Sets the stroke thickness of the element.

        Args:
            thickness (int | str): The thickness to set, specified as an integer (1, 2, 3) or a string ('thin', 'bold', 'extra-bold').

        Returns:
            Self: The instance defaults with updated stroke thickness.
        """
        self._strokeWidth = Thickness.from_(thickness)
        return self
    