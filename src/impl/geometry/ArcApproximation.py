import math
from .CircleIntersection import CircleIntersection

from .Point import Point

class ArcApproximation:
    """Generates a list of points approximating an arc between two elements.

    The arc is part of a circle with a given radius, passes through the centers of the elements,
    and starts and ends at the precise intersection points of the circle and the elements' edges.
    """

    @staticmethod
    def generate_points(circle_center: Point, radius: float, start_point: Point, end_point: Point, points_per_circle: int = 36) -> list[Point]:
        """Generate points along the arc between start_point and end_point."""
        cx, cy = circle_center
        angle_start = math.atan2(start_point[1] - cy, start_point[0] - cx)
        angle_end = math.atan2(end_point[1] - cy, end_point[0] - cx)

        # Normalize angles
        angle_start = angle_start % (2 * math.pi)
        angle_end = angle_end % (2 * math.pi)

        # Ensure shortest arc is chosen
        angle_span = (angle_end - angle_start) % (2 * math.pi)
        if angle_span > math.pi:
            angle_span -= 2 * math.pi

        num_points = max(int(points_per_circle * abs(angle_span) / (2 * math.pi)), 2)

        arc_points = []
        for i in range(num_points + 1):
            t = angle_start + (angle_span * i) / num_points
            x = cx + radius * math.cos(t)
            y = cy + radius * math.sin(t)
            arc_points.append((x, y))

        return arc_points
    
