from excaligen.DiagramBuilder import DiagramBuilder

xd = DiagramBuilder()

for y in range(0, 10000, 100):
    for x in range(0, 10000, 100):
        xd.rectangle().center(x, y).size(80, 80)

xd.save('index.excalidraw')