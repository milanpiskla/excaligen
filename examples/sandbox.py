from excaligen.DiagramBuilder import DiagramBuilder

xd = DiagramBuilder()

def cross(center: tuple[float, float], color: str) -> None:
    x, y = center
    xd.line().plot([[x - 20, y], [x + 20, y]]).color(color)
    xd.line().plot([[x, y - 20], [x, y + 20]]).color(color)

cross([0, 0], '#ff0000')
cross([100, 50], '#00ff00')

xd.ellipse().position(0, 0).size(50, 50)
xd.ellipse().position(0, 0).size(100, 100).fade(50)

xd.text().position(0, 0).content('Center').fontsize('L').align('center').baseline('middle').rotate(3.14 / 4)

xd.save('sandbox.excalidraw')