from .AbstractStrokedElement import AbstractStrokedElement
from .AbstractShape import AbstractShape
from ...config.Config import Config
from typing import Self

class AbstractCorneredShape(AbstractStrokedElement, AbstractShape):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self._roundness = config.get("roundness", None)

    def roudness(self, roundness: str) -> Self:
        """Set the roundness style (sharp, round)."""
        match roundness:
            case "sharp":
                self._roundness = None
            case "round":
                self._roundness = { "type": 3 }
            case _:
                raise ValueError(f"Invalid edges '{roundness}'. Use 'sharp', 'round'")
        return self
