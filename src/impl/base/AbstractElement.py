import json
import uuid
from abc import ABC, abstractmethod

from .AbstractStyle import AbstractStyle

class AbstractElement(ABC):
    """Base class for all Excalidraw elements """

    def __init__(self, type: str):
        self.type = type
        self.id = str(uuid.uuid4())
        self.seed = int(uuid.uuid4().int % 1000000000)
        self.version = 1
        self.versionNonce = int(uuid.uuid4().int % 1000000000)
        self.isDeleted = False
        self.x = 0
        self.y = 0

        self._style = None

    def to_json(self) -> str:
        """Serialize to JSON. 
        
        If the element object does not have style, then a default style is used.
        """
        attributes_dictionary = self._get_public_attributes_dictionary(self)
        if self._style == None:
            attributes_dictionary.update(self._get_public_attributes_dictionary(self._get_default_style()))

        return json.dumps(attributes_dictionary)

        # return json.dumps(self, cls = ElementEncoder)

    @abstractmethod
    def _get_default_style(self) -> AbstractStyle:
        """Must be overridden in the derived class."""
        pass

    def _get_public_attributes_dictionary(self, obj) -> dict:
        """Returns the object's public attributes in dictionary.
        
        The private attributes starting with '_' are excluded."""
        return {key: value for key, value in obj.__dict__.items() if not key.startswith('_')}