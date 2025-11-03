"""
Description: Text element.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..base.AbstractElement import AbstractElement
from ..colors.Color import Color
from ...defaults.Defaults import Defaults
from ..inputs.Font import Font
from ..inputs.Fontsize import Fontsize
from ..inputs.Align import Align
from ..inputs.Baseline import Baseline
from typing import Self

_ANCHOR_OFFSETS_COEFFS = {
    "left" : {
        "top" : (0.0, 0.0),
        "middle" : (0.0, 0.5),
        "bottom" : (0.0, 1.0) 
    },
    "center" : {
        "top" : (0.5, 0.0),
        "middle" : (0.5, 0.5),
        "bottom" : (0.5, 1.0) 
    },
    "right" : {
        "top" : (1.0, 0.0),
        "middle" : (1.0, 0.5),
        "bottom" : (1.0, 1.0) 
    }
}

class Text(AbstractElement):
    """A class representing text elements in excaligen.
    The Text class is designed to handle and manipulate text elements within the excaligen 
    framework. It provides various text customization options including font styles, sizes, 
    alignments, and colors. The class supports auto-resizing capabilities and multiple font 
    families.
    """
    CHAR_WIDTH_FACTOR = 0.6  # Approximate width of a character relative to the font size
    LINE_HEIGHT_FACTOR = 1.25  # Approximate line height factor

    def __init__(self, defaults: Defaults):
        super().__init__("text", defaults)
        self._text: str = ""
        self._font_size = getattr(defaults, "_font_size")
        self._font_family = getattr(defaults, "_font_family")
        self._text_align = getattr(defaults, "_text_align")
        self._vertical_align = getattr(defaults, "_vertical_align")
        self._line_height = getattr(defaults, "_line_height")
        self._auto_resize = getattr(defaults, "_auto_resize")
        self._stroke_color = getattr(defaults, "_stroke_color")
        self._width = getattr(defaults, "_width")
        self._height = getattr(defaults, "_height")
        self._container_id: str | None = None
        self.__is_anchored: bool = False

    def content(self, text: str) -> Self:
        """Set the text content and automatically calculate width and height.

        Args:
            text (str): The text content to set.

        Returns:
            Self: The current instance of the Text class.
        """
        def action():
            self._text = text
            self.__calculate_dimensions()

        self.__check_anchor_and_do_action(action)
        return self

    def fontsize(self, size: int | str) -> Self:
        """Set the font size by int or by string ('S', 'M', 'L', 'XL').

        Args:
            size (int | str): The font size to set.

        Raises:
            ValueError: If an invalid size string is provided.
            TypeError: If the size is not an int or a valid string.

        Returns:
            Self: The current instance of the Text class.
        """
        def action():
            self._font_size = Fontsize.from_(size)
            self.__calculate_dimensions()

        self.__check_anchor_and_do_action(action)
        return self

    def font(self, family: str) -> Self:
        """Set the font family ('Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code').

        Args:
            family (str): The font family to set.

        Raises:
            ValueError: If an invalid font family is provided.

        Returns:
            Self: The current instance of the Text class.
        """
        self._font_family = Font.from_(family)
        return self

    def align(self, align: str) -> Self:
        """Set the horizontal text alignment (left, center, right).

        Args:
            align (str): The horizontal alignment to set.

        Raises:
            ValueError: If an invalid alignment is provided.

        Returns:
            Self: The current instance of the Text class.
        """
        def action():
            self._text_align = Align.from_(align)
            self.__calculate_dimensions()

        self.__check_anchor_and_do_action(action)
        return self

    def baseline(self, baseline: str) -> Self:
        """Set the vertical text alignment (top, middle, bottom).

        Args:
            baseline (str): The vertical alignment to set.

        Raises:
            ValueError: If an invalid vertical alignment is provided.

        Returns:
            Self: The current instance of the Text class.
        """
        def action():
            self._vertical_align = Baseline.from_(baseline)
            self.__calculate_dimensions()

        self.__check_anchor_and_do_action(action)
        return self

    def spacing(self, height: float) -> Self:
        """Set the line height manually.

        Args:
            height (float): The line height to set.

        Returns:
            Self: The current instance of the Text class.
        """
        self._line_height = height
        return self

    def autoresize(self, enabled: bool) -> Self:
        """Enable or disable automatic text box resizing.

        Args:
            enabled (bool): Whether to enable automatic resizing.

        Returns:
            Self: The current instance of the Text class.
        """
        self._auto_resize = enabled
        return self

    def color(self, color: str | Color) -> Self:
        """Set the text color as #RRGGBB, color name or Color object.

        Args:
            color (str | Color): The color to set.

        Returns:
            Self: The current instance of the Text class.
        """
        self._stroke_color = Color.from_(color)
        return self
    
    def anchor(self, x: float, y: float, align: str | None = None, baseline: str | None = None) -> Self:
        """Anchor the text element to a specific point (x, y).
        It takes horizontal and vertical alignment into account.

        Args:
            x (float): The x-coordinate to anchor to.  
            y (float): The y-coordinate to anchor to.  
            align (str | None, optional): The horizontal alignment ('left', 'center', 'right').  
            baseline (str | None, optional): The vertical alignment ('top', 'middle', 'bottom').

        Returns:
            Self: The current instance of the Text class.
        """
        self.__is_anchored = True

        if align:
            self.align(align)

        if baseline:
            self.baseline(baseline)
        
        self.__do_anchor(x, y)
        return self
    
    def center(self, x: float, y: float) -> Self:
        """
        Centers the text element at the given (x, y) coordinates.
        It is equivalent to calling anchor(x, y, "center", "middle")

        Args:
            x (float): The x-coordinate to center the element.
            y (float): The y-coordinate to center the element.

        Returns:
            Self: The instance of the element, allowing for method chaining.
        """
        return self.anchor(x, y, "center", "middle")

    def __calculate_dimensions(self):
        """Calculate the width and height based on the text content."""
        lines = self._text.split("\n")
        width = max(len(line) for line in lines) * self._font_size * self.CHAR_WIDTH_FACTOR
        height = len(lines) * self._font_size * self.LINE_HEIGHT_FACTOR

        self._size(width, height)

    def __do_anchor(self, x: float, y: float) -> None:
        """Calculate the position based on anchoring and alignment."""
        cx, cy = _ANCHOR_OFFSETS_COEFFS[self._text_align][self._vertical_align]
        self._x = x - cx * self._width
        self._y = y - cy * self._height

    def __get_anchor(self) -> tuple[float, float]:
        """Get the anchor point based on current position and alignment.

        Returns:
            tuple[float, float]: The (x, y) coordinates of the anchor point.
        """
        cx, cy = _ANCHOR_OFFSETS_COEFFS[self._text_align][self._vertical_align]
        return (self._x + cx * self._width, self._y + cy * self._height)
    
    def __check_anchor_and_do_action(self, action) -> None:
        """Check if anchored, get anchor point, do action, re-anchor."""
        if self.__is_anchored:
            x, y = self.__get_anchor()
            action()
            self.__do_anchor(x, y)
        else:
            action()
