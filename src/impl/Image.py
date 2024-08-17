from .base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Image(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("image", config)
        self.src = config.get("src", "")
        self.width = config.get("width", 100)
        self.height = config.get("height", 100)
        self.scale = config.get("scale", 1)
