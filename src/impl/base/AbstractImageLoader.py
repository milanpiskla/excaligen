from abc import ABC, abstractmethod

class AbstractImageLoader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load(self, file_path: str) -> bytes:
        pass
