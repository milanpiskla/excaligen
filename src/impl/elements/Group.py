from ..base.AbstractElement import AbstractElement
from ...config.Config import Config, DEFAULT_CONFIG

class Group(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("group", config)
        self.elements = config.get("elements", [])
