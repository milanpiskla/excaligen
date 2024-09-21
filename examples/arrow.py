from src.Excalidraw import Excalidraw
import math

xd = Excalidraw()
start_element = xd.ellipse().position(-50, -50).size(100, 100).label(xd.text().content("center"))

for angle in range(0, 360, 30):
    x = 300 * math.cos(angle * math.pi / 180)
    y = 300 * math.sin(angle * math.pi / 180)
    end_element = xd.rectangle().position(x - 50, y - 25).size(100, 50).label(xd.text().content(str(angle)))
    xd.arrow().bind(start_element, end_element)

xd.save('arrow.excalidraw')