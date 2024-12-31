"""
Description: Base class for all Excalidraw elements.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

import uuid
from typing import Self
from ...config.Config import Config

# TODO make it consistent with excalidraw/packages/excalidraw/element/types.ts

class AbstractElement:
    """Base class for all Excalidraw elements."""

    def __init__(self, element_type: str, config: Config):
        self._type = element_type
        self._id = str(uuid.uuid4())
        self._seed = int(uuid.uuid4().int % 1000000000)
        self._version = 1
        self._version_nonce = int(uuid.uuid4().int % 1000000000)
        self._is_deleted = False
        self._x: float = config.get("x", 0)
        self._y: float = config.get("y", 0)
        self._width = 0.0
        self._height = 0.0
        self._opacity: int = config.get("opacity", 100)
        self._angle = config.get("angle", 0)
        self._index: str | None = None
        self._group_ids: list[str] = []
        self._frame_id: str | None = None
        self._link: None | str = None
        self._bound_elements = None
        self.__is_centered = False

    def position(self, x: float, y: float) -> Self:
        self._x = x
        self._y = y
        return self
    
    def center(self, x: float, y: float) -> Self:
        self.__is_centered = True
        self._x = x - 0.5 * self._width
        self._y = y - 0.5 * self._height
        return self

    def rotate(self, angle: float) -> Self:
        self._angle = angle
        return self

    def opacity(self, opacity: int) -> Self:
        if not (0 <= opacity <= 100):
            raise ValueError("Opacity values must be in the range: 0-100.")
        self._opacity = opacity
        return self

    def link(self, target: "str | AbstractElement") -> Self:
        match target:
            case AbstractElement():
                self._link = f"https://excalidraw.com/?element={target._id}"
            case str():
                self._link = target
            case _:
                raise ValueError("Link target must be a string or an AbstractElement.")
        return self

    def get_center(self) -> tuple[float, float]:
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
