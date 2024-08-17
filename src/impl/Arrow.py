from .base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Arrow(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("arrow", config)
        self.start = config.get("start", None)
        self.end = config.get("end", None)
        self.startArrowhead = config.get("startArrowhead", None)
        self.endArrowhead = config.get("endArrowhead", "arrow")
        self.points = config.get("points", [])
