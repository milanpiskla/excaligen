"""
Description: Elbow connection between two elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractElement import AbstractElement
from .AaLineSegmentIntersection import AaLineSegmentIntersection
from .Directions import Directions

from .Point import Point
from typing import Optional, Callable

import copy

MIN_SEGMENT_HINT: float = 30.0
MAX_ELBOWS = 8

Segment = tuple[Point, Point]

class ElbowConnection:
    class Trajectory:
        def __init__(self):
            self._points: list[Point] = []
            self._distance: float = 0.0

        def is_better_than(self, other: 'ElbowConnection.Trajectory') -> bool:
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
        
        def add_point(self, point: Point) -> None:
            if len(self._points) > 0:
                xlast, ylast = self._points[-1]
                x, y = point
                self._distance += max(abs(x - xlast), abs(y - ylast))
            
            self._points.append(point)

        def pop_point(self):
            self._points.pop()

    def __init__(self, start_element: AbstractElement, end_element: AbstractElement, start_dir: str, end_dir: str, min_segment_hint = MIN_SEGMENT_HINT):
        self._start_element = start_element
        self._end_element = end_element
        self._start_dir = start_dir
        self._end_dir = end_dir

        self._start_point = self._find_edge_point(self._start_element, self._start_dir)
        self._end_point = self._find_edge_point(self._end_element, self._end_dir)

        self._vertical_segments: list[Segment] = []
        self._horizontal_segments: list[Segment] = []

        self._min_segment_hint = min_segment_hint

        self._xmin = 0.0
        self._xmax = 0.0
        self._ymin = 0.0
        self._ymax = 0.0

        self._best_trajectory = ElbowConnection.Trajectory()
        self._current_trajectory = ElbowConnection.Trajectory()

        self._is_already_computed = False

    def points(self) -> list[Point]:
        if not self._is_already_computed:
            self._compute_bounds()
            start_segment = self._find_free_segment(self._start_point, self._start_dir, self._end_element)
            if not start_segment or not AaLineSegmentIntersection.is_aa_segment(start_segment[0], start_segment[1]):
                return [self._start_point, self._end_point]
        
            self._fill_segments()
                
            p1, p2 = start_segment
            self._current_trajectory.add_point(p1)
            self._cross_vertical(p1, p2) if AaLineSegmentIntersection.is_horizontal_segment(p1, p2) else self._cross_horizontal(p1, p2)

            self._is_already_computed = True

        return self._best_trajectory.get_points()

    def _find_edge_point(self, element: AbstractElement, direction: str) -> Point:
        if direction not in Directions.keys():
            raise ValueError(f'Wrong direction {direction}, shoould be one of the U, L, D, R')
        
        cx, cy = element.get_center()
        a, b = element._width / 2, element._height / 2
        dx, dy = Directions.dxdy(direction)
        
        return cx + a * dx, cy + b * dy

    def _find_horizontal_gap_segment(self) -> Optional[Segment]:
        """Find a line in the middle of the horizontal space between the rectangles."""
        y1 = max(self._start_element._y, self._end_element._y)
        y2 = min(self._start_element._y + self._start_element._height, self._end_element._y + self._end_element._height)

        return ((self._xmin, (y1 + y2) / 2), (self._xmax, (y1 + y2) / 2)) if y1 > y2 else None
    
    def _find_vertical_gap_segment(self) -> Optional[Segment]:
        """Find a line in the middle of the vertical space between the rectangles."""
        x1 = max(self._start_element._x, self._end_element._x)
        x2 = min(self._start_element._x + self._start_element._width, self._end_element._x + self._end_element._width)
        
        return (((x1 + x2) / 2, self._ymin), ((x1 + x2) / 2, self._ymax)) if x1 > x2 else None

    def _compute_bounds(self) -> None:
        self._xmin = min(self._start_element._x, self._end_element._x) - self._min_segment_hint
        self._xmax = max(self._start_element._x + self._start_element._width, self._end_element._x + self._end_element._width) + self._min_segment_hint
        self._ymin = min(self._start_element._y, self._end_element._y) - self._min_segment_hint
        self._ymax = max(self._start_element._y + self._start_element._height, self._end_element._y + self._end_element._height) + self._min_segment_hint

    def _fill_segments(self) -> None:
        self._add_segment_if_valid(self._find_horizontal_gap_segment())
        self._add_segment_if_valid(self._find_vertical_gap_segment())
        self._add_segment_if_valid(self._find_free_segment(self._end_point, self._end_dir, self._start_element))
        self._add_segment(((self._xmin, self._ymin), (self._xmax, self._ymin)))
        self._add_segment(((self._xmin, self._ymax), (self._xmax, self._ymax)))
        self._add_segment(((self._xmin, self._ymin), (self._xmin, self._ymax)))
        self._add_segment(((self._xmax, self._ymin), (self._xmax, self._ymax)))

    def _add_segment_if_valid(self, segment: Optional[Segment]) -> None:
        if segment:
            self._add_segment(segment)
            
    def _add_segment(self, segment: Segment) -> None:
        if AaLineSegmentIntersection.is_vertical_segment(segment[0], segment[1]):
            self._vertical_segments.append(segment)
        elif AaLineSegmentIntersection.is_horizontal_segment(segment[0], segment[1]):
            self._horizontal_segments.append(segment)
        else:
            raise Exception('Not AA segment')

    def _find_free_segment(self, start: Point, direction: str, obstacle: AbstractElement) -> Optional[Segment]:
        def manhattan_distance(p1: Point, p2: Point) -> float:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        x, y = start
        w, h = self._xmax - self._xmin, self._ymax - self._ymin
        dx, dy = Directions.dxdy(direction)
        end = self._clamp_point((x + w * dx, y + h * dy))

        intersections = AaLineSegmentIntersection.with_rectangle(start, end, obstacle.get_center(), obstacle._width / 2, obstacle._height / 2)
        return (start, end) if not intersections else (start, min(intersections, key = lambda point: manhattan_distance(point, start)))

    def _clamp_point(self, point: Point) -> Point:
        x, y = point
        return (min(max(x, self._xmin), self._xmax), min(max(y, self._ymin), self._ymax))

    # Recursive magic follows :)
    # TODO optimize the algorithm to not cross segments that were already 
    # intersected in previous iterations

    def _cross_horizontal(self, p1: Point, p2: Point) -> None:
        self._cross_segment(p1, p2, self._cross_vertical, self._horizontal_segments)

    def _cross_vertical(self, p1: Point, p2: Point) -> None:
        self._cross_segment(p1, p2, self._cross_horizontal, self._vertical_segments)

    def _cross_segment(self, p1: Point, p2: Point, cross_function: Callable, cross_segments: list[Segment]) -> None:
        if self._current_trajectory.get_elbows_count() < MAX_ELBOWS:
            self._try_complete_trajectory(p1, p2)
            for q1, q2 in cross_segments:
                intersection = AaLineSegmentIntersection.with_aa_line_segment(p1, p2, q1, q2)
                if intersection:
                    self._current_trajectory.add_point(intersection)
                    cross_function(q1, q2)
                    self._current_trajectory.pop_point()

    def _try_complete_trajectory(self, p1: Point, p2: Point) -> None:
        if AaLineSegmentIntersection.is_point_on_segment(self._end_point, p1, p2):
            self._current_trajectory.add_point(self._end_point)
            if self._current_trajectory.is_better_than(self._best_trajectory):
                self._best_trajectory = copy.deepcopy(self._current_trajectory)
            
            self._current_trajectory.pop_point()
