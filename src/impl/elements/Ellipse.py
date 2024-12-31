"""
Description: Ellipse shape.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..base.AbstractShape import AbstractShape
from ...config.Config import Config, DEFAULT_CONFIG

class Ellipse(AbstractStrokedElement, AbstractShape):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("ellipse", config)
