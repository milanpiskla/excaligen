from excaligen.DiagramBuilder import DiagramBuilder

xd = DiagramBuilder()
start_element = xd.ellipse().center(-150, -150).size(100, 100).label(xd.text().content("center 1"))
end_element = xd.ellipse().center(150, 150).size(100, 100).label(xd.text().content("center 2"))
xd.arrow().elbow().bind(start_element, end_element)

xd.save('arrow_elbow.excalidraw')
