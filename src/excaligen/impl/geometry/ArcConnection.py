"""
Description: Connection between two elements using an arc.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractElement import AbstractElement
from .CircleIntersection import CircleIntersection
from .ArcApproximation import ArcApproximation
from .Point import Point

from typing import Optional

import math

class ArcConnection:
    def __init__(self, start_element: AbstractElement, end_element: AbstractElement, radius: float):
        self._start_element = start_element
        self._end_element = end_element
        self._radius = radius

    def points(self) -> list[Point]:
        center_start = self._start_element.get_center()
        center_end = self._end_element.get_center()

        # Step 1: Compute possible circle centers
        circle_centers = self._compute_circle_centers(center_start, center_end, self._radius)

        if not circle_centers:
            raise ValueError("No circle can be formed with the given radius and centers.")

        # Step 2: Choose the appropriate circle center
        circle_center = self._select_circle_center(circle_centers, center_start, center_end)

        # Compute angles from circle center to element centers
        angle_start_element = math.atan2(center_start[1] - circle_center[1], center_start[0] - circle_center[0]) % (2 * math.pi)
        angle_end_element = math.atan2(center_end[1] - circle_center[1], center_end[0] - circle_center[0]) % (2 * math.pi)

        # Determine arc direction
        arc_direction = (angle_end_element - angle_start_element) % (2 * math.pi)
        if arc_direction > math.pi:
            # Arc goes the other way
            angle_start_element, angle_end_element = angle_end_element, angle_start_element

        # Step 3: Find intersection points with the elements

        start_edge_point, end_edge_point = self.__find_intersection_points(circle_center, angle_start_element, angle_end_element)

        return ArcApproximation.generate_points(circle_center, self._radius, start_edge_point, end_edge_point)

    def __find_intersection_points(self, circle_center: Point, angle_start_element: float, angle_end_element: float) -> tuple[Point, Point]:
        start_point = self.__find_intersection_with_element(self._start_element, circle_center, angle_start_element, angle_end_element)
        if start_point is None:
            raise Exception("Cannot find intersection as start point")

        end_point = self.__find_intersection_with_element(self._end_element, circle_center, angle_start_element, angle_end_element)
        if end_point is None:
            raise Exception("Cannot find intersection as end point")
        
        return start_point, end_point

    def __find_intersection_with_element(self, element: AbstractElement, circle_center: Point, angle_start_element: float, angle_end_element: float) -> Optional[Point]:
        """Find the precise intersection point between a circle and the element's edge."""

        element_center = element.get_center()

        # Shift coordinates to element's local coordinate system
        cx, cy = circle_center
        angle = element._angle

        # Translate circle center relative to element center
        dx = cx - element_center[0]
        dy = cy - element_center[1]

        a, b = element._width / 2, element._height / 2

        match element._type:
            case 'ellipse':
                intersection_points = CircleIntersection.with_ellipse(dx, dy, self._radius, a, b, angle)
            case 'rectangle' | 'image' | 'text':
                intersection_points = CircleIntersection.with_rectangle(dx, dy, self._radius, a, b, angle)
            case 'diamond':
                intersection_points = CircleIntersection.with_diamond(dx, dy, self._radius, a, b, angle)
            case _:
                return None  # Unsupported element type

        if not intersection_points:
            return None

        # Prepare to select the correct intersection point
        valid_points = []
        for ix, iy in intersection_points:
            # Translate back to global coordinates
            ix_global = ix + element_center[0]
            iy_global = iy + element_center[1]

            # Calculate angle from circle center to intersection point
            angle_point = math.atan2(iy_global - circle_center[1], ix_global - circle_center[0]) % (2 * math.pi)

            # Check if angle_point lies between angle_start_element and angle_end_element
            if angle_start_element <= angle_end_element:
                if angle_start_element <= angle_point <= angle_end_element:
                    valid_points.append((ix_global, iy_global))
            else:
                # Angles wrap around 2*pi
                if angle_point >= angle_start_element or angle_point <= angle_end_element:
                    valid_points.append((ix_global, iy_global))

        if not valid_points:
            return None

        # Select the intersection point closest to the element center
        min_dist = float('inf')
        selected_point = None
        for point in valid_points:
            dist = math.hypot(point[0] - element_center[0], point[1] - element_center[1])
            if dist < min_dist:
                min_dist = dist
                selected_point = point

#        return tuple(p + t for p, t in zip(selected_point, element.get_center()))
        return selected_point
    

    def _compute_circle_centers(self, A: Point, B: Point, radius: float) -> list[Point]:
        """Compute the possible circle centers given two points and a radius."""
        # Midpoint between A and B
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        # Distance between A and B
        dx, dy = B[0] - A[0], B[1] - A[1]
        d = math.hypot(dx, dy)

        # Check if a circle is possible
        if d > 2 * radius:
            return []

        # Calculate distance from midpoint to circle centers
        h = math.sqrt(radius**2 - (d / 2)**2)

        # Direction vectors
        rx, ry = -dy / d, dx / d

        # Possible circle centers
        cx1, cy1 = mx + h * rx, my + h * ry
        cx2, cy2 = mx - h * rx, my - h * ry

        return [(cx1, cy1), (cx2, cy2)]

    def _select_circle_center(self, centers: list[Point], A: Point, B: Point) -> Point:
        """Select the circle center where A and B are ordered clockwise."""
        # For each center, compute the angles from center to A and B
        for center in centers:
            angle_A = math.atan2(A[1] - center[1], A[0] - center[0])
            angle_B = math.atan2(B[1] - center[1], B[0] - center[0])

            # Normalize angles to [0, 2*pi]
            angle_A = angle_A % (2 * math.pi)
            angle_B = angle_B % (2 * math.pi)

            # If moving from angle_A to angle_B is in the clockwise direction
            if (angle_B - angle_A) % (2 * math.pi) < math.pi:
                return center

        # If none satisfy the condition, return the first one
        return centers[0]
