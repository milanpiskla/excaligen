from ..base.AbstractElement import AbstractElement
from .AaLineSegmentIntersection import AaLineSegmentIntersection

from .Point import Point
from typing import Optional

import math

MIN_SEGMENT_HINT: float = 10.0
MAX_ELBOWS = 8

Segment = tuple[Point, Point]

class ElbowConnection:
    def __init__(self, start_element: AbstractElement, end_element: AbstractElement, start_dir: str, end_dir: str, min_segment_hint = MIN_SEGMENT_HINT):
        self._start_element = start_element
        self._end_element = end_element
        self._start_dir = start_dir
        self._end_dir = end_dir

        self._start_point = self.__find_edge_point(self._start_element, self._start_dir)
        self._end_point = self.__find_edge_point(self._end_element, self._end_dir)

        self._vertical_segments: list[Segment] = []
        self._horizontal_segments: list[Segment] = []

        self._min_segment_hint = min_segment_hint

        self._xmin = 0.0
        self._xmax = 0.0
        self._ymin = 0.0
        self._ymax = 0.0

    def points(self) -> list[Point]:
        self._compute_bounds()
        self._fill_horizontal_routes()
        self._fill_vertical_routes()


        path = [start_point]

        return path
    
    def __find_edge_point(self, element: AbstractElement, direction: str) -> Point:
        if direction not in ['N', 'W', 'S', 'E']:
            raise ValueError(f'Wrong direction {direction}, shoould be one of the N, W, S, E')
        
        cx, cy = element.get_center()
        a, b = element._width / 2, element._height / 2

        match direction:
            case 'N':
                return cx, cy - b
            case 'W':
                return cx - a, cy
            case 'S':
                return cx, cy + b
            case 'E':
                return cx + a, cy

    def _compute_horizontal_space(self) -> float:
        """Compute the horizontal space between the rectangles."""
        x1_min = self._start_element._x
        x1_max = self._start_element._x + self._start_element._width
        x2_min = self._end_element._x
        x2_max = self._end_element._x + self._end_element._width

        if x1_max < x2_min:
            return x2_min - x1_max
        elif x2_max < x1_min:
            return x1_min - x2_max
        else:
            return 0  # Rectangles overlap horizontally

    def _compute_vertical_space(self) -> float:
        """Compute the vertical space between the rectangles."""
        y1_min = self._start_element._y
        y1_max = self._start_element._y + self._start_element._height
        y2_min = self._end_element._y
        y2_max = self._end_element._y + self._end_element._height

        if y1_max < y2_min:
            return y2_min - y1_max
        elif y2_max < y1_min:
            return y1_min - y2_max
        else:
            return 0  # Rectangles overlap vertically

    def _compute_bounds(self) -> None:
        self._xmin = min(self._start_element._x, self._end_element._x) - self._min_segment_hint
        self._xmax = max(self._start_element._x + self._start_element._width, self._end_element._x + self._end_element._width) + self._min_segment_hint
        self._ymin = min(self._start_element._y, self._end_element._y) - self._min_segment_hint
        self._ymax = max(self._start_element._y + self._start_element._height, self._end_element._y + self._end_element._height) + self._min_segment_hint

    def _fill_horizontal_routes(self) -> None:
        pass

    def _fill_vertical_routes(self) -> None:
        pass

    def _cross_vertical(self, horizontal: Segment, points: list[Point]) -> list[Point]:
        p1, p2 = horizontal
        if AaLineSegmentIntersection.is_point_on_segment(self._end_point, p1, p2):
            points.append(self._end_point)
            return points
        
        if len(points) > MAX_ELBOWS:
            return []
        
        for vertical in self._vertical_segments:
            q1, q2 = vertical
            intersection = AaLineSegmentIntersection.with_aa_line_segment(p1, p2, q1, q2)
            if intersection is None:
                return []
            else:
                points.append(intersection)
                return self._cross_horizontal(vertical, points)

        return points

    def _cross_horizontal(self, vertical: Segment, points: list[Point]) -> list[Point]:
        p1, p2 = vertical
        if AaLineSegmentIntersection.is_point_on_segment(self._end_point, p1, p2):
            points.append(self._end_point)
            return points
        
        if len(points) > MAX_ELBOWS:
            return []
        
        for horizontal in self._horizontal_segments:
            q1, q2 = horizontal
            intersection = AaLineSegmentIntersection.with_aa_line_segment(p1, p2, q1, q2)
            if intersection is None:
                return []
            else:
                points.append(intersection)
                return self._cross_vertical(horizontal, points)

        return points
