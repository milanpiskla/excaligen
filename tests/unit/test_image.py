"""
Description: Unit tests for image handling.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
from src.excaligen.impl.elements.Image import Image
from src.excaligen.impl.base.AbstractImageListener import AbstractImageListener
from src.excaligen.impl.images.ImageLoader import ImageLoader
from excaligen.defaults.Defaults import Defaults
import os
import io

class DummyImageListener(AbstractImageListener):
    def __init__(self):
        self.images = {}

    def _on_image(self, id: str, mime_type: str, data_url: str):
        self.images[id] = (mime_type, data_url)

@pytest.fixture
def image_listener():
    return DummyImageListener()

@pytest.fixture
def image_loader():
    return ImageLoader()

def test_image_load_svg(image_listener, image_loader):
    image_element = Image(Defaults(), image_listener, image_loader)
    svg_data = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"></svg>'
    image_element.data(svg_data)
    assert len(image_listener.images) == 1
    file_id, (mime_type, data_url) = next(iter(image_listener.images.items()))
    assert mime_type == "image/svg+xml"
    assert data_url.startswith("data:image/svg+xml;base64,")

def test_image_load_png(image_listener, image_loader):
    image_element = Image(Defaults(), image_listener, image_loader)
    # Generate a simple PNG image in memory
    png_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01' \
               b'\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00' \
               b'\x00\x00\nIDAT\x08\xd7c``\x00\x00\x00\x02\x00\x01' \
               b'\xe2!\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82'
    # Use the data directly
    image_element.data(png_data)
    assert len(image_listener.images) == 1
    file_id, (mime_type, data_url) = next(iter(image_listener.images.items()))
    assert mime_type == "image/png"
    assert data_url.startswith("data:image/png;base64,")

def test_image_fit(image_listener, image_loader):
    image_element = Image(Defaults(), image_listener, image_loader)
    svg_data = '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"></svg>'
    image_element.data(svg_data).fit(100, 100)
    assert image_element._width == 100
    assert image_element._height == 50
