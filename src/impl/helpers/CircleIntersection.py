import math

Point = tuple[float, float]

class CircleIntersection:
    """Provides methods to compute precise intersections between a circle and various shapes."""

    @staticmethod
    def circle_ellipse_intersections(dx, dy, R, a, b) -> list[Point]:
        """Find precise intersections between a circle and an ellipse centered at origin.

        Solves the system:
            (x - dx)^2 + (y - dy)^2 = R^2
            (x/a)^2 + (y/b)^2 = 1

        Returns:
            list[Point]: Intersection points in local coordinates.
        """
        # Solving the system analytically can be complex.
        # Here, we use a numerical approach with a fine angle step.
        points = []
        angle_step = 1  # degrees
        for angle_deg in range(0, 360, angle_step):
            t = math.radians(angle_deg)
            x = a * math.cos(t)
            y = b * math.sin(t)
            # Check if point lies on the circle
            left_side = (x - dx) ** 2 + (y - dy) ** 2
            right_side = R ** 2
            if abs(left_side - right_side) < 1e-5:
                points.append((x, y))
        return points

    @staticmethod
    def circle_rectangle_intersections(dx, dy, R, a, b) -> list[Point]:
        """Find precise intersections between a circle and a rectangle centered at origin.

        Returns:
            list[Point]: Intersection points in local coordinates.
        """
        # Edges of the rectangle
        lines = [
            ((-a, -b), (-a, b)),   # Left edge
            ((-a, b), (a, b)),     # Top edge
            ((a, b), (a, -b)),     # Right edge
            ((a, -b), (-a, -b))    # Bottom edge
        ]
        points = []
        for (x1, y1), (x2, y2) in lines:
            intersections = CircleIntersection.circle_line_intersections(dx, dy, R, x1, y1, x2, y2)
            points.extend(intersections)
        return points

    @staticmethod
    def circle_diamond_intersections(dx, dy, R, a, b) -> list[Point]:
        """Find precise intersections between a circle and a diamond centered at origin.

        Returns:
            list[Point]: Intersection points in local coordinates.
        """
        # Edges of the diamond (rotated square)
        # The diamond has vertices at (0, b), (a, 0), (0, -b), (-a, 0)
        # Edges are between these points
        lines = [
            ((0, b), (a, 0)),      # Upper right edge
            ((a, 0), (0, -b)),     # Lower right edge
            ((0, -b), (-a, 0)),    # Lower left edge
            ((-a, 0), (0, b))      # Upper left edge
        ]
        points = []
        for (x1, y1), (x2, y2) in lines:
            intersections = CircleIntersection.circle_line_intersections(dx, dy, R, x1, y1, x2, y2)
            points.extend(intersections)
        return points

    @staticmethod
    def circle_line_intersections(cx, cy, R, x1, y1, x2, y2) -> list[Point]:
        """Find intersections between a circle and a line segment.

        Args:
            cx, cy: Circle center coordinates.
            R: Circle radius.
            x1, y1: Start point of the line segment.
            x2, y2: End point of the line segment.

        Returns:
            list[Point]: Intersection points within the line segment.
        """
        # Shift line coordinates to circle's coordinate system
        x1 -= cx
        y1 -= cy
        x2 -= cx
        y2 -= cy

        dx = x2 - x1
        dy = y2 - y1

        # Quadratic equation coefficients
        dr2 = dx**2 + dy**2
        D = x1 * y2 - x2 * y1
        discriminant = R**2 * dr2 - D**2

        if discriminant < 0:
            return []

        sqrt_discriminant = math.sqrt(discriminant)
        sign_dy = 1 if dy >= 0 else -1

        intersections = []
        for sign in [1, -1]:
            x = (D * dy + sign * sign_dy * dx * sqrt_discriminant) / dr2
            y = (-D * dx + sign * abs(dy) * sqrt_discriminant) / dr2

            # Check if the intersection point lies within the line segment
            t = ((x - x1) * dx + (y - y1) * dy) / dr2
            if 0 <= t <= 1:
                # Shift back to original coordinate system
                ix = x + cx
                iy = y + cy
                intersections.append((ix, iy))

        return intersections
