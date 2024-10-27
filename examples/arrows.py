from src.Excalidraw import Excalidraw

xd = Excalidraw()
start_element = xd.rectangle().center(-150, -150).size(100, 100).label(xd.text().content("center 1"))
end_element = xd.rectangle().center(150, 150).size(100, 100).label(xd.text().content("center 2"))
#xd.arrow().hspline().bind(start_element, end_element)
xd.arrow().hspline().bind(start_element, end_element)

xd.save('arrows.excalidraw')
