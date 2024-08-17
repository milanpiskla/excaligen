from .base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Diamond(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("diamond", config)
        self.width = config.get("width", 100)
        self.height = config.get("height", 100)
