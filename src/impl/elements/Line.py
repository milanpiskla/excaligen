from ..base.AbstractLine import AbstractLine
from ...config.Config import Config, DEFAULT_CONFIG
from typing import Self

class Line(AbstractLine):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
