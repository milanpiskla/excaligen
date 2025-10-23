"""
Description: Helper for the fill input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Fill:
    @staticmethod
    def from_(style: str) -> str:
        """
        Set the fill style for the shape.

        Args:
            style (str): The fill style to be applied. Must be one of 'hatchure', 'cross-hatch', or 'solid'.

        Raises:
            ValueError: If the provided style is not one of 'hatchure', 'cross-hatch', or 'solid'.
        """

        match style:
            case "hatchure" | "cross-hatch" | "solid":
                return style
            case _:
                raise ValueError(f"Invalid fill style '{style}'. Use 'hatchure', 'cross-hatch', or 'solid'.")