"""
Description: Factory for creating elements.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from ...config.Config import Config, DEFAULT_CONFIG
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
        self._config: Config = DEFAULT_CONFIG

    def config(self, config: Config) -> Self:
        """Set the configuration for the element factory.

        Args:
            config (Config): The configuration settings.

        Returns:
            Self: The current instance of the ElementFactory class.
        """
        self._config = config
        return self

    def rectangle(self, listener: AbstractPlainLabelListener) -> Rectangle:
        """Create a rectangle element with the current configuration.

        Returns:
            Rectangle: The rectangle element.
        """
        return Rectangle(listener, self._config)

    def diamond(self, listener: AbstractPlainLabelListener) -> Diamond:
        """Create a diamond element with the current configuration.

        Returns:
            Diamond: The diamond element.
        """
        return Diamond(listener, self._config)

    def ellipse(self, listener: AbstractPlainLabelListener) -> Ellipse:
        """Create an ellipse element with the current configuration.

        Returns:
            Ellipse: The ellipse element.
        """
        return Ellipse(listener, self._config)

    def arrow(self, listener: AbstractPlainLabelListener) -> Arrow:
        """Create an arrow element with the current configuration.

        Returns:
            Arrow: The arrow element.
        """
        return Arrow(listener, self._config)

    def line(self) -> Line:
        """Create a line element with the current configuration.

        Returns:
            Line: The line element.
        """
        return Line(self._config)

    def text(self) -> Text:
        """Create a text element with the current configuration.

        Returns:
            Text: The text element.
        """
        return Text(self._config)

    def image(self, listener: AbstractImageListener, loader: AbstractImageLoader) -> Image:
        """Create an image element with the current configuration.

        Args:
            listener (AbstractImageListener): The image listener.
            loader (AbstractImageLoader): The image loader.

        Returns:
            Image: The image element.
        """
        return Image(listener, loader, self._config)

    def frame(self) -> Frame:
        """Create a frame element with the current configuration.

        Returns:
            Frame: The frame element.
        """
        return Frame(self._config)

    def group(self) -> Group:
        """Create a group element with the current configuration.

        Returns:
            Group: The group element.
        """
        return Group(self._config)
    
    def color(self) -> Color:
        """Create a color object.

        Returns:
            Color: The color object.
        """
        return Color()


