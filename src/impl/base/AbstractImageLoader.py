"""
Description: Interface to image loaders.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from abc import ABC, abstractmethod
from ..images.ImageData import ImageData

class AbstractImageLoader(ABC):
    @abstractmethod
    def load_from_file(self, file_path: str) -> ImageData:
        pass

    @abstractmethod
    def load_from_data(self, data: bytes | str) -> ImageData:
        pass

    @abstractmethod
    def load_from_url(self, url: str) -> ImageData:
        pass
