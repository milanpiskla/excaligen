"""
Description: Image loader implementation.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from ..base.AbstractImageLoader import AbstractImageLoader
from .ImageData import ImageData
import os
import base64
import struct
from xml.etree import ElementTree as ET

class ImageLoader(AbstractImageLoader):
    def load_from_file(self, file_path: str) -> ImageData:
        # Read the file extension to determine the type
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".svg":
            with open(file_path, "r", encoding="utf-8") as svg_file:
                svg_content = svg_file.read()
            return self._process_svg(svg_content)
        else:
            with open(file_path, "rb") as image_file:
                binary_data = image_file.read()
            return self._process_binary_image(binary_data)

    def load_from_data(self, data: bytes | str) -> ImageData:
        if isinstance(data, str):
            if self._is_valid_svg(data):
                return self._process_svg(data)
            else:
                raise ValueError("Invalid SVG data. Ensure the string is a well-formed SVG.")
        elif isinstance(data, bytes):
            return self._process_binary_image(data)
        else:
            raise TypeError("Unsupported data type. Use 'bytes' for images and 'str' for SVG.")

    def _process_svg(self, svg_content: str) -> ImageData:
        width, height = self._get_svg_size(svg_content)
        mime_type = "image/svg+xml"
        content_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
        data_url = f"data:{mime_type};base64,{content_base64}"
        return ImageData(width, height, mime_type, data_url, content=svg_content)

    def _process_binary_image(self, data: bytes) -> ImageData:
        mime_type = self._detect_mime_type(data)
        if mime_type is None:
            raise ValueError("Unsupported image format. Only SVG, PNG, JPEG, and GIF are supported.")
        width, height = self._detect_image_size(data, mime_type)
        encoded_data = base64.b64encode(data).decode('utf-8')
        data_url = f"data:{mime_type};base64,{encoded_data}"
        return ImageData(width, height, mime_type, data_url, content=data)

    def _is_valid_svg(self, data: str) -> bool:
        try:
            root = ET.fromstring(data)
            return root.tag == '{http://www.w3.org/2000/svg}svg' or root.tag == 'svg'
        except ET.ParseError:
            return False

    def _get_svg_size(self, svg_data: str) -> tuple[float, float]:
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
            viewBox_values = viewBox.strip().split()
            if len(viewBox_values) == 4:
                try:
                    _, _, viewBox_width, viewBox_height = map(float, viewBox_values)
                    return viewBox_width, viewBox_height
                except ValueError:
                    pass  # If parsing fails, we'll fall back to default

        # Return default size if neither width/height nor viewBox are available or valid
        return 0, 0

    def _detect_mime_type(self, data: bytes) -> str | None:
        if data.startswith(b'\x89PNG\r\n\x1a\n'):
            return 'image/png'
        elif data.startswith(b'\xff\xd8'):
            return 'image/jpeg'
        elif data.startswith(b'GIF8'):
            return 'image/gif'
        else:
            return None

    def _detect_image_size(self, data: bytes, mime_type: str) -> tuple[int, int]:
        if mime_type == "image/png":
            return self._get_png_size(data)
        elif mime_type == "image/jpeg":
            return self._get_jpeg_size(data)
        elif mime_type == "image/gif":
            return self._get_gif_size(data)
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
            index = 0
            size = len(data)
            while index < size:
                # JPEG markers start with 0xFF
                if data[index] != 0xFF:
                    index += 1
                    continue
                marker = data[index + 1]
                index += 2
                if marker == 0xD8:  # Start of Image (SOI)
                    continue
                elif marker == 0xD9:  # End of Image (EOI)
                    break
                elif 0xC0 <= marker <= 0xCF and marker != 0xC4 and marker != 0xC8 and marker != 0xCC:
                    # SOF markers for baseline DCT, progressive DCT, etc.
                    length = struct.unpack(">H", data[index:index+2])[0]
                    index += 2  # Skip length bytes
                    bits_per_sample = data[index]
                    index += 1  # Skip bits per sample
                    height, width = struct.unpack(">HH", data[index:index+4])
                    return width, height
                else:
                    # Skip the segment
                    length = struct.unpack(">H", data[index:index+2])[0]
                    index += length
            return 0, 0
        except (IndexError, struct.error):
            return 0, 0

    def _get_gif_size(self, data: bytes) -> tuple[int, int]:
        """Get the width and height of a GIF image from its binary data."""
        try:
            width, height = struct.unpack("<HH", data[6:10])
            return width, height
        except struct.error:
            return 0, 0
