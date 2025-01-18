"""
A listener for handling plain text labels in the system.

This abstract base class defines the interface for processing plain text labels.
Concrete implementations should override the _on_text method to specify how
text labels should be handled.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from abc import ABC, abstractmethod
from ..elements.Text import Text

class AbstractPlainLabelListener(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _on_text(self, text: str) -> Text:
        pass
