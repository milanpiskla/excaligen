"""Approximator for Arcs.

It generates a list of points that approximate circular arc. 
The Excalidraw interprets these points as control points of Catmull-Rom splines.
"""

Point = list[float, float] | tuple[float, float]

class ArcApproximation:
    """This class generates list of approximation points for the given 2 points and radius.

    The given 2 points are assumed as starting and ending points of an arc, clock-wise.

    """
    def __init__(self):
        pass

    def generate_points(a0: Point, a1: Point, radius: float, points_per_circle = 12) -> list[Point]:
        return [] # TODO

