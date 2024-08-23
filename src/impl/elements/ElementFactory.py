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
from .Group import Group
from .Frame import Frame

class ElementFactory():
    def __init__(self):
        self.config = DEFAULT_CONFIG

    def config(self, config: Config):
        self.config = config
        return self

    def rectangle(self):
        return Rectangle(self.config)

    def diamond(self):
        return Diamond(self.config)

    def ellipse(self):
        return Ellipse(self.config)

    def arrow(self):
        return Arrow(self.config)

    def line(self):
        return Line(self.config)

    def text(self):
        return Text(self.config)

    def image(self, listener: AbstractImageListener, loader: AbstractImageLoader):
        return Image(listener, loader, self.config)

    def group(self):
        return Group(self.config)

    def frame(self):
        return Frame(self.config)
