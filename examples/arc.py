from src.Excalidraw import Excalidraw
import math

xd = Excalidraw()

RADIUS = 300
elements = []

for angle in range(0, 360, 30):
    radians = angle * math.pi / 180
    x = RADIUS * math.cos(radians)
    y = RADIUS * math.sin(radians)

    #rect = xd.rectangle().center(x, y).size(80, 60)
    rect = xd.ellipse().center(x, y).size(80, 60)
    elements.append(rect)

start_element = elements[0]
for i in range(1, len(elements)):
    xd.arrow().arc(radius=RADIUS).bind(start_element, elements[i])
    start_element = elements[i]

# Save the diagram
xd.save('arc.excalidraw')
