from excaligen.SceneBuilder import SceneBuilder
from typing import Dict, Any

scene = SceneBuilder()
scene.defaults().font("Nunito").fontsize(16)

# Data structure for the mind map
mind_map_data = {
    "Excaligen": {
        "Shapes": {
            "Rectangle": {},
            "Ellipse": {},
            "Diamond": {}
        },
        "Styles": {
            "Colors": {"RGB": {}, "HSL": {}, "Named": {}},
            "Strokes": {"Solid": {}, "Dashed": {}, "Dotted": {}}
        },
        "Power": {
            "Automation": {},
            "Recursion": {},
            "Clean Code": {}
        }
    }
}

def draw_node(label: str, x: float, y: float, parent_node=None):
    """Recursively draws the mind map."""
    # Create the node
    node = scene.rectangle().label(label).position(x, y).size(120, 50).background("AliceBlue")
    
    # Connect to parent if it exists
    if parent_node:
        scene.arrow().bind(parent_node, node).stroke("solid").color("Gray")
    
    return node

def generate_tree(data: Dict[str, Any], parent_node=None, x=0, y=0, level=1):
    """
    Generates the tree structure recursively.
    Returns the total height of the subtree.
    """
    keys = list(data.keys())
    if not keys:
        return 60 # Default height for a leaf node

    current_y = y
    
    for key in keys:
        children = data[key]
        
        # Draw the current node
        node = draw_node(key, x, current_y, parent_node)
        
        # Recursively draw children
        subtree_height = 0
        if children:
            # Calculate height of children to center the parent vertically relative to them? 
            # For simplicity in this demo, we just propagate down-right.
            # A proper tree layout algo is more complex, but this shows the idea.
             subtree_height = generate_tree(children, node, x + 150, current_y, level + 1)
        else:
             subtree_height = 60

        current_y += subtree_height
        
    return current_y - y

# Start generation
# We handle the root manually to kick it off nicely or adjust the data structure to have a single root key.
# My data has "Excaligen" as root key.
generate_tree(mind_map_data, x=50, y=300)

scene.save("mind_map.excalidraw")
