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
from ..ImageLoader import ImageLoader

from .AbstractImageListener import AbstractImageListener

from ...config.Config import Config

import json

class ExcalidrawStructure(AbstractImageListener):
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
        self._image_loader = ImageLoader()

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
        return self._append_element(self._factory.image(self, self._image_loader))

    def group(self) -> Group:
        return self._append_element(self._factory.group())

    def frame(self) -> Frame:
        return self._append_element(self._factory.frame())

    def to_json(self) -> str:
        return json.dumps(self, cls = self.ElementEncoder, indent = 2)

    def on_image(self, id: str, mime_type: str, data_url: str) -> None:
        self.files[id] = {
            "mimeType": mime_type,
            "id": id,
            "dataURL": data_url
        }

    def _append_element(self, element: AbstractElement) -> AbstractElement:
        self.elements.append(element)
        return element
        
