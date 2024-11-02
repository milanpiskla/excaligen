from ..base.AbstractElement import AbstractElement
from ..base.AbstractStrokedElement import AbstractStrokedElement
from ..geometry.ArcApproximation import ArcApproximation
from ..geometry.BezierApproximation import BezierApproximation
from ..geometry.HalfLineIntersection import HalfLineIntersection

from ...config.Config import Config, DEFAULT_CONFIG

from typing import Self, Tuple, List, Optional
import math

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

    def roundness(self, roundness: str) -> Self:
        """Set the roundness style (sharp, round)."""
        match roundness:
            case "sharp":
                self._roundness = None
            case "round":
                self._roundness = { "type": 3 }
            case _:
                raise ValueError(f"Invalid edges '{roundness}'. Use 'sharp', 'round'")
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
        start_center_x, start_center_y = start.get_center()
        end_center_x, end_center_y = end.get_center()

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
            self.roundness('round')
            start_center = start.get_center()
            end_center = end.get_center()

            # Calculate tangent vectors if necessary
            if self.__connection == 'hspline':
                delta_x = (end_center[0] - start_center[0]) / 2
                self.__start_vector = (delta_x, 0)
                self.__end_vector = (-delta_x, 0)
            elif self.__connection == 'vspline':
                delta_y = (end_center[1] - start_center[1]) / 2
                self.__start_vector = (0, delta_y)
                self.__end_vector = (0, -delta_y)
            # For 'spline', use the provided self.__start_vector and self.__end_vector

            # Find intersection points with elements
            start_edge_point = self.__find_intersection_with_element(
                start, start_center, self.__start_vector
            )
            if start_edge_point is None:
                raise ValueError("Cannot find intersection with start element")

            end_edge_point = self.__find_intersection_with_element(
                end, end_center, self.__end_vector
            )
            if end_edge_point is None:
                raise ValueError("Cannot find intersection with end element")

            # Control points for Bezier curve
            b0 = start_edge_point
            b1 = (b0[0] + self.__start_vector[0], b0[1] + self.__start_vector[1])
            b3 = end_edge_point
            b2 = (b3[0] + self.__end_vector[0], b3[1] + self.__end_vector[1])

            # Use BezierApproximation to generate points
            bezier = BezierApproximation()
            bezier_points = bezier.generate_points(b0, b1, b2, b3)

            # Set arrow's position to the first point
            self._x = bezier_points[0][0]
            self._y = bezier_points[0][1]

            # Convert bezier_points to relative coordinates
            relative_points = [[x - self._x, y - self._y] for x, y in bezier_points]
            self._points = relative_points


        elif self.__connection == 'arc':
            # Use ArcApproximation to generate arc points
        # Calculate the center positions of the start and end elements
            self.roundness('round')
            start_center = start.get_center()
            end_center = end.get_center()
            arc_approx = ArcApproximation()
            try:
                arc_points = arc_approx.generate_points(
                    start_center,
                    end_center,
                    self.__radius,
                    start,
                    end
                )
            except ValueError as e:
                raise ValueError(f"Cannot create arc: {e}")

            # Set arrow's position to the first point
            self._x = arc_points[0][0]
            self._y = arc_points[0][1]

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

    def __calculate_edge_point(self, element: AbstractElement, target_x: float, target_y: float) -> Tuple[float, float]:
        """Calculate the point on the edge of the element closest to the target point."""
        width, height = element._width, element._height
        center_x, center_y = element.get_center()

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

    def __find_intersection_with_element(self, element: AbstractElement, element_center: Tuple[float, float], vector: Tuple[float, float]) -> Optional[Tuple[float, float]]:
        """Find the precise intersection point between a half-line and the element's edge.

        Args:
            element (AbstractElement): The element to find the intersection with.
            element_center (Tuple[float, float]): The center of the element.
            vector (Tuple[float, float]): The direction vector of the half-line.

        Returns:
            Optional[Tuple[float, float]]: The intersection point on the edge of the element.
        """
        # Shift coordinates to element's local coordinate system
        # In local coordinates, the element center is at (0, 0)
        # The half-line starts at (0, 0)
        # The vector is the direction vector

        # If the element is rotated, we need to rotate the vector accordingly
        angle = element._angle
        if angle != 0:
            cos_a = math.cos(-angle)
            sin_a = math.sin(-angle)
            vx, vy = vector
            vx_rot = vx * cos_a - vy * sin_a
            vy_rot = vx * sin_a + vy * cos_a
        else:
            vx_rot, vy_rot = vector

        # Depending on element type, compute intersection
        ew, eh = element._width, element._height

        if element._type == 'ellipse':
            a = ew / 2
            b = eh / 2
            intersection_point = HalfLineIntersection.with_ellipse(0, 0, vx_rot, vy_rot, a, b)
        elif element._type == 'rectangle':
            a = ew / 2
            b = eh / 2
            intersection_point = HalfLineIntersection.with_rectangle(0, 0, vx_rot, vy_rot, a, b)
        elif element._type == 'diamond':
            a = ew / 2
            b = eh / 2
            intersection_point = HalfLineIntersection.with_diamond(0, 0, vx_rot, vy_rot, a, b)
        else:
            return None  # Unsupported element type

        if intersection_point is None:
            return None

        ix, iy = intersection_point

        # Rotate back if necessary
        if angle != 0:
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            ix_global = ix * cos_a - iy * sin_a
            iy_global = ix * sin_a + iy * cos_a
        else:
            ix_global, iy_global = ix, iy

        # Translate back to global coordinates
        ix_global += element_center[0]
        iy_global += element_center[1]

        return (ix_global, iy_global)