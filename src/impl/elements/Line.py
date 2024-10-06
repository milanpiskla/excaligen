from ..base.AbstractStrokedElement import AbstractStrokedElement
from ...config.Config import Config, DEFAULT_CONFIG
from typing import Self

class Line(AbstractStrokedElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
        self._points = config.get("points", [])
        self._roundness = config.get("roundness", None)

    def points(self, points: list[tuple[float, float]]) -> Self:
        self._points = points
        return self

    def edges(self, edges: str) -> Self:
        """Set the roundness style (sharp, round)."""
        match edges:
            case "sharp":
                self._roundness = None
            case "round":
                self._roundness = { "type": 3 }
            case _:
                raise ValueError(f"Invalid edges '{edges}'. Use 'sharp', 'round'")
        return self
