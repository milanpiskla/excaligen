from ..base.AbstractElement import AbstractElement
from .HalfLineIntersection import HalfLineIntersection
from .Point import Point
from .BezierApproximation import BezierApproximation

from typing import Optional
import math

class BezierConnection:
    def __init__(self, start_element: AbstractElement, end_element: AbstractElement, start_angle = 0.0, end_angle = 0.0):
        self._start_element = start_element
        self._end_element = end_element
        self._start_angle = start_angle
        self._end_angle = end_angle
        self._start_weight = 0.5
        self._end_weight = 0.5

    def points(self) -> list[Point]:
        vsx = math.cos(self._start_angle)
        vsy = math.sin(self._start_angle)
        vex = math.cos(self._end_angle)
        vey = math.sin(self._end_angle)

        b0, b3 = self.__find_intersection_points(vsx, vsy, vex, vey)
        w = abs(b0[0] - b3[0])
        h = abs(b0[1] - b3[1])
        b1 = b0[0] + vsx * w * self._start_weight, b0[1] + vsy * h * self._start_weight
        b2 = b3[0] + vex * w * self._end_weight, b3[1] + vey * h * self._end_weight

        return BezierApproximation().generate_points(b0, b1, b2, b3)
    
    def __find_intersection_points(self, vsx: float, vsy: float, vex: float, vey: float) -> tuple[Point, Point]:
        start_point = self.__find_intersection_with_element(self._start_element, 0.0, 0.0, vsx, vsy)
        if start_point is None:
            raise Exception("Cannot find intersection as start point")

        end_point = self.__find_intersection_with_element(self._end_element, 0.0, 0.0, vex, vey)
        if end_point is None:
            raise Exception("Cannot find intersection as end point")
        
        return start_point, end_point

    def __find_intersection_with_element(self, element: AbstractElement, dx: float, dy: float, vx: float, vy: float) -> Optional[Point]:
        """Find the precise intersection point between a half-line and the element's edge."""

        a, b = element._width / 2, element._height / 2
        intersection: Point = (0.0, 0.0)

        match element._type:
            case "rectangle" | "image" | "text":
                intersection = HalfLineIntersection.with_rectangle(dx, dy, vx, vy, a, b, element._angle)
            
            case "diamond":
                intersection = HalfLineIntersection.with_diamond(dx, dy, vx, vy, a, b, element._angle)
            
            case "ellipse":
                intersection = HalfLineIntersection.with_ellipse(dx, dy, vx, vy, a, b, element._angle)

            case _:
                raise TypeError(f"Cannot find intersection with unknown type {element._type}")
            
        return tuple(p + t for p, t in zip(intersection, element.get_center()))
            
