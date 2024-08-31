from src.Excalidraw import Excalidraw

xd = Excalidraw()
xd.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000")
xd.text().position(100, 100).content("Hello, Excalifont!").fontsize(40).font("excalifont").align("center").baseline("top").spacing(1.5).color("#0000FF").autoresize(True)
xd.save('texts.excalidraw')
