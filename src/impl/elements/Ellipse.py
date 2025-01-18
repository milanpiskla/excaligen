"""
Description: Ellipse shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..base.AbstractShape import AbstractShape
from ...config.Config import Config, DEFAULT_CONFIG

class Ellipse(AbstractStrokedElement, AbstractShape):
    def __init__(self, listener: AbstractPlainLabelListener, config: Config = DEFAULT_CONFIG):
        super().__init__("ellipse", listener, config)
