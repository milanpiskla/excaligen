"""
Description: Ellipse shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..base.AbstractShape import AbstractShape
from ..elements.Text import Text
from ...defaults.Defaults import Defaults
from typing import Self, override

class Ellipse(AbstractStrokedElement, AbstractShape):
    """
    A class representing an elliptical shape element.

    This class extends both AbstractStrokedElement and AbstractShape to create an
     ellipse element that can be rendered with stroke properties. The ellipse
    is defined by its center point and two radii (rx and ry).
    """
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None):
        super().__init__("ellipse", defaults, listener, label)

    @override
    def size(self, width: float, height: float) -> Self:
        """
        Set the size of the ellipse.

        Parameters:
        width (float): The width of the ellipse.
        height (float): The height of the ellipse.

        Returns:
        Self: The instance of the ellipse with the updated size.
        """
        return self._size(width, height)._center_label()