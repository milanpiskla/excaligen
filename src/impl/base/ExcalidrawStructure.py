from AbstractElement import AbstractElement
from ..ElementFactory import ElementFactory
from ..Rectangle import Rectangle
from ..Diamond import Diamond
from ..Ellipse import Ellipse

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

    def arrow(self):
        # TODO: implementation
        pass

    def line(self):
        # TODO: implementation
        pass

    def text(self):
        # TODO: implementation
        pass

    def image(self):
        # TODO: implementation
        pass

    def group(self):
        # TODO: implementation
        pass

    def frame(self):
        # TODO: implementation
        pass



    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def _append_element(self, element: AbstractElement) -> AbstractElement:
        self.elements.append(element.to_dictionary())
        return element
