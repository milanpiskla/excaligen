from ..base.AbstractElement import AbstractElement
from ..helpers.ElementCenterer import ElementCenterer
from ...config.Config import Config, DEFAULT_CONFIG
from typing import Self, Union

class Text(AbstractElement):
    FONT_MAPPING = {
        "hand-drawn": 1,
        "normal": 2,
        "code": 3,
        "excalifont": 5,
        "comic-shaans": 8,
        "lilita-one": 7,
        "nunito": 6
    }

    SIZE_MAPPING = {
        "s": 16,
        "m": 20,
        "l": 24,
        "xl": 32
    }

    CHAR_WIDTH_FACTOR = 0.6  # Approximate width of a character relative to the font size
    LINE_HEIGHT_FACTOR = 1.25  # Approximate line height factor

    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("text", config)
        self._text = config.get("text", "")
        self._font_size = config.get("fontSize", 16)
        self._font_family = config.get("fontFamily", 1)
        self._text_align = config.get("textAlign", "center")
        self._vertical_align = config.get("verticalAlign", "middle")
        self._line_height = config.get("lineHeight", 1.25)
        self._auto_resize = config.get("autoResize", True)
        self._stroke_color = config.get("strokeColor", "#000000")  # Default to black
        self._width = config.get("width", 100)
        self._height = config.get("height", 100)
        self.__centerer = ElementCenterer(self)

    def content(self, text: str) -> Self:
        """Set the text content and automatically calculate width and height."""
        self._text = text
        self.__calculate_dimensions()
        return self

    def center(self, x: float, y: float) -> Self:
        """Set the center coordinates of the text element"""
        self.__centerer.center(x, y)

        return self

    def __calculate_dimensions(self):
        """Calculate the width and height based on the text content."""
        lines = self._text.split("\n")
        width = max(len(line) for line in lines) * self._font_size * self.CHAR_WIDTH_FACTOR
        height = len(lines) * self._font_size * self.LINE_HEIGHT_FACTOR

        self.__centerer.size(width, height)

        self._width = width
        self._height = height

    def fontsize(self, size: Union[int, str]) -> Self:
        """Set the font size by int or by string ('S', 'M', 'L', 'XL')."""
        if isinstance(size, int):
            self._font_size = size
        elif isinstance(size, str):
            original_size = size
            size = size.lower()
            if size in self.SIZE_MAPPING:
                self._font_size = self.SIZE_MAPPING[size]
            else:
                raise ValueError(f"Invalid size '{original_size}'. Use 'S', 'M', 'L', 'XL'.")
        else:
            raise TypeError("Font size must be an int or one of 'S', 'M', 'L', 'XL'.")
        self.__calculate_dimensions()  # Recalculate dimensions when font size changes
        return self

    def font(self, family: str) -> Self:
        """Set the font family ('Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code')."""
        family = family.lower().replace(" ", "-")
        if family in self.FONT_MAPPING:
            self._font_family = self.FONT_MAPPING[family]
        else:
            raise ValueError(f"Invalid font '{family}'. Use 'Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code'.")
        return self

    def align(self, align: str) -> Self:
        """Set the horizontal text alignment (left, center, right)."""
        match align:
            case "left" | "center" | "right":
                self._text_align = align
            case _:
                raise ValueError(f"Invalid alignment '{align}'. Use 'left', 'center', 'right'.")
        return self

    def baseline(self, align: str) -> Self:
        """Set the vertical text alignment (top, middle, bottom)."""
        match align:
            case "top" | "middle" | "bottom":
                self._vertical_align = align
            case _:
                raise ValueError(f"Invalid vertical alignment '{align}'. Use 'top', 'middle', 'bottom'.")
        return self

    def spacing(self, height: float) -> Self:
        """Set the line height manually."""
        self._line_height = height
        return self

    def autoresize(self, enabled: bool) -> Self:
        """Enable or disable automatic text box resizing."""
        self._auto_resize = enabled
        return self

    def color(self, color: str) -> Self:
        """Set the text color."""
        self._stroke_color = color
        return self
