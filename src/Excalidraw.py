from impl.ElementFactory import ElementFactory

class Excalidraw():
    def __init__(self):
        self.factory = ElementFactory()

    def config(self):
        self.factory.config()
        return self

    def rectangle(self):
        return self.factory.rectangle()

    def diamond(self):
        pass

    def ellipse(self):
        pass

    def arrow(self):
        pass

    def line(self):
        pass

    def text(self):
        pass

    def image(self):
        pass

    def group(self):
        pass

    def frame(self):
        pass




