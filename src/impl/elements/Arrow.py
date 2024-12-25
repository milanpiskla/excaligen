from ..base.AbstractElement import AbstractElement
from ..base.AbstractLine import AbstractLine

from ..geometry.StraightConnection import StraightConnection
from ..geometry.ArcConnection import ArcConnection
from ..geometry.CurveConnection import CurveConnection
from ..geometry.ElbowConnection import ElbowConnection
from ..geometry.Directions import Directions
from ..geometry.Point import Point

from ...config.Config import Config, DEFAULT_CONFIG

from enum import Enum
from typing import Self

class Arrow(AbstractLine):
    """Represents an arrow element in Excalidraw, capable of different styles like straight lines, splines, arcs, etc."""

    class ConnectionType(Enum):
        STRAIGHT = 0
        ARC = 1
        CURVE = 2
        ELBOW = 3

    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("arrow", config)
        self._start_binding = None
        self._end_binding = None
        self._start_arrowhead = config.get("startArrowhead", None)
        self._end_arrowhead = config.get("endArrowhead", "arrow")
        self._elbowed = False
        self.__start_gap = 1
        self.__end_gap = 1
        self.__start_angle: float | str = 0.0
        self.__end_angle: float | str = 0.0
        self.__start_direction: str = None
        self.__end_direction: str = None
        self.__radius: float = None  # For arc connections
        self.__start_element: AbstractElement = None
        self.__end_element: AbstractElement = None
        self.__connection_type = Arrow.ConnectionType.STRAIGHT
        self.__is_already_bound = False

    def curve(self, start_angle: float | str, end_angle: float | str) -> Self:
        """Approximates a cubic Bezier using the given start and end tangent vectors."""
        self.__connection_type = Arrow.ConnectionType.CURVE
        self.__start_angle = start_angle
        self.__end_angle = end_angle
        self.roundness('round')
        self.__try_connect_elements()
        return self
    
    def arc(self, radius: float) -> Self:
        """Approximates an arc between the bound elements with the given radius."""
        self.__connection_type = Arrow.ConnectionType.ARC
        self.__radius = radius
        self.roundness('round')
        self.__try_connect_elements()
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

    def elbow(self, start_direction: str, end_direction: str) -> Self:
        """Set the arrow to have an elbow (right-angle turn)."""
        self._elbowed = True
        self.__connection_type = Arrow.ConnectionType.ELBOW
        self.__start_direction = start_direction
        self.__end_direction = end_direction
        self.__try_connect_elements()
        return self 

    def bind(self, start: AbstractElement, end: AbstractElement) -> Self:
        """Bind the arrow between two elements, supporting different connection styles."""
        self.__start_element = start
        self.__end_element = end
        self.__try_connect_elements()
        return self

    def __try_connect_elements(self) -> Self:
        if self.__start_element is not None and self.__end_element is not None:
            if not self.__is_already_bound:
                self.__set_binding_attributes()
                self.__is_already_bound = True
        
            self.__calculate_points()
            self.__try_update_binding_attributes_with_fixed_points()

        return self

    def __calculate_points(self) -> Self:
        match self.__connection_type:
            case Arrow.ConnectionType.STRAIGHT:
                self.__transform_points(StraightConnection(self.__start_element, self.__end_element).points())

            case Arrow.ConnectionType.ARC:
                self.__transform_points(ArcConnection(self.__start_element, self.__end_element, self.__radius).points())

            case Arrow.ConnectionType.CURVE:
                self.__transform_points(CurveConnection(self.__start_element, self.__end_element, self.__start_angle, self.__end_angle).points())

            case Arrow.ConnectionType.ELBOW:
                self.__transform_points(ElbowConnection(self.__start_element, self.__end_element, self.__start_direction, self.__end_direction).points())

        return self

    def __set_binding_attributes(self) -> Self:
        self._start_binding = self.__compute_binding_attributes(self.__start_element._id, self.__start_gap)
        self._end_binding = self.__compute_binding_attributes(self.__end_element._id, self.__end_gap)

        self.__start_element._add_bound_element(self)
        self.__end_element._add_bound_element(self)

        return self
    
    def __compute_binding_attributes(self, id: str, gap: float) -> dict[str, any]:
        result = {"focus": 0}
        result["elementId"] = id
        result["gap"] = gap
        return result

    def __try_update_binding_attributes_with_fixed_points(self) -> Self:
        if self.__connection_type == Arrow.ConnectionType.ELBOW:
            self._start_binding["fixedPoint"] = self.__compute_fixed_point(self.__start_direction)
            self._end_binding["fixedPoint"] = self.__compute_fixed_point(self.__end_direction)

    def __transform_points(self, points: list[Point]) -> Self:
        self._x = points[0][0]
        self._y = points[0][1]

        relative_points = [[x - self._x, y - self._y] for x, y in points]
        self.points(relative_points)

        return self
    
    def __compute_fixed_point(self, direction: str) -> Point:
        dx, dy = Directions.dxdy(direction)
        return ((dx + 1.0) / 2.0, (dy + 1.0) / 2.0)
    