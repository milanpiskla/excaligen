class ImageData:
    def __init__(
        self,
        width: float,
        height: float,
        mime_type: str,
        data_url: str,
        content: str | bytes = None
    ):
        self.width = width
        self.height = height
        self.mime_type = mime_type
        self.data_url = data_url
        self.content = content
