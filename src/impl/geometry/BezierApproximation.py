from typing import Tuple, List
import math

Point = Tuple[float, float]

class BezierApproximation:
    def __init__(
        self,
        error_threshold: float = 1.0,
        curvature_threshold: float = 40.0,
        max_recursion_depth: int = 10
    ):
        """
        :param error_threshold: Smaller values produce more subdivisions. Try 0.1 or even 0.01 for more detail.
        :param curvature_threshold: Lower values produce more subdivisions if the curve is 'bendy'. Try values like 1.0 or 0.5.
        :param max_recursion_depth: Maximum levels of recursion to prevent infinite loops. 8-12 is typical.
        """
        self.error_threshold = error_threshold
        self.curvature_threshold = curvature_threshold
        self.max_recursion_depth = max_recursion_depth

    def generate_points(self, B0: Point, B1: Point, B2: Point, B3: Point) -> List[Point]:
        """
        Generates a list of points approximating the cubic Bezier defined by B0..B3.
        """
        result = []
        self.__subdivide_curve(B0, B1, B2, B3, 0, result)
        return result

    def __subdivide_curve(
        self, B0: Point, B1: Point, B2: Point, B3: Point, depth: int, result: List[Point]
    ):
        """
        Recursively subdivide the Bezier curve if needed until thresholds are met or max depth reached.
        """
        # Always add the first point at the start of recursion layers
        if depth == 0:
            result.append(B0)

        # Evaluate midpoints for error calculation
        B_mid = self.__cubic_bezier(0.5, B0, B1, B2, B3)

        # Straight-line approximation points for the error test
        # Using just a linear interpolation between endpoints B0 and B3 as a baseline
        linear_mid = ((B0[0] + B3[0]) * 0.5, (B0[1] + B3[1]) * 0.5)
        linear_error = math.hypot(linear_mid[0] - B_mid[0], linear_mid[1] - B_mid[1])

        # Curvature estimation: check derivative magnitude at mid t
        curvature = self.__curvature(0.5, B0, B1, B2, B3)

        # Decide whether to subdivide
        if (linear_error > self.error_threshold or curvature > self.curvature_threshold) and depth < self.max_recursion_depth:
            # Subdivide
            # De Casteljau’s subdivision
            B01 = self.__midpoint(B0, B1)
            B12 = self.__midpoint(B1, B2)
            B23 = self.__midpoint(B2, B3)
            B012 = self.__midpoint(B01, B12)
            B123 = self.__midpoint(B12, B23)
            B_split = self.__midpoint(B012, B123)

            # Left segment: B0, B01, B012, B_split
            self.__subdivide_curve(B0, B01, B012, B_split, depth + 1, result)
            # Right segment: B_split, B123, B23, B3
            self.__subdivide_curve(B_split, B123, B23, B3, depth + 1, result)
        else:
            # No more subdivision needed, just add endpoint B3
            result.append(B3)

    def __cubic_bezier(self, t: float, B0: Point, B1: Point, B2: Point, B3: Point) -> Point:
        """Compute a point on the cubic Bezier curve at parameter t."""
        x = (1 - t)**3 * B0[0] + 3 * (1 - t)**2 * t * B1[0] + 3 * (1 - t) * t**2 * B2[0] + t**3 * B3[0]
        y = (1 - t)**3 * B0[1] + 3 * (1 - t)**2 * t * B1[1] + 3 * (1 - t) * t**2 * B2[1] + t**3 * B3[1]
        return (x, y)

    def __bezier_derivative(self, t: float, B0: Point, B1: Point, B2: Point, B3: Point) -> Point:
        """Calculate the first derivative of the cubic Bezier curve at parameter t."""
        dx = 3*(1 - t)**2 * (B1[0] - B0[0]) + 6*(1 - t)*t*(B2[0] - B1[0]) + 3*t**2*(B3[0] - B2[0])
        dy = 3*(1 - t)**2 * (B1[1] - B0[1]) + 6*(1 - t)*t*(B2[1] - B1[1]) + 3*t**2*(B3[1] - B2[1])
        return (dx, dy)

    def __curvature(self, t: float, B0: Point, B1: Point, B2: Point, B3: Point) -> float:
        """Estimate curvature at parameter t by derivative magnitude."""
        dx, dy = self.__bezier_derivative(t, B0, B1, B2, B3)
        return math.hypot(dx, dy)

    @staticmethod
    def __midpoint(p1: Point, p2: Point) -> Point:
        return ((p1[0] + p2[0]) * 0.5, (p1[1] + p2[1]) * 0.5)
