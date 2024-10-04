import uuid
from typing import Self
from ...config.Config import Config

class AbstractElement:
    """Base class for all Excalidraw elements."""

    def __init__(self, element_type: str, config: Config):
        self._type = element_type
        self._id = str(uuid.uuid4())
        self._seed = int(uuid.uuid4().int % 1000000000)
        self._version = 1
        self._version_nonce = int(uuid.uuid4().int % 1000000000)
        self._is_deleted = False
        self._x = config.get("x", 0)
        self._y = config.get("y", 0)
        self._opacity = config.get("opacity", 100)
        self._angle = config.get("angle", 0)
        self._index = config.get("index", None)
        self._group_ids = config.get("groupIds", [])
        self._frame_id = config.get("frameId", None)
        self._link = config.get("link", None)
        self._bound_elements = None

    def position(self, x: float, y: float) -> Self:
        self._x = x
        self._y = y
        return self

    def rotate(self, angle: float) -> Self:
        self._angle = angle
        return self

    def opacity(self, opacity: float) -> Self:
        self._opacity = opacity
        return self

    def _add_bound_element(self, element: "AbstractElement") -> None:
        self._bound_elements = self._bound_elements or []
        self._bound_elements.append({"id": element._id, "type": element._type})
