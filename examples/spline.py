from excaligen.DiagramBuilder import DiagramBuilder

xg = DiagramBuilder()
start_element = xg.ellipse().center(-150, -150).size(120, 80).label(xg.text().content("center 1"))
end_element = xg.ellipse().center(150, 150).size(120, 80).label(xg.text().content("center 2"))
xg.arrow().curve(0.0, 3.14 * 0.75).bind(start_element, end_element)

xg.save('spline.excalidraw')