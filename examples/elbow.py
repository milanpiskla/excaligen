from src.Excaligen import Excaligen

xd = Excaligen()
rect1 = xd.rectangle().position(-300, -20).size(300, 100)
rect2 = xd.rectangle().position(300, 20).size(300, 100)

xd.arrow().elbow('W', 'E').bind(rect1, rect2)

xd.save('elbow.excalidraw')