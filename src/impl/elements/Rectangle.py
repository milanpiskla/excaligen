from ..base.AbstractCorneredShape import AbstractCorneredShape
from ...config.Config import Config, DEFAULT_CONFIG

class Rectangle(AbstractCorneredShape):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("rectangle", config)
