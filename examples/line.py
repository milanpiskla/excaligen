from excaligen.DiagramBuilder import DiagramBuilder
import math

def cubic_bezier(t, B0, B1, B2, B3):
    """Calculate the position on a cubic Bézier curve at parameter t."""
    x = (1 - t)**3 * B0[0] + 3 * (1 - t)**2 * t * B1[0] + 3 * (1 - t) * t**2 * B2[0] + t**3 * B3[0]
    y = (1 - t)**3 * B0[1] + 3 * (1 - t)**2 * t * B1[1] + 3 * (1 - t) * t**2 * B2[1] + t**3 * B3[1]
    return (x, y)

def bezier_derivative(t, B0, B1, B2, B3):
    """Calculate the derivative of the cubic Bézier curve at parameter t."""
    dx = 3 * (1 - t)**2 * (B1[0] - B0[0]) + 6 * (1 - t) * t * (B2[0] - B1[0]) + 3 * t**2 * (B3[0] - B2[0])
    dy = 3 * (1 - t)**2 * (B1[1] - B0[1]) + 6 * (1 - t) * t * (B2[1] - B1[1]) + 3 * t**2 * (B3[1] - B2[1])
    return (dx, dy)

def curvature(t, B0, B1, B2, B3):
    """Estimate curvature based on the derivative magnitude."""
    dx, dy = bezier_derivative(t, B0, B1, B2, B3)
    return (dx**2 + dy**2)**0.5

def generate_adaptive_bezier_points(B0, B1, B2, B3, initial_t_values=7, error_threshold=0.05):
    """Generate points on a cubic Bézier curve with adaptive sampling."""
    t_values = [i / initial_t_values for i in range(initial_t_values + 1)]
    points = [cubic_bezier(t, B0, B1, B2, B3) for t in t_values]
    
    # Iteratively refine t values based on curvature
    refined_points = [points[0]]  # Start with the first point

    for i in range(1, len(points)):
        t_start = t_values[i - 1]
        t_end = t_values[i]

        # Estimate curvature at midpoint
        t_mid = (t_start + t_end) / 2
        mid_point = cubic_bezier(t_mid, B0, B1, B2, B3)
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

xd = DiagramBuilder()

B0 = (0, 0)
B1 = (200, 0)

for n in range(7):
    B3 = (300, (n - 3) * 100)
    B2 = (100, B3[1])
    bezier_points = generate_adaptive_bezier_points(B0, B1, B2, B3)

    xd.line().color('#104060').points(bezier_points).sloppiness(0).stroke('solid').roundness('round').thickness(2)

xd.save('line.excalidraw')