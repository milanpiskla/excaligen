"""
Description: Diamond shape.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from ..base.AbstractCorneredShape import AbstractCorneredShape
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ...config.Config import Config, DEFAULT_CONFIG

class Diamond(AbstractCorneredShape):
    def __init__(self, listener: AbstractPlainLabelListener, config: Config = DEFAULT_CONFIG):
        super().__init__("diamond", listener, config)
