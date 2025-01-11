from abc import ABC, abstractmethod
from ..elements.Text import Text

class AbstractPlainLabelListener(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def on_text(self, text: str) -> Text:
        pass
