from src.Excalidraw import Excalidraw

xd = Excalidraw()

# Create two shapes
rect1 = xd.rectangle().position(100, 100).size(80, 60)
rect2 = xd.rectangle().position(300, 200).size(80, 60)

# Create an arc arrow between the two shapes
xd.arrow().arc(radius=180).bind(rect1, rect2)

# Save the diagram
xd.save('arc.excalidraw')
