"""
Description: Arrow element.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details


from ..base.AbstractElement import AbstractElement
from ..base.AbstractLine import AbstractLine
from ..base.AbstractLabeledElement import AbstractLabeledElement
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..elements.Text import Text

from ..geometry.StraightConnection import StraightConnection
from ..geometry.ArcConnection import ArcConnection
from ..geometry.CurveConnection import CurveConnection
from ..geometry.ElbowConnection import ElbowConnection
from ..geometry.Directions import Directions
from ..geometry.Point import Point

from ..inputs.Arrowheads import Arrowheads

from ...defaults.Defaults import Defaults

from enum import Enum
from typing import Self, Any

class Arrow(AbstractLine, AbstractLabeledElement):
    """A class representing an arrow element in Excalidraw with various connection styles.

    It creates arrow elements that can connect different elements
    in various ways including straight lines, curves, arcs and elbowed connections. It supports
    customizable arrowheads, gaps between connected elements, and different binding behaviors.
    The arrow can be styled with:
    - Different connection types (straight, arc, curve, elbow)
    - Customizable start and end arrowheads
    - Adjustable gaps between connected elements
    - Binding capabilities to connect elements
    - Various arrow directions and angles
    """
    class ConnectionType(Enum):
        STRAIGHT = 0
        ARC = 1
        CURVE = 2
        ELBOW = 3

    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None) -> None:
        AbstractLine.__init__(self, "arrow", defaults)
        self._init_labels(listener, label)
        self._start_binding = None
        self._end_binding = None
        self._start_arrowhead = getattr(defaults, "_start_arrowhead")
        self._end_arrowhead = getattr(defaults, "_end_arrowhead")
        self._elbowed = False
        self.__start_gap = 1
        self.__end_gap = 1
        self.__start_angle: float | str = 0.0
        self.__end_angle: float | str = 0.0
        self.__start_direction: str | None = None
        self.__end_direction: str | None = None
        self.__radius: float | None = None  # For arc connections
        self.__start_element: AbstractElement | None = None
        self.__end_element: AbstractElement | None = None
        self.__connection_type = Arrow.ConnectionType.STRAIGHT
        self.__is_already_bound = False

    def curve(self, start_angle: float | str, end_angle: float | str) -> Self:
        """Generate a curve between the bound elements using the given start and end tangent angles.

        Args:
            start_angle (float | str): The start tangent angle. It's either float value in radians or one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively.
            end_angle (float | str): The end tangent angle. It's either float value in radians or one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self.__connection_type = Arrow.ConnectionType.CURVE
        self.__start_angle = start_angle
        self.__end_angle = end_angle
        self.roundness('round')
        self.__try_connect_elements()
        return self
    
    def arc(self, radius: float) -> Self:
        """Approximate an arc between the bound elements with the given radius.

        The center of the arc is determined by the radius and the positions of the bound elements
        by assuming the center of the start element and the center of the end element are oriented clockwise.

        Args:
            radius (float): The radius of the arc.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self.__connection_type = Arrow.ConnectionType.ARC
        self.__radius = radius
        self.roundness('round')
        self.__try_connect_elements()
        return self

    def gap(self, gap: float, end_gap: float | None = None) -> Self:
        """Set the gap at the start and end of the arrow.

        Args:
            gap (float): The gap at the start of the arrow.
            end_gap (float, optional): The gap at the end of the arrow. Defaults to the value of `gap`.

        Returns:
            Self: The current instance of the Arrow class.
        """
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

    def arrowheads(self, start: str | None = None, end: str | None = 'arrow') -> Self:
        """Set the arrowhead styles for the start and end of the arrow.

        Valid arrowheads values are None, 'arrow', 'bar', 'dot' and 'triangle'.

        Args:
            start (str, optional): The style of the start arrowhead. Defaults to None.
            end (str, optional): The style of the end arrowhead. Defaults to 'arrow'.

        Raises:
            ValueError: If an invalid arrowhead style is provided.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self._start_arrowhead, self._end_arrowhead = Arrowheads.from_(start, end)
        return self

    def elbow(self, start_direction: str, end_direction: str) -> Self:
        """Set the arrow to have an elbow (right-angle turn).

        Args:
            start_direction (str): The direction of the start elbow. It's one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively.
            end_direction (str): The direction of the end elbow. It's one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self._elbowed = True
        self.__connection_type = Arrow.ConnectionType.ELBOW
        self.__start_direction = start_direction
        self.__end_direction = end_direction
        self.__try_connect_elements()
        return self 

    def bind(self, start: AbstractElement, end: AbstractElement) -> Self:
        """Bind the arrow between two elements, supporting different connection styles.

        Args:
            start (AbstractElement): The start element.
            end (AbstractElement): The end element.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self.__start_element = start
        self.__end_element = end
        self.__try_connect_elements()
        return self
    
    def __try_connect_elements(self) -> Self:
        """Attempt to connect the bound elements based on the connection type.

        Returns:
            Self: The current instance of the Arrow class.
        """
        if self.__start_element is not None and self.__end_element is not None:
            if not self.__is_already_bound:
                self.__set_binding_attributes()
                self.__is_already_bound = True
        
            self.__calculate_points()
            self.__try_update_binding_attributes_with_fixed_points()

        return self

    def __calculate_points(self) -> Self:
        """Calculate the points for the arrow based on the connection type.

        Returns:
            Self: The current instance of the Arrow class.
        """
        match self.__connection_type:
            case Arrow.ConnectionType.STRAIGHT:
                self.__transform_points(StraightConnection(self.__start_element, self.__end_element).points()) # type: ignore

            case Arrow.ConnectionType.ARC:
                self.__transform_points(ArcConnection(self.__start_element, self.__end_element, self.__radius).points()) # type: ignore

            case Arrow.ConnectionType.CURVE:
                self.__transform_points(CurveConnection(self.__start_element, self.__end_element, self.__start_angle, self.__end_angle).points()) # type: ignore

            case Arrow.ConnectionType.ELBOW:
                self.__transform_points(ElbowConnection(self.__start_element, self.__end_element, self.__start_direction, self.__end_direction).points()) # type: ignore

        return self

    def __set_binding_attributes(self) -> Self:
        """Set the binding attributes for the arrow.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self._start_binding = self.__compute_binding_attributes(self.__start_element._id, self.__start_gap) # type: ignore
        self._end_binding = self.__compute_binding_attributes(self.__end_element._id, self.__end_gap) # type: ignore

        self.__start_element._add_bound_element(self) # type: ignore already checked
        self.__end_element._add_bound_element(self) # type: ignore already checked

        return self
    
    def __compute_binding_attributes(self, id: str, gap: float) -> dict[str, Any]:
        """Compute the binding attributes for an element.

        Args:
            id (str): The ID of the element.
            gap (float): The gap for the binding.

        Returns:
            dict[str, Any]: The binding attributes.
        """
        result: dict[str, Any] = {"focus": 0}
        result["elementId"] = id
        result["gap"] = gap
        return result

    def __try_update_binding_attributes_with_fixed_points(self) -> Self:
        """Update the binding attributes with fixed points if the connection type is elbow.

        Returns:
            Self: The current instance of the Arrow class.
        """
        if self.__connection_type == Arrow.ConnectionType.ELBOW:
            self._start_binding["fixedPoint"] = self.__compute_fixed_point(self.__start_direction) # type: ignore
            self._end_binding["fixedPoint"] = self.__compute_fixed_point(self.__end_direction) # type: ignore
        
        return self

    def __transform_points(self, points: list[Point]) -> Self:
        """Transform the points for the arrow.

        Args:
            points (list[Point]): The points to transform.

        Returns:
            Self: The current instance of the Arrow class.
        """
        self._x = points[0][0]
        self._y = points[0][1]

        relative_points = [(x - self._x, y - self._y) for x, y in points]
        self.points(relative_points) # type: ignore

        return self
    
    def __compute_fixed_point(self, direction: str) -> Point:
        """Compute the fixed point for a given direction.

        Args:
            direction (str): The direction for the fixed point.

        Returns:
            Point: The computed fixed point.
        """
        dx, dy = Directions.dxdy(direction)
        return ((dx + 1.0) / 2.0, (dy + 1.0) / 2.0)
