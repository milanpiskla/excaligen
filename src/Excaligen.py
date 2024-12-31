"""
Description: Excalidraw file generator. 
This module defines the Excalidraw class, which serves as the main interface with fluent API for creating
Excalidraw diagram. 

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from .impl.base.ExcaligenStructure import ExcaligenStructure
from .config.Config import Config
from .impl.elements.Rectangle import Rectangle
from .impl.elements.Diamond import Diamond
from .impl.elements.Ellipse import Ellipse
from .impl.elements.Arrow import Arrow
from .impl.elements.Line import Line
from .impl.elements.Text import Text
from .impl.elements.Image import Image
from .impl.elements.Frame import Frame
from .impl.elements.Group import Group
from .impl.colors.Color import Color

from typing import Self

class Excaligen(ExcaligenStructure):
    """The Excalidraw class provides methods to add various diagram elements.

    The elemnts include rectangles, diamonds, ellipses, arrows, lines, text, images, groups, and frames.
    Additionally, it offers serialization of the diagram to JSON and allows saving it to a file.
    """
    def __init__(self):
        super().__init__()

    def config(self, config: Config) -> Self:
        """Configure the diagram with the given settings.

        Args:
            config (Config): The configuration settings.

        Returns:
            Self: The current instance of the Excaligen class.
        """
        return super().config(config)
    
    def grid(self, size: int, step: int, enabled: bool) -> Self:
        """Set the grid properties for the diagram.

        Args:
            size (int): The size of the grid.
            step (int): The step size of the grid.
            enabled (bool): Whether the grid is enabled.

        Returns:
            Self: The current instance of the Excaligen class.
        """
        return super().grid(size, step, enabled)
    
    def background(self, color: str) -> Self:
        """Set the background color of the diagram.

        Args:
            color (str): The background color.

        Returns:
            Self: The current instance of the Excaligen class.
        """
        return super().background(color)

    def rectangle(self) -> Rectangle:
        """Add a rectangle element to the diagram.

        Returns:
            Rectangle: The rectangle element.
        """
        return super().rectangle()

    def diamond(self) -> Diamond:
        """Add a diamond element to the diagram.

        Returns:
            Diamond: The diamond element.
        """
        return super().diamond()

    def ellipse(self) -> Ellipse:
        """Add an ellipse element to the diagram.

        Returns:
            Ellipse: The ellipse element.
        """
        return super().ellipse()

    def arrow(self) -> Arrow:
        """Add an arrow element to the diagram.

        Returns:
            Arrow: The arrow element.
        """
        return super().arrow()

    def line(self) -> Line:
        """Add a line element to the diagram.

        Returns:
            Line: The line element.
        """
        return super().line()

    def text(self) -> Text:
        """Add a text element to the diagram.

        Returns:
            Text: The text element.
        """
        return super().text()

    def image(self) -> Image:
        """Add an image element to the diagram.

        Returns:
            Image: The image element.
        """
        return super().image()

    def frame(self) -> Frame:
        """Add a frame element to the diagram.

        Returns:
            Frame: The frame element.
        """
        return super().frame()

    def group(self) -> Group:
        """Generate a group (virtual container).

        Returns:
            Group: The group container.
        """
        return super().group()

    def color(self) -> Color:
        """Create a color object.

        It can be used as an argument for setting stroke and background colors.

        Returns:
            Color: The color object.
        """
        return super().color()

    def json(self) -> str:
        """Serialize the diagram to a JSON string.

        Returns:
            str: The JSON representation of the diagram.
        """
        return super().json()

    def save(self, file: str) -> Self:
        """Save the current diagram to a file.

        Args:
            file (str): The path to the file where the diagram will be saved.

        Returns:
            Self: The current instance of the Excaligen class.
        """
        return super().save(file)
