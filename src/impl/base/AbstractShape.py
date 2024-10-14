from .AbstractElement import AbstractElement
from ..helpers.ElementCenterer import ElementCenterer
from ...config.Config import Config
from typing import Self

class AbstractShape(AbstractElement):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self._width = config.get("width", 100)
        self._height = config.get("height", 100)
        self._background_color = config.get("backgroundColor", "transparent")
        self._fill_style = config.get("fillStyle", "hachure")
        self.__centerer = ElementCenterer(self)

    def size(self, width: float, height: float) -> Self:
        """Set the shape size."""
        self.__centerer.size(width, height)

        self._width = width
        self._height = height

        return self

    def center(self, x: float, y: float) -> Self:
        """Set the center coordinates of the shape"""
        self.__centerer.center(x, y)

        return self

    def background(self, color: str) -> Self:
        """Set the background (fill) color."""
        self._background_color = color
        return self

    def fill(self, style: str) -> Self:
        """Set the fill style (hatchure, cross-hatch, solid)."""
        match style:
            case "hatchure" | "cross-hatch" | "solid":
                self._fill_style = style
            case _:
                raise ValueError(f"Invalid style '{style}' for fill. Use 'hatchure', 'cross-hatch', 'solid'.")
        return self

