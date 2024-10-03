import uuid
from typing import Self, Union
from ..base.AbstractShape import AbstractShape
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractImageLoader import AbstractImageLoader
from ..base.ImageData import ImageData
from ...config.Config import Config, DEFAULT_CONFIG

class Image(AbstractShape):
    def __init__(self, listener: AbstractImageListener, loader: AbstractImageLoader, config: Config = DEFAULT_CONFIG):
        super().__init__("image", config)
        self._file_id = str(uuid.uuid4())
        self._scale = [1, 1]
        self._status = "pending"
        self._stroke_color = "#808080"
        self._background_color = "transparent"
        self.__listener = listener
        self.__loader = loader

    def file(self, path: str) -> Self:
        """Load image data from a file and set it."""
        image_data = self.__loader.load_from_file(path)
        self._apply_image_data(image_data)
        return self

    def data(self, data: Union[bytes, str]) -> Self:
        """Set image data from raw bytes or SVG string."""
        image_data = self.__loader.load_from_data(data)
        self._apply_image_data(image_data)
        return self

    def _apply_image_data(self, image_data: ImageData) -> None:
        """Apply image data to the Image element."""
        self.size(image_data.width, image_data.height)
        self.__listener.on_image(self._file_id, image_data.mime_type, image_data.data_url)

    def fit(self, max_width: float, max_height: float) -> Self:
        """Scale the image to fit within a bounding box while maintaining aspect ratio."""
        original_width, original_height = self._width, self._height

        if original_width == 0 or original_height == 0:
            return self  # Avoid division by zero

        width_ratio = max_width / original_width
        height_ratio = max_height / original_height
        scaling_factor = min(width_ratio, height_ratio)

        new_width = original_width * scaling_factor
        new_height = original_height * scaling_factor

        return self.size(new_width, new_height)
