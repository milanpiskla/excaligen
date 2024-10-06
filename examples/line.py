from src.Excalidraw import Excalidraw
import math

xd = Excalidraw()

xd.line().color('#00FF00').points([(0, 0), (100, 50)]).sloppiness(2).stroke('solid')
xd.line().color('#0000FF').points([(0, 0), (100, -50)]).sloppiness(0).stroke('dotted')
xd.line().color('#FF0000').points([(0, 0), (-100, -50), (-100, 50)]).sloppiness(0).stroke('dashed').roundness('round')

xd.save('line.excalidraw')