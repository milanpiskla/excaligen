"""
Description: Line element.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details


from ..base.AbstractLine import AbstractLine
from ..base.AbstractShape import AbstractShape
from ..colors.Color import Color
from ..inputs.Fill import Fill
from ...defaults.Defaults import Defaults
from typing import Self
from ..geometry.ArcApproximation import ArcApproximation
import math

class Line(AbstractLine, AbstractShape):
    """A line element that draws a straight or curved line segments between the given points.

    This class represents a line element in the drawing canvas.
    It provides functionality for creating and manipulating straight pr curved lines with specified 
    configurations for styling and positioning.

    > [!WARNING]
    > Do not instantiate this class directly. Use `SceneBuilder.line()` instead.
    """
    def __init__(self, defaults: Defaults):
        super().__init__("line", defaults)
        self._background_color = getattr(defaults, "_background_color")
        self._fill_style = getattr(defaults, "_fill_style")

    def background(self, color: str | Color) -> Self:
        """
        Set the background (fill) color of the shape created by a closed line segments.
        Args:
            color (str | Color): The background color, specified as a hex string (#RRGGBB), 
                     a color name, or a Color object.
        
        Returns:
            Self: The instance of the class for method chaining.
        """
        self._background_color = Color.from_(color)
        return self

    def fill(self, style: str) -> Self:
        """
        Set the fill style for the shape created by a closed line segments.

        Parameters:
        style (str): The fill style to be applied. Must be one of 'hachure', 'cross-hatch', or 'solid'.

        Returns:
        Self: The instance of the shape with the updated fill style.

        Raises:
        ValueError: If the provided style is not one of 'hachure', 'cross-hatch', or 'solid'.
        """
        self._fill_style = Fill.from_(style)
        return self
    
    def close(self):
        """Close the line by connecting the last point to the first point."""
        if len(self._points) > 2:
            self._points.append(self._points[0])
        return self

    def arc(self, x: float, y: float, radius: float, start_angle: float, angle_span: float) -> Self:
        """
        Adds an arc to the line.
        Approximates an arc between two points, given by the center of the arc, radius, start angle and angle span.

        Args:
            x (float): The x-coordinate of the center of the arc.
            y (float): The y-coordinate of the center of the arc.
            radius (float): The radius of the arc.
            start_angle (float): The starting angle of the arc, in radians.
            angle_span (float): The angle span of the arc, in radians.

        Returns:
            Self: The instance of the class for method chaining.
        """
        start_point = (radius * math.cos(start_angle) + x, radius * math.sin(start_angle) + y)
        end_point = (radius * math.cos(start_angle + angle_span) + x, radius * math.sin(start_angle + angle_span) + y)
        
        POINTS_PER_SEGMENT = 5 if self._roundness == None else ArcApproximation.DEFAULT_POINTS_PER_SEGMENT
        self._points.extend(ArcApproximation.generate_points((x, y), radius, start_point, end_point, POINTS_PER_SEGMENT))
            
        return self
    
