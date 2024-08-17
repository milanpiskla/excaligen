from .base.AbstractShape import AbstractShape
from ..config.Config import Config, DEFAULT_CONFIG

class Rectangle(AbstractShape):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("rectangle", config)
        self.roundness = config.get("roundness", None)
