"""
Description: Unit tests for few elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
from src.excaligen.Excaligen import Excaligen
from src.excaligen.config.Config import DEFAULT_CONFIG

def test_excalidraw_init():
    xd = Excaligen()
    assert xd._type == "excalidraw"
    assert xd._version == 2
    assert xd._source == "https://excalidraw.com"
    assert isinstance(xd._elements, list)
    assert len(xd._elements) == 0

def test_add_rectangle():
    xd = Excaligen()
    rect = xd.rectangle()
    assert rect._type == "rectangle"
    assert len(xd._elements) == 1
    assert xd._elements[0]._type == "rectangle"

def test_add_text():
    xd = Excaligen()
    text = xd.text().content("Hello, Excalidraw!")
    assert text._text == "Hello, Excalidraw!"
    assert text._font_size == DEFAULT_CONFIG['fontSize']
    assert len(xd._elements) == 1
    assert xd._elements[0]._type == "text"

def test_json_output():
    xd = Excaligen()
    xd.rectangle().size(200, 100)
    json_output = xd.json()
    assert "rectangle" in json_output
    assert '"width": 200' in json_output
    assert '"height": 100' in json_output

def test_save_to_file(tmp_path):
    xd = Excaligen()
    xd.rectangle().size(200, 100)
    file_path = tmp_path / "output.json"
    xd.save(str(file_path))
    assert file_path.exists()
    assert file_path.read_text().count("rectangle") == 1
