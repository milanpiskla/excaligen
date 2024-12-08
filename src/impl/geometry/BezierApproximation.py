"""Approximator for cubic Bezier splines.

The Excalidraw uses Catmull-Rom splines; however using cubic Bezier splines might be
more practical for some visualisations.
"""

from .Point import Point
import math

HINT_LENGTH_BETWEEN_POINTS = 80

class BezierApproximation:
    """This class generates list of points for the given Bezier control points.

    The generated points can be used as control points for Catmull-Rom splines.
    The implementation uses adaptive sampling, i.e. the spline parts with 
    larger curvature are approximated with higher amount of points.
    """
    @staticmethod
    def generate_points(b0: Point, b1: Point, b2: Point, b3: Point, initial_t_values = 0, error_threshold = 0.5) -> list[Point]:
        if initial_t_values == 0:
            initial_t_values =  math.floor(BezierApproximation.__bezier_length(b0, b1, b2, b3) / HINT_LENGTH_BETWEEN_POINTS)

        return BezierApproximation.__generate_adaptive_bezier_points(b0, b1, b2, b3, initial_t_values, error_threshold)

    @staticmethod
    def __cubic_bezier(t, B0, B1, B2, B3):
        """Calculate the position on a cubic Bézier curve at parameter t."""
        x = (1 - t)**3 * B0[0] + 3 * (1 - t)**2 * t * B1[0] + 3 * (1 - t) * t**2 * B2[0] + t**3 * B3[0]
        y = (1 - t)**3 * B0[1] + 3 * (1 - t)**2 * t * B1[1] + 3 * (1 - t) * t**2 * B2[1] + t**3 * B3[1]
        return (x, y)

    @staticmethod
    def __bezier_derivative(t, B0, B1, B2, B3):
        """Calculate the derivative of the cubic Bézier curve at parameter t."""
        dx = 3 * (1 - t)**2 * (B1[0] - B0[0]) + 6 * (1 - t) * t * (B2[0] - B1[0]) + 3 * t**2 * (B3[0] - B2[0])
        dy = 3 * (1 - t)**2 * (B1[1] - B0[1]) + 6 * (1 - t) * t * (B2[1] - B1[1]) + 3 * t**2 * (B3[1] - B2[1])
        return (dx, dy)

    @staticmethod
    def __curvature(t, B0, B1, B2, B3):
        """Estimate curvature based on the derivative magnitude."""
        dx, dy = BezierApproximation.__bezier_derivative(t, B0, B1, B2, B3)
        return (dx**2 + dy**2)**0.5

    @staticmethod
    def __bezier_length(B0, B1, B2, B3, N=1000):
        """
        Approximate the arc length of the cubic Bézier curve using Simpson's rule.
        
        Parameters:
            B0, B1, B2, B3: Control points as (x, y).
            N: Number of subdivisions (should be even, will be adjusted if not).
        """
        if N % 2 != 0:
            N += 1  # Ensure N is even for Simpson's rule

        dt = 1.0 / N
        total = 0.0

        for i in range(N + 1):
            t = i * dt
            s = BezierApproximation.__curvature(t, B0, B1, B2, B3)

            # Simpson's rule coefficients
            if i == 0 or i == N:
                coeff = 1
            elif i % 2 == 0:
                coeff = 2
            else:
                coeff = 4

            total += coeff * s

        length = (dt / 3.0) * total
        return length

    @staticmethod
    def __generate_adaptive_bezier_points(B0, B1, B2, B3, initial_t_values=7, error_threshold=0.05):
        """Generate points on a cubic Bézier curve with adaptive sampling."""
        t_values = [i / initial_t_values for i in range(initial_t_values + 1)]
        points = [BezierApproximation.__cubic_bezier(t, B0, B1, B2, B3) for t in t_values]
        
        # Iteratively refine t values based on curvature
        refined_points = [points[0]]  # Start with the first point

        for i in range(1, len(points)):
            t_start = t_values[i - 1]
            t_end = t_values[i]

            # Estimate curvature at midpoint
            t_mid = (t_start + t_end) / 2
            mid_point = BezierApproximation.__cubic_bezier(t_mid, B0, B1, B2, B3)
            start_point = points[i - 1]
            end_point = points[i]

            # Calculate the distance between the midpoint and the linear interpolation of start and end points
            linear_mid = ((start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2)
            error = ((mid_point[0] - linear_mid[0])**2 + (mid_point[1] - linear_mid[1])**2)**0.5

            # If error is larger than the threshold, add the midpoint for more accuracy
            if error > error_threshold:
                refined_points.append(mid_point)
            
            # Always add the end point
            refined_points.append(end_point)
        
        return refined_points