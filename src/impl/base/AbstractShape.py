from .AbstractElement import AbstractElement
from ..elements.Text import Text
from ...config.Config import Config
from typing import Self
from typing import Union

class AbstractShape(AbstractElement):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self.width = config.get("width", 100)
        self.height = config.get("height", 100)
        self.strokeColor = config.get("strokeColor", "#000000")
        self.strokeWidth = config.get("strokeWidth", 1)
        self.strokeStyle = config.get("strokeStyle", "solid")
        self.backgroundColor = config.get("backgroundColor", "transparent")
        self.fillStyle = config.get("fillStyle", "hachure")
        self.roughness = config.get("roughness", 1)

    def size(self, width: float, height: float) -> Self:
        """Set the shape size."""
        self.width = width
        self.height = height
        return self

    def color(self, color: str) -> Self:
        """Set the stroke (outline) color."""
        self.strokeColor = color
        return self

    def thickness(self, thickness: Union[int, str]) -> Self:
        """Set the stroke thickness by int (1, 2, 3) or by string ('thin', 'bold', 'extra-bold')."""
        match thickness:
            case 1 | 2 | 3:
                self.strokeWidth = thickness
            case "thin":
                self.roughness = 0
            case "bold":
                self.roughness = 1
            case "extra-bold":
                self.roughness = 2
            case _:
                raise ValueError(f"Invalid thickness '{thickness}'. Use 1, 2, 3 or 'thin', 'bold', 'extra-bold'.")
        return self

    def sloppiness(self, value: Union[int, str]):
        """Set the stroke sloppiness by int (0, 1, 2) or by string ('architect', 'artist', 'cartoonist')."""
        match value:
            case 0 | 1 | 2:
                self.roughness = value
            case "architect":
                self.roughness = 0
            case "artist":
                self.roughness = 1
            case "cartoonist":
                self.roughness = 2
            case _:
                raise ValueError(f"Invalid value '{value}' for sloppiness. Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'.")
        return self

    def stroke(self, style: str) -> Self:
        """Set the stroke style (solid, dotted, dashed)."""
        match style:
            case "solid" | "dotted" | "dashed":
                self.strokeStyle = style
            case _:
                raise ValueError(f"Invalid style '{style}' for stroke. Use 'solid', 'dotted', 'dashed'.")
        return self

    def background(self, color: str) -> Self:
        """Set the background (fill) color."""
        self.backgroundColor = color
        return self

    def fill(self, style: str) -> Self:
        """Set the fill style (hatchure, cross-hatch, solid)."""
        match style:
            case "hatchure" | "cross-hatch" | "solid":
                self.fillStyle = style
            case _:
                raise ValueError(f"Invalid style '{style}' for fill. Use 'hatchure', 'cross-hatch', 'solid'.")
        return self
    
    def label(self, text: Text) -> Self:
        text._calculate_dimensions()
        #text.width = min(self.width * 0.8, text.width)  # Fit within 80% of the shape width
        #text.height = min(self.height * 0.8, text.height)  # Fit within 80% of the shape height
        text.x = self.x + (self.width - text.width) / 2  # Center horizontally
        text.y = self.y + (self.height - text.height) / 2  # Center vertically

        self._addBoundElement(text)
        return self
