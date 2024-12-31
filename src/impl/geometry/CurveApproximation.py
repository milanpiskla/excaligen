"""
Description: Approximator to roughly mimic Bezier splines.
The Excalidraw uses Catmull-Rom splines; however using cubic Bezier splines might be
more practical for some visualisations, e.g. the cases we need to connect 2 elements
while defining the start and end angles of the connected arrow.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from .Point import Point
import math

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, s):
    return (a[0] * s, a[1] * s)

def length(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def normalize_angle(angle):
    """Normalizes an angle to (-pi, pi]."""
    return angle - (math.ceil((angle + math.pi) / (2 * math.pi)) - 1) * 2 * math.pi

def components(angle):
    """Returns the components (cos(angle), sin(angle)) for a given angle."""
    return (math.cos(angle), math.sin(angle))

def cross(a, b):
    """2D cross product: a.x * b.y - a.y * b.x"""
    return a[0] * b[1] - a[1] * b[0]

class CurveApproximation:
    """Generates control points for Catmull-Rom splines."""

    @staticmethod
    def generate_points(A0, A3, start_angle=0.0, end_angle=0.0, alpha=0.28) -> list[tuple[float, float]]:
        """
        Generate four points [P0, P1, P2, P3]:
        - P0 = A0
        - P3 = A3
        - P1 based on start tangent and a small perpendicular offset
        - P2 based on end tangent and a small perpendicular offset

        Parameters:
            A0, A3: tuples (x, y) defining the start and end points.
            start_angle, end_angle: angles defining tangents in radians.
            alpha: factor controlling the perpendicular offset magnitude.

        Returns:
            [P0, P1, P2, P3]
        """
        # Baseline
        D = sub(A3, A0)
        L = length(D)
        if L == 0:
            return [A0, A0, A0, A0]  # Degenerate case

        # Tangent directions
        T0u = components(start_angle)
        T3u = components(end_angle)

        # Adjust tangents to bounding box proportions
        w, h = abs(D[0]), abs(D[1])
        T0p = (T0u[0] * w, T0u[1] * h)
        T3p = (T3u[0] * w, T3u[1] * h)

        # Fixed tangent factor
        TANGENT_FACTOR = 0.333
        P1_prime = add(A0, mul(T0p, TANGENT_FACTOR))
        P2_prime = add(A3, mul(T3p, TANGENT_FACTOR))

        # Perpendicular directions
        N0 = (-T0u[1], T0u[0])
        N3 = (-T3u[1], T3u[0])

        # Signs for perpendicular offsets
        s1 = -1.0 if cross(D, T0u) > 0 else 1.0
        s2 = -1.0 if cross(sub(A0, A3), T3u) > 0 else 1.0

        # Offset magnitudes
        dir_angle = math.atan2(D[1], D[0])
        aspect_ratio = max(w, h) / (min(w, h) + 1e-9)  # Avoid division by zero
        start_offset = alpha * abs(normalize_angle(start_angle - dir_angle)) / math.pi * L
        end_offset = alpha * abs(normalize_angle(end_angle - dir_angle + math.pi)) / math.pi * L

        # Dynamically adjust offsets for narrow bounding boxes
        start_offset *= (1 + 0.20 / (aspect_ratio + 1))
        end_offset *= (1 + 0.20 / (aspect_ratio + 1))

        # Apply offsets
        P1 = add(P1_prime, mul(N0, s1 * start_offset))
        P2 = add(P2_prime, mul(N3, s2 * end_offset))

        return [A0, P1, P2, A3]
