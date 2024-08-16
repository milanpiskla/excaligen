import uuid
from typing import Any
from ...config import Config

class AbstractElement():
    """Base class for all Excalidraw elements """

    def __init__(self, type: str, config: Config):
        self.type = type
        self.id = str(uuid.uuid4())
        self.seed = int(uuid.uuid4().int % 1000000000)import uuid
from typing import Any
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
        self.roughness = config.get("roughness", 1)
        self.strokeStyle = config.get("strokeStyle", "solid")
        self.strokeWidth = config.get("strokeWidth", 1)
        self.strokeColor = config.get("strokeColor", "#000000")
        self.fillStyle = config.get("fillStyle", "hachure")
        self.groupIds = config.get("groupIds", [])
        self.frameId = config.get("frameId", None)
        self.link = config.get("link", None)

    def to_dictionary(self) -> dict[str, Any]:
        """Creates a dictionary from public attributes."""
        return self._get_public_attributes_dictionary(self)

    def _get_public_attributes_dictionary(self, obj) -> dict:
        """Returns the object's public attributes in dictionary.
        
        The private attributes starting with '_' are excluded."""
        return {key: value for key, value in obj.__dict__.items() if not key.startswith('_')}

    def _config(self, config: Config) -> None:
        """Configures the attributes"""
        for key in self.__dict__.keys():
            if key in config:
                self.__dict__[key] = config[key]

        self.version = 1
        self.versionNonce = int(uuid.uuid4().int % 1000000000)
        self.isDeleted = False
        self.x = 0
        self.y = 0
        self.opacity = 100
        self.angle = 0
        self.index = None
        self.roughness = 1
        self.strokeStyle = "solid"
        self.strokeWidth = 1
        self.strokeColor = "#000000"
        self.fillStyle = "hachure"
        self.roundness = None
        self.groupIds = []
        self.frameId = None 
        self.link = None
        # TODO: add other attributes that are common for all Excalidraw elements

        self._config(config)

    def to_dictionary(self) -> dict[str, Any]:
        """Creates a dictionary from public attributes.
        """
        return self._get_public_attributes_dictionary(self)

    def _get_public_attributes_dictionary(self, obj) -> dict:
        """Returns the object's public attributes in dictionary.
        
        The private attributes starting with '_' are excluded."""
        return {key: value for key, value in obj.__dict__.items() if not key.startswith('_')}
