"""
Description: Default values for elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ..impl.inputs.Sloppiness import Sloppiness
from ..impl.inputs.Stroke import Stroke
from ..impl.inputs.Thickness import Thickness
from ..impl.inputs.Roundness import Roundness
from ..impl.inputs.Fill import Fill
from ..impl.inputs.Fontsize import Fontsize
from ..impl.inputs.Font import Font
from ..impl.inputs.Align import Align
from ..impl.inputs.Baseline import Baseline
from ..impl.colors.Color import Color

from typing import Self, Any

class Defaults:
    def __init__(self):
        self._width: float = 130,
        self._height: float = 80,
        self._opacity:int = 100,
        self._angle: float = 0,
        self._roughness: int | str = 1,
        self._roundness: str | dict[str, Any] | None = Roundness.from_('round'),
        self._strokeStyle: str = "solid", 
        self._strokeWidth: float = 1,
        self._strokeColor: str = "#000000",
        self._backgroundColor: str = "transparent",
        self._fillStyle: str = "hachure",
        self._fontSize: int = 16,
        self._fontFamily:int = Font.from_("Hand drawn"),
        self._textAlign: str = "center",
        self._verticalAlign: str = "middle",
        self._autoResize = True,
        self._lineHeight: float = 1.25,

    def size(self, width: float, height: float) -> Self:
        """
        Sets the size of the element.

        Args:
            width (float): The width of the element.
            height (float): The height of the element.

        Returns:
            Self: The instance defaults with updated size.
        """
        self.width = width
        self.height = height
        return self
    
    def opacity(self, opacity: int) -> Self:
        """
        Sets the opacity of the element.

        Args:
            opacity (int): The opacity of the element (0-100).

        Returns:
            Self: The instance defaults with updated opacity.

                    Raises:
            ValueError: If the opacity value is not within the range 0-100.
        """
        if not (0 <= opacity <= 100):
            raise ValueError("Opacity values must be in the range: 0-100.")
        self._opacity = opacity
        return self

    def rotate(self, angle: float) -> Self:
        """
        Sets the rotation angle of the element.

        Args:
            angle (float): The rotation angle in radians.

        Returns:
            Self: The instance defaults with updated angle.
        """
        self._angle = angle
        return self
    
    def sloppiness(self, sloppiness: int | str) -> Self:
        """
        Sets the sloppiness of the element.

        Args:
            sloppiness (int | str): The sloppiness value to set, specified as an integer (0, 1, 2) or a string ('architect', 'artist', 'cartoonist').

        Returns:
            Self: The instance defaults with updated sloppiness.
        """
        self._roughness = Sloppiness.from_(sloppiness)
        return self
    
    def roundness(self, roundness: str) -> Self:
        """
        Sets the roundness style of the element.

        Args:
            roundness (str): The roundness style to set. Acceptable values are:
                 - "sharp": Sets the shape to have sharp corners.
                 - "round": Sets the shape to have rounded corners.
        Returns:
            Self: The instance defaults with updated roundness style.
        """
        self._roundness = Roundness.from_(roundness)
        return self

    def stroke(self, style: str) -> Self:
        """
        Sets the stroke style of the element.

        Args:
            stroke (str): The stroke style to set, specified as a string ('solid', 'dashed', 'dotted').

        Returns:
            Self: The instance defaults with updated stroke style.
        """
        self._strokeStyle = Stroke.from_(style)
        return self
    
    def thickness(self, thickness: int | str) -> Self:
        """
        Sets the stroke thickness of the element.

        Args:
            thickness (int | str): The thickness to set, specified as an integer (1, 2, 3) or a string ('thin', 'bold', 'extra-bold').

        Returns:
            Self: The instance defaults with updated stroke thickness.
        """
        self._strokeWidth = Thickness.from_(thickness)
        return self
    
    def color(self, color: str | Color) -> Self:
        """Set the stroke (outline) color as #RRGGBB, color name or Color object.

        Args:
            color (str | Color): The color to set, specified as a hex string $RRGGBB, color name, or Color object.

        Returns:
            Self: The current instance of the AbstractStrokedElement class.
        """
        self._strokeColor = Color.from_(color)
        return self
    
    def background(self, color: str | Color) -> Self:
        """
        Sets the background color of the element.

        Args:
            color (str | Color): The background color, specified as a hex string (#RRGGBB), a color name, or a Color object.

        Returns:
            Self: The instance defaults with updated background color.
        """
        self._backgroundColor = Color.from_(color)
        return self

    def fill(self, style: str) -> Self:
        """
        Sets the fill style of the element.

        Args:
            style (str): The fill style to be applied. Must be one of 'hatchure', 'cross-hatch', or 'solid'.

        Returns:
            Self: The instance defaults with updated fill style.
        """
        self._fillStyle = Fill.from_(style)
        return self
    
    def fontsize(self, size: int | str) -> Self:
        """
        Sets the font size of the text element.

        Args:
            size (int | str): The font size to set, specified as an integer (e.g., 12, 14, 16) or a string ('small', 'medium', 'large').

        Returns:
            Self: The instance defaults with updated font size.
        """
        self._fontSize = Fontsize.from_(size)
        return self
    
    def font(self, family: str) -> Self:
        """
        Sets the font family of the text element.

        Args:
            family (str): The font family to set, specified as a string ('Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code').

        Returns:
            Self: The instance defaults with updated font family.
        """
        self._fontFamily = Font.from_(family)
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
        self._textAlign = Align.from_(align)

    def baseline(self, align: str) -> Self:
        """Set the vertical text alignment (top, middle, bottom).

        Args:
            align (str): The vertical alignment to set.

        Raises:
            ValueError: If an invalid vertical alignment is provided.

        Returns:
            Self: The current instance of the Text class.
        """
        self._verticalAlign = Baseline.from_(align)

    def autoresize(self, enabled: bool) -> Self:
        """Enable or disable automatic text box resizing.

        Args:
            enabled (bool): Whether to enable automatic resizing.

        Returns:
            Self: The current instance of the Text class.
        """
        self._autoResize = enabled
        return self

    def spacing(self, height: float) -> Self:
        """Set the line height manually.

        Args:
            height (float): The line height to set.

        Returns:
            Self: The current instance of the Text class.
        """
        self._lineHeight = height
        return self

