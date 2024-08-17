from .base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Line(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
        self.points = config.get("points", [])
