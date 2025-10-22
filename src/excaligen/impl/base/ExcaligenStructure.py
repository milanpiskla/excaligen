"""
Description: Base class for Excaligen to hide implementation details from the user.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from .AbstractElement import AbstractElement
from ..elements.ElementFactory import ElementFactory
from ..elements.Rectangle import Rectangle
from ..elements.Diamond import Diamond
from ..elements.Ellipse import Ellipse
from ..elements.Arrow import Arrow
from ..elements.Line import Line
from ..elements.Text import Text
from ..elements.Image import Image
from ..elements.Frame import Frame
from ..elements.Group import Group
from ..colors.Color import Color
from ..images.ImageLoader import ImageLoader
from ..indexer.IndexGenerator import IndexGenerator

from .AbstractImageListener import AbstractImageListener
from .AbstractPlainLabelListener import AbstractPlainLabelListener

from ...defaults.Defaults import Defaults
from typing import Self, cast

import json

class ExcaligenStructure(AbstractImageListener, AbstractPlainLabelListener):
    class ElementEncoder(json.JSONEncoder):
        """JSON encoder for Excalidraw elements.

        Serializes object attributes starting with a single underscore,
        converting them from snake_case to camelCase for JSON output.
        Ignores attributes containing double underscores or without leading underscores.
        """

        def default(self, obj):
            result = {}
            for attr_name, value in obj.__dict__.items():
                if attr_name.startswith('_') and not '__' in attr_name:
                    json_key = self._snake_to_camel(attr_name.lstrip('_'))
                    result[json_key] = value
            return result

        @staticmethod
        def _snake_to_camel(snake_str: str) -> str:
            """Convert snake_case string to camelCase."""
            components = snake_str.split('_')
            return components[0] + ''.join(x.title() for x in components[1:])

    _START_INDEX = 'a0'
    
    def __init__(self):
        self._type = "excalidraw"
        self._version = 2
        self._source = "https://excalidraw.com"
        self._elements: list[AbstractElement] = []
        self._app_state = {
            "gridSize": 20,
            "gridStep": 5,
            "gridModeEnabled": False, 
            "viewBackgroundColor": "#ffffff"
        }
        self._files = {}
        self.__factory = ElementFactory()
        self.__image_loader = ImageLoader()
        self.__indexer = IndexGenerator(self._START_INDEX)
        self.__index = self._START_INDEX

    def defaults(self) -> Defaults:
        return self.__factory.defaults()

    def grid(self, size: int, step: int, enabled: bool) -> Self:
        self._app_state["gridSize"] = size
        self._app_state["gridStep"] = step
        self._app_state["gridModeEnabled"] = enabled
        return self
    
    def background(self, color: str) -> Self:
        self._app_state["viewBackgroundColor"] = color
        return self

    def rectangle(self) -> Rectangle:
        return cast(Rectangle, self.__append_element(self.__factory.rectangle(self)))

    def diamond(self) -> Diamond:
        return cast(Diamond, self.__append_element(self.__factory.diamond(self)))

    def ellipse(self) -> Ellipse:
        return cast(Ellipse, self.__append_element(self.__factory.ellipse(self)))

    def arrow(self) -> Arrow:
        return cast(Arrow, self.__append_element(self.__factory.arrow(self)))

    def line(self) -> Line:
        return cast(Line, self.__append_element(self.__factory.line()))

    def text(self) -> Text:
        return cast(Text, self.__append_element(self.__factory.text()))

    def image(self) -> Image:
        return cast(Image, self.__append_element(self.__factory.image(self, self.__image_loader)))

    def frame(self) -> Frame:
        return cast(Frame, self.__append_element(self.__factory.frame()))

    def group(self) -> Group:
        return self.__factory.group()

    def color(self) -> Color:
        return self.__factory.color()

    def json(self) -> str:
        return json.dumps(self, cls = self.ElementEncoder, indent = 2)

    def save(self, file_path: str) -> Self:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.json())
                return self

        except Exception as e:
            print(f"Error Writing '{file_path}': {e}")      
            return self  

    def _on_image(self, id: str, mime_type: str, data_url: str) -> None:
        self._files[id] = {
            "mimeType": mime_type,
            "id": id,
            "dataURL": data_url
        }

    def _on_text(self, text: str) -> Text:
        return self.__append_element(self.__factory.text().content(text))

    def __append_element(self, element: AbstractElement) -> AbstractElement:
        element._index = self.__index
        self._elements.append(element)
        self.__index = self.__indexer.next()
        
        return element
        
