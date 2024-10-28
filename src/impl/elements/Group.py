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

import uuid

Element = Rectangle | Diamond | Ellipse | Arrow | Line | Text | Image | Frame

class Group():
    def __init__(self, *args: Element):
        id = str(uuid.uuid4())
        for arg in args:
            if isinstance(arg, Element):
                arg._add_group_id(id)
            else:
                raise ValueError(f"All arguments of Group must be Elements, not `{str(arg)}`")
