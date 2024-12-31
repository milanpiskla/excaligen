"""
Description: Image element.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

import uuid
from typing import Self
from ..base.AbstractElement import AbstractElement
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractImageLoader import AbstractImageLoader
from ..images.ImageData import ImageData
from ...config.Config import Config, DEFAULT_CONFIG

class Image(AbstractElement):
    def __init__(self, listener: AbstractImageListener, loader: AbstractImageLoader, config: Config = DEFAULT_CONFIG):
        super().__init__("image", config)
        self._file_id = str(uuid.uuid4())
        self._scale = [1, 1]
        self._status = "pending"
        self._background_color = "transparent"
        self._width = 0
        self._height = 0
        self.__listener = listener
        self.__loader = loader

    def file(self, path: str) -> Self:
        """Load image data from a file and set it.

        Args:
            path (str): The path to the image file.

        Returns:
            Self: The current instance of the Image class.
        """
        image_data = self.__loader.load_from_file(path)
        self._apply_image_data(image_data)
        return self

    def data(self, data: bytes | str) -> Self:
        """Set image data from raw bytes or SVG string.

        Args:
            data (bytes | str): The raw image data or SVG string.

        Returns:
            Self: The current instance of the Image class.
        """
        image_data = self.__loader.load_from_data(data)
        self._apply_image_data(image_data)
        return self

    def url(self, url: str) -> Self:
        """Load image data from a URL and set it.

        Args:
            url (str): The URL to the image.

        Returns:
            Self: The current instance of the Image class.
        """
        image_data = self.__loader.load_from_url(url)
        self._apply_image_data(image_data)
        return self

    def _apply_image_data(self, image_data: ImageData) -> None:
        """Apply image data to the Image element.

        Args:
            image_data (ImageData): The image data to apply.
        """
        self._size(image_data.width, image_data.height)
        self.__listener.on_image(self._file_id, image_data.mime_type, image_data.data_url)

    def fit(self, max_width: float, max_height: float) -> Self:
        """Scale the image to fit within a bounding box while maintaining aspect ratio.

        Args:
            max_width (float): The maximum width of the bounding box.
            max_height (float): The maximum height of the bounding box.

        Returns:
            Self: The current instance of the Image class.
        """
        original_width, original_height = self._width, self._height

        if original_width == 0 or original_height == 0:
            return self  # Avoid division by zero

        width_ratio = max_width / original_width
        height_ratio = max_height / original_height
        scaling_factor = min(width_ratio, height_ratio)

        new_width = original_width * scaling_factor
        new_height = original_height * scaling_factor

        return self._size(new_width, new_height)
