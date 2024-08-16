from base.AbstractElement import AbstractElement
from ..config.Config import Config, DEFAULT_CONFIG

class Ellipse(AbstractElement):
    def __init__(self, config: Config):
        super().__init__("ellipse", config)
