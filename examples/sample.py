from src.Excalidraw import Excalidraw

xd = Excalidraw()
xd.rectangle().position(100, 200).size(200, 400)
xd.rectangle().position(-100, 200).size(60, 80).stroke("dotted").color('#802020').background('#202080').fill('hatchure')
xd.diamond().position(0, 0).stroke('dashed').color('#208020').background('#802020').fill('cross-hatch').edges('round')
xd.save('sample.excalidraw')
