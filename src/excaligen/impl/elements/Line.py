"""
Description: Line element.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractLine import AbstractLine
from ...config.Config import Config, DEFAULT_CONFIG

class Line(AbstractLine):
    """A line element that draws a straight or curved line segments between the given points.

    This class represents a line element in the drawing canvas.
    It provides functionality for creating and manipulating straight pr curved lines with specified 
    configurations for styling and positioning.
    """
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("line", config)
