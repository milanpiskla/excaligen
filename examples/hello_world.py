from excaligen.SceneBuilder import SceneBuilder

# Create a new SceneBuilder instance
scene = SceneBuilder()

# Add a simple text element
scene.text("Hello, World!")

# Save the diagram to a file
scene.save("hello_world.excalidraw")
