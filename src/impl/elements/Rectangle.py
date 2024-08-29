from ..base.AbstractEdgedShape import AbstractEdgedShape
from ...config.Config import Config, DEFAULT_CONFIG

class Rectangle(AbstractEdgedShape):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("rectangle", config)
