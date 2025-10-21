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
        self._font_size = getattr("_fontSize", defaults)
        self._font_family = getattr("_fontFamily", defaults)
        self._text_align = getattr("_textAlign", defaults)
        self._vertical_align = getattr("_verticalAlign", defaults)
        self._line_height = getattr("_lineHeight", defaults)
        self._auto_resize = getattr("_autoResize", defaults)
        self._stroke_color = getattr("_strokeColor", defaults)
        self._width = getattr("_width", defaults)
        self._height = getattr("_height", defaults)
        self._container_id: str | None = None

    def content(self, text: str) -> Self:
        """Set the text content and automatically calculate width and height.

        Args:
            text (str): The text content to set.

        Returns:
            Self: The current instance of the Text class.
        """
        self._text = text
        self.__calculate_dimensions()
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
        self._font_size = Fontsize.from_(size)
        self.__calculate_dimensions()  # Recalculate dimensions when font size changes
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
        self._text_align = Align.from_(align)
        return self

    def baseline(self, align: str) -> Self:
        """Set the vertical text alignment (top, middle, bottom).

        Args:
            align (str): The vertical alignment to set.

        Raises:
            ValueError: If an invalid vertical alignment is provided.

        Returns:
            Self: The current instance of the Text class.
        """
        self._vertical_align = Baseline.from_(align)
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

    def __calculate_dimensions(self):
        """Calculate the width and height based on the text content."""
        lines = self._text.split("\n")
        width = max(len(line) for line in lines) * self._font_size * self.CHAR_WIDTH_FACTOR
        height = len(lines) * self._font_size * self.LINE_HEIGHT_FACTOR

        self._size(width, height)

        self._width = width
        self._height = height

