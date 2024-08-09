import json
import uuid

from .ElementEncoder import ElementEncoder

class AbstractElement:
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
        return json.dumps(self, cls = ElementEncoder)

