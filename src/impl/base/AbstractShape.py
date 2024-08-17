from .AbstractElement import AbstractElement
from ...config.Config import Config
from typing import Self

class AbstractShape(AbstractElement):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self.width = config.get("width", 100)
        self.height = config.get("height", 100)

    def size(self, width: float, height: float) -> Self:
        self.width = width
        self.height = height

        return self