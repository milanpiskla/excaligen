from .AbstractElement import AbstractElement
from ..elements.Text import Text
from ...config.Config import Config
from typing import Self
from typing import Union

class AbstractShape(AbstractElement):
    def __init__(self, type: str, config: Config):
        super().__init__(type, config)
        self._width = config.get("width", 100)
        self._height = config.get("height", 100)
        self._stroke_color = config.get("strokeColor", "#000000")
        self._stroke_width = config.get("strokeWidth", 1)
        self._stroke_style = config.get("strokeStyle", "solid")
        self._background_color = config.get("backgroundColor", "transparent")
        self._fill_style = config.get("fillStyle", "hachure")
        self._roughness = config.get("roughness", 1)

    def size(self, width: float, height: float) -> Self:
        """Set the shape size."""
        self._width = width
        self._height = height
        return self

    def color(self, color: str) -> Self:
        """Set the stroke (outline) color."""
        self._stroke_color = color
        return self

    def thickness(self, thickness: Union[int, str]) -> Self:
        """Set the stroke thickness by int (1, 2, 3) or by string ('thin', 'bold', 'extra-bold')."""
        match thickness:
            case 1 | 2 | 3:
                self._stroke_width = thickness
            case "thin":
                self._roughness = 0
            case "bold":
                self._roughness = 1
            case "extra-bold":
                self._roughness = 2
            case _:
                raise ValueError(f"Invalid thickness '{thickness}'. Use 1, 2, 3 or 'thin', 'bold', 'extra-bold'.")
        return self

    def sloppiness(self, value: Union[int, str]):
        """Set the stroke sloppiness by int (0, 1, 2) or by string ('architect', 'artist', 'cartoonist')."""
        match value:
            case 0 | 1 | 2:
                self._roughness = value
            case "architect":
                self._roughness = 0
            case "artist":
                self._roughness = 1
            case "cartoonist":
                self._roughness = 2
            case _:
                raise ValueError(f"Invalid value '{value}' for sloppiness. Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'.")
        return self

    def stroke(self, style: str) -> Self:
        """Set the stroke style (solid, dotted, dashed)."""
        match style:
            case "solid" | "dotted" | "dashed":
                self._stroke_style = style
            case _:
                raise ValueError(f"Invalid style '{style}' for stroke. Use 'solid', 'dotted', 'dashed'.")
        return self

    def background(self, color: str) -> Self:
        """Set the background (fill) color."""
        self._background_color = color
        return self

    def fill(self, style: str) -> Self:
        """Set the fill style (hatchure, cross-hatch, solid)."""
        match style:
            case "hatchure" | "cross-hatch" | "solid":
                self._fill_style = style
            case _:
                raise ValueError(f"Invalid style '{style}' for fill. Use 'hatchure', 'cross-hatch', 'solid'.")
        return self
    
    def label(self, text: Text) -> Self:
        #text._calculate_dimensions() # TODO is this needed?
        #text.width = min(self.width * 0.8, text.width)  # Fit within 80% of the shape width
        #text.height = min(self.height * 0.8, text.height)  # Fit within 80% of the shape height
        text._x = self._x + (self._width - text._width) / 2  # Center horizontally
        text._y = self._y + (self._height - text._height - text._line_height) / 2  # Center vertically

        self._add_bound_element(text)
        return self
