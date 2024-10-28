from src.Excaligen import Excaligen

# Initialize Excalidraw instance
xd = Excaligen()

# Add a rectangle
xd.rectangle().position(50, 50).size(200, 100).color("#FF5733").background("#C70039")

# Add text
xd.text().content("Hello, Excalidraw!").position(50, 0).fontsize(24).color("#154360")

# Export to JSON file
xd.save('my_diagram.excalidraw')