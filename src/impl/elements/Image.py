import os
import base64
import imghdr
import uuid
import struct

from typing import Self, Union
from xml.etree import ElementTree as ET

from ..base.AbstractShape import AbstractShape
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractImageLoader import AbstractImageLoader
from ...config.Config import Config, DEFAULT_CONFIG

class Image(AbstractShape):
    def __init__(self, listener: AbstractImageListener, loader: AbstractImageLoader, config: Config = DEFAULT_CONFIG):
        super().__init__("image", config)
        self.fileId = str(uuid.uuid4())
        self.scale = [1, 1]
        self.status = "pending"
        self.strokeColor = "#808080"
        self.backgroundColor = "transparent"
        self._listener = listener
        self._loader = loader

    def file(self, path: str) -> Self:
        """Load image data from a file and set it. Supports both SVG and binary image files."""
        file_extension = os.path.splitext(path)[1].lower()

        if file_extension == ".svg":
            # SVG files are handled as text
            with open(path, "r", encoding="utf-8") as svg_file:
                svg_content = svg_file.read()
            width, height = self._get_svg_size(svg_content)
            self.size(width, height)
            return self.data(svg_content)
        else:
            # Other image types (PNG, JPEG) are handled as binary
            with open(path, "rb") as image_file:
                binary_data = image_file.read()
            width, height = self._detect_image_size(binary_data)
            self.size(width, height)
            return self.data(binary_data)

    def data(self, data: Union[bytes, str]) -> Self:
        """Set image data. Supports raw bytes for images and SVG strings."""
        if isinstance(data, str):
            # Validate and handle SVG data
            if self._is_valid_svg(data):
                width, height = self._get_svg_size(data)
                self.size(width, height)
                return self._set_svg_data(data)
            else:
                raise ValueError("Invalid SVG data. Ensure the string is a well-formed SVG.")
        elif isinstance(data, bytes):
            # Handle binary image data (PNG, JPEG)
            width, height = self._detect_image_size(data)
            self.size(width, height)
            return self._set_binary_data(data)
        else:
            raise TypeError("Unsupported data type. Use 'bytes' for images and 'str' for SVG.")

    def fit(self, max_width: float, max_height: float) -> Self:
            """Scale the image to fit within a bounding box while maintaining aspect ratio."""
            original_width, original_height = self.width, self.height
            
            # Calculate the scaling factor for both dimensions
            width_ratio = max_width / original_width
            height_ratio = max_height / original_height
            scaling_factor = min(width_ratio, height_ratio)

            # Scale the image dimensions
            new_width = original_width * scaling_factor
            new_height = original_height * scaling_factor

            # Update the size of the image
            return self.size(new_width, new_height)

    def _get_svg_size(self, svg_data: str) -> tuple[float, float]:
        """Get the width and height of an SVG image from its string content.

        If width and height are not provided, fall back to viewBox. If neither is provided, return (0, 0).
        """
        root = ET.fromstring(svg_data)
        
        # Check for width and height attributes
        width = root.attrib.get('width')
        height = root.attrib.get('height')

        if width and height:
            # Attempt to parse width and height values if they are present
            try:
                return float(width), float(height)
            except ValueError:
                pass  # If parsing fails, we'll fall back to viewBox

        # Check for viewBox attribute as a fallback
        viewBox = root.attrib.get('viewBox')
        if viewBox:
            viewBox_values = viewBox.split()
            if len(viewBox_values) == 4:
                try:
                    _, _, viewBox_width, viewBox_height = map(float, viewBox_values)
                    return viewBox_width, viewBox_height
                except ValueError:
                    pass  # If parsing fails, we'll fall back to default

        # Return default size if neither width/height nor viewBox are available or valid
        return 0, 0

    def _get_png_size(self, data: bytes) -> tuple[int, int]:
        """Get the width and height of a PNG image from its binary data."""
        try:
            width, height = struct.unpack(">II", data[16:24])
            return width, height
        except struct.error:
            return 0, 0

    def _get_jpeg_size(self, data: bytes) -> tuple[int, int]:
        """Get the width and height of a JPEG image from its binary data."""
        try:
            index = 2
            while index < len(data):
                marker, code, length = data[index], data[index + 1], data[index + 2:index + 4]
                if marker != 0xFF:
                    break
                if code in {0xC0, 0xC1, 0xC2, 0xC3}:
                    # Found the Start of Frame (SOF) marker
                    height, width = struct.unpack(">HH", data[index + 5:index + 9])
                    return width, height
                index += 2 + struct.unpack(">H", length)[0]
            return 0, 0
        except struct.error:
            return 0, 0

    def _detect_image_size(self, data: bytes, mime_type: str = None) -> tuple[int, int]:
        """Detect the size of an image based on its data and optional MIME type."""
        mime_type = mime_type or imghdr.what(None, data)
        
        if mime_type == "png":
            return self._get_png_size(data)
        elif mime_type == "jpeg":
            return self._get_jpeg_size(data)
        else:
            return 0, 0

    def _is_valid_svg(self, data: str) -> bool:
        """Validate if the string is a well-formed SVG."""
        root = ET.fromstring(data)
        return root.tag == '{http://www.w3.org/2000/svg}svg'

    def _set_svg_data(self, svg: str) -> Self:
        """Handle valid SVG string data."""
        mime_type = "image/svg+xml"
        content = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
        data_url = f"data:{mime_type};base64,{content}"
        self._listener.on_image(self.fileId, mime_type, data_url)
        return self

    def _set_binary_data(self, data: bytes) -> Self:
        """Handle binary image data (PNG, JPEG)."""
        mime_type = self._detect_mime_type(data)
        if mime_type is None:
            raise ValueError("Unsupported image format. Only SVG, PNG, and JPEG are supported.")

        # Convert data to base64 encoded string
        encoded_data = base64.b64encode(data).decode('utf-8')
        data_url = f"data:{mime_type};base64,{encoded_data}"
        
        # Notify the listener with the image data
        self._listener.on_image(self.fileId, mime_type, data_url)
        
        return self

    def _detect_mime_type(self, data: bytes) -> str:
        """Detect the MIME type of the image data."""
        mime_type = imghdr.what(None, h=data)
        if mime_type in ["png", "jpeg"]:
            return f"image/{mime_type}"
        return None
