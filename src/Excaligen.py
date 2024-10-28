"""Excalidraw file generator.

This module defines the Excalidraw class, which serves as the main interface with fluent API for creating
Excalidraw diagram. 
"""

from .impl.base.ExcaligenStructure import ExcaligenStructure, Element
from .config.Config import Config
from .impl.elements.Rectangle import Rectangle
from .impl.elements.Diamond import Diamond
from .impl.elements.Ellipse import Ellipse
from .impl.elements.Arrow import Arrow
from .impl.elements.Line import Line
from .impl.elements.Text import Text
from .impl.elements.Image import Image
from .impl.elements.Frame import Frame
from .impl.elements.Group import Group

from typing import Self

class Excaligen(ExcaligenStructure):
    """The Excalidraw class provides methods to add various diagram elements.

    The elemnts include rectangles, diamonds, ellipses, arrows, lines, text, images, groups, and frames.
    Additionally, it offers serialization of the diagram to JSON and allows saving it to a file.
    """
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

    def frame(self) -> Frame:
        return super().frame()

    def group(self, *args: Element) -> None:
        return super().group(*args)

    def json(self) -> str:
        return super().json()

    def save(self, file: str) -> Self:
        return super().save(file)
