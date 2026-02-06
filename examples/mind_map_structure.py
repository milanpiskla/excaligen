from excaligen.SceneBuilder import SceneBuilder
import math

def create_mind_map_structure():
    scene = SceneBuilder()
    
    # Configuration
    RADIUS = 700
    XOFFSET = -200
    
    # Sci-Fi Parody Data
    # Center: The Ultimate Goal
    center_label = "Orbital Laser 9000"
    center_bg = "#ff7675" # Angry red
    
    # Left Side: Critical Components
    left_labels = [
        "Main Beam", "Warp Core", "Tractor Field", 
        "Heat Exhaust", "Drone Bay", "Canteen", "5G Tower"
    ]
    # Right Side: Project Status
    right_labels = [
        "Over Budget", "Delayed", "Boss Angry", 
        "Spies Everywhere", "Crew Strike", "Out of Coffee", "Kaboom"
    ]

    # Central Goal
    center_element = (
        scene.rectangle(center_label)
        .center(0, 0)
        .size(180, 80)
        .roundness('round')
        .background(center_bg)
        .fill("solid")
    )

    # Creating symmetrical branches
    for i in range(7):
        # Map 0..6 to -3..3 for angle calculation to keep symmetry
        angle_index = i - 3
        angle = angle_index * math.pi / 12
        
        # --- Right Side (Status) ---
        xr = RADIUS * math.cos(angle) + XOFFSET
        yr = RADIUS * math.sin(angle)
        
        right_node = (
            scene.rectangle(right_labels[i])
            .center(xr, yr)
            .size(160, 60)
            .roundness('round')
            .background("#74b9ff") # Soft blue
            .fill("hachure")
        )
        
        # Curve from Center to Right
        (
            scene.arrow()
            .curve(0, math.pi) 
            .bind(center_element, right_node)
            .arrowheads(None, 'arrow')
            .stroke("solid")
        )
        
        # --- Left Side (Components) ---
        # Mirror the position
        xl = RADIUS * math.cos(angle + math.pi) - XOFFSET
        yl = RADIUS * math.sin(angle + math.pi)
        
        left_node = (
            scene.rectangle(left_labels[i])
            .center(xl, yl)
            .size(160, 60)
            .roundness('round')
            .background("#55efc4") # Mint green
            .fill("hachure")
        )
        
        # Curve from Center to Left
        (
            scene.arrow()
            .curve(math.pi, 0)
            .bind(center_element, left_node)
            .arrowheads(None, 'arrow')
            .stroke("solid")
        )

    scene.save("mind_map_structure.excalidraw")

if __name__ == "__main__":
    create_mind_map_structure()
