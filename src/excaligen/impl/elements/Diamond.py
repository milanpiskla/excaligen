"""
Description: Diamond shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractCorneredShape import AbstractCorneredShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..elements.Text import Text
from ...defaults.Defaults import Defaults
from typing import Self, override

class Diamond(AbstractCorneredShape):
    """A class representing a diamond shape in the diagram.

    Diamond shape is a four-sided polygon with equal sides and opposite angles equal.
    """
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None):
        super().__init__("diamond", defaults, listener, label)

    @override
    def size(self, width: float, height: float) -> Self:
        """
        Set the size of the diamond.

        Parameters:
        width (float): The width of the diamond.
        height (float): The height of the diamond.

        Returns:
        Self: The instance of the diamond with the updated size.
        """
        return self._size(width, height)._center_label()
    