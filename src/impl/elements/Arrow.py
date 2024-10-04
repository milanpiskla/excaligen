import math
from ..base.AbstractElement import AbstractElement
from ..base.AbstractShape import AbstractShape
from ...config.Config import Config, DEFAULT_CONFIG
from typing import Self

class Arrow(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("arrow", config)
        self._start_binding = None
        self._end_binding = None
        self._start_arrowhead = config.get("startArrowhead", None)
        self._end_arrowhead = config.get("endArrowhead", "arrow")
        self._points = []

    def points(self, points: list[tuple[float, float]]) -> Self:
        self._points = points
        return self

    def bind(self, start: AbstractElement, end: AbstractElement) -> Self:
        """Bind the arrow between two elements."""
        # Calculate the center positions of the start and end elements
        start_center_x, start_center_y = self.__get_element_center(start)
        end_center_x, end_center_y = self.__get_element_center(end)

        # Calculate edge points
        start_x, start_y = self.__calculate_edge_point(start, end_center_x, end_center_y)
        end_x, end_y = self.__calculate_edge_point(end, start_center_x, start_center_y)

        # Set arrow points relative to the arrow's position
        self._points = [
            [0, 0],  # Start point at (0, 0)
            [end_x - start_x, end_y - start_y]  # End point relative to start
        ]

        # Set arrow position at the calculated start point
        self._x = start_x
        self._y = start_y

        # Set bindings
        self._start_binding = {
            "elementId": start._id,
            "focus": 0,
            "gap": 1
        }
        self._end_binding = {
            "elementId": end._id,
            "focus": 0,
            "gap": 1
        }

        # Add bound elements
        start._add_bound_element(self)
        end._add_bound_element(self)

        return self

    def __get_element_center(self, element: AbstractElement) -> tuple[float, float]:
        """Calculate the center of an element."""
        width = getattr(element, '_width', 0)
        height = getattr(element, '_height', 0)
        center_x = element._x + width / 2
        center_y = element._y + height / 2
        return center_x, center_y

    def __calculate_edge_point(self, element: AbstractElement, target_x: float, target_y: float) -> tuple[float, float]:
        """Calculate the point on the edge of the element closest to the target point."""
        x, y = element._x, element._y
        width = getattr(element, '_width', 0)
        height = getattr(element, '_height', 0)
        center_x, center_y = self.__get_element_center(element)

        dx = target_x - center_x
        dy = target_y - center_y

        if width == 0 or height == 0 or (dx == 0 and dy == 0):
            # If the element has no size or target is at the center, return the center
            return center_x, center_y

        # Compute scaling factors to reach the edge
        if dx != 0:
            t_x = (width / 2) / abs(dx)
        else:
            t_x = float('inf')

        if dy != 0:
            t_y = (height / 2) / abs(dy)
        else:
            t_y = float('inf')

        t = min(t_x, t_y)

        # Compute the edge point
        ex = center_x + t * dx
        ey = center_y + t * dy

        return ex, ey
