"""
Description: Base class for shapes with corners.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from .AbstractStrokedElement import AbstractStrokedElement
from .AbstractShape import AbstractShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...defaults.Defaults import Defaults
from ..inputs.Roundness import Roundness
from typing import Self, Any

class AbstractCorneredShape(AbstractStrokedElement, AbstractShape):
    def __init__(self, type: str, listener: AbstractPlainLabelListener, defaults: Defaults):
        super().__init__(type, listener, defaults)
        self._roundness: str | dict[str, Any] | None = getattr("roundness", defaults)

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
