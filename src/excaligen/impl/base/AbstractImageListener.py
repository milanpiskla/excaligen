"""
Description: Interface to image listeners.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from abc import ABC, abstractmethod

class AbstractImageListener(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _on_image(self, id: str, mime_type: str, data_url: str) -> None:
        pass

