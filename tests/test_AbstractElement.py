import pytest

from src.impl.base.AbstractElement import AbstractElement
from src.impl.base.AbstractStyle import AbstractStyle

def test_to_json():
    class TestElement(AbstractElement):
        def __init__(self):
            super().__init__("test")

        def _get_default_style(self) -> AbstractStyle:
            return AbstractStyle()

    element = TestElement()
    print(element.to_json())
    assert True
