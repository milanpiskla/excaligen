import uuid
from typing import Self
from ...config.Config import Config

class AbstractElement:
    """Base class for all Excalidraw elements"""

    def __init__(self, type: str, config: Config):
        self.type = type
        self.id = str(uuid.uuid4())
        self.seed = int(uuid.uuid4().int % 1000000000)
        self.version = 1
        self.versionNonce = int(uuid.uuid4().int % 1000000000)
        self.isDeleted = False
        self.x = config.get("x", 0)
        self.y = config.get("y", 0)
        self.opacity = config.get("opacity", 100)
        self.angle = config.get("angle", 0)
        self.index = config.get("index", None)
        self.groupIds = config.get("groupIds", [])
        self.frameId = config.get("frameId", None)
        self.link = config.get("link", None)
        self.boundElements = None

    def position(self, x: float, y: float) -> Self:
        self.x = x
        self.y = y
        
        return self
    
    def _addBoundElement(self, element: "AbstractElement") -> None:
        self.boundElements = self.boundElements or []
        self.boundElements.append({"id": element.id, "type": element.type})
