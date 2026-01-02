"""
Description: Base class for shapes with corners.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details


from .AbstractStrokedElement import AbstractStrokedElement
from .AbstractShape import AbstractShape
from .AbstractRoundableElement import AbstractRoundableElement
from .AbstractLabeledElement import AbstractLabeledElement
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..elements.Text import Text
from ...defaults.Defaults import Defaults
from typing import Self, Any

class AbstractCorneredShape(AbstractStrokedElement, AbstractShape, AbstractRoundableElement, AbstractLabeledElement):
    def __init__(self, type: str, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None):
        super().__init__(type, defaults)
        self._init_labels(listener, label)
        self._roundness: str | dict[str, Any] | None = getattr(defaults, "_roundness")
