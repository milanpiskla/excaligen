from excaligen.SceneBuilder import SceneBuilder
import math

def create_pie_chart():
    scene = SceneBuilder()
    
    # Data to visualize
    data = [
        {"label": "Code/AI", "value": 40, "color": "#f4f1de", "fill": "solid"},
        {"label": "Design", "value": 30, "color": "#81b29a", "fill": "cross-hatch"},
        {"label": "Coffee", "value": 20, "color": "#3d405b", "fill": "hachure"},
        {"label": "Sleep", "value": 10, "color": "#e07a5f", "fill": "cross-hatch"}
    ]
    
    total = sum(item["value"] for item in data)
    current_angle = 0
    center = (0, 0)
    radius = 150
    
    # Legend position
    legend_x = 200
    legend_y = -100
    
    for item in data:
        percentage = item["value"] / total
        angle_span = percentage * 360
        
        # Calculate points for the arc
        points = [center]
        steps = int(angle_span)  # One point per degree for smoothness
        if steps < 2: steps = 2
            
        for i in range(steps + 1):
            angle = math.radians(current_angle + i * (angle_span / steps))
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
            
        # Create the slice (Sector)
        (
            scene.line()
            .points(points)
            .close()  # Connect back to center to form a closed shape
            .background(item["color"])
            .fill(item["fill"])
            .stroke("solid")
            .roundness("sharp")
        )
        
        # Add Legend Item
        scene.rectangle().size(20, 20).position(legend_x, legend_y).background(item["color"]).fill(item["fill"])
        scene.text(f"{item['label']} ({item['value']}%)").position(legend_x + 30, legend_y).anchor(legend_x + 30, legend_y, "left", "top")
        
        legend_y += 40
        current_angle += angle_span
        
    scene.text("Daily Developer Life").center(0, -200).fontsize("L")
    
    scene.save("pie_chart.excalidraw")

if __name__ == "__main__":
    create_pie_chart()
