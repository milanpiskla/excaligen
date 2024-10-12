from .AbstractElement import AbstractElement
from ...config.Config import Config
from typing import Self

class AbstractShape(AbstractElement):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self._width = config.get("width", 100)
        self._height = config.get("height", 100)
        self._background_color = config.get("backgroundColor", "transparent")
        self._fill_style = config.get("fillStyle", "hachure")
        self._is_centered__ = False

    def size(self, width: float, height: float) -> Self:
        """Set the shape size."""
        if self._is_centered__:
            self._set_position_for_new_size(width, height)

        self._width = width
        self._height = height

        return self

    def center(self, x: float, y: float) -> Self:
        """Set the center coordinates of the shape"""
        self._is_centered__ = True
        self._set_position_for_new_center(x, y)

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
    
    def _set_position_for_new_center(self, x: float, y: float) -> None:
        self._x = x - 0.5 * self._width
        self._y = y - 0.5 * self._height

    def _set_position_for_new_size(self, width: float, height: float) -> None:
        self._x = self._x + 0.5 * self._width - 0.5 * width
        self._y = self._y + 0.5 * self._height - 0.5 * height


