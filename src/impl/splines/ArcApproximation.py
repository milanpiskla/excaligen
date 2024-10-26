import math
from ..helpers.CircleIntersection import CircleIntersection

Point = tuple[float, float]

class ArcApproximation:
    """Generates a list of points approximating an arc between two elements.

    The arc is part of a circle with a given radius, passes through the centers of the elements,
    and starts and ends at the precise intersection points of the circle and the elements' edges.
    """

    def __init__(self):
        pass

    def generate_points(
        self,
        center_start: Point,
        center_end: Point,
        radius: float,
        element_start: 'AbstractElement',
        element_end: 'AbstractElement',
        points_per_circle: int = 36
    ) -> list[Point]:
        """Generates points approximating an arc between two elements.

        Args:
            center_start (Point): Center of the start element.
            center_end (Point): Center of the end element.
            radius (float): Radius of the circle defining the arc.
            element_start (AbstractElement): The start element.
            element_end (AbstractElement): The end element.
            points_per_circle (int, optional): Number of points to use for a full circle.

        Returns:
            List[Point]: A list of points approximating the arc.

        Raises:
            ValueError: If the arc cannot be created with the given parameters.
        """
        # Step 1: Compute possible circle centers
        circle_centers = self._compute_circle_centers(center_start, center_end, radius)

        if not circle_centers:
            raise ValueError("No circle can be formed with the given radius and centers.")

        # Step 2: Choose the appropriate circle center
        circle_center = self._select_circle_center(circle_centers, center_start, center_end)

        # Step 3: Find intersection points with the elements
        start_edge_point = self._find_intersection_with_element(circle_center, radius, element_start, center_start)
        end_edge_point = self._find_intersection_with_element(circle_center, radius, element_end, center_end)

        if not start_edge_point or not end_edge_point:
            raise ValueError("Cannot find intersection points between circle and elements.")

        # Step 4: Generate arc points between the two intersection points
        arc_points = self._generate_arc_points(
            circle_center,
            radius,
            start_edge_point,
            end_edge_point,
            points_per_circle
        )

        return arc_points

    def _compute_circle_centers(self, A: Point, B: Point, radius: float) -> list[Point]:
        """Compute the possible circle centers given two points and a radius."""
        # Midpoint between A and B
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        # Distance between A and B
        dx, dy = B[0] - A[0], B[1] - A[1]
        d = math.hypot(dx, dy)

        # Check if a circle is possible
        if d > 2 * radius:
            return []

        # Calculate distance from midpoint to circle centers
        h = math.sqrt(radius**2 - (d / 2)**2)

        # Direction vectors
        rx, ry = -dy / d, dx / d

        # Possible circle centers
        cx1, cy1 = mx + h * rx, my + h * ry
        cx2, cy2 = mx - h * rx, my - h * ry

        return [(cx1, cy1), (cx2, cy2)]

    def _select_circle_center(self, centers: list[Point], A: Point, B: Point) -> Point:
        """Select the circle center where A and B are ordered clockwise."""
        # For each center, compute the angles from center to A and B
        for center in centers:
            angle_A = math.atan2(A[1] - center[1], A[0] - center[0])
            angle_B = math.atan2(B[1] - center[1], B[0] - center[0])

            # Normalize angles to [0, 2*pi]
            angle_A = angle_A % (2 * math.pi)
            angle_B = angle_B % (2 * math.pi)

            # If moving from angle_A to angle_B is in the clockwise direction
            if (angle_B - angle_A) % (2 * math.pi) < math.pi:
                return center

        # If none satisfy the condition, return the first one
        return centers[0]

    def _find_intersection_with_element(
        self,
        circle_center: Point,
        radius: float,
        element: 'AbstractElement',
        element_center: Point
    ) -> Point:
        """Find the precise intersection point between the circle and the element's edge.

        Args:
            circle_center (Point): The center of the circle.
            radius (float): The radius of the circle.
            element (AbstractElement): The element to find the intersection with.
            element_center (Point): The center of the element.

        Returns:
            Point: The intersection point on the edge of the element.
        """
        # Shift coordinates to element's local coordinate system
        cx, cy = circle_center
        ex, ey = element._x, element._y
        ew, eh = getattr(element, '_width', 0), getattr(element, '_height', 0)
        angle = getattr(element, '_angle', 0)

        # Translate circle center relative to element center
        dx = cx - element_center[0]
        dy = cy - element_center[1]

        # Rotate coordinates if the element is rotated
        if angle != 0:
            cos_a = math.cos(-angle)
            sin_a = math.sin(-angle)
            dx, dy = dx * cos_a - dy * sin_a, dx * sin_a + dy * cos_a

        # Depending on element type, compute intersection
        if element._type == 'ellipse':
            # Equation of an ellipse: (x/a)^2 + (y/b)^2 = 1
            a = ew / 2
            b = eh / 2
            intersection_points = CircleIntersection.circle_ellipse_intersections(dx, dy, radius, a, b)
        elif element._type == 'rectangle':
            a = ew / 2
            b = eh / 2
            intersection_points = CircleIntersection.circle_rectangle_intersections(dx, dy, radius, a, b)
        elif element._type == 'diamond':
            a = ew / 2
            b = eh / 2
            intersection_points = CircleIntersection.circle_diamond_intersections(dx, dy, radius, a, b)
        else:
            return None  # Unsupported element type

        if not intersection_points:
            return None

        # Choose the intersection point that is closest to the line from the circle center to the element center
        min_angle_diff = float('inf')
        selected_point = None
        for ix, iy in intersection_points:
            # Angle from circle center to intersection point
            angle_point = math.atan2(iy - dy, ix - dx)
            # Angle from circle center to element center (which is at origin in local coords)
            angle_center = math.atan2(-dy, -dx)
            angle_diff = abs((angle_point - angle_center + math.pi) % (2 * math.pi) - math.pi)
            if angle_diff < min_angle_diff:
                min_angle_diff = angle_diff
                selected_point = (ix, iy)

        # Rotate back
        if angle != 0:
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            ix_rot, iy_rot = selected_point[0] * cos_a - selected_point[1] * sin_a, selected_point[0] * sin_a + selected_point[1] * cos_a
        else:
            ix_rot, iy_rot = selected_point

        # Translate back to global coordinates
        ix_global = ix_rot + element_center[0]
        iy_global = iy_rot + element_center[1]

        return (ix_global, iy_global)

    def _generate_arc_points(
        self,
        circle_center: Point,
        radius: float,
        start_point: Point,
        end_point: Point,
        points_per_circle: int
    ) -> list[Point]:
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
