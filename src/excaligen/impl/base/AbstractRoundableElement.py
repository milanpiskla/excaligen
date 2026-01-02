"""
Description: Mixin for elements that support roundness.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from typing import Self, Any
from ..inputs.Roundness import Roundness
from ...defaults.Defaults import Defaults

class AbstractRoundableElement:
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
