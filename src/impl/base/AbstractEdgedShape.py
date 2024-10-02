from .AbstractShape import AbstractShape
from ...config.Config import Config
from typing import Self

class AbstractEdgedShape(AbstractShape):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self._roundness = config.get("roundness", None)

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
