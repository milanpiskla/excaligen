"""
Description: Base class for lines and arrows.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...defaults.Defaults import Defaults
from ..geometry.Point import Point
from ..inputs.Roundness import Roundness
from typing import Self

class AbstractLine(AbstractStrokedElement):
    def __init__(self, type: str, defaults: Defaults, listener: AbstractPlainLabelListener | None = None):
        super().__init__(type, listener, defaults)
        self._points: list[Point] = []
        self._roundness = getattr("_roundness", defaults)

    def points(self, points: list[Point]) -> Self:
        """
        Sets the points for the line and calculates the width and height.
        Args:
            points (list[Point]): A list of Point objects representing the coordinates of the line.
        Returns:
            Self: The instance of the class with updated points, width, and height.
        """
        self._points = points

        x_coords, y_coords = zip(*points)
        self._width = max(x_coords) - min(x_coords)
        self._height = max(y_coords) - min(y_coords)

        return self

    def roundness(self, roundness: str) -> Self:
        """
        Set the roundness style of the shape.

        Parameters:
        roundness (str): The roundness style to set. Acceptable values are:
                 - "sharp": Sets the shape to have sharp corners.
                 - "round": Sets the shape to have rounded corners.

        Returns:
        Self: The instance of the shape with the updated roundness style.

        Raises:
        ValueError: If the provided roundness style is not "sharp" or "round".
        """
        self._roundness = Roundness.from_(roundness)
        return self
