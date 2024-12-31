"""
Description: Provides methods to compute precise intersections between a half-line and various shapes.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

import math
from typing import Optional

from .Vector2D import Vector2D
from .Point import Point

class HalfLineIntersection:
    """Provides methods to compute precise intersections between a half-line and various shapes."""

    @staticmethod
    def with_ellipse(dx: float, dy: float, vx: float, vy: float, a: float, b: float, angle: float) -> Optional[Point]:
        """Find the intersection between a half-line and an ellipse centered at origin.

        The half-line starts at point (dx, dy) and moves in direction (vx, vy).
        The ellipse has semi-axes a and b.

        Returns:
            Optional[Point]: The intersection point in local coordinates, or None if no intersection.
        """
        # Parametric equations of the half-line:
        # x = dx + t * vx
        # y = dy + t * vy

        # Ellipse equation:
        # (x / a)^2 + (y / b)^2 = 1

        # Substitute the parametric equations into the ellipse equation
        # Solve for t >= 0

        vxr, vyr = Vector2D.rotate(vx, vy, -angle)

        # Coefficients of the quadratic equation At^2 + Bt + C = 0
        A = (vxr**2) / a**2 + (vyr**2) / b**2
        B = 2 * (dx * vxr) / a**2 + 2 * (dy * vyr) / b**2
        C = (dx**2) / a**2 + (dy**2) / b**2 - 1

        discriminant = B**2 - 4 * A * C

        if discriminant < 0 or A == 0:
            return None  # No intersection

        sqrt_discriminant = math.sqrt(discriminant)

        t1 = (-B - sqrt_discriminant) / (2 * A)
        t2 = (-B + sqrt_discriminant) / (2 * A)

        # We need t >= 0
        ts = [t for t in [t1, t2] if t >= 0]

        if not ts:
            return None  # No valid intersection

        # Choose the smallest t (closest intersection)
        t = min(ts)

        # Compute the intersection point
        ix = dx + t * vxr
        iy = dy + t * vyr

        return Vector2D.rotate(ix, iy, angle)

    @staticmethod
    def with_rectangle(dx: float, dy: float, vx: float, vy: float, a: float, b: float, angle: float) -> Optional[Point]:
        """Find the intersection between a half-line and a rectangle centered at origin.

        Returns:
            Optional[Point]: The intersection point in local coordinates, or None if no intersection.
        """
        # Edges of the rectangle
        lines = [
            ((-a, -b), (-a, b)),   # Left edge
            ((-a, b), (a, b)),     # Top edge
            ((a, b), (a, -b)),     # Right edge
            ((a, -b), (-a, -b))    # Bottom edge
        ]

        intersections = []

        vxr, vyr = Vector2D.rotate(vx, vy, -angle)

        for (x1, y1), (x2, y2) in lines:
            intersection = HalfLineIntersection.half_line_line_intersection(dx, dy, vxr, vyr, x1, y1, x2, y2)
            if intersection:
                intersections.append(intersection)

        if not intersections:
            return None

        # Choose the intersection closest to (dx, dy)
        min_dist = float('inf')
        closest_point = (0.0, 0.0)
        for x, y in intersections:
            dist = math.hypot(x - dx, y - dy)
            if dist < min_dist:
                min_dist = dist
                closest_point = (x, y)

        return Vector2D.rotate(closest_point[0], closest_point[1], angle)

    @staticmethod
    def with_diamond(dx: float, dy: float, vx: float, vy: float, a: float, b: float, angle: float) -> Optional[Point]:
        """Find the intersection between a half-line and a diamond centered at origin.

        Returns:
            Optional[Point]: The intersection point in local coordinates, or None if no intersection.
        """
        # Edges of the diamond (rotated square)
        lines = [
            ((0, b), (a, 0)),      # Upper right edge
            ((a, 0), (0, -b)),     # Lower right edge
            ((0, -b), (-a, 0)),    # Lower left edge
            ((-a, 0), (0, b))      # Upper left edge
        ]

        intersections = []

        vxr, vyr = Vector2D.rotate(vx, vy, -angle)

        for (x1, y1), (x2, y2) in lines:
            intersection = HalfLineIntersection.half_line_line_intersection(dx, dy, vxr, vyr, x1, y1, x2, y2)
            if intersection:
                intersections.append(intersection)

        if not intersections:
            return None

        # Choose the intersection closest to (dx, dy)
        min_dist = float('inf')
        closest_point = (0.0, 0.0)
        for x, y in intersections:
            dist = math.hypot(x - dx, y - dy)
            if dist < min_dist:
                min_dist = dist
                closest_point = (x, y)

        return Vector2D.rotate(closest_point[0], closest_point[1], angle)

    @staticmethod
    def half_line_line_intersection(px, py, vx, vy, x1, y1, x2, y2) -> Optional[Point]:
        """Find intersection between a half-line starting at (px, py) with direction (vx, vy)
        and a line segment from (x1, y1) to (x2, y2).

        Returns:
            Optional[Point]: The intersection point, or None if no intersection.
        """
        dx_line = x2 - x1
        dy_line = y2 - y1

        denominator = dx_line * vy - dy_line * vx

        if denominator == 0:
            return None  # Parallel lines

        t2 = ((vx * (y1 - py) - vy * (x1 - px)) / denominator)
        t1 = ((dx_line * (y1 - py) - dy_line * (x1 - px)) / denominator)

        if t1 >= 0 and 0 <= t2 <= 1:
            x = px + t1 * vx
            y = py + t1 * vy
            return (x, y)
        else:
            return None  # No valid intersection
