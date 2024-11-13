from .Vector2D import Vector2D
import math

Point = tuple[float, float]

class CircleIntersection:
    """Provides methods to compute precise intersections between a circle and various shapes."""

    @staticmethod
    def with_ellipse(dx, dy, R, a, b, angle, tolerance=1e-5) -> list[Point]:
        """Find precise intersections between a circle and an ellipse centered at origin.

        Solves the equation:
            f(theta) = (a * cos(theta) - dx)^2 + (b * sin(theta) - dy)^2 - R^2 = 0

        Args:
            dx, dy (float): Coordinates of the circle center.
            R (float): Radius of the circle.
            a, b (float): Semi-major and semi-minor axes of the ellipse.
            tolerance (float): Tolerance for root finding.

        Returns:
            list[Point]: Intersection points in local coordinates.
        """
        dxr, dyr = Vector2D.rotate(dx, dy, -angle)

        def f(theta):
            return (a * math.cos(theta) - dxr)**2 + (b * math.sin(theta) - dyr)**2 - R**2

        # Initialize list of possible roots
        roots = []

        # Number of intervals to divide [0, 2*pi]
        num_intervals = 360  # Adjust for accuracy

        # Generate theta values
        theta_values = [i * 2 * math.pi / num_intervals for i in range(num_intervals + 1)]

        # Find intervals where f(theta) changes sign
        for i in range(num_intervals):
            theta1 = theta_values[i]
            theta2 = theta_values[i + 1]
            f1 = f(theta1)
            f2 = f(theta2)

            # Check for sign change
            if f1 * f2 <= 0:
                # Possible root in this interval
                root = CircleIntersection.bisect(f, theta1, theta2, tolerance)
                if root is not None:
                    # Check for duplicates
                    if all(abs(root - existing_root) > tolerance for existing_root in roots):
                        roots.append(root)

        # Compute intersection points
        points = []
        for theta in roots:
            x = a * math.cos(theta)
            y = b * math.sin(theta)
            points.append((x, y))

        return [Vector2D.rotate(x, y, angle) for (x, y) in points]


    @staticmethod
    def bisect(f, a, b, tol):
        """Bisection method to find root of function f in interval [a, b]."""
        fa = f(a)
        fb = f(b)

        if fa * fb > 0:
            return None  # No root in this interval

        for _ in range(100):  # Maximum iterations
            c = (a + b) / 2
            fc = f(c)

            if abs(fc) < tol:
                return c

            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

        return (a + b) / 2  # Return the midpoint if no exact root found

    @staticmethod
    def with_rectangle(dx, dy, R, a, b, angle) -> list[Point]:
        """Find precise intersections between a circle and a rectangle centered at origin.

        Returns:
            list[Point]: Intersection points in local coordinates.
        """
        dxr, dyr = Vector2D.rotate(dx, dy, -angle)

        # Edges of the rectangle
        lines = [
            ((-a, -b), (-a, b)),   # Left edge
            ((-a, b), (a, b)),     # Top edge
            ((a, b), (a, -b)),     # Right edge
            ((a, -b), (-a, -b))    # Bottom edge
        ]
        points = []
        for (x1, y1), (x2, y2) in lines:
            intersections = CircleIntersection.with_line(dxr, dyr, R, x1, y1, x2, y2)
            points.extend(intersections)
        
        return [Vector2D.rotate(x, y, angle) for (x, y) in points]

    @staticmethod
    def with_diamond(dx, dy, R, a, b, angle) -> list[Point]:
        """Find precise intersections between a circle and a diamond centered at origin.

        Returns:
            list[Point]: Intersection points in local coordinates.
        """

        dxr, dyr = Vector2D.rotate(dx, dy, -angle)

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
            intersections = CircleIntersection.with_line(dxr, dyr, R, x1, y1, x2, y2)
            points.extend(intersections)

        return [Vector2D.rotate(x, y, angle) for (x, y) in points]

    @staticmethod
    def with_line(cx, cy, R, x1, y1, x2, y2) -> list[Point]:
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
