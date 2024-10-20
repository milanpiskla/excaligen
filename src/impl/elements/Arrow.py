from ..base.AbstractElement import AbstractElement
from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..splines.ArcApproximation import ArcApproximation
from ..splines.BezierApproximation import BezierApproximation

from ...config.Config import Config, DEFAULT_CONFIG

from typing import Self, Tuple, List

class Arrow(AbstractStrokedElement):
    """Represents an arrow element in Excalidraw, capable of different styles like straight lines, splines, arcs, etc."""

    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("arrow", config)
        self._start_binding = None
        self._end_binding = None
        self._start_arrowhead = config.get("startArrowhead", None)
        self._end_arrowhead = config.get("endArrowhead", "arrow")
        self._points = []
        self.__start_gap = 1
        self.__end_gap = 1
        self.__connection = 'straight'  # default connection style
        self.__start_vector = (0, 0)
        self.__end_vector = (0, 0)
        self.__radius = None  # For arc connections

    def points(self, points: List[Tuple[float, float]]) -> Self:
        self._points = points
        return self

    def spline(self, start_vector: Tuple[float, float], end_vector: Tuple[float, float]) -> Self:
        """Approximates a Bezier spline using the given start and end tangent vectors."""
        self.__connection = 'spline'
        self.__start_vector = start_vector
        self.__end_vector = end_vector
        return self
    
    def hspline(self) -> Self:
        """Approximates a Bezier spline with horizontal start and end tangent vectors."""
        self.__connection = 'hspline'
        return self

    def vspline(self) -> Self:
        """Approximates a Bezier spline with vertical start and end tangent vectors."""
        self.__connection = 'vspline'
        return self

    def arc(self, radius: float) -> Self:
        """Approximates an arc between the bound elements with the given radius."""
        self.__connection = 'arc'
        self.__radius = radius
        return self

    def gap(self, gap: float, end_gap: float = None) -> Self:
        """Set the gap at the start and end of the arrow."""
        if end_gap is None:
            end_gap = gap
        self.__start_gap = gap
        self.__end_gap = end_gap
        # Update bindings if they exist
        if self._start_binding is not None:
            self._start_binding['gap'] = self.__start_gap
        if self._end_binding is not None:
            self._end_binding['gap'] = self.__end_gap
        return self

    def arrowheads(self, start: str = 'none', end: str = 'arrow') -> Self:
        """Set the arrowhead styles for the start and end of the arrow."""
        valid_arrowheads = {'none', 'arrow', 'bar', 'dot', 'triangle'}
        start = start.lower()
        end = end.lower()
        if start not in valid_arrowheads:
            raise ValueError(f"Invalid start arrowhead '{start}'. Valid options are {valid_arrowheads}.")
        if end not in valid_arrowheads:
            raise ValueError(f"Invalid end arrowhead '{end}'. Valid options are {valid_arrowheads}.")
        self._start_arrowhead = None if start == 'none' else start
        self._end_arrowhead = None if end == 'none' else end
        return self

    def elbow(self) -> Self:
        """Set the arrow to have an elbow (right-angle turn)."""
        self.__connection = 'elbow'
        return self 

    def bind(self, start: AbstractElement, end: AbstractElement) -> Self:
        """Bind the arrow between two elements, supporting different connection styles."""
        # Calculate the center positions of the start and end elements
        start_center_x, start_center_y = self.__get_element_center(start)
        end_center_x, end_center_y = self.__get_element_center(end)

        # Calculate edge points
        start_x, start_y = self.__calculate_edge_point(start, end_center_x, end_center_y)
        end_x, end_y = self.__calculate_edge_point(end, start_center_x, start_center_y)

        # Set arrow position at the calculated start point
        self._x = start_x
        self._y = start_y

        if self.__connection == 'elbow':
            # Create an elbow path
            mid_x = end_x if abs(end_x - start_x) > abs(end_y - start_y) else start_x
            mid_y = start_y if abs(end_x - start_x) > abs(end_y - start_y) else end_y
            self._points = [
                [0, 0],
                [mid_x - start_x, mid_y - start_y],
                [end_x - start_x, end_y - start_y]
            ]
        elif self.__connection in ['hspline', 'vspline', 'spline']:
            # Use Bezier approximation to create spline
            start_point = (start_x, start_y)
            end_point = (end_x, end_y)

            if self.__connection == 'hspline':
                # Horizontal tangents
                delta_x = (end_x - start_x) / 2
                self.__start_vector = (delta_x, 0)
                self.__end_vector = (-delta_x, 0)
            elif self.__connection == 'vspline':
                # Vertical tangents
                delta_y = (end_y - start_y) / 2
                self.__start_vector = (0, delta_y)
                self.__end_vector = (0, -delta_y)
            # For 'spline', use the provided start_vector and end_vector

            # Control points for Bezier curve
            b0 = start_point
            b1 = (start_point[0] + self.__start_vector[0], start_point[1] + self.__start_vector[1])
            b2 = (end_point[0] + self.__end_vector[0], end_point[1] + self.__end_vector[1])
            b3 = end_point

            # Use BezierApproximation to generate points
            bezier = BezierApproximation()
            bezier_points = bezier.generate_points(b0, b1, b2, b3)

            # Convert bezier_points to relative coordinates
            relative_points = [[x - self._x, y - self._y] for x, y in bezier_points]
            self._points = relative_points
        elif self.__connection == 'arc':
            # Use ArcApproximation to generate arc points
            start_point = (start_x, start_y)
            end_point = (end_x, end_y)
            arc_approx = ArcApproximation()
            arc_points = arc_approx.generate_points(start_point, end_point, self.__radius)
            # Convert arc_points to relative coordinates
            relative_points = [[x - self._x, y - self._y] for x, y in arc_points]
            self._points = relative_points
        else:
            # Default is straight line
            self._points = [
                [0, 0],  # Start point at (0, 0)
                [end_x - start_x, end_y - start_y]  # End point relative to start
            ]

        # Set bindings
        self._start_binding = {
            "elementId": start._id,
            "focus": 0,
            "gap": self.__start_gap
        }
        self._end_binding = {
            "elementId": end._id,
            "focus": 0,
            "gap": self.__end_gap
        }

        # Add bound elements
        start._add_bound_element(self)
        end._add_bound_element(self)

        return self

    def __get_element_center(self, element: AbstractElement) -> Tuple[float, float]:
        """Calculate the center of an element."""
        width = getattr(element, '_width', 0)
        height = getattr(element, '_height', 0)
        center_x = element._x + width / 2
        center_y = element._y + height / 2
        return center_x, center_y

    def __calculate_edge_point(self, element: AbstractElement, target_x: float, target_y: float) -> Tuple[float, float]:
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
