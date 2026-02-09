"""
Description: Base class for lines and arrows.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details


from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..base.AbstractRoundableElement import AbstractRoundableElement
from ...defaults.Defaults import Defaults
from ..geometry.Point import Point
from typing import Self

class AbstractLine(AbstractStrokedElement, AbstractRoundableElement):
    def __init__(self, type: str, defaults: Defaults):
        super().__init__(type, defaults)
        self._points: list[Point] = []
        self._roundness = getattr(defaults, "_roundness")

    def points(self, points: list[Point]) -> Self:
        """
        Sets the points for the line and calculates the width and height.
        Args:
            points (list[Point]): A list of Point objects representing the coordinates of the line.
        Returns:
            Self: The instance of the class with updated points, width, and height.
        """
        self._points = points
        self.__update_width_height()

        return self

    def append(self, points: list[Point]) -> Self:
        """
        Appends points to the line.
        Args:
            points (list[Point]): A list of Point objects to append.
        Returns:
            Self: The instance of the class with updated points, width, and height.
        """
        self._points.extend(points)
        self.__update_width_height()

        return self

    def prepend(self, points: list[Point]) -> Self:
        """
        Prepends points to the line.
        Args:
            points (list[Point]): A list of Point objects to prepend.
        Returns:
            Self: The instance of the class with updated points, width, and height.
        """
        self._points = points + self._points
        self.__update_width_height()

        return self

    def __update_width_height(self) -> None:
        """
        Updates the width and height of the line.
        """
        x_coords, y_coords = zip(*self._points)
        self._width = max(x_coords) - min(x_coords)
        self._height = max(y_coords) - min(y_coords)
