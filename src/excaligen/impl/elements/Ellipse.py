"""
Description: Ellipse shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..base.AbstractShape import AbstractShape
from ...defaults.Defaults import Defaults

class Ellipse(AbstractStrokedElement, AbstractShape):
    """
    A class representing an elliptical shape element.

    This class extends both AbstractStrokedElement and AbstractShape to create an
     ellipse element that can be rendered with stroke properties. The ellipse
    is defined by its center point and two radii (rx and ry).
    """
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener):
        super().__init__("ellipse", defaults, listener)
