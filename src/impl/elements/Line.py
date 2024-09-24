from ..base.AbstractElement import AbstractElement
from ...config.Config import Config, DEFAULT_CONFIG
from typing import Self

class Line(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
        self.points = config.get("points", [])

    def plot(self, points: list[tuple[float, float]]) -> Self:
        self.points = points
        return self

    def color(self, color: str) -> Self:
        """Set the stroke (outline) color."""
        self.strokeColor = color
        return self
