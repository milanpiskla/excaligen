from ..base.AbstractStrokedElement import AbstractStrokedElement
from ...config.Config import Config, DEFAULT_CONFIG
from ..geometry.Point import Point
from typing import Self

class AbstractLine(AbstractStrokedElement):
    def __init__(self, type: str, config: Config = DEFAULT_CONFIG):
        super().__init__(type, config)
        self._points: list[Point] = []
        self._roundness = config.get("roundness", None)

    def points(self, points: list[Point]) -> Self:
        self._points = points

        x_coords, y_coords = zip(*points)
        self._width = max(x_coords) - min(x_coords)
        self._height = max(y_coords) - min(y_coords)

        return self

    def roundness(self, roundness: str) -> Self:
        """Set the roundness style (sharp, round)."""
        match roundness:
            case "sharp":
                self._roundness = None
            case "round":
                self._roundness = { "type": 3 }
            case _:
                raise ValueError(f"Invalid edges '{roundness}'. Use 'sharp', 'round'")
        return self
