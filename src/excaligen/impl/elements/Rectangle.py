"""
Description: Rectangle shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractCorneredShape import AbstractCorneredShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...config.Config import Config, DEFAULT_CONFIG

class Rectangle(AbstractCorneredShape):
    """
    A class representing a rectangular shape in a 2D space.

    The rectangle is defined by its position and dimensions,
    and can be configured with various visual properties through the config parameter.
    """
    def __init__(self, listener: AbstractPlainLabelListener, config: Config = DEFAULT_CONFIG):
        super().__init__("rectangle", listener, config)
