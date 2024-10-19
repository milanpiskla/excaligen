"""Approximator for cubic Bezier splines.

The Excalidraw uses Catmull-Rom splines; however using cubic Bezier splines might be
more practical for some visualisations.
"""

Point = list[float, float] | tuple[float, float]

class BezierApproximation:
    """This class generates list of points for the given Bezier control points.

    The generated points can be used as control points for Catmull-Rom splines.
    The implementation uses adaptive sampling, i.e. the spline parts with 
    larger curvature are approximated with higher amount of points.
    """
    def __init__(self):
        pass

    def generate_points(b0: Point, b1: Point, b2: Point, b3: Point, initial_t_values = 7, error_threshold = 0.05) -> list[Point]:
        return [] # TODO

