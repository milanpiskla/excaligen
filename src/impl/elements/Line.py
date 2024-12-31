"""
Description: Line element.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from ..base.AbstractLine import AbstractLine
from ...config.Config import Config, DEFAULT_CONFIG

class Line(AbstractLine):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
