import pytest
from src.Excalidraw import Excalidraw
from src.config.Config import DEFAULT_CONFIG

def test_excalidraw_init():
    xd = Excalidraw()
    assert xd.type == "excalidraw"
    assert xd.version == 2
    assert xd.source == "https://excalidraw.com"
    assert isinstance(xd.elements, list)
    assert len(xd.elements) == 0

def test_add_rectangle():
    xd = Excalidraw()
    rect = xd.rectangle()
    assert rect.type == "rectangle"
    assert len(xd.elements) == 1
    assert xd.elements[0].type == "rectangle"

def test_add_text():
    xd = Excalidraw()
    text = xd.text().content("Hello, Excalidraw!")
    assert text.text == "Hello, Excalidraw!"
    assert text.fontSize == DEFAULT_CONFIG['fontSize']
    assert len(xd.elements) == 1
    assert xd.elements[0].type == "text"

def test_json_output():
    xd = Excalidraw()
    xd.rectangle().size(200, 100)
    json_output = xd.json()
    assert "rectangle" in json_output
    assert '"width": 200' in json_output
    assert '"height": 100' in json_output

def test_save_to_file(tmp_path):
    xd = Excalidraw()
    xd.rectangle().size(200, 100)
    file_path = tmp_path / "output.json"
    xd.save(str(file_path))
    assert file_path.exists()
    assert file_path.read_text().count("rectangle") == 1
