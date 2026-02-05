"""
Description: Helper for the fill input processing.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Fill:
    @staticmethod
    def from_(style: str) -> str:
        """
        Set the fill style for the shape.

        Args:
            style (str): The fill style to be applied. Must be one of 'hachure', 'cross-hatch', or 'solid'.

        Raises:
            ValueError: If the provided style is not one of 'hachure', 'cross-hatch', or 'solid'.
        """

        match style:
            case "hachure" | "cross-hatch" | "solid":
                return style
            case _:
                raise ValueError(f"Invalid fill style '{style}'. Use 'hachure', 'cross-hatch', or 'solid'.")