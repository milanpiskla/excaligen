"""
Description: Rectangle shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractCorneredShape import AbstractCorneredShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..elements.Text import Text
from ...defaults.Defaults import Defaults
from typing import Self, override

class Rectangle(AbstractCorneredShape):
    """
    A class representing a rectangular shape in a 2D space.

    The rectangle is defined by its position and dimensions,
    and can be configured with various visual properties through the config parameter.

    > [!WARNING]
    > Do not instantiate this class directly. Use `SceneBuilder.rectangle()` instead.
    """
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None):
        super().__init__("rectangle", defaults, listener, label)

    @override
    def size(self, width: float, height: float) -> Self:
        """
        Set the size of the rectangle.

        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

        Returns:
        Self: The instance of the rectangle with the updated size.
        """
        return self._size(width, height)._justify_label()