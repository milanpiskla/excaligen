from src.Excalidraw import Excalidraw

xd = Excalidraw()
start_element = xd.rectangle().position(100, 200).size(200, 400)
end_element = xd.rectangle().position(-100, 200).size(60, 80)
xd.arrow().bind(start_element, end_element)
xd.save('arrow.excalidraw')