from excaligen.DiagramBuilder import DiagramBuilder

xd = DiagramBuilder()
start_element = xd.rectangle().center(-150, -150).size(100, 100).label(xd.text().content("center 1"))
end_element = xd.rectangle().center(150, 150).size(100, 100).label(xd.text().content("center 2"))
xd.arrow().curve('R', 'L').bind(start_element, end_element)


xd.save('arrows.excalidraw')
