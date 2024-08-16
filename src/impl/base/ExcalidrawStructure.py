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

import json

class ExcalidrawStructure:
    def __init__(self):
        self.type = "excalidraw"
        self.version = 2
        self.source = "https://excalidraw.com"
        self.elements: list[AbstractElement] = []
        
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
        return json.dumps(self.__dict__)

    def _append_element(self, element: AbstractElement) -> AbstractElement:
        self.elements.append(element.to_dictionary())
        return element
