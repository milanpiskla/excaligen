"""
Description: Diamond shape.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractCorneredShape import AbstractCorneredShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...defaults.Defaults import Config, DEFAULT_CONFIG

class Diamond(AbstractCorneredShape):
    """A class representing a diamond shape in the diagram.

    Diamond shape is a four-sided polygon with equal sides and opposite angles equal.
    """
    def __init__(self, listener: AbstractPlainLabelListener, config: Config = DEFAULT_CONFIG):
        super().__init__("diamond", listener, config)
