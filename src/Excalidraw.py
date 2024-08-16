from .impl.base.ExcalidrawStructure import ExcalidrawStructure
from .config.Config import Config
from .impl.Rectangle import Rectangle
from .impl.Diamond import Diamond
from .impl.Ellipse import Ellipse

class Excalidraw(ExcalidrawStructure):
    def __init__(self):
        super()

    def config(self, config: Config) -> Excalidraw:
        self.config(config)
        return self

    def rectangle(self) -> Rectangle:
        return super().rectangle()

    def diamond(self) -> Diamond:
        return super().diamond()

    def ellipse(self) -> Ellipse:
        return super().ellipse()

    def arrow(self):
        return super().arrow()

    def line(self):
        return super().line()

    def text(self):
        return super().text()

    def image(self):
        return super().image()

    def group(self):
        return super().group()

    def frame(self):
        return super().frame()

    def to_json(self) -> str:
        return super().to_json()


