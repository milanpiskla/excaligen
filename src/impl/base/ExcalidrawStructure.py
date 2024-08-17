from .AbstractElement import AbstractElement
from ..ElementFactory import ElementFactory
from ..Rectangle import Rectangle
from ..Diamond import Diamond
from ..Ellipse import Ellipse
from ..Arrow import Arrow
from ..Line import Line
from ..Text import Text
from ..Image import Image
from ..Group import Group
from ..Frame import Frame

from ...config.Config import Config
from typing import Any

import json

class ExcalidrawStructure:
    class ElementEncoder(json.JSONEncoder):
        """JSON encoder for Excalidraw elements
        
        It serializes the object attributes to JSON except the ones starting with underscore '_'.
        """
        def default(self, obj):
            return {key: value for key, value in obj.__dict__.items() if not key.startswith('_')}

    def __init__(self):
        self.type = "excalidraw"
        self.version = 2
        self.source = "https://excalidraw.com"
        self.elements: list[AbstractElement] = []
        self.appState = {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff"
        }
        self.files = {
        }
        
        self._factory = ElementFactory()

    def config(self, config: Config):
        self._factory.config(config)

    def rectangle(self) -> Rectangle:
        return self._append_element(self._factory.rectangle())

    def diamond(self) -> Diamond:
        return self._append_element(self._factory.diamond())

    def ellipse(self) -> Ellipse:
        return self._append_element(self._factory.ellipse())

    def arrow(self) -> Arrow:
        return self._append_element(self._factory.arrow())

    def line(self) -> Line:
        return self._append_element(self._factory.line())

    def text(self) -> Text:
        return self._append_element(self._factory.text())

    def image(self) -> Image:
        return self._append_element(self._factory.image())

    def group(self) -> Group:
        return self._append_element(self._factory.group())

    def frame(self) -> Frame:
        return self._append_element(self._factory.frame())

    def to_json(self) -> str:
        return json.dumps(self, cls = self.ElementEncoder, indent = 2)

    def _append_element(self, element: AbstractElement) -> AbstractElement:
        self.elements.append(element)
        return element

    def _append_file(self) -> None:
        # TODO: implement
        pass

    # def _get_public_attributes_dictionary(self, obj) -> dict[str, Any]:
    #     """Returns the object's public attributes in dictionary.
        
    #     The private attributes starting with '_' are excluded."""
    #     return {key: value for key, value in obj.__dict__.items() if not key.startswith('_')}
