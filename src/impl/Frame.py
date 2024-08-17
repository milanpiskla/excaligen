from .base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Frame(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("frame", config)
        self.title = config.get("title", "")
        self.backgroundColor = config.get("backgroundColor", "transparent")
