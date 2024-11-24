import math

from .Point import Point
from typing import Optional

class AaLineSegmentIntersection:
    """Provides methods to compute intersections between axis aligned line segments and various shapes."""

    @staticmethod
    def with_rectangle(p1: Point, p2: Point, center: Point, a: float, b: float) -> list[Point]:
        if not AaLineSegmentIntersection.is_aa_segment(p1, p2):
            raise Exception("Only axis aligned segments are supported")
        
        cx, cy = center
        intersections = []
        if AaLineSegmentIntersection.is_horizontal_segment(p1, p2):
            x1, y1 = p1
            x2, _ = p2
            
            if AaLineSegmentIntersection._is_inbetween(y1, cy - b, cy + b):
                if AaLineSegmentIntersection._is_inbetween(cx - a, x1, x2):
                    intersections.append((cx - a, y1))
                if AaLineSegmentIntersection._is_inbetween(cx + a, x1, x2):
                    intersections.append((cx + a, y1))
                    
        else: # vertical segment
            x1, y1 = p1
            _, y2 = p2

            if AaLineSegmentIntersection._is_inbetween(x1, cx - a, cx + a):
                if AaLineSegmentIntersection._is_inbetween(cy - b, y1, y2):
                    intersections.append((x1, cy - b))
                if AaLineSegmentIntersection._is_inbetween(cy + b, y1, y2):
                    intersections.append((x1, cy + b))

        return intersections

    @staticmethod
    def with_aa_line_segment(p1: Point, p2: Point, q1: Point, q2: Point) -> Optional[Point]:
        if AaLineSegmentIntersection.is_vertical_segment(p1, p2):
            if AaLineSegmentIntersection.is_horizontal_segment(q1, q2):
                x = p1[0]
                y = q1[1]
                return (x, y) if AaLineSegmentIntersection._is_inbetween(y, p1[1], p2[1]) else None
            else:
                raise Exception('Only intersections between vertical and horizontal segments are supported')

        elif AaLineSegmentIntersection.is_horizontal_segment(p1, p2):
            if AaLineSegmentIntersection.is_vertical_segment(q1, q2):
                x = q1[0]
                y = p1[1]
                return (x, y) if AaLineSegmentIntersection._is_inbetween(x, p1[0], p2[0]) else None
            else:
                raise Exception('Only intersections between vertical and horizontal segments are supported')
            
        else:
            raise Exception('Only intersections between vertical and horizontal segments are supported')

    @staticmethod 
    def is_point_on_segment(p: Point, p1: Point, p2: Point) -> bool:
        if AaLineSegmentIntersection.is_horizontal_segment(p1, p2):
            return math.isclose(p[1], p1[1]) and AaLineSegmentIntersection._is_inbetween(p[0], p1[0], p2[0])
        elif AaLineSegmentIntersection.is_vertical_segment(p1, p2):
            return math.isclose(p[0], p1[0]) and AaLineSegmentIntersection._is_inbetween(p[1], p1[1], p2[1])
        else:
            raise Exception("Only axis aligned segments are supported")

    @staticmethod 
    def is_aa_segment(p1: Point, p2: Point) -> bool:
        return AaLineSegmentIntersection.is_vertical_segment(p1, p2) | AaLineSegmentIntersection.is_horizontal_segment(p1, p2)

    @staticmethod 
    def is_vertical_segment(p1: Point, p2: Point) -> bool:
        return math.isclose(p1[0], p2[0])

    @staticmethod 
    def is_horizontal_segment(p1: Point, p2: Point) -> bool:
        return math.isclose(p1[1], p2[1])
    
    @staticmethod 
    def _is_inbetween(v: float, s: float, t: float) -> bool:
        if s < t:
            return v >= s and v <= t
        else:
            return v >= t and v <= s

