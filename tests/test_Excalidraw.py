import pytest
from src.Excalidraw import Excalidraw


def test_Excalidraw():
    e = Excalidraw()
    r = e.rectangle()

    print(e.to_json())

    assert True
