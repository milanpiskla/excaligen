from ..base.AbstractElement import AbstractElement
from .AaLineSegmentIntersection import AaLineSegmentIntersection

from .Point import Point
from typing import Optional, Callable

import math
import copy

MIN_SEGMENT_HINT: float = 10.0
MAX_ELBOWS = 8

Segment = tuple[Point, Point]

class ElbowConnection:
    class Trajectory:
        def __init__(self):
            self._points: list[Point] = []
            self._distance: float = 0.0

        def is_better_than(self, other: ElbowConnection.Trajectory) -> bool:
            if len(other._points) == 0:
                return True

            if len(self._points) < len(other._points):
                return True
            
            if len(self._points) == len(other._points):
                if self._distance < other._distance:
                    return True
                
            return False

        def get_elbows_count(self) -> int:
            return len(self._points)

        def get_points(self) -> list[Point]:
            return self._points
        
        def reset(self):
            self._points.clear()
            self._distance = 0
        
        def add_point(self, point: Point) -> None:
            if len(self._points) > 0:
                xlast, ylast = self._points[-1]
                x, y = point
                self._distance += math.max(abs(x - xlast), abs(y - ylast))
            
            self._points.append(point)

        def pop_point(self):
            self._points.pop()

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

        self._best_trajectory = ElbowConnection.Trajectory()
        self._current_trajectory = ElbowConnection.Trajectory()

    def points(self) -> list[Point]:
        self._compute_bounds()
        self._fill_horizontal_routes()
        self._fill_vertical_routes()

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

    def _find_horizontal_gap_line(self) -> Optional(float):
        """Find a line in the middle of the horizontal space between the rectangles."""
        y1 = math.max(self._start_element._y, self._end_element._y)
        y2 = math.min(self._start_element._y + self._start_element._height, self._end_element._y + self._end_element._height)

        return (y1 + y2) / 2 if y1 < y2 else None
    
    def _find_vertical_gap_line(self) -> Optional(float):
        """Find a line in the middle of the vertical space between the rectangles."""
        x1 = math.max(self._start_element._x, self._end_element._x)
        x2 = math.min(self._start_element._x + self._start_element._width, self._end_element._x + self._end_element._width)
        
        return (x1 + x2) / 2 if x1 < x2 else None

    def _compute_bounds(self) -> None:
        self._xmin = min(self._start_element._x, self._end_element._x) - self._min_segment_hint
        self._xmax = max(self._start_element._x + self._start_element._width, self._end_element._x + self._end_element._width) + self._min_segment_hint
        self._ymin = min(self._start_element._y, self._end_element._y) - self._min_segment_hint
        self._ymax = max(self._start_element._y + self._start_element._height, self._end_element._y + self._end_element._height) + self._min_segment_hint

    def _fill_horizontal_routes(self) -> None:
        pass

    def _fill_vertical_routes(self) -> None:
        pass

    # def _cross_horizontal(self, p1:Point, p2: Point) -> None:
    #     if self._current_trajectory.get_elbows_count() < MAX_ELBOWS:
    #         if not self._try_complete_trajectory(p1, p2):
    #             for q1, q2 in self._horizontal_segments:
    #                 intersection = AaLineSegmentIntersection.with_aa_line_segment(p1, p2, q1, q2)
    #                 if intersection:
    #                     self._current_trajectory.add_point(intersection)
    #                     self._cross_vertical(intersection[0], intersection[1])
        
    #     self._current_trajectory.pop_point()

    # def _cross_vertical(self, p1:Point, p2: Point) -> None:
    #     if self._current_trajectory.get_elbows_count() < MAX_ELBOWS:
    #         if not self._try_complete_trajectory(p1, p2):
    #             for q1, q2 in self._vertical_segments:
    #                 intersection = AaLineSegmentIntersection.with_aa_line_segment(p1, p2, q1, q2)
    #                 if intersection:
    #                     self._current_trajectory.add_point(intersection)
    #                     self._cross_horizontal(intersection[0], intersection[1])
        
    #     self._current_trajectory.pop_point()


    # Recursive magic follows :)

    def _cross_horizontal(self, p1:Point, p2: Point) -> None:
        self._cross_segment(p1, p2, self._cross_vertical, self._horizontal_segments)

    def _cross_vertical(self, p1:Point, p2: Point) -> None:
        self._cross_segment(p1, p2, self._cross_horizontal, self._vertical_segments)

    def _cross_segment(self, p1:Point, p2: Point, cross_function: Callable, cross_segments: list[Segment]) -> None:
        if self._current_trajectory.get_elbows_count() < MAX_ELBOWS:
            if not self._try_complete_trajectory(p1, p2):
                for q1, q2 in cross_segments:
                    intersection = AaLineSegmentIntersection.with_aa_line_segment(p1, p2, q1, q2)
                    if intersection:
                        self._current_trajectory.add_point(intersection)
                        cross_function(intersection[0], intersection[1])
        
        self._current_trajectory.pop_point()

    def _try_complete_trajectory(self, p1: Point, p2: Point) -> bool:
        if AaLineSegmentIntersection.is_point_on_segment(self._end_point, p1, p2):
            self._current_trajectory.add_point(self._end_point)
            if self._current_trajectory.is_better_than(self._best_trajectory):
                self._best_trajectory = copy.deepcopy(self._current_trajectory)
                return True
