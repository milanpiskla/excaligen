from abc import ABC, abstractmethod

class AbstractImageListener:
    def __init__(self):
        pass

    @abstractmethod
    def on_image(self, id: str, mime_type: str, data_url: str) -> None:
        pass

