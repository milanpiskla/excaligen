from src.Excaligen import Excaligen

xd = Excaligen()
start_element = xd.rectangle().center(-150, -150).size(100, 100).label(xd.text().content("center 1"))
end_element = xd.rectangle().center(150, 150).size(100, 100).label(xd.text().content("center 2"))
#xd.arrow().hspline().bind(start_element, end_element)
xd.arrow().hspline().bind(start_element, end_element)
xd.arrow().spline((150, -300), (-150, 300)).bind(start_element, end_element)


xd.save('arrows.excalidraw')
