# Example of generating texts
from src.Excaligen import Excaligen

xd = Excaligen()
label = xd.text().content("Hello, World!").fontsize("M").font("Hand-drawn").spacing(1.5).color("#FF0000")
xd.rectangle().position(10, 20).size(300, 100).label(label)
xd.save('label.excalidraw')
