from .AbstractElement import AbstractElement
from ..elements.ElementFactory import ElementFactory
from ..elements.Rectangle import Rectangle
from ..elements.Diamond import Diamond
from ..elements.Ellipse import Ellipse
from ..elements.Arrow import Arrow
from ..elements.Line import Line
from ..elements.Text import Text
from ..elements.Image import Image
from ..elements.Group import Group
from ..elements.Frame import Frame
from ..images.ImageLoader import ImageLoader

from .AbstractImageListener import AbstractImageListener

from ...config.Config import Config
from typing import Self

import json

class ExcalidrawStructure(AbstractImageListener):
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

    def __init__(self):
        self._type = "excalidraw"
        self._version = 2
        self._source = "https://excalidraw.com"
        self._elements: list[AbstractElement] = []
        self._app_state = {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff"
        }
        self._files = {}
        self.__factory = ElementFactory()
        self.__image_loader = ImageLoader()

    def config(self, config: Config) -> Self:
        self.__factory.config(config)
        return self

    def rectangle(self) -> Rectangle:
        return self.__append_element(self.__factory.rectangle())

    def diamond(self) -> Diamond:
        return self.__append_element(self.__factory.diamond())

    def ellipse(self) -> Ellipse:
        return self.__append_element(self.__factory.ellipse())

    def arrow(self) -> Arrow:
        return self.__append_element(self.__factory.arrow())

    def line(self) -> Line:
        return self.__append_element(self.__factory.line())

    def text(self) -> Text:
        return self.__append_element(self.__factory.text())

    def image(self) -> Image:
        return self.__append_element(self.__factory.image(self, self.__image_loader))

    def group(self) -> Group:
        return self.__append_element(self.__factory.group())

    def frame(self) -> Frame:
        return self.__append_element(self.__factory.frame())

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

    def on_image(self, id: str, mime_type: str, data_url: str) -> None:
        self._files[id] = {
            "mimeType": mime_type,
            "id": id,
            "dataURL": data_url
        }

    def __append_element(self, element: AbstractElement) -> AbstractElement:
        self._elements.append(element)
        return element
        
