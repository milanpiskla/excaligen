"""
Description: Base class for shapes with corners.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from .AbstractStrokedElement import AbstractStrokedElement
from .AbstractShape import AbstractShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...config.Config import Config
from typing import Self, Any

class AbstractCorneredShape(AbstractStrokedElement, AbstractShape):
    def __init__(self, type: str, listener: AbstractPlainLabelListener, config: Config):
        super().__init__(type, listener, config)
        self._roundness: str | dict[str, Any] | None = config.get("roundness", None)

    def roudness(self, roundness: str) -> Self:
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
        match roundness:
            case "sharp":
                self._roundness = None
            case "round":
                self._roundness = { "type": 3 }
            case _:
                raise ValueError(f"Invalid roundness '{roundness}'. Use 'sharp', 'round'")
        return self
