"""Approximator to roughly mimic Bezier splines.

The Excalidraw uses Catmull-Rom splines; however using cubic Bezier splines might be
more practical for some visualisations.
"""

from .Point import Point
import math

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def mul(a, s):
    return (a[0]*s, a[1]*s)

def length(v):
    return math.sqrt(v[0]*v[0] + v[1]*v[1])

def normalize(v):
    l = length(v)
    if l == 0:
        return (0,0)
    return (v[0]/l, v[1]/l)

def cross(a, b):
    # 2D cross product result (a x b) is scalar: ax*by - ay*bx
    return a[0]*b[1] - a[1]*b[0]

TANGENT_FACTOR = 0.3

class CurveApproximation:
    """This class generates list of points for the given Bezier control points.

    The generated points can be used as control points for Catmull-Rom splines.
    """
    @staticmethod
    def generate_points(A0, A1, A2, A3, alpha=0.075) -> list[Point]:
        """
        Generate the four points [P0, P1, P2, P3] as described:
        - P0 = A0
        - P3 = A3
        - P1 based on start tangent and a small perpendicular offset
        - P2 based on end tangent and a small perpendicular offset
        The sign of the offset depends on relative position of A3 and A0 respectively.
        
        Parameters:
            A0, A1, A2, A3: tuples (x, y) defining the geometry
            alpha: factor controlling the perpendicular offset magnitude (fraction of baseline length)
        
        Returns:
            [P0, P1, P2, P3]
        """

        # Baseline
        D = sub(A3, A0)
        L = length(D)
        if L == 0:
            # Degenerate case
            return [A0, A0, A0, A0]

        # Start and end tangents
        T0 = sub(A1, A0)
        T3 = sub(A2, A3)

        # Normalize tangents
        T0u = normalize(T0)
        T3u = normalize(T3)

        # Preliminary P1 and P2 (no offset yet)
        P1_prime = add(A0, mul(T0u, TANGENT_FACTOR * L))
        P2_prime = add(A3, mul(T3u, TANGENT_FACTOR * L))

        # Compute perpendiculars
        # If T0u = (tx, ty), a perpendicular is (-ty, tx)
        N0 = (-T0u[1], T0u[0])
        # For T3u similarly
        N3 = (-T3u[1], T3u[0])

        # Determine sign for P1 offset:
        # Check where A3 lies relative to line from A0 in direction T0u using cross product
        # D = A3 - A0 already computed
        c1 = cross(D, T0u)
        # If c1 > 0, A3 is to left; if c1 < 0, A3 to right. Choose offset sign accordingly.
        s1 = 1.0 if c1 < 0 else -1.0

        # Determine sign for P2 offset:
        # Check where A0 lies relative to line from A3 in direction T3u
        D_rev = sub(A0, A3)
        c2 = cross(D_rev, T3u)
        s2 = 1.0 if c2 < 0 else -1.0

        # Offset magnitude
        h = alpha * L

        # Apply offsets
        P1 = add(P1_prime, mul(N0, s1 * h))
        P2 = add(P2_prime, mul(N3, s2 * h))

        P0 = A0
        P3 = A3
        return [P0, P1, P2, P3]
