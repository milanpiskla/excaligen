"""Group is virtual only element that groups real elements together.

It is not written in Excalidraw file, the element belonging to a group refers
to the group by groupIds attribute instead.
"""

from ..elements.Rectangle import Rectangle
from ..elements.Diamond import Diamond
from ..elements.Ellipse import Ellipse
from ..elements.Arrow import Arrow
from ..elements.Line import Line
from ..elements.Text import Text
from ..elements.Image import Image
from ..elements.Frame import Frame
from ...config.Config import Config, DEFAULT_CONFIG

from typing import Self

import uuid

Element = Rectangle | Diamond | Ellipse | Arrow | Line | Text | Image | Frame

class Group():
    def __init__(self, config: Config = DEFAULT_CONFIG):
        self.__id = str(uuid.uuid4())

    def elements(self, *elements: Element) -> Self:
        for element in elements:
            element._add_group_id(self.__id) # type: ignore

        return self
