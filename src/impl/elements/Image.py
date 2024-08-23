from ..base.AbstractShape import AbstractShape
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractImageLoader import AbstractImageLoader
from ...config.Config import Config, DEFAULT_CONFIG

from typing import Self

import uuid
import base64

class Image(AbstractShape):
    def __init__(self, listener: AbstractImageListener, loader: AbstractImageLoader, config: Config = DEFAULT_CONFIG):
        super().__init__("image", config)
        self.fileId = str(uuid.uuid4())
        self.scale = [1, 1]
        self.status = "pending"
        self.strokeColor = "#808080"
        self.backgroundColor = "transparent"
        self._listener = listener
        self._loader = loader

    def svg(self, svg: str) -> Self:
        content = base64.b64encode(svg.encode('utf-8')).decode('utf-8')

        mime_type = "image/svg+xml"
        data_url = f"data:image/svg+xml;base64,{content}"

        self._listener.on_image(self.fileId, mime_type, data_url)
        return self


    def file(self, path: str) -> Self:
        data = self._loader.load(path)
        content = base64.b64encode(data).decode('utf-8')

        mime_type = "image/png"
        data_url = f"data:image/png;base64,{content}"

        self._listener.on_image(self.fileId, mime_type, data_url)
        return self
