"""
Description: Base class for all Excalidraw elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import uuid
from typing import Self
from ...defaults.Defaults import Defaults

from ..inputs.Opacity import Opacity

# TODO make it consistent with excalidraw/packages/excalidraw/element/types.ts

class AbstractElement:
    """Base class for all Excalidraw elements."""

    def __init__(self, element_type: str, defaults: Defaults):
        self._type = element_type
        self._id = str(uuid.uuid4())
        self._seed = int(uuid.uuid4().int % 1000000000)
        self._version: int = 1
        self._version_nonce = int(uuid.uuid4().int % 1000000000)
        self._is_deleted = False
        self._x: float = 0
        self._y: float = 0
        self._width: float = getattr(defaults, "_width")
        self._height: float = getattr(defaults, "_height")
        self._opacity: int = getattr(defaults, "_opacity")
        self._angle: float = getattr(defaults, "_angle")
        self._index: str | None = None
        self._group_ids: list[str] = []
        self._frame_id: str | None = None
        self._link: None | str = None
        self._bound_elements = None
        self.__is_centered = False

    def position(self, x: float, y: float) -> Self:
        """
        Sets the position of the element.

        Args:
            x (float): The x-coordinate of the element.
            y (float): The y-coordinate of the element.

        Returns:
            Self: The instance of the element with updated position.
        """
        self._x = x
        self._y = y
        return self
    
    def center(self, x: float, y: float) -> Self:
        """
        Centers the element at the given (x, y) coordinates.

        This method sets the element's position such that its center is located
        at the specified (x, y) coordinates. It also marks the element as centered.

        Args:
            x (float): The x-coordinate to center the element.
            y (float): The y-coordinate to center the element.

        Returns:
            Self: The instance of the element, allowing for method chaining.
        """
        self.__is_centered = True
        self._x = x - 0.5 * self._width
        self._y = y - 0.5 * self._height
        return self

    def rotate(self, angle: float) -> Self:
        """
        Rotate the element clockwise by a specified angle.

        Args:
            angle (float): The angle to rotate the element clockwise by, in radians.

        Returns:
            Self: The instance of the element after rotation.
        """
        self._angle = angle
        return self

    def opacity(self, opacity: int) -> Self:
        """
        Set the opacity of the element.

        Args:
            opacity (int): The opacity value to set, must be in the range 0-100. 100 is fully opaque, 0 is fully transparent.

        Returns:
            Self: The instance of the element with updated opacity.

        Raises:
            ValueError: If the opacity value is not within the range 0-100.
        """
        self._opacity = Opacity.from_(opacity)
        return self

    def link(self, target: "str | AbstractElement") -> Self:
        """
        Establishes a link to the given target, which can be either a string URL or an AbstractElement instance.

        Args:
            target (str | AbstractElement): The target to link to. If it's an AbstractElement, a URL will be generated using its ID. 
                             If it's a string, it will be used directly as the link.

        Returns:
            Self: The instance of the current object with the updated link.

        Raises:
            ValueError: If the target is neither a string nor an AbstractElement.
        """
        match target:
            case AbstractElement():
                self._link = f"https://excalidraw.com/?element={target._id}"
            case str():
                self._link = target
            case _:
                raise ValueError("Link target must be a string or an AbstractElement.")
        return self

    def get_center(self) -> tuple[float, float]:
        """
        Calculate and return the center coordinates of the element.

        Returns:
            tuple[float, float]: A tuple containing the x and y coordinates of the center of the element.
        """
        return (self._x + 0.5 * self._width, self._y + 0.5 * self._height)

    def _size(self, width: float, height: float) -> Self:
        """Set the shape size."""
        if self.__is_centered:
            self._x = self._x + 0.5 * self._width - 0.5 * width
            self._y = self._y + 0.5 * self._height - 0.5 * height

        self._width = width
        self._height = height
        
        return self

    def _add_bound_element(self, element: "AbstractElement") -> None:
        self._bound_elements = self._bound_elements or []

        if not element._id in self._bound_elements: # TODO check if this works to prevent binding twice
            self._bound_elements.append({"id": element._id, "type": element._type})
