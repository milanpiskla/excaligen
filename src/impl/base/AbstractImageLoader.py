from abc import ABC, abstractmethod
from typing import Union
from ..images.ImageData import ImageData

class AbstractImageLoader(ABC):
    @abstractmethod
    def load_from_file(self, file_path: str) -> ImageData:
        pass

    @abstractmethod
    def load_from_data(self, data: Union[bytes, str]) -> ImageData:
        pass
