"""
Description: Diamond shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractCorneredShape import AbstractCorneredShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...defaults.Defaults import Defaults

class Diamond(AbstractCorneredShape):
    """A class representing a diamond shape in the diagram.

    Diamond shape is a four-sided polygon with equal sides and opposite angles equal.
    """
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener):
        super().__init__("diamond", defaults, listener)
