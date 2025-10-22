"""
Description: Factory for creating elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ...defaults.Defaults import Defaults
from ..base.AbstractImageListener import AbstractImageListener
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..base.AbstractImageLoader import AbstractImageLoader
from ..colors.Color import Color

from .Rectangle import Rectangle
from .Diamond import Diamond
from .Ellipse import Ellipse
from .Arrow import Arrow
from .Line import Line
from .Text import Text
from .Image import Image
from .Frame import Frame
from .Group import Group

from typing import Self

class ElementFactory():
    def __init__(self):
        self._defaults: Defaults = Defaults()

    def defaults(self) -> Defaults:
        """Get the default parameters for elements.

        Returns:
            Defaults: The default parameters for elements.
        """
        return self._defaults

    def rectangle(self, listener: AbstractPlainLabelListener) -> Rectangle:
        """Create a rectangle element with the current configuration.

        Returns:
            Rectangle: The rectangle element.
        """
        return Rectangle(self._defaults, listener)

    def diamond(self, listener: AbstractPlainLabelListener) -> Diamond:
        """Create a diamond element with the current configuration.

        Returns:
            Diamond: The diamond element.
        """
        return Diamond(self._defaults, listener)

    def ellipse(self, listener: AbstractPlainLabelListener) -> Ellipse:
        """Create an ellipse element with the current configuration.

        Returns:
            Ellipse: The ellipse element.
        """
        return Ellipse(self._defaults, listener)

    def arrow(self, listener: AbstractPlainLabelListener) -> Arrow:
        """Create an arrow element with the current configuration.

        Returns:
            Arrow: The arrow element.
        """
        return Arrow(self._defaults, listener)

    def line(self) -> Line:
        """Create a line element with the current configuration.

        Returns:
            Line: The line element.
        """
        return Line(self._defaults)

    def text(self) -> Text:
        """Create a text element with the current configuration.

        Returns:
            Text: The text element.
        """
        return Text(self._defaults)

    def image(self, listener: AbstractImageListener, loader: AbstractImageLoader) -> Image:
        """Create an image element with the current configuration.

        Args:
            listener (AbstractImageListener): The image listener.
            loader (AbstractImageLoader): The image loader.

        Returns:
            Image: The image element.
        """
        return Image(self._defaults, listener, loader)

    def frame(self) -> Frame:
        """Create a frame element with the current configuration.

        Returns:
            Frame: The frame element.
        """
        return Frame(self._defaults)

    def group(self) -> Group:
        """Create a group element with the current configuration.

        Returns:
            Group: The group element.
        """
        return Group(self._defaults)
    
    def color(self) -> Color:
        """Create a color object.

        Returns:
            Color: The color object.
        """
        return Color()


