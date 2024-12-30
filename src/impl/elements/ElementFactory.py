from ...config.Config import Config, DEFAULT_CONFIG
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractImageLoader import AbstractImageLoader
from ..colors.Color import Color

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

class ElementFactory():
    def __init__(self):
        self._config: Config = DEFAULT_CONFIG

    def config(self, config: Config) -> Self:
        self._config = config
        return self

    def rectangle(self) -> Rectangle:
        return Rectangle(self._config)

    def diamond(self) -> Diamond:
        return Diamond(self._config)

    def ellipse(self) -> Ellipse:
        return Ellipse(self._config)

    def arrow(self) -> Arrow:
        return Arrow(self._config)

    def line(self) -> Line:
        return Line(self._config)

    def text(self) -> Text:
        return Text(self._config)

    def image(self, listener: AbstractImageListener, loader: AbstractImageLoader) -> Image:
        return Image(listener, loader, self._config)

    def frame(self) -> Frame:
        return Frame(self._config)

    def group(self) -> Group:
        return Group(self._config)
    
    def color(self) -> Color:
        return Color()
    

