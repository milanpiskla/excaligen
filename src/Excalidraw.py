from .impl.base.ExcalidrawStructure import ExcalidrawStructure
from .config.Config import Config
from .impl.elements.Rectangle import Rectangle
from .impl.elements.Diamond import Diamond
from .impl.elements.Ellipse import Ellipse
from .impl.elements.Arrow import Arrow
from .impl.elements.Line import Line
from .impl.elements.Text import Text
from .impl.elements.Image import Image
from .impl.elements.Group import Group
from .impl.elements.Frame import Frame

from typing import Self

class Excalidraw(ExcalidrawStructure):
    def __init__(self):
        super().__init__()

    def config(self, config: Config) -> Self:
        return super().config(config)

    def rectangle(self) -> Rectangle:
        return super().rectangle()

    def diamond(self) -> Diamond:
        return super().diamond()

    def ellipse(self) -> Ellipse:
        return super().ellipse()

    def arrow(self) -> Arrow:
        return super().arrow()

    def line(self) -> Line:
        return super().line()

    def text(self) -> Text:
        return super().text()

    def image(self) -> Image:
        return super().image()

    def group(self) -> Group:
        return super().group()

    def frame(self) -> Frame:
        return super().frame()

    def json(self) -> str:
        return super().json()

    def save(self, file: str) -> Self:
        return super().save(file)
