from ..config.Config import Config, DEFAULT_CONFIG
from .Rectangle import Rectangle
from .Diamond import Diamond
from .Ellipse import Ellipse

class ElementFactory():
    def __init__(self):
        self.config = DEFAULT_CONFIG

    def config(self, config: Config):
        self.config = config
        return self

    def rectangle(self):
        return Rectangle(self.config)

    def diamond(self):
        return Diamond(self.config)

    def ellipse(self):
        return Ellipse(self.config)

    # TODO: add other Excalidraw elements
