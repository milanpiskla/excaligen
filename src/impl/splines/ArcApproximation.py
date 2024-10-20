"""Approximator for Arcs.

It generates a list of points that approximate a circular arc.
Excalidraw interprets these points as control points of Catmull-Rom splines.
"""

from typing import List, Tuple
import math

Point = Tuple[float, float]

class ArcApproximation:
    """This class generates a list of approximation points for the given 2 points and radius.

    The given 2 points are assumed to be the starting and ending points of an arc.
    """

    def __init__(self):
        pass

    def generate_points(self, a0: Point, a1: Point, radius: float, points_per_circle: int = 12) -> List[Point]:
        """Generates points approximating an arc between a0 and a1 with the specified radius.

        Args:
            a0 (Point): Starting point of the arc.
            a1 (Point): Ending point of the arc.
            radius (float): Radius of the arc.
            points_per_circle (int, optional): Number of points to use for a full circle. Defaults to 12.

        Returns:
            List[Point]: A list of points approximating the arc.

        Raises:
            ValueError: If the distance between points is greater than the diameter of the circle.
        """
        # Calculate the distance between the two points
        dx = a1[0] - a0[0]
        dy = a1[1] - a0[1]
        d = math.hypot(dx, dy)

        # Check if the distance between points is greater than 2 * radius
        if d > 2 * radius:
            raise ValueError("The distance between points is greater than the diameter of the circle.")

        # Calculate the midpoint between a0 and a1
        mx = (a0[0] + a1[0]) / 2
        my = (a0[1] + a1[1]) / 2

        # Calculate the distance from the midpoint to the circle center
        try:
            h = math.sqrt(radius**2 - (d / 2)**2)
        except ValueError:
            raise ValueError("Invalid radius. Cannot create an arc with the given radius and points.")

        # Calculate the direction vector from a0 to a1
        dx_normalized = dx / d
        dy_normalized = dy / d

        # Calculate the vector perpendicular to the line from a0 to a1
        perp_dx = -dy_normalized
        perp_dy = dx_normalized

        # Calculate the two possible circle centers
        c1x = mx + h * perp_dx
        c1y = my + h * perp_dy
        c2x = mx - h * perp_dx
        c2y = my - h * perp_dy

        # Choose one of the centers (you can add logic to select based on requirements)
        center = (c1x, c1y)

        # Calculate the start and end angles
        angle0 = math.atan2(a0[1] - center[1], a0[0] - center[0])
        angle1 = math.atan2(a1[1] - center[1], a1[0] - center[0])

        # Determine if we need to adjust the angle to ensure correct arc direction
        if (angle1 - angle0) <= 0:
            angle1 += 2 * math.pi

        # Calculate the angle span
        angle_span = angle1 - angle0

        # Calculate the number of points based on the angle span
        num_points = max(int(points_per_circle * abs(angle_span) / (2 * math.pi)), 2)

        # Generate points along the arc
        points = []
        for i in range(num_points + 1):
            t = angle0 + (angle_span * i) / num_points
            x = center[0] + radius * math.cos(t)
            y = center[1] + radius * math.sin(t)
            points.append((x, y))

        return points
