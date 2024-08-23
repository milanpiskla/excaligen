from .base.AbstractImageLoader import AbstractImageLoader

class ImageLoader(AbstractImageLoader):
    def __init__(self):
        super().__init__()

    def load(self, file_path: str) -> bytes:
        with open(file_path, "rb") as image_file:
            return image_file.read()



