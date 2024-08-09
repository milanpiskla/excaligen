import pytest

from src.impl.base.AbstractElement import AbstractElement

def test_to_json():
    element = AbstractElement("test")
    print(element.to_json())
    assert True

