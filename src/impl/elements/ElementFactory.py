from ...config.Config import Config, DEFAULT_CONFIG
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractImageLoader import AbstractImageLoader

from .Rectangle import Rectangle
from .Diamond import Diamond
from .Ellipse import Ellipse
from .Arrow import Arrow
from .Line import Line
from .Text import Text
from .Image import Image
from .Frame import Frame
from .Group import Group

from typing import Self

Element = Rectangle | Diamond | Ellipse | Arrow | Line | Text | Image | Frame

class ElementFactory():
    def __init__(self):
        self.config = DEFAULT_CONFIG

    def config(self, config: Config) -> Self:
        self.config = config
        return self

    def rectangle(self) -> Rectangle:
        return Rectangle(self.config)

    def diamond(self) -> Diamond:
        return Diamond(self.config)

    def ellipse(self) -> Ellipse:
        return Ellipse(self.config)

    def arrow(self) -> Arrow:
        return Arrow(self.config)

    def line(self) -> Line:
        return Line(self.config)

    def text(self) -> Text:
        return Text(self.config)

    def image(self, listener: AbstractImageListener, loader: AbstractImageLoader) -> Image:
        return Image(listener, loader, self.config)

    def frame(self) -> Frame:
        return Frame(self.config)

    def group(self, *args: Element) -> Group:
        return Group(*args)
