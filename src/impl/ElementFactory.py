from .Rectangle import Rectangle
from typing import Any

type Config = dict[str, Any]

class ElementFactory():
    def __init__(self):
        self.config = None

    def config(self, config: Config):
        return self

    def rectangle(self):
        return Rectangle()