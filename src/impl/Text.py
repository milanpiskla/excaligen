from base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Text(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("text", config)
        self.text = config.get("text", "")
        self.fontSize = config.get("fontSize", 16)
        self.fontFamily = config.get("fontFamily", 1)
        self.textAlign = config.get("textAlign", "center")
        self.verticalAlign = config.get("verticalAlign", "middle")
        self.lineHeight = config.get("lineHeight", 1.25)
        self.autoResize = config.get("autoResize", True)
