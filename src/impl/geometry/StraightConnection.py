"""
Description: Straight connection between two elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractElement import AbstractElement
from .HalfLineIntersection import HalfLineIntersection
from .Point import Point

from typing import Optional

class StraightConnection:
    def __init__(self, start_element: AbstractElement, end_element: AbstractElement):
        self._start_element = start_element
        self._end_element = end_element

    def points(self) -> list[Point]:
        xs, ys = self._start_element.get_center()
        xe, ye = self._end_element.get_center()

        points = []

        start_point = self.__find_intersection_with_element(self._start_element, 0.0, 0.0, xe - xs, ye - ys)
        if start_point is None:
            raise Exception("Cannot find intersection as start point")
        points.append(start_point)

        end_point = self.__find_intersection_with_element(self._end_element, 0.0, 0.0, xs - xe, ys - ye)
        if end_point is None:
            raise Exception("Cannot find intersection as end point")
        points.append(end_point)
        
        return points

    def __find_intersection_with_element(self, element: AbstractElement, dx: float, dy: float, vx: float, vy: float) -> Optional[Point]:
        """Find the precise intersection point between a half-line and the element's edge."""

        a, b = element._width / 2, element._height / 2
        intersection: Point = (0.0, 0.0)

        match element._type:
            case "rectangle" | "image" | "text":
                intersection = HalfLineIntersection.with_rectangle(dx, dy, vx, vy, a, b, element._angle) # type: ignore
            
            case "diamond":
                intersection = HalfLineIntersection.with_diamond(dx, dy, vx, vy, a, b, element._angle) # type: ignore
            
            case "ellipse":
                intersection = HalfLineIntersection.with_ellipse(dx, dy, vx, vy, a, b, element._angle) # type: ignore

            case _:
                raise TypeError(f"Cannot find intersection with unknown type {element._type}")
            
        return tuple(p + t for p, t in zip(intersection, element.get_center()))
            
