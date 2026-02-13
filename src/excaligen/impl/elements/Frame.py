"""
Description: Frame container for elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractElement import AbstractElement
from ..base.AbstractShape import AbstractShape

from ..elements.Rectangle import Rectangle
from ..elements.Diamond import Diamond
from ..elements.Ellipse import Ellipse
from ..elements.Arrow import Arrow
from ..elements.Line import Line
from ..elements.Text import Text
from ..elements.Image import Image
from ...defaults.Defaults import Defaults

from typing import Self

Element = Rectangle | Diamond | Ellipse | Arrow | Line | Text | Image

DEFAULT_FRAME_INSET: float = 30.0

class Frame(AbstractShape):
    """A visual container that can hold other elements and automatically adjusts its size.
    
    Frame is a fundamental layout component that serves as a container for other elements.
    It can automatically calculate its dimensions based on its contents or be explicitly
    sized. Frames can also have titles and background colors, making them useful for
    grouping related elements and creating visual hierarchies in the layout.

    > [!WARNING]
    > Do not instantiate this class directly. Use `SceneBuilder.frame()` instead.
    """
    def __init__(self, defaults: Defaults, title: str | None = None):
        super().__init__("frame", defaults)
        self._width = 0.0
        self._height = 0.0
        self._background_color = getattr(defaults, "_background_color")
        self._title = title

    def title(self, title: str) -> Self:
        """Set the title of the frame.

        Args:
            title (str): The title of the frame.

        Returns:
            Self: The current instance of the Frame class.
        """
        self._title = title
        return self
    
    def elements(self, *elements: AbstractElement) -> Self:
        """Add elements to the frame and adjust the frame size accordingly.

        Args:
            elements (AbstractElement): The elements to add to the frame.

        Returns:
            Self: The current instance of the Frame class.
        """
        min_x, min_y = 0.0, 0.0
        max_x, max_y = 0.0, 0.0
        
        for element in elements:
            element._frame_id = self._id

            min_x = min(min_x, element._x)
            min_y = min(min_y, element._y)
            max_x = max(max_x, element._x + element._width)
            max_y = max(max_y, element._y + element._height)

        if self._width == 0.0 and self._height == 0.0:
            width = max_x - min_x + 2 * DEFAULT_FRAME_INSET
            height = max_y - min_y + 2 * DEFAULT_FRAME_INSET
            self.size(width, height)
            self.position(min_x - DEFAULT_FRAME_INSET, min_y - DEFAULT_FRAME_INSET)

        return self

